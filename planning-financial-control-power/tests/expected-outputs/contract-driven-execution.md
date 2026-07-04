# Expected Output — Contract-Driven Execution

## Expected control header

```txt
Mode: M2 Forecast Ready
Run type: draft
Use case: planning + finance forecast
Contracts used:
- DL-11-PLAN-release-milestone-planner
- DL-27-FIN-project-cost-calculator
Skills called:
- release milestone planner
- project cost calculator
Graph nodes read:
- WP
- DEP
- RA
- RATE
- ASM
- EVD
Graph deltas proposed:
- MS
- COST
- FCST
- ASM/MD if needed
Graph nodes written:
- none unless user approves
Circuit breaker state: HALF_OPEN or CLOSED depending on budget basis
Allowed output: draft milestone plan and forecast
Blocked claims:
- approved baseline unless M3
- budget RAG if approved budget/threshold missing
Next action: approve write-back or provide missing finance/baseline data
```

## Expected behavior

```txt
The Power validates DL Skill contracts before calling them.
The Power validates returned outputs before using them.
DL Skills return draft deltas only.
The Power blocks official budget status if budget basis is incomplete.
```

## Failure behavior

If required contract is missing:

```txt
Circuit Breaker: Contract breaker OPEN
Blocked: controlled workflow
Allowed fallback: draft checklist of missing contracts
```

If cost basis is missing:

```txt
Circuit Breaker: Finance breaker HALF_OPEN/OPEN
Blocked: reliable forecast, budget status
Allowed fallback: cost assumption or missing finance data checklist
```
