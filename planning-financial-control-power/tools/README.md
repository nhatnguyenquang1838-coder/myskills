# PFC Validation Tools

## Install dependencies

```bash
pip install pyyaml jsonschema
```

## Validate Project Control Graph

```bash
python tools/validate_project_control.py tests/fixtures/valid-project-control.yaml
python tools/validate_project_control.py tests/fixtures/invalid-project-control.yaml
```

Expected:

```txt
valid-project-control.yaml -> PASS
invalid-project-control.yaml -> FAIL
```

## Validate DL Skill Contract

```bash
python tools/validate_dl_contract.py contracts/dl-skills/DL-00-CORE-cognitive-intake-gate.yaml
python tools/validate_dl_contract.py contracts/dl-skills/DL-11-PLAN-release-milestone-planner.yaml
python tools/validate_dl_contract.py contracts/dl-skills/DL-12-PLAN-resource-allocator.yaml
python tools/validate_dl_contract.py contracts/dl-skills/DL-27-FIN-project-cost-calculator.yaml
python tools/validate_dl_contract.py contracts/dl-skills/DL-26-RPT-report-builder.yaml
```

## Rule

```txt
No M3 official workflow if required graph/contract validation fails.
```
