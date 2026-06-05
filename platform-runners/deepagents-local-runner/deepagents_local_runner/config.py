from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


RUNNER_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = RUNNER_ROOT.parent.parent
REPORT_PATH = RUNNER_ROOT / "DEEPAGENTS_LOCAL_SMOKE_RESULT.md"


@dataclass(frozen=True)
class SkillSource:
    label: str
    library: str
    status: str
    path: Path
    expected_count: int


SKILL_SOURCES: tuple[SkillSource, ...] = (
    SkillSource(
        label="stable_13",
        library="stable_baseline",
        status="stable_baseline",
        path=REPO_ROOT / "skills" / "p0-first-13-platform-callable-skills" / "skills",
        expected_count=13,
    ),
    SkillSource(
        label="six_department_draft_l3",
        library="candidate_draft_l3",
        status="draft_l3",
        path=REPO_ROOT / "skills" / "p0-six-department-draft-l3-skills" / "skills",
        expected_count=2,
    ),
    SkillSource(
        label="top8_draft_l3",
        library="candidate_draft_l3",
        status="draft_l3",
        path=REPO_ROOT / "skills" / "smb-candidate-draft-l3-skills" / "skills",
        expected_count=2,
    ),
)


CANDIDATE_LIBRARY_ROOT = (
    REPO_ROOT / "skills" / "smb-callable-candidate-skills" / "candidates"
)

CANDIDATE_CARD_STATUSES: tuple[str, ...] = (
    "mock_callable",
    "dry_run_callable",
    "deepagents_smoke_passed",
    "component_only",
    "draft_l3",
)

STABLE_CUSTOMER_CALLABLE_COUNT = 13
