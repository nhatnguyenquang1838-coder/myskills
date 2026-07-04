---
name: context-audit
description: Check that loaded context is current, linked, relevant, and not biased by stale or historical data.
---

# Context Audit Skill

## Purpose

Prevent wrong context from driving planning and finance conclusions.

## Reads

```txt
loaded_context
project_control_graph
history_index
retrieval_log
baseline_version
```

## Writes

```txt
context_audit_result
stale_context_flags
bias_risk_flags
retrieval_log_updates
```

## Checks

```txt
current baseline loaded
context linked to target graph node
history labeled as benchmark only
raw archive not used as current fact
old baseline not overriding current baseline
missing source IDs flagged
```

## Output

```txt
PASS or FAIL
loaded_context_table
bias_risks
stale_context
required_fix
```
