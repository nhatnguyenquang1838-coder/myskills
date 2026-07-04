# Planning & Financial Control Power — Readiness Scorecard

Last rescored: 2026-07-04
Version assessed: v0.2 draft after Kiro hook schema verification, bootstrap smoke, and logging smoke

## Scale

| Score | Meaning |
|---:|---|
| 0 | Not designed |
| 1 | Rough idea only |
| 2 | Structure drafted, weak linkage |
| 3 | Usable draft, incomplete guardrails/tests |
| 4 | Production-ready for personal/team use |
| 5 | Distribution-ready, documented, tested, versioned |

## Component readiness

| Component | Target | Previous Score | Rescore | Notes |
|---|---:|---:|---:|---|
| Final architecture | 4.5 | 4.0 | 4.0 | Architecture unchanged; runtime controls remain explicit |
| Project Control Graph | 5.0 | 3.9 | 3.9 | Schema/fixtures exist; full clean-checkout validation still open |
| Skills | 4.5 | 3.9 | 3.9 | P0 contracts exist; full clean-checkout contract validation still open |
| Intake / onboarding | 5.0 | 3.8 | 3.9 | Bootstrap smoke created `.pm/` and `.kiro/` runtime structure |
| Tools / MCP | 3.5 | 2.5 | 2.8 | Added Kiro hook validator; MCP still placeholder |
| Hooks | 4.0 | 3.2 | 3.8 | Kiro v1 schema verified; native hook bundle added and locally validated; IDE runtime still needs pilot verification |
| Knowledge base | 4.0 | 4.0 | 4.0 | Unchanged |
| Steering | 4.5 | 4.5 | 4.5 | Unchanged |
| Patterns | 4.0 | 3.6 | 3.6 | Unchanged |
| Context / history | 4.5 | 3.9 | 3.9 | Unchanged; memory-index validator still missing |
| Guardrails | 5.0 | 4.5 | 4.5 | Unchanged |
| Checkpoint / versioning | 4.0 | 3.6 | 3.7 | Added checkpoint for hook/bootstrap/logging smoke |
| Output templates | 4.5 | 4.1 | 4.1 | Unchanged |
| Circuit Breaker | 4.5 | 4.2 | 4.2 | Unchanged |
| Memory Context Controller | 4.5 | 3.8 | 3.8 | Schema still missing |
| Contract Runtime | 4.5 | 4.0 | 4.0 | Unchanged; validator run evidence still open |
| Bootstrap / Install | 4.0 | 3.5 | 3.9 | Linux bootstrap smoke passed and installs native Kiro hook JSON |
| Enforcement Layer | 4.5 | 4.0 | 4.0 | Enforcement hooks now available as Kiro v1 JSON; optional broad hooks disabled by default |

## Approximate readiness

Simple average across current scored components:

```txt
Approx readiness: 3.99 / 5
Status: MVP-live candidate; one clean-checkout validation blocker remains before team pilot
```

Practical interpretation:

```txt
The Power now has native Kiro v1 hook assets, a hook validator, bootstrap hook installation, and logging smoke evidence.
It is still not team-ready until graph/contract validators are run from a real clean checkout and Kiro IDE hook runtime behavior is observed during pilot use.
```

## Release gates

```txt
MVP usable:       >= 3.5 / 5
MVP live target:  >= 3.7 / 5
Team usable:      >= 4.0 / 5
Distributable:    >= 4.5 / 5
```

## Current decision

```txt
Current state: MVP-live candidate
Reason: schema-verified Kiro hook bundle exists, bootstrap installs hooks, logging smoke test passed, and checkpoint evidence was created.
Remaining blocker: full graph/contract validator run in clean local checkout.
```

## Completed from last target

```txt
DONE: Kiro hook schema verification
DONE: Kiro v1 hook JSON schema
DONE: native Kiro v1 hook bundle
DONE: Kiro hook validator
DONE: bootstrap installs .kiro/hooks/pfc-workspace-hooks.json
DONE: bootstrap smoke in target workspace
DONE: logging smoke in clean target workspace
DONE: checkpoint update
```

## Still missing for v0.3 team pilot

```txt
clean-checkout graph/contract validation transcript
memory-index schema validator
history-index template and schema
trap tests for hallucination / stale history / unsupported budget claim
full M0/M1/M2/M3 examples
scoring-rubric.md linking each score to supporting files and tests
Kiro IDE runtime observation for enabled hooks
```
