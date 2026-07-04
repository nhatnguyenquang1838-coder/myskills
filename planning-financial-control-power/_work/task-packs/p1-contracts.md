# Task Pack P1 — DL Skill Contracts

## Goal

Create minimum full contracts for the DL Skills required to make v0.2 live.

## Required P0 contracts

| ID | DL Skill | Output file |
|---|---|---|
| CTR-01 | DL-00-CORE-cognitive-intake-gate | `contracts/dl-skills/DL-00-CORE-cognitive-intake-gate.yaml` |
| CTR-02 | DL-11-PLAN-release-milestone-planner | `contracts/dl-skills/DL-11-PLAN-release-milestone-planner.yaml` |
| CTR-03 | DL-12-PLAN-resource-allocator | `contracts/dl-skills/DL-12-PLAN-resource-allocator.yaml` |
| CTR-04 | DL-27-FIN-project-cost-calculator | `contracts/dl-skills/DL-27-FIN-project-cost-calculator.yaml` |
| CTR-05 | DL-26-RPT-report-builder | `contracts/dl-skills/DL-26-RPT-report-builder.yaml` |

## Minimum contract quality

Each contract must include:

```txt
purpose
input_contract
output_contract
preconditions
postconditions
constraints
failure_modes
control_requirements
evidence_rule
pfc_integration
```

## Exit criteria

```txt
[ ] All P0 contracts exist.
[ ] All P0 contracts validate against schema.
[ ] Each contract declares forbidden claims.
[ ] Each contract declares graph nodes read and draft deltas.
[ ] Each contract declares required circuit breakers.
```
