# Task Pack P0 — Foundation

## Goal

Close the minimum foundation gaps needed before the Power can be called live.

## Tasks

| ID | Task | Output | Done when |
|---|---|---|---|
| FND-01 | Add run graph policy | `steering/16-run-graph-policy.md` | policy explains persistent graph, run graph, draft delta, write-back |
| FND-02 | Add complex UC gate | `steering/17-complex-use-case-gate.md` | complex UCs require baseline/readiness/node-chain check |
| FND-03 | Add UC-00 baseline standard | `knowledge/use-cases/uc-00-create-controlled-baseline-standard.md` | baseline creation has full standard schema |
| FND-04 | Update README live usage | `README.md` | user can understand install/run/live status |
| FND-05 | Rescore readiness | `tests/readiness-scorecard.md` | score reflects P0 completion |

## Execution order

```txt
FND-01 -> FND-02 -> FND-03 -> FND-04 -> FND-05
```

## Exit criteria

```txt
[ ] Standards define how the Power runs.
[ ] Complex UCs cannot bypass baseline gate.
[ ] UC-00 baseline standard exists.
[ ] README points to live path.
```
