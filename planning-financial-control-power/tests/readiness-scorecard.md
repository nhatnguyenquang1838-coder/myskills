# Planning & Financial Control Power — Readiness Scorecard

## Scale

| Score | Meaning |
|---:|---|
| 0 | Not designed |
| 1 | Rough idea only |
| 2 | Structure drafted, weak linkage |
| 3 | Usable draft, incomplete guardrails/tests |
| 4 | Production-ready for personal/team use |
| 5 | Distribution-ready, documented, tested, versioned |

## Component readiness

| Component | Target | v0.1 Score | Notes |
|---|---:|---:|---|
| Final architecture | 4.5 | 3.5 | Operating model exists; needs diagram and scenario validation |
| Project Control Graph | 5.0 | 3.5 | YAML template exists; needs schema validation |
| Skills | 4.5 | 3.5 | Contracts exist; need examples and expected outputs |
| Intake / onboarding | 5.0 | 3.5 | Policy and template exist; needs live flow test |
| Tools / MCP | 3.5 | 2.0 | Placeholder only; MVP can run without MCP |
| Hooks | 4.0 | 2.5 | Hook templates exist; exact Kiro schema needs validation |
| Knowledge base | 4.0 | 3.0 | Core method notes exist; more examples needed |
| Steering | 4.5 | 4.0 | Strong first version; needs contradiction review |
| Patterns | 4.0 | 2.5 | Two patterns exist; need more scenarios |
| Context / history | 4.5 | 3.0 | Policy exists; needs history-index template/test |
| Guardrails | 5.0 | 3.5 | Fact-check rules exist; needs trap tests |
| Checkpoint / versioning | 4.0 | 3.0 | Template and policy exist; needs workflow test |
| Output templates | 4.5 | 3.5 | Main templates exist; need more output variants |

## Weighted v0.1 assessment

```txt
Approx readiness: 3.25 / 5
Status: first usable design skeleton
```

## Release gates

```txt
MVP usable:       >= 3.5 / 5
Team usable:      >= 4.0 / 5
Distributable:    >= 4.5 / 5
```

## Next target

Raise v0.2 to >= 3.7 by adding:

```txt
schema validation
history-index template
more cascade patterns
scenario expected outputs
install script
hook schema verification
```
