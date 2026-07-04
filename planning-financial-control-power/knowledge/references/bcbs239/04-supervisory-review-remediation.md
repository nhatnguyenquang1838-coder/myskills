# BCBS 239 — Supervisory Review and Remediation

Source: SRC-BCBS239-2013, Principles 12-14.

## Purpose for skills

Use this file when a skill supports:

```txt
audit readiness
control review
remediation tracking
supervisory-style challenge
independent validation
risk data/reporting gap closure
home/host or cross-unit coordination
```

## Principle 12 — Review

Core meaning:

```txt
Compliance with risk data aggregation and reporting principles should be periodically reviewed and evaluated.
```

## PFC implementation

| Review expectation | PFC mechanism |
|---|---|
| periodic review | readiness rescoring and checkpoints |
| ability to test aggregation/reporting | scenario tests and fire-drill-style use cases |
| access to reports/documents | evidence ledger and source index |
| independent validation | fact-checker and context-auditor roles |

## Principle 13 — Remedial Actions and Supervisory Measures

Core meaning:

```txt
Deficiencies should trigger timely remediation, escalation, and stronger measures when gaps persist.
```

## PFC implementation

| Remediation expectation | PFC mechanism |
|---|---|
| deficiencies identified | missing-data log, blocked claims, breaker log |
| remedial action | improvement backlog / decision-needed list |
| timetable | owner + due date fields |
| escalation | decision-needed report, risk escalation |
| stronger response | Circuit Breaker OPEN for persistent unsupported official claims |

## Principle 14 — Home/Host Cooperation

Core meaning:

```txt
Relevant supervisors across jurisdictions should cooperate and share information to avoid inconsistent or redundant reviews.
```

## PFC interpretation

For project delivery context, this means cross-team/cross-entity reporting should use a shared source of truth and avoid conflicting local reports.

PFC implementation:

```txt
Project Control Graph = shared baseline
Run Context Graph = scoped view
Evidence ledger = common source reference
Decision log = authority trail
Report source_ids = shared traceability
```

## Guardrails

```txt
No periodic review -> readiness may become stale
No owner/due date -> remediation is incomplete
No evidence ledger -> review cannot validate claims
No checkpoint -> baseline or report history is weak
Persistent breaker OPEN -> escalation required
```

## Circuit breakers

| Breaker | Opens when |
|---|---|
| Evidence breaker | review/remediation claim lacks evidence |
| Baseline breaker | compliance/controlled-state claim lacks baseline |
| Context breaker | review uses stale or conflicting sources |
| Contract breaker | DL Skill lacks validation/remediation output contract |

## Skill contract requirements

Audit/review/remediation DL Skills must declare:

```txt
review scope
input evidence required
output findings format
remediation item format
owner/due-date requirement
escalation rule
confidence rating
```

## Output pattern

```txt
Review scope:
Findings:
Evidence used:
Severity:
Remediation action:
Owner:
Due date:
Escalation needed:
Breaker state:
```
