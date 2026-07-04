# Task Pack P2 — Validation

## Goal

Make the Power mechanically checkable before live use.

## Tasks

| ID | Task | Output | Done when |
|---|---|---|---|
| VAL-01 | Add Project Control Graph validator | `tools/validate_project_control.py` | validates sample YAML against schema |
| VAL-02 | Add DL Skill contract validator | `tools/validate_dl_contract.py` | validates P0 contracts against schema |
| VAL-03 | Add valid graph fixture | `tests/fixtures/valid-project-control.yaml` | passes validator |
| VAL-04 | Add invalid graph fixture | `tests/fixtures/invalid-project-control.yaml` | fails validator with clear errors |
| VAL-05 | Add validation README | `tools/README.md` | explains how to run validators |

## Exit criteria

```txt
[ ] Valid graph passes.
[ ] Invalid graph fails.
[ ] Valid contracts pass.
[ ] Missing required fields fail.
[ ] README documents local validation commands.
```
