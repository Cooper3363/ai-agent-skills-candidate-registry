from __future__ import annotations

import argparse
import base64
import json
import mimetypes
import os
import re
import sys
import time
import urllib.error
import urllib.request
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

from .config import REPO_ROOT, RUNNER_ROOT


RESULT_PATH = (
    REPO_ROOT
    / "skills"
    / "smb-callable-candidate-skills"
    / "REAL_MEDIA_MINIMAL_SAMPLE_SMOKE_RESULT.md"
)
DEFAULT_OUTPUT_ROOT = RUNNER_ROOT / "media-smoke" / "real-media-minimal-samples"
DEFAULT_FALLBACK_REPORT_ROOT = RUNNER_ROOT / "media-smoke" / "reports"


@dataclass(frozen=True)
class ImageSampleCase:
    candidate_id: str
    title: str
    prompt: str
    manual_review_triggers: tuple[str, ...]


SAMPLE_CASES: tuple[ImageSampleCase, ...] = (
    ImageSampleCase(
        candidate_id="marketing_real_poster_banner_agent_candidate",
        title="Mock event poster",
        prompt=(
            "Create a clean square poster for a fictional small stationery shop. "
            "Text: Weekend Stationery Sale, Friday to Sunday, notebooks and pens. "
            "Use a friendly modern retail style. Do not include real brand names, "
            "logos, people, trademarks, copyrighted characters, or absolute claims."
        ),
        manual_review_triggers=(
            "brand_or_trademark",
            "people_or_portrait",
            "pricing_or_promotion_claim",
            "copyright_or_policy_sensitive_content",
        ),
    ),
    ImageSampleCase(
        candidate_id="ecommerce_product_main_image_agent_candidate",
        title="Mock product hero image",
        prompt=(
            "Create a clean ecommerce hero image for a fictional 500ml stainless "
            "steel thermos in matte white on a neutral background. Use mock product "
            "attributes only. Do not include real brand names, logos, certifications, "
            "packaging replicas, people, or misleading performance claims."
        ),
        manual_review_triggers=(
            "product_misrepresentation",
            "trademark_or_packaging_risk",
            "fake_certification",
            "unclear_specs",
        ),
    ),
    ImageSampleCase(
        candidate_id="store_menu_poster_generation_candidate",
        title="Mock menu poster",
        prompt=(
            "Create a simple square menu poster for a fictional noodle shop. Menu: "
            "Tomato Noodles 18, Mushroom Noodles 20, Iced Tea 8. Use a warm casual "
            "style. Do not include real logos, real restaurant names, health claims, "
            "copyrighted artwork, or misleading promotion claims."
        ),
        manual_review_triggers=(
            "price_or_menu_uncertainty",
            "food_health_claim",
            "trademark_or_font_risk",
            "promotion_promise",
        ),
    ),
)


def _env(name: str, fallback: str = "") -> str:
    return os.environ.get(name, fallback).strip()


def _route_config() -> dict[str, Any]:
    base_url = _env("IMAGE_RELAY_BASE_URL") or _env("OPENAI_BASE_URL")
    api_key = _env("IMAGE_RELAY_API_KEY") or _env("OPENAI_API_KEY")
    endpoint = _env("IMAGE_RELAY_ENDPOINT", "/images/generations")
    model = _env("IMAGE_RELAY_MODEL", "gpt-image-1")
    size = _env("IMAGE_RELAY_SIZE", "1024x1024")
    response_format = _env("IMAGE_RELAY_RESPONSE_FORMAT", "b64_json")
    approved = _env("REAL_MEDIA_SMOKE_APPROVED") == "1"
    return {
        "approved": approved,
        "has_base_url": bool(base_url),
        "has_api_key": bool(api_key),
        "base_url": base_url,
        "api_key": api_key,
        "endpoint": endpoint if endpoint.startswith("/") else f"/{endpoint}",
        "model": model,
        "size": size,
        "response_format": response_format,
    }


def _safe_slug(text: str) -> str:
    return re.sub(r"[^a-zA-Z0-9_.-]+", "-", text).strip("-")


def _redacted_route(config: dict[str, Any]) -> str:
    base_url = str(config.get("base_url") or "")
    endpoint = str(config.get("endpoint") or "")
    if not base_url:
        return "missing"
    return f"{base_url.rstrip('/')}{endpoint}"


