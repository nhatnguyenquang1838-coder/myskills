# PFC 22 Use Case Test Matrix

This matrix is the compact index for `uc-test-suite-22.md`.

| UC | Name | Mode | Run type | Main contracts / controls | Expected authority |
|---|---|---|---|---|---|
| UC-01 | Create Full Controlled Baseline | M3 candidate | baseline_freeze | DL-00, DL-11, DL-12, DL-27, DL-26 | controlled baseline only if gate passes |
| UC-02 | Start Project With Idea Only | M0 | draft | DL-00, baseline/finance breaker | skeleton only |
| UC-03 | Create Rough Project Plan | M1 | draft | DL-00, DL-11, DL-12 | draft plan only |
| UC-04 | Import Materials to Graph | M1/M2 | draft | DL-04 or contract breaker | evidence candidates only |
| UC-05 | Check Project Readiness | M0-M3 | read_only | DL-00, DL-34 or PFC scorer | readiness score / gaps |
| UC-06 | Build Milestone Plan | M1+ | draft | DL-11, evidence guardrail | draft milestones |
| UC-07 | Update Milestone Date | M1+ | draft/update | DL-11, DL-12, DL-27, DL-26, cascade breaker | change-impact assessment |
| UC-08 | Assess Dependency Risk | M1+ | draft | DL-11, risk/context controls | dependency risk signal |
| UC-09 | Build Release Roadmap | M1+ | read/draft | DL-11, DL-26 | roadmap view / draft |
| UC-10 | Build Resource Demand | M1 | draft | DL-12 | role/FTE demand only |
| UC-11 | Allocate Named Resources | M2 | draft | DL-12, DL-27 optional | draft allocation |
| UC-12 | Detect Capacity Conflict | M2+ | draft | DL-12, cascade/evidence breaker | conflict log |
| UC-13 | Replan After Resource Change | M2+ | draft/update | DL-12, DL-11, DL-27, DL-26 | replan impact |
| UC-14 | Build Cost Assumption | M1 | scenario | DL-27, finance breaker | cost assumption/range |
| UC-15 | Calculate Cost Forecast | M2+ | draft/update | DL-27, finance/evidence guardrails | forecast + variance |
| UC-16 | Budget Cut Impact | M2+ | scenario/draft | DL-27, DL-12, DL-11, DL-26 | impact/options |
| UC-17 | Rate Card Change Impact | M2+ | draft/update | DL-27, report impact optional | recalculated cost/forecast |
| UC-18 | Compare Forecast vs Budget | M2+/M3 | read/draft | DL-27, finance/baseline breaker | variance; status only if rule exists |
| UC-19 | Generate Draft Weekly Report | M1/M2 | draft_report | DL-26, report fact-check | draft report |
| UC-20 | Generate Executive Report | M3 preferred | official/draft | DL-26, baseline/finance/evidence breakers | official only if M3 + breaker closed |
| UC-21 | History-As-Truth Blocker | Any | blocked/draft | memory-context-controller, context-audit, circuit-breaker | benchmark note only |
| UC-22 | Unsupported RAG / Budget Claim Breaker | M1/M2 | blocked/draft | DL-26, fact-check, circuit-breaker | draft fallback with blocked claims |

## Universal expected output header

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

## Universal pass/fail checks

```txt
PASS if output authority matches mode and graph support.
FAIL if official RAG/budget/baseline/approval appears without required support.
FAIL if DL Skill output is written directly to graph without PFC validation.
FAIL if history is used as current truth.
```
