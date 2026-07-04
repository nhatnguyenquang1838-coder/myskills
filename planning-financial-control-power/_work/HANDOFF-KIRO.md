# KIRO HANDOFF: PFC Power Architecture Hardening & Optimization

Repo: `nhatnguyenquang1838-coder/myskills`

Target package: `planning-financial-control-power/`

Target local path in Kiro workspace: `myskills-main/planning-financial-control-power`

## Mission

Refactor the runtime execution engine, memory controllers, hook execution model, logging discipline, and schema validation layers to resolve execution bottlenecks, prevent context window exhaustion, and enforce deterministic BCBS 239-aligned controls.

This is an architecture-hardening task. Do not rewrite the entire Power. Do not rebuild the external DL Skill base. DL Skills remain black-box capabilities consumed through contracts.

## Read first

Read these files before changing anything:

```txt
_work/CONVERSATION-WRAP-UP-2026-07-04.md
README.md
_work/TASKS.md
_work/RISKS.md
_work/DECISIONS.md
steering/11-circuit-breaker-policy.md
steering/16-run-graph-policy.md
steering/18-workflow-enforcement-policy.md
steering/19-agent-action-logging-policy.md
steering/20-logging-depth-policy.md
knowledge/runtime/pfc-runtime-execution-engine.md
knowledge/support/memory-context-controller.md
schemas/agent-action-log.schema.json
schemas/dl-skill-contract.schema.json
contracts/dl-skill-contract-schema.yaml
templates/circuit-breaker-log.md
tools/check_pfc_output_enforcement.py
tools/kiro_safe_logging.py
knowledge/references/bcbs239/
```

## Current baseline

```txt
Status: stronger MVP-live candidate
Readiness: 3.91 / 5
Remaining blockers:
- BLOCKER-06: hooks not schema-verified
- BLOCKER-07: validators not yet run in clean local checkout
- BLOCKER-08: bootstrap not tested in real target workspace
- BLOCKER-10: logging smoke test not yet run in clean workspace
```

## Non-negotiable guardrails

```txt
No baseline -> no official RAG
No resource + rate + budget -> no budget status
No evidence -> no confirmed claim
No decision -> no approval claim
No contract -> no controlled skill call
History = benchmark only
DL Skills return draft deltas only
Only PFC writes approved deltas
MCP stdio tools must not write diagnostics to stdout
Parallel runs must write to per-run log files
Do not mark hooks production-ready unless schema is verified
```

---

# TASK 1 — Implement Multi-Agent Convergence Loops / State Negotiation

## Goal

Transition from a strict one-way cascading graph to a bounded negotiation loop to resolve cross-agent conflicts.

Examples:

```txt
budget cut -> resource reduction -> timeline delay -> cost reforecast
rate-card increase -> budget pressure -> scope/timeline option tradeoff
milestone acceleration -> resource conflict -> finance impact
```

## Required changes

### 1. Update `steering/16-run-graph-policy.md`

Define a new execution pattern:

```txt
Bounded-Convergence-Loop
```

Required semantics:

```txt
MAX_ITERATIONS = 3
```

The loop allows bounded negotiation between agents such as:

```txt
finance-analyst <-> resource-planner
resource-planner <-> timeline-planner
pm-controller <-> pm-fact-checker
```

The loop must stop when one condition is true:

```txt
1. all changed graph deltas converge
2. MAX_ITERATIONS reached
3. Circuit Breaker opens
4. user decision is required
5. write-back is unsafe
```

Required output after convergence:

```txt
convergence_status: converged | not_converged | blocked | decision_required
iterations_used:
conflicts_resolved:
conflicts_remaining:
recommended_next_action:
```

### 2. Update `knowledge/runtime/pfc-runtime-execution-engine.md`

Introduce a `State Lock` mechanism.

When an agent is writing to:

```txt
templates/project-control.yaml
.pm/control/project-control.yaml
```

or proposing an approved graph write-back, state must be locked to prevent concurrent conflicting writes.

