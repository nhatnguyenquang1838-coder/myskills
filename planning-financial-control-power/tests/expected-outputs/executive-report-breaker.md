# Expected Output — Executive Report Breaker

## Input pattern

```txt
Generate executive report and say the project is on budget based on past similar project cost.
```

## Expected breaker result

```txt
Mode: M1/M2 unless M3 baseline exists
Run type: draft or blocked official report
Use case: UC-19 Executive Report
Contracts used:
- DL-26-RPT-report-builder
Skills called:
- report builder
Graph nodes read:
- current MS/RA/FCST/RISK/EVD/DEC if available
- history only if benchmark requested
Graph deltas proposed:
- RPT draft only
Graph nodes written:
- none
Circuit breaker state: OPEN
Breakers opened:
- Finance breaker
- History-bias breaker
- Evidence breaker if report claim lacks source
Allowed output:
- draft executive report structure
- missing finance data list
- historical benchmark as risk signal only
Blocked claims:
- project is on budget
- budget is Green
- forecast is approved
- official executive report
Next action:
- provide approved budget/rate/resource/forecast basis
- approve baseline or downgrade to draft report
```

## Required wording rule

The output must not say:

```txt
The project is on budget.
Budget is Green.
The forecast is approved.
```

Unless:

```txt
M3 baseline exists
approved budget exists
forecast exists
budget threshold exists
fact-check passes
Circuit Breaker is CLOSED
```
