# Checkpoint — Convergence, Tiered Hooks, Context Isolation, BCBS239 Invariants

Date: 2026-07-04
Scope: Resolve runtime execution bottlenecks, context window exhaustion risk, and deterministic BCBS239 enforcement gaps.

## Implemented

```txt
Bounded-Convergence-Loop with MAX_ITERATIONS = 3
State Lock mechanism for Project Control Graph write path
Tiered hook schema with execution_tier = blocking | async
Tiered hook validation/execution utility behavior
Circuit Breaker context isolation directive
Memory Context Controller Isolate-and-Condense function
BCBS239 principle tags required in semantic action logs
Deterministic DL-27 finance total invariant checks
```

## Updated files

```txt
steering/16-run-graph-policy.md
knowledge/runtime/pfc-runtime-execution-engine.md
schemas/kiro-hook.schema.json
steering/20-logging-depth-policy.md
tools/validate_kiro_hooks.py
hooks/kiro-v1/pfc-workspace-hooks.json
steering/11-circuit-breaker-policy.md
knowledge/support/memory-context-controller.md
templates/circuit-breaker-log.md
schemas/agent-action-log.schema.json
tools/kiro_safe_logging.py
tools/check_pfc_output_enforcement.py
README.md
_work/TASKS.md
```

## Runtime execution changes

### Bounded-Convergence-Loop

```txt
MAX_ITERATIONS = 3
Agents return draft deltas only.
PM Controller compares deltas, not prose.
No convergence after iteration 3 -> block/downgrade; do not invent compromise.
```

### State Lock

```txt
Recommended lock file: .pm/control/.project-control.lock
Only PM Controller acquires/releases lock.
Before write-back, state_hash_before must still match.
Concurrent write or stale hash -> Contract/Baseline breaker.
```

### Tiered hooks

```txt
Tier 1 blocking: deterministic structural checks on critical path.
Tier 2 async: heavy qualitative audits in background.
```

### Circuit Breaker recovery

```txt
Never pass full trailing conversational history after breaker trip.
Use Isolate-and-Condense packet only:
1. 2-sentence failure summary
2. exact breached constraint
3. structured circuit-breaker log
```

### BCBS239 invariants

```txt
Semantic action log now requires bcbs239_principle_tag.
Valid tags map to knowledge/references/bcbs239/*.md.
DL-27 finance output must reconcile array totals to declared total budget/amount.
Failed invariant prints: TRIP: enforcement-output-gate.kiro.hook
```

## Remaining validation required

```txt
Run clean-checkout validators.
Run validate_kiro_hooks.py against native hook bundle.
Run deterministic DL-27 passing/failing fixtures.
Pilot State Lock under concurrent Kiro workflow.
Pilot Isolate-and-Condense after a real breaker trip.
```
