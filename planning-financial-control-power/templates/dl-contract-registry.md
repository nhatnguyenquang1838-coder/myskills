# DL Contract Registry

## Purpose

Track which DL Skill contracts are available for Planning & Financial Control Power.

## Registry

| DL Skill Contract | Category | Contract Maturity | Supports PFC UC | Required For Baseline? | Allowed PFC Usage | Gap / Action |
|---|---|---:|---|---:|---|---|
| DL-00-CORE-cognitive-intake-gate | CORE | C0 | UC-00, UC-01, UC-02, UC-04 | Yes | blocked until contract exists | create contract |
| DL-01-CORE-project-setup | CORE | C0 | UC-00, UC-01, UC-02 | Yes | blocked until contract exists | create contract |
| DL-04-CORE-document-intake | CORE | C0 | UC-00, UC-00A, UC-03 | Yes | blocked until contract exists | create contract |
| DL-10-PLAN-dependency-tracker | PLAN | C0 | UC-00, UC-05, UC-07, UC-24 | Yes | blocked until contract exists | create contract |
| DL-11-PLAN-release-milestone-planner | PLAN | C0 | UC-00, UC-05, UC-06, UC-08, UC-22 | Yes | blocked until contract exists | create contract |
| DL-12-PLAN-resource-allocator | PLAN | C0 | UC-00, UC-09, UC-10, UC-11, UC-12 | Yes | blocked until contract exists | create contract |
| DL-14-FIN-budget-cost-tracking | FIN | C0 | UC-00, UC-14, UC-15, UC-17 | Yes | blocked until contract exists | create contract |
| DL-27-FIN-project-cost-calculator | FIN | C0 | UC-00, UC-13, UC-14, UC-15, UC-16, UC-17 | Yes | blocked until contract exists | create contract |
| DL-16-RISK-risk-register | RISK | C0 | UC-00, UC-07, UC-21, UC-22, UC-23, UC-24 | Yes | blocked until contract exists | create contract |
| DL-17-RISK-issue-blocker-tracker | RISK | C0 | UC-21, UC-22, UC-24, UC-33 | No | blocked until contract exists | create contract |
| DL-21-RPT-executive-status-report | RPT | C0 | UC-19, UC-20 | No | blocked until contract exists | create contract |
| DL-26-RPT-report-builder | RPT | C0 | UC-18, UC-19, UC-20, UC-21, UC-22, UC-23 | No | blocked until contract exists | create contract |
| DL-31-CORE-red-team-devils-advocate | CORE | C0 | UC-19, UC-28, UC-30, UC-32, UC-34 | No | blocked until contract exists | create contract |
| DL-34-CORE-standalone-readiness-check | CORE | C0 | UC-00, UC-00B, UC-00C, UC-04, UC-19 | Yes | blocked until contract exists | create contract |

## Usage rules

```txt
C0 = no contract = do not call
C1-C2 = draft/scenario only
C3 = controlled workflow with checks
C4 = M2/M3 support with checks
C5 = production/team use
```
