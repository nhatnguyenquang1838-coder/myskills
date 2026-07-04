# 04 — Cascade Rules

## Purpose

Planning and finance changes must propagate through the graph.

## Cascade engine

```txt
Changed node -> linked nodes -> required skills -> report refresh -> fact check
```

## Cascade matrix

| Changed item | Must check |
|---|---|
| Work package | Timeline, resource, cost, report |
| Milestone | Resource, cost, report |
| Dependency | Timeline, risk, report |
| Resource allocation | Timeline feasibility, cost, report |
| Rate card | Cost, forecast, report |
| Budget | Forecast, RAG, report |
| Risk | Linked timeline/resource/cost, report |
| Decision | Any linked node |
| Assumption | Any dependent calculation/report |

## Required sequence for milestone change

```txt
1. timeline-planning
2. resource-planning-allocation
3. cost-calculator
4. report-builder
5. fact-check
```

## Required output from cascade check

```txt
changed_nodes
affected_nodes
required_skills
blocked_claims
missing_data
next_actions
```

## Rule

Do not update report status without checking all linked nodes.
