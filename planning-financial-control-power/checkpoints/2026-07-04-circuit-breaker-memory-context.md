# Checkpoint — Circuit Breaker + Memory Context Controller

Date: 2026-07-04
Scope: Supporting documents for Planning & Financial Control Power

## Added

```txt
knowledge/support/circuit-breaker.md
knowledge/support/memory-context-controller.md
steering/11-circuit-breaker-policy.md
steering/12-memory-context-controller.md
templates/circuit-breaker-log.md
templates/memory-index.yaml
templates/context-retrieval-log.md
skills/circuit-breaker/SKILL.md
skills/memory-context-controller/SKILL.md
hooks/circuit-breaker-check.kiro.hook
tests/scenarios/circuit-breaker-memory-context.md
```

## Design decisions

1. Circuit Breaker blocks fake confidence, not useful draft work.
2. Memory Context Controller retrieves memory by graph links, not by keyword alone.
3. Memory supports the Project Control Graph; it never replaces it.
4. Historical data remains benchmark/risk signal unless explicitly approved as evidence.
5. Breaker states are CLOSED, HALF_OPEN, and OPEN.
6. Breaker severity ranges from S0 to S4.

## Integration point

```txt
User request
-> Memory Context Controller
-> Context Audit
-> Skill execution
-> Fact Check
-> Circuit Breaker
-> Output Template
```

## Next improvement

```txt
1. Add schema validation for memory-index.yaml.
2. Add circuit-breaker expected output examples.
3. Add hook schema verification.
4. Add scoring rubric for Circuit Breaker and Memory Context Controller readiness.
```
