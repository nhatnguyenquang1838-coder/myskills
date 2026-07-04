# PFC Output Enforcement Checker

Tool:

```txt
tools/check_pfc_output_enforcement.py
```

## Purpose

Lightweight static check for Power outputs and reports.

It checks:

```txt
required output header fields
unsafe certainty phrases
unsupported RAG/budget/approval wording
```

## Usage

```bash
python tools/check_pfc_output_enforcement.py path/to/output.md
```

## Required header fields

```txt
Mode:
Run type:
Use case:
Contracts used:
Skills called:
Graph nodes read:
Graph deltas proposed:
Circuit breaker state:
Allowed output:
Blocked claims:
Next action:
```

## Important limitation

This checker does not prove semantic correctness.

It only catches common enforcement omissions before manual review.

## Recommended test flow

```txt
1. Generate UC output.
2. Run this checker.
3. Review with uc-enforcement-checklist.md.
4. Record result in uc-enforcement-test-results.md.
```
