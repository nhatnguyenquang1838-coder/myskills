# UC-01 Onboarding Output

## Required output header

```txt
Mode: M0 Empty Start
Run type: onboarding / draft
Use case: UC-01 — Start New Project With Idea Only
Agents used:
- pm-controller
Skills used:
- intake-gate
- memory-context-controller
- circuit-breaker
Hooks triggered:
- intake-completeness-check
Graph nodes read:
- none / existing graph if present
Graph nodes written:
- project
- work_packages
- assumptions
- missing_data
Circuit breaker state:
- Baseline breaker: OPEN
- Finance breaker: OPEN
- Evidence breaker: HALF_OPEN
Guardrails applied:
- no official RAG
- no controlled baseline
- no reliable forecast
- no approved timeline
Bias checks:
- no historical benchmark used as current truth
- no old project assumption copied
Hallucination checks:
- unknowns recorded as missing data
- assumptions labeled low confidence
Allowed output:
- draft project skeleton
- missing-data list
- next-step questions
Blocked claims:
- project is on track
- budget is sufficient
- timeline is approved
- resource plan is feasible
Next action:
- collect enough materials for UC-00 Create Full Controlled Baseline
```

## Draft response pattern

```md
Mode: M0 Empty Start  
Run type: onboarding / draft  
Use case: UC-01 — Start New Project With Idea Only

I created a draft project skeleton. This is not a controlled baseline.

## Captured

| Item | Value | Confidence |
|---|---|---|
| Project name | TBD | Low |
| Objective | TBD | Low |
| Timeline | Missing | None |
| Resource | Missing | None |
| Finance | Missing | None |

## Missing data

| ID | Missing item | Required for | Blocking level |
|---|---|---|---|
| MD-001 | Target timeline | Milestone planning | Limitation |
| MD-002 | Resource availability | Resource planning | Limitation |
| MD-003 | Budget or rate card | Cost forecast | Blocker |

## Blocked claims

- Official RAG
- Approved baseline
- Reliable cost forecast
- Confirmed resource feasibility

## Next questions

1. What is the main project objective?
2. Is there a target date or fixed deadline?
3. What are the main deliverables?
4. Which team or roles may be involved?
5. Is there any budget cap or rate assumption?
```
