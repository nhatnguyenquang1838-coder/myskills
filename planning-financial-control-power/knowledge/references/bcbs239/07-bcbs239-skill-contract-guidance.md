# BCBS 239 — DL Skill Contract Guidance

## Purpose

Define what DL Skill contracts must expose when supporting BCBS239-style risk data aggregation and reporting controls.

This is a Power-owned contract guideline. It does not change DL Skill implementation.

## Contract requirement categories

A DL Skill supporting PFC must expose:

```txt
purpose
inputs
outputs
preconditions
postconditions
side effects
constraints
failure modes
control requirements
evidence rule
PFC integration metadata
```

## BCBS239-derived contract questions

### Governance questions

```txt
Who owns the output?
Who approves the output?
What evidence supports the output?
What are the known limitations?
What validation is required?
```

### Aggregation questions

```txt
What graph nodes are accepted?
What calculations or transformations are performed?
What source IDs are required?
What missing data blocks the output?
What manual assumptions are allowed?
```

### Reporting questions

```txt
Who is the audience?
What is the reporting period?
What source IDs support report claims?
What claims are forbidden?
What conditions downgrade the report to draft?
```

### Review/remediation questions

```txt
What gaps can the skill detect?
What remediation output can it produce?
Does it require owner/due date/severity?
What checkpoint or audit record is required?
```

## Minimum contract fields for BCBS239-sensitive skills

```yaml
purpose:
  guarantees: []
  non_goals: []

input_contract:
  required_inputs: []
  accepted_graph_nodes: []
  forbidden_inputs: []

output_contract:
  required_outputs: []
  produced_graph_deltas: []
  confidence_required: true

constraints:
  must_not_claim: []
  authority_limit: ""

control_requirements:
  required_guardrails: []
  required_circuit_breakers: []
  required_bias_checks: []
  required_hallucination_checks: []

evidence_rule:
  source_required_for_claims: true
  assumptions_allowed: true
  historical_data_allowed_as: "benchmark_only"

pfc_integration:
  supported_use_cases: []
  graph_nodes_read: []
  graph_nodes_written_as_delta: []
  write_back_authority: "approved_delta_only"
```

## Required contract clauses by skill type

### Intake/document skills

Must expose:

```txt
source extraction capability
evidence candidate format
missing-data detection
confidence label
limitation notes
```

Must not claim:

```txt
source is approved
baseline is complete
report is official
```

### Timeline/planning skills

Must expose:

```txt
accepted scope/work package input
milestone output format
dependency output format
date confidence
date source or assumption requirement
```

Must not claim:

```txt
cost impact is zero
resource is sufficient
baseline is approved
```

### Resource skills

Must expose:

```txt
role/FTE allocation format
capacity basis
period coverage
conflict detection
resource assumptions
```

Must not claim:

```txt
team is confirmed without evidence
capacity is sufficient without capacity basis
cost is approved
```

### Finance skills

Must expose:

```txt
rate input requirement
resource allocation requirement
duration requirement
formula / derived_from requirement
budget variance rule
missing finance data behavior
```

Must not claim:

```txt
budget is green without budget threshold
forecast is approved
project is on budget without approved budget
```

### Risk/issue skills

Must expose:

```txt
risk source
probability/impact basis
owner/status requirement
escalation rule
link to affected graph nodes
```

Must not claim:

```txt
risk is closed without decision/evidence
issue is resolved without status source
```

### Report skills

Must expose:

```txt
report type
audience
required source IDs
allowed output authority
blocked claims behavior
confidentiality/distribution fields if applicable
```

Must not claim:

```txt
official RAG without M3
budget status without finance basis
approval without decision ID
```

## Contract maturity scoring

| Score | Meaning | BCBS-sensitive use |
|---:|---|---|
| C0 | no contract | do not call |
| C1 | purpose only | exploratory only |
| C2 | inputs/outputs defined | draft use only |
| C3 | graph + guardrails defined | controlled workflow with checks |
| C4 | tested contract with failure modes | M2/M3 support with checks |
| C5 | validated in real use | production/team use |

## Power rule

```txt
A PFC use case cannot have higher reliability than its critical DL Skill contracts.
```

Example:

```txt
If cost-calculator contract is C2, PFC cannot publish official budget forecast even if other controls pass.
```

## Output validation checklist

After a DL Skill runs, PFC validates:

```txt
[ ] required outputs returned
[ ] output format matches contract
[ ] graph deltas target allowed node types
[ ] forbidden claims are absent
[ ] confidence is present
[ ] source/evidence/derived_from links exist
[ ] missing data is explicit
[ ] output authority is not exceeded
```
