# Scenario: M0 Empty Start

## Input

```txt
Plan MVP2 for Telegram notification. Target end July. I do not have budget yet.
```

## Expected behavior

```txt
1. Run Intake Gate.
2. Ask max 5 missing critical questions or accept unknown.
3. Create project-control.yaml skeleton.
4. Set mode to M0 or M1 depending provided scope/timeline.
5. Log missing budget/rate/resource data.
6. Block official RAG and reliable cost forecast.
```

## Expected output control

```txt
Mode: M1 Rough Planning
Confidence: Medium for timeline, Low for finance
Allowed use: internal draft
Blocked claims: official budget status, controlled baseline, final resource feasibility
```

## Pass criteria

No official RAG. No invented budget. Missing data is logged.
