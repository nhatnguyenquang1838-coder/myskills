---
name: circuit-breaker
description: Detect unsafe or unsupported planning/finance output states and downgrade, block, or recover workflow safely.
---

# Circuit Breaker Skill

## Purpose

Stop fake confidence before it reaches a report, forecast, baseline, or executive output.

## Reads

```txt
user_request
readiness_mode
project_control_graph
output_draft
fact_check_result
context_audit_result
cascade_check_result
missing_data
```

## Writes

```txt
breaker_state
breaker_severity
blocked_claims
allowed_fallback
recovery_questions
circuit_breaker_log
```

## Breaker states

```txt
CLOSED
HALF_OPEN
OPEN
```

## Trigger checks

```txt
evidence_breaker
baseline_breaker
finance_breaker
context_breaker
cascade_breaker
history_bias_breaker
```

## Output contract

```txt
Breaker:
State:
Severity:
Reason:
Blocked claims:
Missing data:
Allowed fallback:
Recovery questions:
Next action:
```

## Guardrail

Do not block useful draft work. Block unsupported official claims.
