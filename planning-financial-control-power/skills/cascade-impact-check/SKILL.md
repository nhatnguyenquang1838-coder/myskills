---
name: cascade-impact-check
description: Traverse linked Project Control Graph nodes after a planning, resource, cost, risk, decision, or assumption change.
---

# Cascade Impact Check Skill

## Purpose

Ensure planning and finance changes propagate through all affected graph nodes.

## Reads

```txt
changed_nodes
project_control_graph
cascade_rules
```

## Writes

```txt
cascade_impact_summary
affected_nodes
required_skills
blocked_claims
next_actions
```

## Algorithm

```txt
1. Identify changed node IDs.
2. Traverse direct links.
3. Traverse second-level links when needed.
4. Classify affected nodes.
5. Determine required skills.
6. Flag missing data and blocked claims.
7. Recommend next action.
```

## Output contract

```txt
changed_nodes
affected_nodes
cascade_path
skills_to_run
missing_data
blocked_claims
confidence
```
