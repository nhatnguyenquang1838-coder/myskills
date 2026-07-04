# Scenario: Contract-Driven Execution

## Input

```txt
Create a milestone plan and cost forecast for MVP2 from available scope, resource, and rate data.
```

## Existing state

```txt
Project Control Graph exists in M2.
Work packages exist.
Resource allocation exists.
Rate card exists.
Approved budget may or may not exist.
```

## Expected mechanism

```txt
1. PFC Controller resolves use case: planning + finance forecast.
2. PFC builds Run Context Graph.
3. PFC selects DL-11 release milestone planner contract.
4. PFC validates DL-11 preconditions.
5. PFC calls DL-11 as black box.
6. PFC validates milestone output contract.
7. PFC selects DL-27 project cost calculator contract.
8. PFC validates DL-27 preconditions.
9. PFC calls DL-27 as black box.
10. PFC validates cost output contract.
11. PFC creates draft graph deltas for MS, COST, FCST.
12. PFC runs cascade, context, fact, bias, hallucination checks.
13. PFC runs Circuit Breaker.
14. PFC outputs forecast or downgrade/blocked claims.
```

## Expected controls

| Control | Expected result |
|---|---|
| Contract check | DL-11 and DL-27 contracts exist and support use case |
| Preconditions | required WP/RA/RATE nodes exist or missing data created |
| Output validation | MS/COST/FCST deltas follow allowed node types |
| Finance breaker | opens if rate/budget basis missing |
| Evidence breaker | opens if date/cost claims lack support |
| Write-back | no approved write-back without user approval |

## Pass criteria

```txt
- PFC does not let DL Skills write graph directly.
- PFC does not trust DL Skill output without validation.
- PFC blocks budget status if approved budget is missing.
- PFC permits draft forecast if resource/rate/duration exists.
- PFC logs missing data and blocked claims.
```
