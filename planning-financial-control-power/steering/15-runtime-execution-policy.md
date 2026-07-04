# 15 — Runtime Execution Policy

## Purpose

Define how the Power runs any user request using graph-aware orchestration and external DL Skill contracts.

## Runtime sequence

```txt
1. Receive user request.
2. Resolve use case.
3. Select readiness mode.
4. Build Run Context Graph.
5. Select DL Skill contracts.
6. Validate preconditions.
7. Execute DL Skills as black boxes.
8. Validate outputs.
9. Build draft graph delta.
10. Run cascade/context/fact/bias/hallucination checks.
11. Run Circuit Breaker.
12. Decide output or write-back.
13. Create checkpoint/audit if needed.
```

## Run Context Graph rule

```txt
Every meaningful run must have a Run Context Graph.
The Run Context Graph is temporary.
It does not replace the persistent Project Control Graph.
```

## Skill execution rule

```txt
No skill call without contract validation.
No output trust without result validation.
No graph write-back without Power approval.
```

## Draft delta rule

DL Skill outputs may create draft deltas only.

```txt
DL Skill output -> draft graph delta -> Power validation -> approved write-back or discard
```

## Required checks

| Situation | Required check |
|---|---|
| Any output claim | fact-check |
| Any context/memory use | context-audit |
| Any changed graph node | cascade-impact-check |
| Any official report/baseline/forecast | circuit-breaker |
| Any historical benchmark | history-bias check |
| Any cost/budget claim | finance breaker |

## Output rule

Every runtime output must state:

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

## Failure rule

When runtime cannot proceed safely:

```txt
1. Stop official path.
2. Downgrade if draft/scenario is safe.
3. Open relevant breaker.
4. Explain missing data or failed contract.
5. Ask only critical recovery questions.
```
