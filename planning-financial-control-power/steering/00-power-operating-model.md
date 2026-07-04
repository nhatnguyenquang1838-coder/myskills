# 00 — Power Operating Model

## Role of this Power

This Power coordinates planning and finance as one control loop.

It must not treat timeline, resource, cost, and report as independent documents.

## Architecture

```txt
Power Controller
  -> Intake Gate
  -> Project Control Graph
  -> Skills
  -> Cascade Engine
  -> Context Loader
  -> Guardrails
  -> Output Templates
  -> Checkpoints
```

## Responsibility boundaries

| Component | Responsibility |
|---|---|
| Power | activation, controller logic, onboarding, rules |
| Skills | specific task processing |
| Agents | role execution |
| Project Control Graph | source of truth |
| Hooks | automatic consistency checks |
| Knowledge Base | reusable methods and patterns |
| History | benchmark only |
| Reports | generated views from graph |

## Non-negotiable rule

Skills do not own truth. They read and write graph nodes.

## Required flow

```txt
User request
-> identify intent
-> run intake/readiness check
-> load linked graph context
-> run relevant skill(s)
-> run cascade check
-> run fact/context check
-> produce controlled output
-> checkpoint when needed
```

## Release target for v0.1

This version is a design skeleton. It should be clear enough for implementation and scenario testing, but not yet treated as production-ready.
