from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

from .config import CANDIDATE_CARD_STATUSES, CANDIDATE_LIBRARY_ROOT, SKILL_SOURCES, SkillSource


@dataclass
class SkillRecord:
    skill_id: str
    source_label: str
    library: str
    status: str
    root: Path
    skill_md: Path
    skill_yaml: Path
    metadata: dict[str, Any] = field(default_factory=dict)

    @property
    def deepagents_name(self) -> str:
        return self.skill_id.replace("_", "-").lower()

    @property
    def deepagents_virtual_prefix(self) -> str:
        if self.library == "stable_baseline":
            source = "stable"
        elif self.library == "candidate_card":
            source = "candidate"
        else:
            source = "draft"
        return f"/skills/{source}/{self.deepagents_name}"

    @property
    def output_fields(self) -> list[str]:
        meta = self.metadata
        if isinstance(meta.get("output_fields"), list):
            return [str(item) for item in meta["output_fields"]]
        if isinstance(meta.get("output_schema"), dict):
            return [str(key) for key in meta["output_schema"].keys()]
        outputs = meta.get("outputs")
        if isinstance(outputs, list):
            names: list[str] = []
            for item in outputs:
                if isinstance(item, dict) and item.get("name"):
                    names.append(str(item["name"]))
                elif isinstance(item, str):
                    names.append(item)
            return names
        return []

    @property
    def forbidden_outputs(self) -> list[str]:
        values = self.metadata.get("forbidden_outputs")
        return [str(item) for item in values] if isinstance(values, list) else []

    @property
    def human_review_triggers(self) -> list[str]:
        values = self.metadata.get("human_review_triggers")
        return [str(item) for item in values] if isinstance(values, list) else []

    @property
    def permissions(self) -> dict[str, Any]:
        value = self.metadata.get("permissions")
        return value if isinstance(value, dict) else {}


def _read_yaml(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        raw = yaml.safe_load(handle) or {}
    return raw if isinstance(raw, dict) else {}


def discover_from_source(source: SkillSource) -> list[SkillRecord]:
    if not source.path.exists():
        return []

    records: list[SkillRecord] = []
    for child in sorted(source.path.iterdir(), key=lambda item: item.name.lower()):
        if not child.is_dir():
            continue
        skill_md = child / "SKILL.md"
        skill_yaml = child / "skill.yaml"
        if not skill_md.exists() or not skill_yaml.exists():
            continue
        metadata = _read_yaml(skill_yaml)
        skill_id = str(
            metadata.get("id")
            or metadata.get("candidate_id")
            or metadata.get("skill_id")
            or child.name
        )
        records.append(
            SkillRecord(
                skill_id=skill_id,
                source_label=source.label,
                library=source.library,
                status=source.status,
                root=child,
                skill_md=skill_md,
                skill_yaml=skill_yaml,
                metadata=metadata,
            )
        )
    return records


def discover_all() -> list[SkillRecord]:
    records: list[SkillRecord] = []
    for source in SKILL_SOURCES:
        records.extend(discover_from_source(source))
    records.extend(discover_candidate_cards({record.skill_id for record in records}))
    return records


def discover_candidate_cards(existing_ids: set[str] | None = None) -> list[SkillRecord]:
    existing_ids = existing_ids or set()
    if not CANDIDATE_LIBRARY_ROOT.exists():
        return []

    records: list[SkillRecord] = []
    for status in CANDIDATE_CARD_STATUSES:
        status_dir = CANDIDATE_LIBRARY_ROOT / status
        if not status_dir.exists():
            continue
        for child in sorted(status_dir.iterdir(), key=lambda item: item.name.lower()):
            if not child.is_dir():
                continue
            candidate_md = child / "CANDIDATE.md"
            candidate_yaml = child / "candidate.yaml"
            if not candidate_md.exists() or not candidate_yaml.exists():
                continue
            metadata = _read_yaml(candidate_yaml)
            skill_id = str(
                metadata.get("candidate_id")
                or metadata.get("id")
                or metadata.get("skill_id")
                or child.name
            )
            if skill_id in existing_ids:
                continue
            records.append(
                SkillRecord(
                    skill_id=skill_id,
                    source_label=f"candidate_card_{status}",
                    library="candidate_card",
                    status=str(metadata.get("status") or status),
                    root=child,
                    skill_md=candidate_md,
                    skill_yaml=candidate_yaml,
                    metadata=metadata,
                )
            )
    return records


def validate_expected_counts(records: list[SkillRecord]) -> list[str]:
    messages: list[str] = []
    for source in SKILL_SOURCES:
        actual = sum(1 for record in records if record.source_label == source.label)
        if actual != source.expected_count:
            messages.append(
                f"{source.label}: expected {source.expected_count}, discovered {actual}"
            )
    return messages


def build_deepagents_files(records: list[SkillRecord]) -> dict[str, str]:
    files: dict[str, str] = {}
    for record in records:
        prefix = record.deepagents_virtual_prefix
        body = record.skill_md.read_text(encoding="utf-8")
        if not body.startswith("---\n"):
            frontmatter = {
                "name": record.deepagents_name,
                "description": (
                    f"Local smoke-test instructions for {record.skill_id}. "
                    f"Library={record.library}; status={record.status}; "
                    "use mock/read-only inputs only."
                ),
                "license": str(
                    record.metadata.get("license", {}).get("content_license")
                    if isinstance(record.metadata.get("license"), dict)
                    else record.metadata.get("license", "internal")
                ),
                "metadata": {
                    "skill_id": record.skill_id,
                    "library": record.library,
                    "status": record.status,
                    "source": record.source_label,
                },
            }
            body = f"---\n{yaml.safe_dump(frontmatter, allow_unicode=True)}---\n\n{body}"
        files[f"{prefix}/SKILL.md"] = body
        files[f"{prefix}/skill.yaml"] = record.skill_yaml.read_text(encoding="utf-8")
    return files


def inventory_rows(records: list[SkillRecord]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for record in records:
        rows.append(
            {
                "skill_id": record.skill_id,
                "library": record.library,
                "status": record.status,
                "source": record.source_label,
                "output_fields": record.output_fields,
                "permissions": record.permissions,
                "forbidden_outputs": record.forbidden_outputs,
                "human_review_triggers": record.human_review_triggers,
            }
        )
    return rows
