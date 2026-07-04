---
name: planning-financial-control
displayName: Planning & Financial Control
description: Coordinate timeline planning, resource allocation, cost forecasting, reporting, intake, context loading, and evidence guardrails through a linked Project Control Graph.
keywords:
  - planning
  - finance
  - budget
  - forecast
  - resource
  - timeline
  - milestone
  - report
  - RAG
  - project control
  - PM
version: 0.1.0
author: DW
---

# Planning & Financial Control Power

## Purpose

Use this Power when the user asks to plan project timeline, allocate resources, calculate cost/budget impact, build delivery reports, assess change impact, or manage planning-finance cascade.

## Core operating model

```txt
Power Controller
  -> Intake Gate
  -> Project Control Graph
  -> Skill Routing
  -> Cascade Check
  -> Context Audit
  -> Fact Check
  -> Output Template
  -> Checkpoint
```

## Source of truth

The source of truth is not the chat and not the Power knowledge base.

The source of truth is the workspace graph:

```txt
.pm/control/project-control.yaml
```

## Required graph chain

```txt
WP -> MS -> RA -> COST -> FCST -> RPT
```

Where:

```txt
WP    = Work Package
MS    = Milestone
RA    = Resource Allocation
COST  = Cost Line
FCST  = Forecast
RPT   = Report
```

Every important node should link to at least one of:

```txt
Evidence
Assumption
Decision
Risk
Change Request
Baseline Version
```

## Skills

Primary skills:

```txt
timeline-planning
resource-planning-allocation
cost-calculator
report-builder
```

Control skills:

```txt
intake-gate
cascade-impact-check
context-audit
fact-check
```

## Operating modes

| Mode | Use when | Allowed | Blocked |
|---|---|---|---|
| M0 Empty Start | only idea/project name exists | skeleton, questions, assumptions | RAG, cost forecast, official report |
| M1 Rough Planning | rough scope/timeline exists | draft timeline, rough resource demand | official budget status, controlled baseline |
| M2 Forecast Ready | resource/rate/budget enough | forecast, variance, impact assessment | official baseline unless approved |
| M3 Controlled Baseline | approved baseline/evidence exists | RAG, executive report, change control | unsupported claims |

## Intake behavior

1. Ask maximum 5 questions per turn.
2. Accept `unknown` as a valid answer.
3. Continue in assumption mode when safe.
4. Log missing data.
5. Never present draft output as approved baseline.

## Guardrails

```txt
No evidence -> mark assumption
No baseline -> no official RAG
No resource/rate data -> no reliable cost forecast
No source IDs -> no report claim
No decision log -> no approved commitment
History is benchmark only unless approved as evidence
```

## Output control

Every important output must include:

```txt
Mode
Confidence
Allowed use
Blocked claims
Source graph nodes
Evidence used
Assumptions
Missing data
Decisions needed
```

## Onboarding

When first used in a workspace:

1. Check if `.pm/control/project-control.yaml` exists.
2. If missing, run Intake Gate.
3. Create graph skeleton from `templates/project-control.yaml`.
4. Create `.pm/intake/project-intake.yaml`.
5. Score readiness using `templates/readiness-score.md`.
6. Select mode M0/M1/M2/M3.
7. Run only workflows allowed by that mode.

## Final principle

```txt
Start useful. Stay honest. Upgrade confidence only when evidence improves.
```
