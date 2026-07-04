# 12 — Memory Context Controller

## Purpose

Control how the Power stores, retrieves, validates, and downgrades memory.

## Core rule

```txt
Memory supports the graph.
Memory does not replace the graph.
```

## Authority order

```txt
approved baseline
> latest approved decision
> current graph forecast
> documented evidence
> assumption
> historical benchmark
> raw archive
```

## Memory layers

| Layer | Description | Authority |
|---|---|---|
| L0 | current chat/session | low |
| L1 | current task working memory | medium |
| L2 | project graph memory | high |
| L3 | historical benchmark memory | benchmark only |
| L4 | raw archive | low until indexed |

## Retrieval rule

Load memory by linked graph IDs, not by keyword alone.

```txt
target graph node
-> linked nodes
-> linked memories
-> staleness check
-> conflict check
-> context audit
```

## Write rule

Only write memory when it has:

```txt
id
type
source
created_date
confidence
linked_graph_ids
review_date
status
```

## Staleness triggers

```txt
baseline version changes
linked graph node changes
conflicting evidence appears
review date expires
owner marks obsolete
```

## Conflict rule

If memory conflicts with graph:

```txt
1. Use graph.
2. Flag conflict.
3. Create missing-data or decision-needed item.
4. Do not merge silently.
```

## Circuit breaker triggers

Open Circuit Breaker when:

```txt
stale memory used as current fact
historical memory used as current truth
memory has no source/confidence
required linked graph node missing
memory conflicts with approved baseline
```

## Output labels

When memory influences output, label it as:

```txt
Current fact
Decision memory
Assumption memory
Historical benchmark
Pattern memory
Unknown / missing data
```