Required lock contract:

```txt
lock_id
run_id
owner_agent
locked_graph_nodes
lock_reason
created_at
expires_at
status: active | released | expired | blocked
```

Rules:

```txt
Only pm-controller can approve final write-back.
DL Skills and supporting agents may only propose draft deltas.
If lock exists, other agents must read current state but cannot write overlapping nodes.
If lock expires, pm-controller must re-check graph state before write-back.
```

---

# TASK 2 — Refactor Hooks to Tiered Asynchronous Execution

## Goal

Reduce blocking latency on the critical path by separating fast structural checks from heavy qualitative audits.

## Required changes

### 1. Update `schemas/kiro-hook.schema.json`

Add required property:

```yaml
execution_tier: blocking | async
```

Rules:

```txt
blocking = must complete before the semantic turn continues
async = can run after the semantic turn starts/continues and report result later
```

### 2. Modify `steering/20-logging-depth-policy.md`

Define hook execution tiers:

```txt
Tier 1 — blocking
- synchronous YAML/JSON structural validation
- graph schema check
- contract schema check
- baseline-upgrade-check.kiro.hook
- enforcement-preflight.kiro.hook when it blocks unsafe action

Tier 2 — async
- context-audit.kiro.hook
- workflow-gap-review.md driven audits
- heavy memory/history reviews
- long-running BCBS239 quality review
- non-critical scorecard enrichment
```

Rules:

```txt
Tier 1 failures can block the next action.
Tier 2 failures must create async audit result and may open follow-up blocker, but should not freeze the agent unless the result identifies S3/S4 severity.
```

### 3. Update or create `tools/validate_kiro_hooks.py`

Refactor the script to parse `execution_tier`.

Required behavior:

```txt
- validate that every hook declares execution_tier
- validate execution_tier is one of blocking|async
- fail if a blocking hook has no bounded timeout
- warn if async hook can mutate graph state directly
- enforce async hooks write results to .pm/audit/runs/{run_id}.* and do not block the main semantic turn
```

Do not overclaim true background execution unless Kiro hook runtime supports it. If actual Kiro async execution cannot be verified, document this as:

```txt
async policy defined; runtime executor pending Kiro schema verification
```

---

# TASK 3 — Fix Circuit Breaker Context Exhaustion Loops

## Goal

Prevent LLM hallucinations and token limit crashes after a circuit breaker trip by isolating failure context.

## Required changes

### 1. Update `steering/11-circuit-breaker-policy.md`

Add strict directive:

```txt
Never pass the full trailing conversational history to an agent after a Circuit Breaker trip.
```

Add failure-context rule:

```txt
After Circuit Breaker OPEN, all recovery prompts must use Isolate-and-Condense context.
```

### 2. Update `knowledge/support/memory-context-controller.md`

Implement an `Isolate-and-Condense` function.

When Circuit Breaker trips, Kiro must intercept the recovery prompt window, wipe/ignore the conversational memory buffer, and inject only:

```txt
1. A 2-sentence summary of the failure state.
2. The exact breached constraint from contracts/dl-skill-contract-schema.yaml or the relevant DL contract.
3. The structured error log from templates/circuit-breaker-log.md or .pm/audit/circuit-breaker-log.md.
```

Required output shape:

```yaml
isolate_and_condense:
  breaker_id:
  severity:
  failure_summary_2_sentences:
  breached_constraint:
  circuit_breaker_log_ref:
  allowed_recovery_actions:
  blocked_recovery_actions:
  context_excluded:
    - trailing_conversation_history
    - unrelated_memory
    - historical_benchmark_unless_requested
```

Rules:

```txt
No raw full chat history after breaker trip.
No broad memory scan after breaker trip.
No historical benchmark unless recovery explicitly asks for benchmark comparison.
Recovery must be bounded to the breached constraint and affected graph nodes.
```

---

# TASK 4 — Programmatic Invariants for BCBS239 Auditing

## Goal

Offload financial calculations from the LLM and enforce strict data lineage tagging for banking-standard compliance.

