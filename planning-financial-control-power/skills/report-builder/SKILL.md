---
name: report-builder
description: Build weekly, executive, and change-impact reports from linked Project Control Graph nodes.
---

# Report Builder Skill

## Purpose

Generate reports as views from the Project Control Graph.

## Reads

```txt
milestones
resource_allocations
forecasts
risks
decisions
assumptions
evidence
change_requests
missing_data
```

## Writes

```txt
reports
executive_summary
weekly_status
decisions_needed
```

## Must not do

```txt
Do not invent status.
Do not use history as current fact.
Do not write unsupported RAG/date/cost/resource claims.
```

## Required report sections

```txt
Output Control
Overall RAG
Timeline status
Resource status
Budget status
Key changes
Risks/issues
Decisions needed
Assumptions
Missing data
Evidence used
```

## Guardrail

Every RAG/date/cost/resource claim must reference graph node IDs.
