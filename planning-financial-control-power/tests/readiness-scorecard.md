# Planning & Financial Control Power — Readiness Scorecard

Last rescored: 2026-07-04
Version assessed: v0.2 draft after E2E go-live execution batch

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
| Final architecture | 4.5 | 3.7 | 3.9 | Runtime, contract boundary, run graph, complex gate now defined |
| Project Control Graph | 5.0 | 3.5 | 3.9 | Schema and valid/invalid fixtures added; still needs local validation run |
| Skills | 4.5 | 3.8 | 3.9 | Power-owned support skills exist; P0 external DL contracts added |
| Intake / onboarding | 5.0 | 3.5 | 3.8 | Workspace bootstrap scripts added; live flow still needs real workspace test |
| Tools / MCP | 3.5 | 2.0 | 2.2 | Validators added; MCP remains placeholder by design |
| Hooks | 4.0 | 3.0 | 3.0 | Hook templates exist; exact Kiro hook schema still not verified |
| Knowledge base | 4.0 | 3.5 | 3.9 | BCBS239 reference pack, UC-00 standard, runtime docs added |
| Steering | 4.5 | 4.2 | 4.4 | Added run graph policy and complex use-case gate |
| Patterns | 4.0 | 2.8 | 3.3 | Added UC-00 dry run and expected output patterns |
| Context / history | 4.5 | 3.8 | 3.8 | No major new memory/history schema in this batch |
| Guardrails | 5.0 | 4.0 | 4.2 | BCBS239 guardrails, contract breaker, and expected breaker outputs strengthen controls |
| Checkpoint / versioning | 4.0 | 3.2 | 3.5 | Go-live plan and checkpoints exist; release versioning still manual |
| Output templates | 4.5 | 3.6 | 3.9 | Run execution record, expected outputs, report breaker format added |
| Circuit Breaker | 4.5 | 3.8 | 4.0 | State machine + expected breaker outputs exist; still needs executable tests |
| Memory Context Controller | 4.5 | 3.7 | 3.7 | Stable but not advanced in this batch |
| Contract Runtime | 4.5 | N/A | 3.8 | DL Skill contract schema, registry, P0 contracts, runtime policy, validators added |
| Bootstrap / Install | 4.0 | N/A | 3.5 | Linux/macOS and PowerShell bootstrap scripts added; needs clean workspace test |

## Approximate readiness

Simple average across current scored components:

```txt
Approx readiness: 3.72 / 5
Status: MVP-live candidate, pending actual local validation run and hook schema verification
```

Practical interpretation:

```txt
The Power has crossed the MVP readiness target on design/assets.
It should still be treated as live-candidate, not production/team-ready, until validators are run in a real workspace and Kiro hooks are verified.
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
Reason: core standards, contracts, validators, bootstrap scripts, fixtures, and expected outputs exist.
Remaining blockers: local validation run, clean workspace bootstrap test, Kiro hook schema verification.
```

## Completed from last target

```txt
DONE: run-graph-policy.md
DONE: project-control schema validator
DONE: expected outputs for scenario tests
DONE: install script
DONE: P0 DL Skill contracts
DONE: UC-00 baseline dry-run scenario
```

## Still missing for stronger v0.3

```txt
memory-index schema validator
history-index template and schema
exact Kiro hook schema verification
real clean-workspace test evidence
trap tests for hallucination / stale history / unsupported budget claim
full M0/M1/M2/M3 examples
scoring-rubric.md linking each score to supporting files and tests
```
