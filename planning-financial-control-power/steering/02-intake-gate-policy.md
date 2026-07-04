# 02 — Intake Gate Policy

## Purpose

The Power must work even when users do not have enough material.

## Gate sequence

```txt
G0 Intent Gate
G1 Material Discovery Gate
G2 Minimum Viable Data Gate
G3 Readiness Scoring Gate
G4 Mode Selection Gate
G5 Skill Execution Gate
G6 Output Quality Gate
```

## Intent types

```txt
create_new_plan
update_existing_plan
allocate_resource
calculate_budget
build_report
assess_change_impact
recover_missing_data
```

## Minimum viable data

### Planning

```txt
project/objective
target date or time constraint
work packages or rough scope
known dependencies
```

### Resource

```txt
work packages
roles or team names
rough duration
capacity constraint if known
```

### Finance

```txt
resource allocation or effort
rate card or rate assumption
budget or cost cap if available
```

### Report

```txt
audience
reporting period
current graph nodes or status source
```

## Readiness modes

| Mode | Condition | Allowed | Blocked |
|---|---|---|---|
| M0 | idea only | skeleton, questions | RAG, forecast |
| M1 | rough scope/timeline | draft plan/resource/report | official budget status |
| M2 | resource/rate/budget enough | forecast/variance | approved baseline |
| M3 | approved evidence/baseline | RAG, executive report | unsupported claims |

## Missing data handling

Missing data does not block all work. It limits confidence and output type.
