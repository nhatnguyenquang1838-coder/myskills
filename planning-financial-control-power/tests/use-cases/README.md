# PFC Use Case Test Suite

Purpose: provide standardized test cases for the Planning & Financial Control Power.

These are not historical examples. They are controlled test scenarios.

## Files

| File | Purpose |
|---|---|
| `uc-test-suite-22.md` | 22 redefined use cases with scenario, mock input, graph state, expected controls, and expected result |
| `uc-test-matrix.yaml` | Machine-readable matrix for quick test planning and future automation |

## Test standard

Every UC test must define:

```txt
Use case ID
Scenario
Mock user input
Mock graph state
Expected mode
Expected run type
Expected contracts / skills
Expected graph reads
Expected graph writes or deltas
Expected guardrails
Expected circuit breaker behavior
Expected result
Pass criteria
```

## Execution rule

```txt
No UC test passes if the Power produces unsupported official RAG, budget, approval, baseline, or forecast claims.
```

## Output check

Every tested output should include:

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
