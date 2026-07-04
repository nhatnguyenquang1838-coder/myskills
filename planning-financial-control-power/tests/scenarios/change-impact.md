# Scenario: Change Impact

## Input

```txt
MS-001 delayed by 2 weeks because vendor API is late.
```

## Expected cascade

```txt
MS-001
-> linked RA nodes
-> linked COST nodes
-> linked FCST nodes
-> linked RPT nodes
```

## Required skills

```txt
timeline-planning
resource-planning-allocation
cost-calculator
report-builder
fact-check
```

## Expected output

```txt
Timeline impact: +2 weeks
Resource impact: extension or conflict check required
Cost impact: recalculation required
Report impact: RAG may change, depending thresholds and evidence
Decision needed: approve extension, add resource, or reduce scope
```

## Pass criteria

The report is not updated before cascade and fact-check complete.
