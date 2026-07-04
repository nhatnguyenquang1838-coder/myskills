# Workflow Enforcement Gap Review

Version: 0.1
Scope: Planning & Financial Control Power

## Purpose

Review the current Power logic across the 22 UC workflows and identify missing enforcement logic.

This is not a new use-case list. It is an enforcement review.

## Current good coverage

The Power already has:

```txt
Project Control Graph
Run Context Graph policy
DL Skill contract boundary
Contract registry and P0 contracts
Readiness modes M0-M3
Circuit Breaker state machine
Memory Context Controller
Context audit
Fact check
BCBS239 guardrail reference pack
22 UC test suite
UC-00 baseline standard
Complex use-case gate
```

## Main missing logic before this enforcement layer

| Gap | Why it matters | Required enforcement |
|---|---|---|
| Step-level pre/post checks are not explicit enough | Agents may skip controls inside a workflow | Define mandatory enforcement gates per runtime step |
| UC-level guardrails are described but not normalized | Different UCs can apply controls inconsistently | Create UC enforcement matrix |
| Hook intent exists but hooks are not tied to steps | Hooks may be called too late or not at all | Define hook timing by workflow step |
| Contract validation exists but not every UC states contract failure behavior | Missing contract may silently downgrade logic | Contract breaker must run before skill call |
| Report outputs can be generated before cascade validation | Creates stale/false report status | Report publish gate must require cascade completion |
| Finance outputs can be produced without explicit forecast basis | Risk of fake budget confidence | Finance basis gate for every cost/budget UC |
| Memory/history controls exist but not forced in report/change UCs | Stale context can leak into official outputs | Context/memory gate before report and complex UCs |
| Write-back rule exists but not UC-specific | Draft deltas may be written too early | Write-back gate per UC run type |
| BCBS239 guardrails exist but not connected to workflow steps | Data/report quality controls may be skipped | Map BCBS guardrails into step checks |
| Test suite exists but no enforcement result template | Hard to record PASS/FAIL consistently | Add UC enforcement checklist/result template |

## Enforcement principle

```txt
Every workflow step must declare:
1. what it checks
2. what it allows
3. what it blocks
4. what breaker opens on failure
5. what hook/template runs
6. what audit evidence is produced
```

## Runtime enforcement ladder

```txt
E0 Intent gate
E1 Readiness gate
E2 Graph gate
E3 Context/memory gate
E4 Contract gate
E5 Skill output gate
E6 Cascade gate
E7 Finance basis gate
E8 Report/output gate
E9 Write-back gate
E10 Checkpoint gate
```

## Missing logic by runtime step

| Step | Current risk | Missing logic to add |
|---|---|---|
| Intent gate | request misclassified | require UC ID or unsupported intent output |
| Readiness gate | official output in M0/M1/M2 | block official authority unless mode allows |
| Graph gate | broad context or no target graph | require target IDs / graph skeleton / missing-data item |
| Context gate | stale memory/history used | require Memory Context Controller before complex/report UCs |
| Contract gate | skill called outside contract | require contract exists and supports UC before skill call |
| Skill output gate | output trusted blindly | validate required outputs, deltas, forbidden claims |
| Cascade gate | report updated before linked nodes checked | require changed-node propagation check |
| Finance gate | budget/forecast claim without basis | require RA + RATE + duration + budget for budget status |
| Report gate | RAG/certainty without evidence | require report fact-check and source IDs |
| Write-back gate | draft deltas persist as truth | require approval + validation + breaker CLOSED |
| Checkpoint gate | no audit trail | require run execution record for meaningful runs |

## Enforcement severity

| Severity | Meaning | Behavior |
|---|---|---|
| E-S0 | no issue | continue |
| E-S1 | minor limitation | continue with note |
| E-S2 | missing support but draft possible | downgrade to draft/scenario |
| E-S3 | official claim unsafe | block official claim |
| E-S4 | contradiction or contract violation | stop workflow |

## Required new artifacts

```txt
steering/18-workflow-enforcement-policy.md
templates/uc-enforcement-checklist.md
tests/use-cases/uc-enforcement-matrix.md
hooks/enforcement-preflight.kiro.hook
hooks/enforcement-contract-gate.kiro.hook
hooks/enforcement-output-gate.kiro.hook
hooks/enforcement-writeback-gate.kiro.hook
```

## Rule

```txt
If a workflow step cannot identify its guardrail and breaker, it is not enforceable.
```