def _write_json_request(url: str, api_key: str, payload: dict[str, Any]) -> dict[str, Any]:
    body = json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(
        url,
        data=body,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=120) as response:
        raw = response.read().decode("utf-8")
    return json.loads(raw)


def _download_url(url: str, output_path: Path) -> None:
    request = urllib.request.Request(url, method="GET")
    with urllib.request.urlopen(request, timeout=120) as response:
        data = response.read()
        content_type = response.headers.get("content-type", "")
    suffix = mimetypes.guess_extension(content_type.split(";")[0].strip()) or output_path.suffix
    if suffix and output_path.suffix != suffix:
        output_path = output_path.with_suffix(suffix)
    output_path.write_bytes(data)


def _save_image_response(response: dict[str, Any], output_path: Path) -> str:
    data = response.get("data")
    if not isinstance(data, list) or not data:
        raise ValueError("image response did not include data[0]")
    first = data[0]
    if not isinstance(first, dict):
        raise ValueError("image response data[0] is not an object")

    b64_json = first.get("b64_json")
    if isinstance(b64_json, str) and b64_json:
        output_path.write_bytes(base64.b64decode(b64_json))
        return str(output_path)

    image_url = first.get("url")
    if isinstance(image_url, str) and image_url:
        _download_url(image_url, output_path)
        return str(output_path)

    raise ValueError("image response did not include b64_json or url")


