# 10 — Checkpoint Policy

## Purpose

Keep design and project-control state auditable.

## Checkpoint types

| Type | Purpose |
|---|---|
| Design checkpoint | Snapshot Power design decisions |
| Project checkpoint | Snapshot Project Control Graph state |
| Report checkpoint | Snapshot published report inputs/outputs |
| Change checkpoint | Snapshot change impact |
| Baseline checkpoint | Freeze approved baseline |

## When checkpoint is required

```txt
before baseline upgrade
before executive/SteerCo report
before major change request
when history is used as benchmark
when readiness mode changes
```

## Checkpoint fields

```txt
date
mode
baseline_version
changed_nodes
affected_nodes
evidence_used
assumptions
missing_data
blocked_claims
decisions_needed
next_actions
```

## Git rule

For reusable Power design, checkpoints can be committed under:

```txt
chat-snapshots/
planning-financial-control-power/checkpoints/
```
