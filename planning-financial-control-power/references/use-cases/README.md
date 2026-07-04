# Use Case Samples

This folder stores sample use-case flows for Planning & Financial Control Power.

These files are examples, not the standard.

## Purpose

Use these samples when testing, demonstrating, or explaining how the Power behaves in common situations.

```txt
Use case samples = concrete examples of jobs the Power can perform
Readiness modes = how much confidence/output authority is allowed
Control flows = example execution paths using agents, skills, hooks, guardrails, and circuit breakers
```

## Sample files

| File | Purpose |
|---|---|
| `critical-flows-with-controls.md` | Sample Mermaid flows for simple and complex cases with agents/skills/hooks/breakers |
| `uc-control-summary.md` | Sample mapping from UC families to agents, skills, hooks, guardrails, bias, hallucination controls |

## Standard guideline

The standard use-case guideline is stored at:

```txt
planning-financial-control-power/knowledge/use-cases/use-case-standard-guideline.md
```

The steering policy is stored at:

```txt
planning-financial-control-power/steering/13-use-case-standard-policy.md
```

## Rule

```txt
Samples illustrate behavior.
Standard guideline defines required structure and control rules.
Steering policy tells agents how to apply the standard.
Templates are copied into target workspaces.
```
