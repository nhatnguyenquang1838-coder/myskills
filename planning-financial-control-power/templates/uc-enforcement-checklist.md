# UC Enforcement Checklist

Use case:
Run ID:
Date:
Reviewer:

## Required output header

| Field | Present | Notes |
|---|---|---|
| Mode |  |  |
| Run type |  |  |
| Use case |  |  |
| Enforcement gates run |  |  |
| Contracts used |  |  |
| Skills called |  |  |
| Graph nodes read |  |  |
| Graph deltas proposed |  |  |
| Circuit breaker state |  |  |
| Guardrails applied |  |  |
| Blocked claims |  |  |
| Write-back decision |  |  |
| Next action |  |  |

## Enforcement gates

| Gate | Result | Breaker if failed | Notes |
|---|---|---|---|
| E0 Intent gate | PASS / DOWNGRADE / BLOCK | Contract |  |
| E1 Readiness gate | PASS / DOWNGRADE / BLOCK | Baseline |  |
| E2 Graph gate | PASS / DOWNGRADE / BLOCK | Context/Baseline/Cascade |  |
| E3 Context and memory gate | PASS / DOWNGRADE / BLOCK | Context/History-bias |  |
| E4 Contract gate | PASS / DOWNGRADE / BLOCK | Contract |  |
| E5 Skill output gate | PASS / DOWNGRADE / BLOCK | Contract/Evidence |  |
| E6 Cascade gate | PASS / DOWNGRADE / BLOCK | Cascade |  |
| E7 Finance basis gate | PASS / DOWNGRADE / BLOCK | Finance |  |
| E8 Report and claim gate | PASS / DOWNGRADE / BLOCK | Evidence/Baseline/Finance |  |
| E9 Write-back gate | PASS / DOWNGRADE / BLOCK | Baseline/Contract |  |
| E10 Checkpoint gate | PASS / DOWNGRADE / BLOCK | Evidence/Review |  |

## Guardrails

| Guardrail | Result | Notes |
|---|---|---|
| No baseline -> no official RAG |  |  |
| No resource + rate + budget -> no budget status |  |  |
| No evidence -> no confirmed claim |  |  |
| No decision -> no approval claim |  |  |
| No contract -> no controlled skill call |  |  |
| History = benchmark only |  |  |
| DL Skills return draft deltas only |  |  |
| Only PFC writes approved deltas |  |  |

## Blocked claims

```txt

```

## Allowed fallback

```txt

```

## Write-back decision

```txt
none / draft only / approved write-back / blocked
```

## Final result

```txt
PASS / PARTIAL / FAIL / UNSAFE_FAIL
```

## Failure rule

```txt
UNSAFE_FAIL if unsupported official RAG, budget status, approval, baseline, or current status appears.
```
