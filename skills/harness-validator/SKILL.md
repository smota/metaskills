---
name: harness-validator
version: 1.0.0
description: Use when auditing, reviewing, or validating an AI coding-agent harness or agent-ready repository. Evaluates instructions, environment, security, scope control, continuity, verification, observability, clean state, and orchestration; reports evidence-backed gaps and prioritized improvements without editing the target project.
dependencies: []
permissions:
  - read:workspace
  - execute:non-destructive
---

# Harness Validator

Perform a read-only, evidence-first audit of the system around an AI coding agent. Assess capabilities and outcomes, not the presence of prescribed filenames or frameworks.

## Non-goals

- Do not edit, install, format, migrate, clean, commit, deploy, or otherwise mutate the target project.
- Do not treat a prompt file alone as a complete harness.
- Do not require `AGENTS.md`, `PROGRESS.md`, Make, Docker, Playwright, OpenTelemetry, worktrees, or any other named tool.
- Do not turn course heuristics or claimed improvement percentages into universal pass/fail thresholds.

## Inputs

Collect or infer:

- target repository and permitted read-only commands;
- project risk and criticality;
- expected task/session duration;
- autonomy, concurrency, deployment, and production-access context;
- known baselines, exceptions, and external systems of record.

If risk or command permission is unclear, inspect files only and mark runtime evidence `unknown`; never guess permission.

## Workflow

1. **Profile applicability.** Classify each check as `required`, `recommended`, or `not_applicable`, with a reason.
2. **Inventory evidence.** Inspect instructions, environment definitions, task state, tests, CI, permissions, connectors, logs, and orchestration artifacts.
3. **Run safe checks.** Execute only explicitly permitted, non-destructive commands. Record command, commit, environment, timestamp, result, and limitations.
4. **Test recoverability.** Apply fresh-session, authority, contradiction, staleness, and handoff-reconciliation tests.
5. **Assess nine categories.** Use [`checklists/harness-assessment.md`](checklists/harness-assessment.md).
6. **Score evidence.** Use the evidence and maturity model below; keep category results separate.
7. **Find systemic issues.** Report conflicts, missing capabilities, stale evidence, redundant controls, and over-detailed instructions.
8. **Recommend improvements.** Prefer the smallest effective change and prioritize safety/truth before maturity features.
9. **Produce artifacts.** Fill [`templates/harness-validation-report.md`](templates/harness-validation-report.md) and, when machine-readable output is useful, [`templates/assessment.json`](templates/assessment.json).
10. **Validate structured output.** Run `python scripts/validate_assessment.py <assessment.json>` from the installed skill directory.

## Evidence model

For every applicable check record:

- applicability: `required`, `recommended`, or `not_applicable` plus rationale;
- evidence state: `verified_pass`, `verified_fail`, `present_unverified`, `missing`, or `unknown`;
- maturity: `0` absent, `1` documented, `2` executable, `3` enforced and evidenced, `4` measured and maintained;
- confidence, risk, effort, provenance, exception, and smallest effective recommendation.

Never average away these blockers:

- unsafe or uncontained access, secret exposure, or destructive automation;
- no executable completion criteria;
- unreproducible environment;
- worker-controlled completion without external evidence;
- cross-boundary claims with inadequate verification.

Prioritize findings as:

- `P0`: safety or truth blocker;
- `P1`: reliability blocker;
- `P2`: scale, continuity, or recovery blocker;
- `P3`: efficiency and maintainability;
- `P4`: optional maturity.

## Required report behavior

- Separate observation from inference and recommendation.
- Cite concrete files, commands, outputs, and limitations.
- Include not-applicable checks and rationale.
- Explain conflicts instead of silently choosing one rule.
- Call out gaps in security, provenance, recovery, non-functional quality, human comprehension, and economics when applicable.
- Flag stale or contradictory guidance as riskier than acknowledged absence.
- Recommend simpler alternatives when advanced loops, multiple agents, or graphs do not demonstrate value.

## Supporting material

- Full checklist: [`checklists/harness-assessment.md`](checklists/harness-assessment.md)
- Lecture traceability and design rationale: [`references/lecture-traceability.md`](references/lecture-traceability.md)
- Report template: [`templates/harness-validation-report.md`](templates/harness-validation-report.md)
- Structured template: [`templates/assessment.json`](templates/assessment.json)
- Complete-template generator: [`scripts/new_assessment.py`](scripts/new_assessment.py)
- Eval cases and fixture outputs: [`evals/`](evals/)
- Fixture-backed behavioral contract runner: [`scripts/run_evals.py`](scripts/run_evals.py)
