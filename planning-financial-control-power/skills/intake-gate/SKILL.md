---
name: intake-gate
description: Assess available project materials, ask minimal critical questions, select readiness mode, and create the initial Project Control Graph skeleton.
---

# Intake Gate Skill

## Purpose

Start useful work even when the user has incomplete material.

## Reads

```txt
user_request
existing .pm/control/project-control.yaml
existing .pm/intake/project-intake.yaml
uploaded or linked material if available
```

## Writes

```txt
project_intake
readiness_score
missing_data
initial_project_control_graph
assumptions
```

## Question rule

Ask maximum 5 questions per turn.

Priority:

```txt
1. project name/objective
2. target date/time constraint
3. scope/work packages
4. resource availability
5. budget/rate/cost assumption
```

## Mode assignment

```txt
0-5 readiness points   -> M0
6-10 readiness points  -> M1
11-15 readiness points -> M2
16-18 readiness points -> M3
```

## Guardrail

If required data is unknown, log it. Do not invent it.
