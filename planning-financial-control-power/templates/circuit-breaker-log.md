# Circuit Breaker Log

| Date | Breaker | Severity | Reason | Blocked Claims | Allowed Fallback | Status |
|---|---|---|---|---|---|---|

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
Breaker:
Severity:
Reason:
Blocked claims:
Missing data:
Allowed fallback:
Recovery questions:
Next action:
Status:
```
