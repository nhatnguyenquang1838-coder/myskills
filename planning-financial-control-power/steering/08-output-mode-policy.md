# 08 — Output Mode Policy

## Purpose

Prevent misleading outputs when readiness is low.

## Required output header

Every major output must start with:

```txt
Mode:
Confidence:
Allowed use:
Blocked claims:
Source graph nodes:
Evidence used:
Assumptions:
Missing data:
Decisions needed:
```

## Mode language

| Mode | Allowed language | Forbidden language |
|---|---|---|
| M0 | initial draft, working assumption | forecast, approved, on track |
| M1 | rough plan, draft estimate | official budget, controlled baseline |
| M2 | forecast, variance estimate | approved baseline unless approved |
| M3 | approved baseline, official status | unsupported claims |

## Confidence labels

```txt
High   = approved source + date + owner
Medium = documented source but not approved baseline
Low    = assumption or incomplete data
Blocked = missing critical input
```

## Output rule

A useful draft is acceptable. A confident unsupported answer is not.