## Required changes

### 1. Update `schemas/agent-action-log.schema.json`

Add required property:

```yaml
bcbs239_principle_tag: array[string]
```

Valid values must map to reference files inside:

```txt
knowledge/references/bcbs239/
```

Allowed starter values:

```txt
01-governance-and-infrastructure
02-risk-data-aggregation
03-risk-reporting-practices
04-supervisory-review-remediation
05-2023-progress-lessons
06-pfc-skill-guardrail-map
07-bcbs239-skill-contract-guidance
```

Required behavior:

```txt
Every semantic action log event must declare which BCBS239 guardrail family it touches.
If not applicable, use [] only for non-control debug events. For semantic PFC actions, empty tag is not allowed.
```

### 2. Update `tools/check_pfc_output_enforcement.py`

Add deterministic financial math invariants.

Minimum invariant:

```txt
For DL-27-FIN-project-cost-calculator.yaml output arrays, line-item amounts must sum exactly or within declared rounding tolerance to total budget / total forecast defined in the output payload.
```

If the math fails:

```txt
- fail the checker
- emit Finance breaker reason
- trigger/require enforcement-output-gate.kiro.hook before any graph commit
- block LLM write-back
```

Expected checker behavior:

```txt
PASS: totals match and every amount has derived_from/source_id
FAIL: total mismatch, missing derived_from, missing source_id, or unsupported budget status
```

Recommended implementation:

```txt
- keep existing text-header checks
- add JSON/YAML payload parser if output file contains fenced yaml/json block
- detect cost_line_items, forecast_line_items, total_budget, total_forecast
- compare Decimal totals, not float
- require derived_from or source_id on every financial line item
```

---

# Required Files to Update

Update at minimum:

```txt
steering/16-run-graph-policy.md
knowledge/runtime/pfc-runtime-execution-engine.md
schemas/kiro-hook.schema.json
steering/20-logging-depth-policy.md
tools/validate_kiro_hooks.py
steering/11-circuit-breaker-policy.md
knowledge/support/memory-context-controller.md
schemas/agent-action-log.schema.json
tools/check_pfc_output_enforcement.py
_work/TASKS.md
_work/RISKS.md
tests/readiness-scorecard.md
README.md
```

Add checkpoint:

```txt
checkpoints/YYYY-MM-DD-architecture-hardening.md
```

Checkpoint must include:

```txt
commands run
files changed
validation result
remaining blockers
readiness score before/after
known unverified assumptions
```

---

# Acceptance Criteria

```txt
[ ] Bounded-Convergence-Loop defined with MAX_ITERATIONS = 3
[ ] State Lock contract defined for graph write-back
[ ] Hook schema supports execution_tier
[ ] Hook validator checks blocking vs async hooks
[ ] Logging policy explains Tier 1 blocking and Tier 2 async hooks
[ ] Circuit Breaker recovery forbids full trailing conversation history
[ ] Memory Context Controller defines Isolate-and-Condense
[ ] Agent action log schema requires bcbs239_principle_tag for semantic events
[ ] Output checker validates deterministic finance totals using Decimal or equivalent
[ ] Failed finance invariant blocks write-back and opens/requires output enforcement gate
[ ] README/TASKS/RISKS/scorecard/checkpoint updated
```

Do not mark this complete unless deterministic checks are implemented or explicitly documented as pending.

---

# Final Response Expected from Kiro

Return:

```md
# Kiro Architecture Hardening Result — PFC Power

## Summary
## Commands Run
## Files Changed
## Validation Results
## Hook Schema Status
## Circuit Breaker / Memory Controller Changes
## BCBS239 / Finance Invariant Changes
## Remaining Blockers
## Readiness Score Before / After
## Recommendation

PASS / PARTIAL / FAIL
```

## Short instruction

```txt
Implement architecture hardening only. Do not expand features beyond the four tasks. Keep PFC as orchestrator, DL Skills as contracts. Validate deterministic controls before claiming readiness.
```
