from __future__ import annotations

import argparse
import os
from typing import Any

from .config import REPORT_PATH
from .env import model_config
from .guardrails import check_text
from .reporting import render_preflight_report
from .skills import build_deepagents_files, discover_all, validate_expected_counts
from .smoke_cases import ALL_CASES


SYSTEM_PROMPT = """You are running a controlled local smoke test for AI.Skills.
Use only the provided mock input and loaded Skill instructions.
Return concise JSON-like output with the fields requested by the relevant Skill.
Never claim to send, write, upload, refund, crawl, call external business APIs, or generate real images.
If a case requires human review, set manual_review_required to true and explain why.
"""


def _import_deepagents() -> tuple[bool, str | None, Any, Any]:
    try:
        from deepagents import FilesystemPermission, create_deep_agent
        from deepagents.backends.utils import create_file_data

        return True, None, (FilesystemPermission, create_deep_agent), create_file_data
    except Exception as exc:  # pragma: no cover - depends on local installation
        return False, str(exc), None, None


def _extract_text(result: Any) -> str:
    if isinstance(result, dict):
        messages = result.get("messages")
        if isinstance(messages, list) and messages:
            last = messages[-1]
            content = getattr(last, "content", None)
            if content is None and isinstance(last, dict):
                content = last.get("content")
            return str(content)
        return str(result)
    return str(result)


def _run_model_smoke(
    records: list[Any],
    imports: Any,
    create_file_data: Any,
    cases: list[Any],
) -> list[dict[str, Any]]:
    FilesystemPermission, create_deep_agent = imports
    deepagents_files = {
        path: create_file_data(content)
        for path, content in build_deepagents_files(records).items()
    }
    record_by_id = {record.skill_id: record for record in records}

    agent = create_deep_agent(
        model=os.environ.get("DEEPAGENTS_MODEL", "openai:gpt-5.5"),
        tools=[],
        system_prompt=SYSTEM_PROMPT,
        skills=["/skills/stable/", "/skills/draft/"],
        permissions=[
            FilesystemPermission(operations=["write"], paths=["/**"], mode="deny"),
        ],
    )

    results: list[dict[str, Any]] = []
    for case in cases:
        record = record_by_id.get(case.skill_id)
        expected = ", ".join(case.expected_fields) if case.expected_fields else "use the Skill output schema"
        prompt = (
            f"Skill ID: {case.skill_id}\n"
            f"Case: {case.title}\n"
            f"Mock input: {case.prompt}\n"
            f"Expected fields: {expected}\n"
            "Return only the structured result and safety notes."
        )
        try:
            result = agent.invoke({"messages": [{"role": "user", "content": prompt}], "files": deepagents_files})
            text = _extract_text(result)
            guardrail = check_text(text, record.forbidden_outputs if record else [])
            results.append(
                {
                    "skill_id": case.skill_id,
                    "title": case.title,
                    "status": "passed" if guardrail.passed else "failed",
                    "findings": guardrail.findings,
                }
            )
        except Exception as exc:
            results.append(
                {
                    "skill_id": case.skill_id,
                    "title": case.title,
                    "status": "error",
                    "findings": [str(exc)],
                }
            )
    return results


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-report", action="store_true", help="Write DEEPAGENTS_LOCAL_SMOKE_RESULT.md")
    parser.add_argument("--metadata-only", action="store_true", help="Skip model calls even if API key exists")
    parser.add_argument("--limit", type=int, default=0, help="Run only the first N smoke cases")
    args = parser.parse_args()

    records = discover_all()
    cases = ALL_CASES[: args.limit] if args.limit else ALL_CASES
    warnings = validate_expected_counts(records)
    cfg = model_config()
    if args.metadata_only:
        cfg["metadata_only"] = True

    import_ok, import_error, imports, create_file_data = _import_deepagents()
    model_results: list[dict[str, Any]] = []
    can_run_model = import_ok and cfg.get("has_api_key") and not cfg.get("metadata_only")
    if can_run_model:
        model_results = _run_model_smoke(records, imports, create_file_data, cases)

    report = render_preflight_report(
        records=records,
        count_warnings=warnings,
        import_ok=import_ok,
        import_error=import_error,
        model_config=cfg,
        case_count=len(cases),
        model_results=model_results,
    )

    if args.write_report:
        REPORT_PATH.write_text(report, encoding="utf-8")
    print(report)

    if warnings or not import_ok:
        return 1
    if model_results and any(item["status"] != "passed" for item in model_results):
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
