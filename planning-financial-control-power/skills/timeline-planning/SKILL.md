---
name: timeline-planning
description: Plan and update project milestones, dependencies, critical path, and timeline impact using the Project Control Graph.
---

# Timeline Planning Skill

## Purpose

Create or update timeline nodes in `.pm/control/project-control.yaml`.

## Reads

```txt
project
work_packages
milestones
dependencies
risks
decisions
assumptions
baseline_version
```

## Writes

```txt
milestones
dependencies
timeline_impact
change_requests
missing_data
```

## Must not do

```txt
Do not create final budget conclusion.
Do not say cost is fine.
Do not set overall RAG alone.
```

## Required output

```txt
changed_milestones
affected_work_packages
dependency_impact
confidence
required_cascade
missing_data
```

## Trigger cascade

When milestone dates, dependency status, or critical path changes:

```txt
resource-planning-allocation
cost-calculator
report-builder
fact-check
```

## Guardrail

Any date must link to evidence, assumption, decision, or baseline version.
