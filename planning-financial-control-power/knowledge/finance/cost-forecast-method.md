# Cost Forecast Method

## Purpose

Calculate cost and forecast from linked resource allocation and rate data.

## Formula

```txt
resource_cost = fte * monthly_rate * duration_months
total_forecast = resource_cost + vendor_cost + infra_cost + contingency
variance = total_forecast - approved_budget
```

## Required graph links

```txt
RA -> RATE -> COST -> FCST -> RPT
```

## Confidence rules

```txt
High = approved rate + confirmed allocation + approved budget
Medium = documented rate/allocation but not approved baseline
Low = assumption-based rate or incomplete allocation
Blocked = no rate/resource basis
```

## Anti-pattern

Reporting budget as Green without rate card, allocation, and budget source.
