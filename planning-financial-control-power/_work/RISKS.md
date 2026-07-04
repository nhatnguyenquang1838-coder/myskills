# Planning & Financial Control Power — Risks

## Risk scale

```txt
Probability: Low / Medium / High
Impact: Low / Medium / High
Status: Open / Monitoring / Closed
```

## RISK-001 — Power becomes bloated with DL Skill implementation

Probability: Medium
Impact: High
Status: Open

Mitigation:

```txt
Keep DL Skills as contracts only.
Do not copy implementation into PFC.
```

Owner: PFC

## RISK-002 — Complex UCs run without baseline

Probability: High
Impact: High
Status: Open

Mitigation:

```txt
Add complex use-case gate.
Block official output if baseline is incomplete.
```

Owner: PFC

## RISK-003 — Graph schema exists but no executable validator

Probability: High
Impact: High
Status: Open

Mitigation:

```txt
Add validation scripts and sample valid/invalid fixtures.
```

Owner: PFC

## RISK-004 — DL Skill contracts remain too shallow

Probability: High
Impact: High
Status: Open

Mitigation:

```txt
Define full contracts for P0 DL Skills.
Require C3+ for MVP official workflows.
```

Owner: PFC

## RISK-005 — Hooks are not executable due to schema mismatch

Probability: Medium
Impact: Medium
Status: Open

Mitigation:

```txt
Verify Kiro hook schema before v0.3 team pilot.
Keep v0.2 hooks as templates only.
```

Owner: PFC

## RISK-006 — Sample use cases are mistaken for standards

Probability: Medium
Impact: Medium
Status: Monitoring

Mitigation:

```txt
Use `use-case-standard-guideline.md` as authority.
Mark reference UCs as samples.
```

Owner: PFC

## RISK-007 — BCBS239 references create false compliance claim

Probability: Medium
Impact: High
Status: Open

Mitigation:

```txt
State BCBS239 is used as control reference.
Do not claim regulatory compliance unless explicit assessment is performed.
```

Owner: PFC

## RISK-008 — Runtime output lacks audit trail

Probability: Medium
Impact: High
Status: Open

Mitigation:

```txt
Require run-execution-record and checkpoints for meaningful runs.
```

Owner: PFC

## RISK-009 — User manually runs random skill outside Power control

Probability: Medium
Impact: Medium
Status: Open

Mitigation:

```txt
Document PFC routing rule.
DL Skill outputs become draft until PFC validates.
```

Owner: PFC

## RISK-010 — MVP scope expands into integrations too early

Probability: High
Impact: Medium
Status: Open

Mitigation:

```txt
Do not start Jira/Confluence/Mail integrations until v0.2 foundation is live.
```

Owner: PFC
