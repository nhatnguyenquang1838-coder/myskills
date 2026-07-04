# 07 — Evidence Guardrail

## Purpose

Prevent hallucination in planning, finance, and reporting outputs.

## Main rules

```txt
No evidence -> mark assumption
No baseline -> no official RAG
No rate/resource data -> no reliable cost forecast
No source IDs -> no report claim
No decision log -> no approved commitment
No history metadata -> no historical benchmark claim
```

## Claim validation

For every claim involving date, number, cost, resource, RAG, delay, scope, dependency, or decision, require at least one of:

```txt
evidence_id
assumption_id
decision_id
derived_from
baseline_version
```

## Classification

Every important output must classify information as:

```txt
Fact
Derived calculation
Assumption
Unknown
Historical benchmark
Decision needed
```

## Blocked wording unless evidence exists

```txt
confirmed
approved
on track
budget is sufficient
no risk
team agreed
final estimate
```

## Fact-check failure output

If unsupported claims exist, return:

```txt
FAIL
unsupported_claims
required_sources
recommended_rewrite
```
