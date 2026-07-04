---
name: cost-calculator
description: Calculate project cost lines, forecast, budget variance, and financial impact from resource allocation and rate data.
---

# Cost Calculator Skill

## Purpose

Calculate cost and forecast nodes in the Project Control Graph.

## Reads

```txt
resource_allocations
rate_cards
cost_lines
forecasts
budget
vendor_contracts
assumptions
evidence
```

## Writes

```txt
cost_lines
forecasts
budget_variance
financial_impact
cost_assumptions
missing_data
```

## Must not do

```txt
Do not set overall project status alone.
Do not override approved budget.
Do not create official forecast without rate/resource basis.
```

## Calculation model

```txt
resource_cost = fte * monthly_rate * duration_months
total_forecast = resource_cost + vendor_cost + infra_cost + contingency
variance = total_forecast - approved_budget
```

## Required output

```txt
cost_lines_created_or_changed
forecast_amount
variance
budget_status_signal
assumptions
missing_data
confidence
```

## Guardrail

If rate card or rate assumption is missing, output missing-data request and optional scenario range only.
