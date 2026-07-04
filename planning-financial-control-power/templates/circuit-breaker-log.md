# Circuit Breaker Log

| Date | Breaker | Severity | Reason | Breached Constraint | Blocked Claims | Allowed Fallback | Status |
|---|---|---|---|---|---|---|---|

## Severity

| Severity | Meaning | Behavior |
|---|---|---|
| S0 | no issue | continue |
| S1 | minor issue | continue with note |
| S2 | confidence limitation | draft only |
| S3 | official claim blocked | block official output |
| S4 | contradiction/unsafe | stop and require resolution |

## Breaker event template

```md
## Breaker Event

Date:
Run ID:
Breaker:
Severity:
Reason:
Breached constraint source:
Breached constraint exact text:
BCBS239 principle tags:
Blocked claims:
Missing data:
Allowed fallback:
Recovery questions:
Next action:
Status:
```

## Isolate-and-Condense recovery packet

Use this shape after any HALF_OPEN or OPEN breaker state.

```yaml
failure_recovery_packet:
  breaker:
  severity:
  failure_summary:
    - "Sentence 1."
    - "Sentence 2."
  breached_constraint:
    source:
    exact_text:
  circuit_breaker_log:
    blocked_claims: []
    missing_data: []
    allowed_fallback:
  next_allowed_actions: []
```
