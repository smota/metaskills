# harness-validator

A portable, read-only skill for auditing whether a project gives AI coding agents a reliable, safe, observable, and recoverable working environment.

## Use it when

- reviewing whether a repository is agent-ready;
- diagnosing recurring agent failures;
- validating long-running or autonomous-agent infrastructure;
- evaluating completion gates, state continuity, observability, or orchestration;
- looking for conflicting, missing, stale, redundant, or over-detailed harness controls.

## Prerequisites

- Read access to the target repository.
- Explicit permission for any commands the audit will execute.
- Python 3 only when validating optional machine-readable output.

The skill has no runtime service, vendor, model, or framework dependency.

## Inputs and outputs

Inputs include the repository, project risk, expected task duration, autonomy/concurrency/deployment context, and permitted commands.

Outputs include:

- a category-by-category maturity assessment;
- evidence-backed findings and non-averaged blockers;
- conflicts, gaps, stale evidence, and over-detailed controls;
- a prioritized sequence of smallest effective improvements;
- optional structured JSON validated by the bundled script.

## Usage

```text
Use harness-validator to audit this repository for long-running coding-agent work. Do not edit anything. Run only existing test and inspection commands, and produce an evidence-backed report.
```

```text
Review this autonomous pull-request loop. Focus on permissions, state recovery, independent verification, stopping conditions, cost budgets, and whether a graph is justified.
```

```text
Assess this small utility with harness-validator. Mark advanced orchestration checks not applicable when appropriate and recommend the simplest reliable setup.
```

## Package contents

```text
skills/harness-validator/
├── SKILL.md
├── README.md
├── checklists/harness-assessment.md
├── evals/cases.json
├── evals/fixture-outputs.json
├── references/lecture-traceability.md
├── scripts/new_assessment.py
├── scripts/validate_assessment.py
├── scripts/run_evals.py
└── templates/
    ├── assessment.json
    └── harness-validation-report.md
```

## Validate structured output

```bash
python skills/harness-validator/scripts/validate_assessment.py \
  skills/harness-validator/templates/assessment.json
```

Expected output:

```text
VALID: 9 categories, 78 checks
```

Every structured assessment must include all 78 canonical checks across nine categories, marking inapplicable checks explicitly. Regenerate a complete blank template after checklist changes with `python skills/harness-validator/scripts/new_assessment.py`.

Run the deterministic contract evals:

```bash
python skills/harness-validator/scripts/run_evals.py skills/harness-validator
```

The eval runner performs fixture-backed behavioral contract evaluation: it validates every scenario's expected and prohibited output behavior plus required instruction-contract evidence. It is deterministic and does not claim to replace a live-model benchmark.

## Success criteria

A successful audit is read-only, application-aware, evidence-backed, explicit about uncertainty, complete across applicable categories, and prioritized by risk reduction rather than artifact count.

## Source basis

The category model synthesizes all fourteen English lectures from [Learn Harness Engineering](https://walkinglabs.github.io/learn-harness-engineering/en/) and extends them with security, provenance, recovery, non-functional quality, human-comprehension, test-strength, and economic checks.
