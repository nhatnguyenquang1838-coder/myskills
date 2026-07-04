#!/usr/bin/env python3
"""Check a PFC output/report against mandatory enforcement headers, unsafe claims, and deterministic finance invariants.

Usage:
  python tools/check_pfc_output_enforcement.py path/to/output.md

This checker catches common unsafe omissions:
- missing required output header fields
- unsupported certainty phrases
- budget/RAG claims without visible blocked-claim/guardrail context
- DL-27 project cost calculator payloads whose cost arrays do not sum to the declared total budget

If a deterministic finance invariant fails, this tool exits non-zero and prints that
`enforcement-output-gate.kiro.hook` must trip before any LLM-mediated commit.
"""

from __future__ import annotations

import json
import re
import sys
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Any

try:  # Optional; JSON still works without PyYAML.
    import yaml  # type: ignore
except Exception:  # pragma: no cover
    yaml = None

REQUIRED_FIELDS = [
    "Mode:",
    "Run type:",
    "Use case:",
    "Contracts used:",
    "Skills called:",
    "Graph nodes read:",
    "Graph deltas proposed:",
    "Circuit breaker state:",
    "Allowed output:",
    "Blocked claims:",
    "Next action:",
]

UNSAFE_PATTERNS = [
    r"\bproject is green\b",
    r"\bbudget is green\b",
    r"\bon budget\b",
    r"\bforecast is approved\b",
    r"\bbaseline is approved\b",
    r"\bno risk\b",
    r"\bno impact\b",
    r"\bconfirmed\b",
    r"\bapproved\b",
]

SAFE_CONTEXT_MARKERS = [
    "blocked claims:",
    "blocked:",
    "not allowed",
    "cannot claim",
    "downgrade",
    "assumption",
    "missing data",
    "circuit breaker",
]

DL27_ID = "DL-27-FIN-project-cost-calculator"
TOTAL_KEYS = {
    "total_budget",
    "budget_total",
    "total_amount",
    "total_cost",
    "forecast_total",
    "project_total",
}
ARRAY_KEYS = {
    "cost_lines",
    "cost_items",
    "line_items",
    "budget_lines",
    "forecast_lines",
    "resource_costs",
    "items",
}
AMOUNT_KEYS = {
    "amount",
    "total",
    "cost",
    "value",
    "line_total",
    "forecast_amount",
    "budget_amount",
}
TOLERANCE = Decimal("0.01")


def lower(text: str) -> str:
    return text.lower()


def has_safe_context(text: str, match_start: int) -> bool:
    window_start = max(0, match_start - 300)
    window_end = min(len(text), match_start + 300)
    window = lower(text[window_start:window_end])
    return any(marker in window for marker in SAFE_CONTEXT_MARKERS)


def to_decimal(value: Any) -> Decimal | None:
    if value is None:
        return None
    if isinstance(value, bool):
        return None
    if isinstance(value, (int, float, Decimal)):
        try:
            return Decimal(str(value))
        except InvalidOperation:
            return None
    if isinstance(value, str):
        cleaned = value.strip().replace(",", "")
        cleaned = re.sub(r"[^0-9.\-]", "", cleaned)
        if not cleaned or cleaned in {"-", "."}:
            return None
        try:
            return Decimal(cleaned)
        except InvalidOperation:
            return None
    return None


def extract_fenced_blocks(text: str, language: str) -> list[str]:
    pattern = re.compile(rf"```{language}\s*(.*?)```", re.IGNORECASE | re.DOTALL)
    return [match.group(1).strip() for match in pattern.finditer(text)]


def parse_payloads(text: str) -> list[Any]:
    payloads: list[Any] = []

    stripped = text.strip()
    if stripped.startswith("{") or stripped.startswith("["):
        try:
            payloads.append(json.loads(stripped))
        except json.JSONDecodeError:
            pass

    for block in extract_fenced_blocks(text, "json"):
        try:
            payloads.append(json.loads(block))
        except json.JSONDecodeError:
            continue

    if yaml is not None:
        for language in ("yaml", "yml"):
            for block in extract_fenced_blocks(text, language):
                try:
                    payloads.append(yaml.safe_load(block))
                except Exception:
                    continue

    return payloads


