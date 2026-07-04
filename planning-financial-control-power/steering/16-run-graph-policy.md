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
| bounded_convergence | bounded negotiation between conflicting agents | draft deltas only until convergence and approval |

## Execution patterns

| Pattern | Use when | Control rule |
|---|---|---|
| Linear cascade | one agent output feeds the next without conflict | validate each output then continue |
| Bounded-Convergence-Loop | two or more agents produce conflicting but negotiable deltas | negotiate up to `MAX_ITERATIONS = 3` then converge, downgrade, or block |

## Bounded-Convergence-Loop

Purpose:

```txt
Resolve cross-agent conflicts without creating unbounded reasoning loops or context exhaustion.
```

Typical cases:

```txt
budget cut -> finance-analyst proposes cost reduction
cost reduction -> resource-planner detects capacity/timeline risk
resource change -> timeline-planner proposes milestone delay
milestone delay -> finance-analyst recalculates forecast
```

Hard limit:

```txt
MAX_ITERATIONS = 3
```

Negotiation state:

```txt
iteration_number
participating_agents
conflict_summary
candidate_deltas
accepted_deltas
rejected_deltas
open_constraints
breaker_state
state_lock_id
```

Convergence rules:

```txt
1. Every agent reads the same Run Context Graph snapshot.
2. Every agent returns draft graph deltas only.
3. The PM Controller compares deltas, not raw prose.
4. The PM Controller accepts only deltas that satisfy graph schema, contract, BCBS239 lineage, and breaker controls.
5. If convergence is not reached after 3 iterations, stop negotiation and return a blocked/downgraded result.
```

Iteration behavior:

| Iteration | Purpose | Expected outcome |
|---:|---|---|
| 1 | independent proposals | identify conflicts |
| 2 | constrained revision | reduce conflict set |
| 3 | final settlement attempt | converge or block |

Stop conditions:

```txt
converged_delta_created
hard_constraint_breached
Circuit Breaker OPEN
MAX_ITERATIONS reached
state lock cannot be acquired
```

Output rule when no convergence:

```txt
Do not invent a compromise.
Return the remaining conflict set, blocked claims, and required decision.
```

## Write-back rule

```txt
DL Skill output -> draft graph delta -> PFC validation -> approved write-back or discard
```

Only the PM Controller may write approved deltas to the Project Control Graph.

During Bounded-Convergence-Loop, no participating agent may write to the persistent Project Control Graph directly.

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

For `bounded_convergence`, the Run Context Graph must also state:

```txt
convergence_loop_id
MAX_ITERATIONS
current_iteration
state_lock_id
agent_delta_versions
conflict_set
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
No convergence after MAX_ITERATIONS -> block or downgrade, never hallucinate settlement
```

## Circuit breaker triggers

| Trigger | Breaker |
|---|---|
| missing graph target for complex UC | Baseline breaker |
| stale graph context | Context breaker |
| changed node without cascade | Cascade breaker |
| graph write requested without approval | Contract/Baseline breaker |
| output claims unsupported by graph | Evidence breaker |
| convergence loop exceeds `MAX_ITERATIONS = 3` | Cascade/Contract breaker |
| parallel write attempted without state lock | Contract/Baseline breaker |

## Output requirement

Every meaningful output must include:

```txt
Run type:
Graph nodes read:
Graph deltas proposed:
Graph nodes written:
Write-back decision:
```

For `bounded_convergence`, output must also include:

```txt
Convergence loop ID:
Iterations used:
Agents involved:
Conflict set:
Accepted deltas:
Rejected deltas:
Remaining blocked claims:
State lock decision:
```
