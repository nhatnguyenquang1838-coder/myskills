# Scenario — UC-00 Baseline Dry Run

## User request

```txt
Create a controlled baseline for MVP2 Telegram Notification from the available scope, milestone, resource, rate, budget, risk, and decision material.
```

## Expected PFC mechanism

```txt
1. Resolve use case: UC-00 Create Full Controlled Baseline.
2. Build Run Context Graph.
3. Validate required DL Skill contracts:
   - DL-00 intake
   - DL-11 milestone planner
   - DL-12 resource allocator
   - DL-27 cost calculator
   - DL-26 report builder
4. Validate graph node chain:
   WP -> MS -> RA -> COST -> FCST -> RPT
5. Validate support nodes:
   EVD, DEC, ASM, RISK, MD
6. Run schema validation.
7. Run cascade check.
8. Run fact check.
9. Run bias/hallucination check.
10. Run Circuit Breaker.
11. If CLOSED and user approves, write BL-001.
```

## Expected output authority

If all required material exists:

```txt
Mode: M3
Run type: baseline_freeze
Circuit breaker: CLOSED
Allowed output: controlled baseline BL-001
```

If finance material is missing:

```txt
Mode: M1/M2
Circuit breaker: Finance breaker HALF_OPEN or OPEN
Allowed output: draft baseline or forecast-ready draft
Blocked: official budget status, M3 baseline
```

## Required output header

```txt
Mode:
Run type:
Use case: UC-00 Create Full Controlled Baseline
Contracts used:
Skills called:
Graph nodes read:
Graph deltas proposed:
Graph nodes written:
Readiness score:
Circuit breaker state:
Allowed output:
Blocked claims:
Missing data:
Next action:
```

## Pass criteria

```txt
[ ] DL Skills do not write graph directly.
[ ] PFC validates contracts before calling skills.
[ ] PFC validates outputs after skills.
[ ] Unsupported baseline/budget/RAG claims are blocked.
[ ] Missing material creates MD-* items.
[ ] Controlled baseline only written after gate pass and approval.
```
