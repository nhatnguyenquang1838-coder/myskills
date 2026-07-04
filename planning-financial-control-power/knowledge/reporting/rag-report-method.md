# RAG Report Method

## Purpose

Generate status reports from linked graph nodes, not from unsupported PM intuition.

## RAG signals

```txt
Timeline RAG  = milestone/dependency status
Resource RAG  = allocation/capacity status
Budget RAG    = forecast/variance status
Risk RAG      = linked risk severity
Overall RAG   = worst of timeline/resource/budget/risk unless decision log overrides
```

## Required report links

```txt
RPT -> MS
RPT -> RA
RPT -> FCST
RPT -> RISK
RPT -> EVD/ASM/DEC
```

## Anti-pattern

Writing an executive status without source graph nodes.
