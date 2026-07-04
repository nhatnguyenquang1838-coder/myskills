# DL Skill Contract Examples

These are examples of how external DL Skills should be represented to the Planning & Financial Control Power.

They are not implementations.

---

# Example 1 — DL-11 PLAN Release Milestone Planner

```yaml
contract_version: "0.1"
skill_id: "DL-11-PLAN-release-milestone-planner"
skill_name: "Release Milestone Planner"
category: "PLAN"
maturity: "detailed"
status: "active"

purpose:
  summary: "Create or update milestone plan from work packages, constraints, and dependencies."
  guarantees:
    - "returns milestone candidates"
    - "returns dependency assumptions when dependency data is incomplete"
  non_goals:
    - "does not calculate final cost"
    - "does not approve baseline"
    - "does not publish report"

input_contract:
  required_inputs:
    - "work_packages"
    - "target_dates_or_constraints"
  optional_inputs:
    - "dependencies"
    - "risks"
    - "historical_benchmarks"
  accepted_graph_nodes: ["WP", "DEP", "RISK", "ASM", "EVD", "DEC"]
  forbidden_inputs:
    - "unsupported budget conclusion"

output_contract:
  required_outputs:
    - "milestone_plan"
    - "dependency_notes"
    - "assumptions"
  produced_graph_deltas: ["MS", "DEP", "ASM", "MD"]
  confidence_required: true

preconditions:
  readiness_modes_allowed: ["M1", "M2", "M3"]
  required_graph_nodes: ["WP"]

constraints:
  must_not_claim:
    - "cost is acceptable"
    - "resource is sufficient"
    - "baseline is approved"

control_requirements:
  required_guardrails:
    - "dates must have evidence, decision, or assumption"
  required_circuit_breakers:
    - "Evidence breaker"
    - "Cascade breaker"

pfc_integration:
  supported_use_cases: ["UC-00", "UC-05", "UC-06", "UC-22"]
  primary_agent_role: "timeline-planner"
  graph_nodes_read: ["WP", "DEP", "RISK", "ASM", "EVD", "DEC"]
  graph_nodes_written_as_delta: ["MS", "DEP", "ASM", "MD"]
  write_back_authority: "approved_delta_only"
```

---

# Example 2 — DL-27 FIN Project Cost Calculator

```yaml
contract_version: "0.1"
skill_id: "DL-27-FIN-project-cost-calculator"
skill_name: "Project Cost Calculator"
category: "FIN"
maturity: "detailed"
status: "active"

purpose:
  summary: "Calculate cost lines, forecast, and variance from resource allocation, rate card, and budget inputs."
  guarantees:
    - "returns cost calculation with derived_from links"
    - "returns missing finance data when basis is incomplete"
  non_goals:
    - "does not approve budget"
    - "does not set overall project status alone"
    - "does not infer rates without assumptions"

input_contract:
  required_inputs:
    - "resource_allocations"
    - "rate_cards_or_rate_assumptions"
    - "duration"
  optional_inputs:
    - "approved_budget"
    - "contingency_rule"
  accepted_graph_nodes: ["RA", "RATE", "COST", "FCST", "ASM", "EVD"]

output_contract:
  required_outputs:
    - "cost_lines"
    - "forecast_amount"
    - "variance_if_budget_exists"
  produced_graph_deltas: ["COST", "FCST", "ASM", "MD"]
  confidence_required: true

preconditions:
  readiness_modes_allowed: ["M1", "M2", "M3"]
  required_graph_nodes: ["RA"]
  required_assumptions_allowed: ["RATE", "duration"]

constraints:
  must_not_claim:
    - "budget is sufficient without approved budget"
    - "forecast is approved"
    - "overall project is green"

control_requirements:
  required_guardrails:
    - "every amount must have derived_from or source_id"
  required_circuit_breakers:
    - "Finance breaker"
    - "Evidence breaker"

pfc_integration:
  supported_use_cases: ["UC-00", "UC-14", "UC-15", "UC-16", "UC-17", "UC-22"]
  primary_agent_role: "finance-analyst"
  graph_nodes_read: ["RA", "RATE", "COST", "FCST", "ASM", "EVD"]
  graph_nodes_written_as_delta: ["COST", "FCST", "ASM", "MD"]
  write_back_authority: "approved_delta_only"
```