def walk_objects(obj: Any) -> list[dict[str, Any]]:
    found: list[dict[str, Any]] = []
    if isinstance(obj, dict):
        found.append(obj)
        for value in obj.values():
            found.extend(walk_objects(value))
    elif isinstance(obj, list):
        for item in obj:
            found.extend(walk_objects(item))
    return found


def looks_like_dl27_payload(obj: dict[str, Any]) -> bool:
    searchable = json.dumps(obj, ensure_ascii=False)
    return DL27_ID in searchable or obj.get("skill_id") == DL27_ID or obj.get("contract_id") == DL27_ID


def declared_total(obj: dict[str, Any]) -> tuple[str, Decimal] | None:
    for key in TOTAL_KEYS:
        if key in obj:
            amount = to_decimal(obj.get(key))
            if amount is not None:
                return key, amount
    return None


def line_amount(item: Any) -> Decimal | None:
    if isinstance(item, (int, float, Decimal, str)):
        return to_decimal(item)
    if not isinstance(item, dict):
        return None
    for key in AMOUNT_KEYS:
        if key in item:
            amount = to_decimal(item.get(key))
            if amount is not None:
                return amount
    quantity = to_decimal(item.get("quantity") or item.get("qty"))
    unit_rate = to_decimal(item.get("unit_rate") or item.get("rate") or item.get("unit_cost"))
    if quantity is not None and unit_rate is not None:
        return quantity * unit_rate
    return None


def candidate_arrays(obj: dict[str, Any]) -> list[tuple[str, list[Any]]]:
    arrays: list[tuple[str, list[Any]]] = []
    for key, value in obj.items():
        if key in ARRAY_KEYS and isinstance(value, list):
            arrays.append((key, value))
    return arrays


def check_dl27_invariants(payloads: list[Any]) -> list[str]:
    failures: list[str] = []
    objects: list[dict[str, Any]] = []
    for payload in payloads:
        objects.extend(walk_objects(payload))

    for obj in objects:
        if not looks_like_dl27_payload(obj):
            continue

        total_pair = declared_total(obj)
        arrays = candidate_arrays(obj)

        if total_pair is None:
            failures.append(f"{DL27_ID}: missing declared total budget/amount field")
            continue
        if not arrays:
            failures.append(f"{DL27_ID}: missing cost/budget/forecast line array")
            continue

        total_key, declared = total_pair
        for array_key, rows in arrays:
            amounts: list[Decimal] = []
            for index, row in enumerate(rows, start=1):
                amount = line_amount(row)
                if amount is None:
                    failures.append(f"{DL27_ID}: {array_key}[{index}] has no deterministic amount")
                else:
                    amounts.append(amount)
            if not amounts:
                continue
            computed = sum(amounts, Decimal("0"))
            if abs(computed - declared) > TOLERANCE:
                failures.append(
                    f"{DL27_ID}: {array_key} sum {computed} != {total_key} {declared}; "
                    "trip enforcement-output-gate.kiro.hook"
                )

    return failures


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: check_pfc_output_enforcement.py <output.md|txt|json|yaml>", file=sys.stderr)
        return 2

    path = Path(sys.argv[1])
    if not path.exists():
        print(f"ERROR: file not found: {path}", file=sys.stderr)
        return 2

    text = path.read_text(encoding="utf-8")
    text_lower = lower(text)

    failures: list[str] = []

    for field in REQUIRED_FIELDS:
        if field.lower() not in text_lower:
            failures.append(f"missing required output header field: {field}")

    for pattern in UNSAFE_PATTERNS:
        for match in re.finditer(pattern, text_lower):
            if not has_safe_context(text, match.start()):
                failures.append(f"unsafe certainty phrase without nearby safe context: {match.group(0)!r}")

    payloads = parse_payloads(text)
    failures.extend(check_dl27_invariants(payloads))

    if failures:
        print(f"FAIL: {path} failed PFC output enforcement")
        for failure in failures:
            print(f"- {failure}")
        if any(DL27_ID in failure for failure in failures):
            print("TRIP: enforcement-output-gate.kiro.hook")
        return 1

    print(f"PASS: {path} satisfies PFC output enforcement")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
