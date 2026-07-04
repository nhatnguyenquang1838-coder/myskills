# 06 — History Bias Policy

## Purpose

Use historical data safely without letting it override current project truth.

## Rule

```txt
History can challenge the plan.
History cannot replace the baseline.
```

## Allowed history usage

```txt
benchmark
risk signal
lesson learned
scenario input
variance comparison
```

## Forbidden usage

```txt
using old delay to declare current delay
using old cost to override approved budget
using draft archive as approved evidence
averaging old projects blindly
using latest file as truth without status check
```

## Required history metadata

```yaml
id:
project:
type:
period:
source:
status: draft | approved | archive
similarity: low | medium | high
use_as: benchmark_only | evidence | scenario_input | do_not_use
bias_risk: low | medium | high
linked_current_ids:
```

## Bias checks

| Bias | Prevention |
|---|---|
| Anchoring | current baseline wins |
| Recency | latest file is not automatically true |
| Confirmation | require counter-signal check |
| Historical | history stays benchmark unless approved as evidence |
| Overconfidence | confidence required on every claim |

## Output language

Use:

```txt
Historical benchmark suggests risk.
```

Do not use:

```txt
This project will delay because past projects delayed.
```
