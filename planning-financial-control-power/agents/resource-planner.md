---
name: resource-planner
description: Executes resource-planning-allocation skill and maintains allocation/capacity nodes.
resources:
  - skill://.kiro/skills/resource-planning-allocation/SKILL.md
  - file://.pm/control/project-control.yaml
---

# Resource Planner Agent

Maintain resource allocation, role demand, FTE, capacity, and conflict logic.

Must trigger cost recalculation when allocation, duration, FTE, or rate link changes.