def _render_report(
    *,
    execute: bool,
    config: dict[str, Any],
    rows: list[dict[str, Any]],
    output_root: Path,
) -> str:
    counts: dict[str, int] = {}
    for row in rows:
        counts[row["status"]] = counts.get(row["status"], 0) + 1

    def line_count(status: str) -> int:
        return counts.get(status, 0)

    table_rows = [
        "| candidate_id | status | provider_route | output_path | usage_or_cost_note | findings |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for row in rows:
        table_rows.append(
            "| "
            + " | ".join(
                [
                    f"`{row['candidate_id']}`",
                    row["status"],
                    row["provider_route"],
                    row.get("output_path", "-"),
                    row.get("usage_or_cost_note", "-"),
                    "; ".join(row.get("findings", []) or ["none"]),
                ]
            )
            + " |"
        )

    boundaries = [
        "max_images_per_candidate=1",
        "total_max_images=3",
        "max_auto_retries=0",
        "sandbox_output_only=true",
        "no_publish=true",
        "no_customer_callable=true",
        "manual_review_required=true",
        "key_visible_to_testbench=false",
        "write_stable_registry=false",
        "write_business_system=false",
        "upload_customer_assets=false",
    ]

    return "\n".join(
        [
            "# REAL_MEDIA_MINIMAL_SAMPLE_SMOKE_RESULT",
            "",
            f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            "",
            "## Summary",
            "",
            f"- Execute mode: {'true' if execute else 'false'}",
            f"- Approval env present: {'true' if config.get('approved') else 'false'}",
            f"- Relay base URL configured: {'true' if config.get('has_base_url') else 'false'}",
            f"- Relay API key configured: {'true' if config.get('has_api_key') else 'false'}",
            f"- Model: `{config.get('model')}`",
            f"- Output root: `{output_root}`",
            "- API keys and secrets are not printed or written by this report.",
            "",
            "## Result Counts",
            "",
            f"- passed: {line_count('passed')}",
            f"- needs_fix: {line_count('needs_fix')}",
            f"- blocked: {line_count('blocked')}",
            f"- failed: {line_count('failed')}",
            "",
            "## Results",
            "",
            "\n".join(table_rows),
            "",
            "## Hard Boundaries",
            "",
            "\n".join(f"- `{item}`" for item in boundaries),
            "",
            "## Notes",
            "",
            "- A passed result only means a controlled minimal mock image sample succeeded.",
            "- It does not make the candidate customer-callable or stable-delivery ready.",
            "- Generated files must remain in a gitignored sandbox output directory.",
        ]
    ) + "\n"


def _blocked_rows(config: dict[str, Any], execute: bool) -> list[dict[str, Any]]:
    findings: list[str] = []
    if not execute:
        findings.append("execute flag not set; preflight only")
    if not config.get("approved"):
        findings.append("REAL_MEDIA_SMOKE_APPROVED=1 is required")
    if not config.get("has_base_url"):
        findings.append("IMAGE_RELAY_BASE_URL or OPENAI_BASE_URL is required")
    if not config.get("has_api_key"):
        findings.append("IMAGE_RELAY_API_KEY or OPENAI_API_KEY is required")
    if not findings:
        return []
    return [
        {
            "candidate_id": case.candidate_id,
            "status": "blocked",
            "provider_route": _redacted_route(config),
            "output_path": "-",
            "usage_or_cost_note": "not_run",
            "findings": findings,
        }
        for case in SAMPLE_CASES
    ]


def _run_samples(config: dict[str, Any], output_root: Path) -> list[dict[str, Any]]:
    run_dir = output_root / datetime.now().strftime("%Y%m%d-%H%M%S")
    run_dir.mkdir(parents=True, exist_ok=True)
    url = _redacted_route(config)
    api_key = str(config["api_key"])
    rows: list[dict[str, Any]] = []

    for case in SAMPLE_CASES:
        output_path = run_dir / f"{_safe_slug(case.candidate_id)}.png"
        payload: dict[str, Any] = {
            "model": config["model"],
            "prompt": case.prompt,
            "size": config["size"],
            "n": 1,
        }
        if config.get("response_format"):
            payload["response_format"] = config["response_format"]

        try:
            started = time.time()
            response = _write_json_request(url, api_key, payload)
            saved_path = _save_image_response(response, output_path)
            elapsed = round(time.time() - started, 2)
            usage = response.get("usage") if isinstance(response, dict) else None
            usage_note = f"elapsed_seconds={elapsed}"
            if usage:
                usage_note += f"; usage={json.dumps(usage, ensure_ascii=False)}"
            rows.append(
                {
                    "candidate_id": case.candidate_id,
                    "status": "passed",
                    "provider_route": url,
                    "output_path": saved_path,
                    "usage_or_cost_note": usage_note,
                    "findings": [
                        "manual_review_required",
                        "content_safety_status=provider_and_platform_review_required",
                        "triggers=" + ",".join(case.manual_review_triggers),
                    ],
                }
            )
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, ValueError, json.JSONDecodeError) as exc:
            rows.append(
                {
                    "candidate_id": case.candidate_id,
                    "status": "failed",
                    "provider_route": url,
                    "output_path": "-",
                    "usage_or_cost_note": "not_available",
                    "findings": [type(exc).__name__, str(exc)],
                }
            )
    return rows


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Controlled minimal real image sample runner for OpenAI-compatible image relay."
    )
    parser.add_argument("--execute", action="store_true", help="Actually call the image relay if all guards pass.")
    parser.add_argument("--write-report", action="store_true", help="Write REAL_MEDIA_MINIMAL_SAMPLE_SMOKE_RESULT.md.")
    parser.add_argument("--report-path", type=Path, default=RESULT_PATH)
    parser.add_argument("--fallback-report-root", type=Path, default=DEFAULT_FALLBACK_REPORT_ROOT)
    parser.add_argument("--output-root", type=Path, default=DEFAULT_OUTPUT_ROOT)
    args = parser.parse_args()

    config = _route_config()
    output_root = args.output_root.resolve()
    blocked = _blocked_rows(config, args.execute)
    rows = blocked if blocked else _run_samples(config, output_root)
    report = _render_report(execute=args.execute, config=config, rows=rows, output_root=output_root)

    if args.write_report:
        try:
            args.report_path.parent.mkdir(parents=True, exist_ok=True)
            args.report_path.write_text(report, encoding="utf-8")
        except OSError:
            args.fallback_report_root.mkdir(parents=True, exist_ok=True)
            fallback = args.fallback_report_root / "REAL_MEDIA_MINIMAL_SAMPLE_SMOKE_RESULT.md"
            fallback.write_text(report, encoding="utf-8")
            print(f"report_write_fallback={fallback}")
    print(report)

    statuses = {row["status"] for row in rows}
    if "blocked" in statuses:
        return 3
    if "failed" in statuses:
        return 2
    if "needs_fix" in statuses:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
