#!/usr/bin/env python3
"""Validate external DL Skill contract YAML/JSON against PFC contract JSON Schema.

Usage:
  python tools/validate_dl_contract.py contracts/dl-skills/DL-11-PLAN-release-milestone-planner.yaml

Dependencies:
  pip install pyyaml jsonschema
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

try:
    import yaml  # type: ignore
except Exception as exc:  # pragma: no cover
    print("ERROR: PyYAML is required. Install with: pip install pyyaml", file=sys.stderr)
    raise SystemExit(2) from exc

try:
    from jsonschema import Draft202012Validator  # type: ignore
except Exception as exc:  # pragma: no cover
    print("ERROR: jsonschema is required. Install with: pip install jsonschema", file=sys.stderr)
    raise SystemExit(2) from exc


def load_data(path: Path):
    text = path.read_text(encoding="utf-8")
    if path.suffix.lower() == ".json":
        return json.loads(text)
    return yaml.safe_load(text)


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: validate_dl_contract.py <contract.yaml|json>", file=sys.stderr)
        return 2

    target = Path(sys.argv[1])
    if not target.exists():
        print(f"ERROR: file not found: {target}", file=sys.stderr)
        return 2

    root = Path(__file__).resolve().parents[1]
    schema_path = root / "schemas" / "dl-skill-contract.schema.json"
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    data = load_data(target)

    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(data), key=lambda e: list(e.path))

    if errors:
        print(f"FAIL: {target} is invalid")
        for err in errors:
            loc = "/".join(str(p) for p in err.path) or "<root>"
            print(f"- {loc}: {err.message}")
        return 1

    print(f"PASS: {target} is valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
