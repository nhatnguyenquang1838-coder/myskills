---
name: memory-context-controller
description: Manage memory retrieval, validation, staleness, conflict handling, and graph-linked context loading.
---

# Memory Context Controller Skill

## Purpose

Retrieve memory safely and ensure it supports, not replaces, the Project Control Graph.

## Reads

```txt
user_request
target_graph_ids
project_control_graph
memory_index
history_index
context_retrieval_log
baseline_version
```

## Writes

```txt
selected_context
memory_conflicts
stale_memory_flags
retrieval_log_update
circuit_breaker_trigger
```

## Algorithm

```txt
1. Identify user intent.
2. Identify target graph nodes.
3. Load current graph nodes.
4. Load linked memories.
5. Check staleness.
6. Check conflicts.
7. Load history only if benchmark/scenario is needed.
8. Trigger Circuit Breaker if memory is unsafe.
9. Produce labeled context bundle.
```

## Output contract

```txt
target_graph_ids
current_nodes_loaded
memories_loaded
history_loaded
stale_items
conflicts
bias_risk
allowed_use
```

## Guardrail

Never use memory as current fact if it conflicts with approved baseline or current graph.
