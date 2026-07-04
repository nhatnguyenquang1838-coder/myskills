# 05 — Context Loading Policy

## Purpose

Prevent context overload and stale/bias-prone outputs.

## Core rule

```txt
Load by graph, not by folder.
```

## Correct context loading

Example request: user asks about `WP-001`.

```txt
1. Load WP-001
2. Load linked milestones
3. Load linked resource allocations
4. Load linked cost lines and forecasts
5. Load linked risks, assumptions, decisions, evidence
6. Load reports only if requested or impacted
7. Load history only if benchmark/scenario is needed
```

## Context priority

```txt
Current approved baseline
> latest approved decision
> current forecast
> current working graph
> historical benchmark
> raw archive
```

## Never auto-load

```txt
raw email exports
old meeting transcripts
old reports before current baseline
unapproved finance sheets
unlinked historical files
```

## Required retrieval log

When history or raw evidence is used, append to:

```txt
.pm/audit/context-retrieval-log.md
```

## Output rule

Every answer must mention source graph nodes when making a timeline, cost, resource, or report claim.
