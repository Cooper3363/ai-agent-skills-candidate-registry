from __future__ import annotations

from datetime import datetime
from typing import Any

from .config import STABLE_CUSTOMER_CALLABLE_COUNT


def markdown_table(headers: list[str], rows: list[list[Any]]) -> str:
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(str(cell) for cell in row) + " |")
    return "\n".join(lines)


def render_preflight_report(
    *,
    records: list[Any],
    count_warnings: list[str],
    import_ok: bool,
    import_error: str | None,
    model_config: dict[str, Any],
    case_count: int,
    model_results: list[dict[str, Any]] | None = None,
) -> str:
    stable_count = sum(1 for record in records if record.library == "stable_baseline")
    draft_count = sum(1 for record in records if record.library == "candidate_draft_l3")
    model_results = model_results or []

    rows = [
        [record.skill_id, record.library, record.status, record.source_label]
        for record in records
    ]
    result_rows = [
        [
            item.get("skill_id", ""),
            item.get("title", ""),
            item.get("status", ""),
            "; ".join(item.get("findings", []) or []),
        ]
        for item in model_results
    ]

    if not result_rows:
        result_rows = [["-", "-", "not_run", "model smoke skipped or not requested"]]

    warnings = count_warnings or ["none"]
    api_status = "configured" if model_config.get("has_api_key") else "missing"
    base_url_status = "configured" if model_config.get("has_base_url") else "not_set"
    smoke_mode = (
        "metadata_only"
        if model_config.get("metadata_only") or not model_config.get("has_api_key")
        else "model_smoke"
    )

    lines = [
        "# DeepAgents Local Smoke Result",
        "",
        f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Summary",
        "",
        f"- Stable customer-callable Skill count remains: {STABLE_CUSTOMER_CALLABLE_COUNT}.",
        f"- Discovered stable baseline Skills: {stable_count}.",
        f"- Discovered draft L3 candidate Skills: {draft_count}.",
        f"- Total discovered Skills for local DeepAgents smoke: {len(records)}.",
        f"- Planned mock smoke cases: {case_count}.",
        f"- DeepAgents import: {'ok' if import_ok else 'failed'}.",
        f"- Model API key: {api_status}.",
        f"- OpenAI-compatible base URL: {base_url_status}.",
        f"- Smoke mode: {smoke_mode}.",
        "- Customer-callable additions from this runner: 0.",
        "",
        "## Count Warnings",
        "",
        "\n".join(f"- {warning}" for warning in warnings),
        "",
        "## Inventory",
        "",
        markdown_table(["Skill ID", "Library", "Status", "Source"], rows),
        "",
        "## Model Smoke Results",
        "",
        markdown_table(["Skill ID", "Case", "Status", "Findings"], result_rows),
        "",
        "## Boundaries",
        "",
        "- This runner does not expose business action tools.",
        "- No email, SMS, CRM, OAuth, calendar, task, support system, ecommerce upload, refund, inventory write, crawl, SEO API, or image generation tool is provided.",
        "- Stable baseline smoke does not rerun platform acceptance.",
        "- Draft L3 smoke does not promote candidates to stable delivery.",
    ]
    if import_error:
        lines.extend(["", "## Import Error", "", f"```text\n{import_error}\n```"])
    return "\n".join(lines) + "\n"
