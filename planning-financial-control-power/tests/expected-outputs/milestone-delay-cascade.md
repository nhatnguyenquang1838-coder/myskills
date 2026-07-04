# Expected Output — Milestone Delay Cascade

## Input pattern

```txt
MS-001 is delayed by 2 weeks because vendor API is late.
```

## Expected control header

```txt
Mode: M1/M2/M3 depending on baseline readiness
Run type: draft or controlled_update
Use case: UC-22 Assess Milestone Delay
Contracts used:
- DL-11-PLAN-release-milestone-planner
- DL-12-PLAN-resource-allocator
- DL-27-FIN-project-cost-calculator
- DL-26-RPT-report-builder
Skills called:
- release milestone planner
- resource allocator
- project cost calculator
- report builder
Graph nodes read:
- MS-001
- linked WP
- linked RA
- linked COST
- linked FCST
- linked RPT
- linked RISK/ASM/EVD/DEC
Graph deltas proposed:
- MS date delta
- RA extension/conflict signal
- COST delta
- FCST delta
- RPT draft impact
- CR if user asks for change control
Graph nodes written:
- none unless user approves
Circuit breaker state: CLOSED, HALF_OPEN, or OPEN depending on cascade completeness
Allowed output:
- change-impact assessment
Blocked claims:
- no report update until cascade complete
- no no-cost-impact claim unless cost recalculated
Next action:
- approve draft delta or provide missing resource/cost data
```

## Expected breaker behavior

If linked RA/COST/FCST are not checked:

```txt
Circuit Breaker: Cascade breaker OPEN
Blocked: official report update
Allowed fallback: draft timeline-only impact with missing cascade data
```

If cost basis is missing:

```txt
Circuit Breaker: Finance breaker HALF_OPEN
Blocked: final cost impact
Allowed fallback: cost assumption range or missing finance data
```
