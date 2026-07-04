# 16 — Run Graph Policy

## Purpose

Define how the Power uses graph context during every execution.

## Core rule

```txt
Every meaningful run must be graph-aware.
Not every run mutates the persistent graph.
```

## Graph levels

| Level | Name | Persistence | Purpose |
|---|---|---|---|
| L1 | Project Control Graph | persistent | source of truth for the workspace/project |
| L2 | Run Context Graph | temporary | scoped graph view for one request |
| L3 | Run Trace / Checkpoint | persistent audit | record what was loaded, proposed, blocked, written |

## Persistent Project Control Graph

Stored in target workspace:

```txt
.pm/control/project-control.yaml
```

Purpose:

```txt
Contains current project truth: scope, timeline, resource, cost, forecast, risks, assumptions, evidence, decisions, and baseline version.
```

## Run Context Graph

A temporary subgraph built for each meaningful run.

Example:

```txt
User asks about MS-001 delay
-> load MS-001
-> load linked WP, RA, COST, FCST, RPT, RISK, ASM, EVD, DEC
```

The Run Context Graph must be scoped, not broad.

```txt
Load by graph IDs and links.
Do not scan all folders by default.
```

## Run Trace / Checkpoint

Meaningful runs must record:

```txt
use case
mode
run type
graph nodes read
graph deltas proposed
contracts used
skills called
controls applied
breaker state
write-back decision
```

Use:

```txt
templates/run-execution-record.md
```

## Run types

| Run type | Description | Write behavior |
|---|---|---|
| read_only | answer from graph | no write |
| draft | propose draft delta | no persistent write unless approved |
| scenario | hypothetical analysis | no persistent write |
| controlled_update | approved update | write approved delta |
| baseline_freeze | freeze controlled baseline | write baseline version and checkpoint |

## Write-back rule

```txt
DL Skill output -> draft graph delta -> PFC validation -> approved write-back or discard
```

Only the PM Controller may write approved deltas to the Project Control Graph.

## Required run graph fields

Every Run Context Graph must state:

```txt
target_graph_ids
nodes_loaded
links_followed
memory_loaded
history_loaded
as_of_date
baseline_version
confidence
```

## Missing graph behavior

If no Project Control Graph exists:

```txt
1. Run Intake Gate.
2. Create M0 graph skeleton.
3. Record missing data.
4. Block official RAG/budget/baseline claims.
```

## Guardrails

```txt
No graph target -> ask or run intake
No linked nodes -> create missing-data item
No evidence/source -> mark as assumption
No approved decision -> no approval claim
No user approval -> no persistent write-back
```

## Circuit breaker triggers

| Trigger | Breaker |
|---|---|
| missing graph target for complex UC | Baseline breaker |
| stale graph context | Context breaker |
| changed node without cascade | Cascade breaker |
| graph write requested without approval | Contract/Baseline breaker |
| output claims unsupported by graph | Evidence breaker |

## Output requirement

Every meaningful output must include:

```txt
Run type:
Graph nodes read:
Graph deltas proposed:
Graph nodes written:
Write-back decision:
```
