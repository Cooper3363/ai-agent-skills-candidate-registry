from __future__ import annotations

import os
from pathlib import Path

from .config import RUNNER_ROOT


def load_dotenv(path: Path | None = None) -> None:
    env_path = path or (RUNNER_ROOT / ".env")
    if not env_path.exists():
        return
    for raw_line in env_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip().lstrip("\ufeff")
        value = value.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = value


def model_config() -> dict[str, str | bool]:
    load_dotenv()
    api_key = os.environ.get("OPENAI_API_KEY", "")
    base_url = os.environ.get("OPENAI_BASE_URL", "")
    model = os.environ.get("DEEPAGENTS_MODEL", "openai:gpt-5.5")
    metadata_only = os.environ.get("DEEPAGENTS_METADATA_ONLY", "0") == "1"
    return {
        "has_api_key": bool(api_key),
        "has_base_url": bool(base_url),
        "model": model,
        "metadata_only": metadata_only,
    }
