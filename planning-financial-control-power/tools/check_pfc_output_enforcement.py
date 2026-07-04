#!/usr/bin/env python3
"""Check a PFC output/report against mandatory enforcement headers and unsafe claims.

Usage:
  python tools/check_pfc_output_enforcement.py path/to/output.md

This is a lightweight static checker. It does not prove correctness. It catches common unsafe omissions:
- missing required output header fields
- unsupported certainty phrases
- budget/RAG claims without visible blocked-claim/guardrail context
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

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


def lower(text: str) -> str:
    return text.lower()


def has_safe_context(text: str, match_start: int) -> bool:
    window_start = max(0, match_start - 300)
    window_end = min(len(text), match_start + 300)
    window = lower(text[window_start:window_end])
    return any(marker in window for marker in SAFE_CONTEXT_MARKERS)


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: check_pfc_output_enforcement.py <output.md|txt>", file=sys.stderr)
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

    if failures:
        print(f"FAIL: {path} failed PFC output enforcement")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print(f"PASS: {path} satisfies lightweight PFC output enforcement")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
