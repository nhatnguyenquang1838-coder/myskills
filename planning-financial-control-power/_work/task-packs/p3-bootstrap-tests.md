# Task Pack P3 — Bootstrap and Tests

## Goal

Make the Power installable into a clean workspace and prove the core runtime with dry-run tests.

## Bootstrap tasks

| ID | Task | Output |
|---|---|---|
| BST-01 | Add Linux/macOS install script | `scripts/install-workspace.sh` |
| BST-02 | Add Windows install script | `scripts/install-workspace.ps1` |
| BST-03 | Add workspace structure template | `.pm` folders from `templates/` |
| BST-04 | Add bootstrap README | `scripts/README.md` |

## Test tasks

| ID | Task | Output |
|---|---|---|
| TST-01 | Add UC-00 baseline dry-run | `tests/scenarios/uc-00-baseline-dry-run.md` |
| TST-02 | Add contract-driven expected output | `tests/expected-outputs/contract-driven-execution.md` |
| TST-03 | Add executive report breaker expected output | `tests/expected-outputs/executive-report-breaker.md` |
| TST-04 | Add milestone delay expected output | `tests/expected-outputs/milestone-delay-cascade.md` |

## Exit criteria

```txt
[ ] Clean workspace gets `.pm/` skeleton.
[ ] UC-00 dry-run documents expected behavior.
[ ] Contract-driven execution has expected output.
[ ] Executive report breaker blocks unsupported claims.
```
