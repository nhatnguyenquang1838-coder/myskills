---
name: fact-check
description: Validate that timeline, resource, cost, RAG, and report claims are supported by graph links, evidence, assumptions, decisions, or derived calculations.
---

# Fact Check Skill

## Purpose

Block hallucinated or unsupported PM claims.

## Reads

```txt
output_draft
project_control_graph
evidence
assumptions
decisions
baseline_version
```

## Writes

```txt
fact_check_result
unsupported_claims
required_sources
recommended_rewrite
```

## Validation rule

For every date, number, cost, RAG, resource, delay, scope, dependency, or commitment claim, require one of:

```txt
evidence_id
assumption_id
decision_id
derived_from
baseline_version
```

## Output

```txt
PASS or FAIL
unsupported_claims
claim_type
required_source
recommended_rewrite
```

## Guardrail

If the output fails, do not publish it as final. Return correction requirements.
