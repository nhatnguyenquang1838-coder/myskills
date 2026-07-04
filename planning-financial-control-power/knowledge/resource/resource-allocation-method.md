# Resource Allocation Method

## Purpose

Translate work packages and milestones into role/FTE/capacity needs.

## Method

```txt
1. Load linked work package and milestone nodes.
2. Identify roles needed.
3. Estimate FTE and duration.
4. Link allocation to milestone.
5. Check capacity/conflict.
6. Trigger cost recalculation.
```

## Required graph links

```txt
WP -> MS -> RA -> COST
```

## Anti-pattern

Declaring capacity sufficient without allocation period or capacity source.
