---
name: resource-planning-allocation
description: Map work packages and milestones to role/FTE/capacity allocations and detect resource conflicts.
---

# Resource Planning & Allocation Skill

## Purpose

Create and update resource allocation nodes in the Project Control Graph.

## Reads

```txt
work_packages
milestones
dependencies
resource_allocations
capacity
risks
assumptions
```

## Writes

```txt
resource_allocations
resource_conflicts
capacity_risks
missing_data
```

## Must not do

```txt
Do not approve timeline.
Do not approve cost.
Do not set overall project status alone.
```

## Required output

```txt
role_demand
allocation_changes
capacity_conflicts
timeline_feasibility_signal
cost_recalculation_required
confidence
missing_data
```

## Trigger cascade

When allocation, FTE, duration, capacity, or role changes:

```txt
cost-calculator
timeline-planning if feasibility is impacted
report-builder
fact-check
```

## Guardrail

Do not state resource feasibility without allocation period, capacity, and linked milestone context.
