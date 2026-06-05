from __future__ import annotations

import json

from .skills import discover_all, inventory_rows, validate_expected_counts


def main() -> int:
    records = discover_all()
    payload = {
        "total": len(records),
        "count_warnings": validate_expected_counts(records),
        "skills": inventory_rows(records),
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0 if not payload["count_warnings"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
