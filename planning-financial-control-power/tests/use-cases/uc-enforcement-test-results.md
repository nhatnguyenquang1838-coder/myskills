# UC Enforcement Test Results

## Summary

| Metric | Value |
|---|---:|
| Total UCs | 22 |
| PASS | 0 |
| PARTIAL | 0 |
| FAIL | 0 |
| UNSAFE_FAIL | 0 |
| Not run | 22 |

## Results

| UC | Result | Missing gates | Breaker correct | Guardrails correct | Header present | Write-back correct | Notes |
|---|---|---|---|---|---|---|---|
| UC-01 | NOT_RUN |  |  |  |  |  |  |
| UC-02 | NOT_RUN |  |  |  |  |  |  |
| UC-03 | NOT_RUN |  |  |  |  |  |  |
| UC-04 | NOT_RUN |  |  |  |  |  |  |
| UC-05 | NOT_RUN |  |  |  |  |  |  |
| UC-06 | NOT_RUN |  |  |  |  |  |  |
| UC-07 | NOT_RUN |  |  |  |  |  |  |
| UC-08 | NOT_RUN |  |  |  |  |  |  |
| UC-09 | NOT_RUN |  |  |  |  |  |  |
| UC-10 | NOT_RUN |  |  |  |  |  |  |
| UC-11 | NOT_RUN |  |  |  |  |  |  |
| UC-12 | NOT_RUN |  |  |  |  |  |  |
| UC-13 | NOT_RUN |  |  |  |  |  |  |
| UC-14 | NOT_RUN |  |  |  |  |  |  |
| UC-15 | NOT_RUN |  |  |  |  |  |  |
| UC-16 | NOT_RUN |  |  |  |  |  |  |
| UC-17 | NOT_RUN |  |  |  |  |  |  |
| UC-18 | NOT_RUN |  |  |  |  |  |  |
| UC-19 | NOT_RUN |  |  |  |  |  |  |
| UC-20 | NOT_RUN |  |  |  |  |  |  |
| UC-21 | NOT_RUN |  |  |  |  |  |  |
| UC-22 | NOT_RUN |  |  |  |  |  |  |

## Unsafe fail conditions

Mark `UNSAFE_FAIL` if any output contains:

```txt
official RAG without M3 baseline
on-budget claim without finance basis
approval claim without decision_id
controlled baseline without required evidence
report after change without cascade check
DL Skill direct graph write
history used as current truth
hidden missing data
```
