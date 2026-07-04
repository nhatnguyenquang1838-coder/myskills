# Checkpoint — 22 UC Test Suite

Date: 2026-07-04
Scope: Create standardized use-case test suite for Planning & Financial Control Power.

## Added

```txt
tests/use-cases/README.md
tests/use-cases/uc-test-suite-22.md
tests/use-cases/uc-test-matrix.md
```

## Purpose

Provide 22 redefined UC scenarios with:

```txt
scenario
mock input
mock graph state
expected mode
expected run type
expected contracts / skills
expected graph reads
expected graph deltas
expected guardrails / circuit breakers
expected result
pass criteria
```

## Coverage

```txt
UC-01 Create Full Controlled Baseline
UC-02 Start Project With Idea Only
UC-03 Create Rough Project Plan
UC-04 Import Materials to Graph
UC-05 Check Project Readiness
UC-06 Build Milestone Plan
UC-07 Update Milestone Date
UC-08 Assess Dependency Risk
UC-09 Build Release Roadmap
UC-10 Build Resource Demand
UC-11 Allocate Named Resources
UC-12 Detect Capacity Conflict
UC-13 Replan After Resource Change
UC-14 Build Cost Assumption
UC-15 Calculate Cost Forecast
UC-16 Budget Cut Impact
UC-17 Rate Card Change Impact
UC-18 Compare Forecast vs Budget
UC-19 Generate Draft Weekly Report
UC-20 Generate Executive Report
UC-21 History-As-Truth Blocker
UC-22 Unsupported RAG / Budget Claim Breaker
```

## Note

A machine-readable YAML matrix was attempted but blocked by the connector safety layer. A compact Markdown matrix was added instead.

## Next improvement

```txt
1. Split UC suite into one file per UC if needed for automation.
2. Add expected output artifacts per UC.
3. Add a simple test runner to check required output headers.
4. Convert matrix to JSON/YAML locally if connector allows smaller chunks.
```
