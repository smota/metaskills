---
name: skill-creator
version: 1.0.0
description: Use when creating, improving, evaluating, benchmarking, packaging, or evolving AI agent skills. Triggers include create a skill, build a skill, skill creator, skill builder, improve a skill, evaluate a skill, benchmark a skill, convert workflow to skill, convert sub-agent to skill, skill telemetry, learning workflow, production-ready SKILL.md.
dependencies: []
permissions:
  - read:workspace
  - write:workspace
---

# Skill Creator

Use this skill to create, improve, evaluate, benchmark, and evolve portable skills consistently across projects.

This skill is inspired by Claude Skill Creator's lifecycle of Create, Eval, Improve, and Benchmark, and by `metaskills/skill-builder` guidance for production-ready `SKILL.md` files, progressive disclosure, and converting sub-agents to skills.

## Non-goals

Do not create a hosted skill platform or hidden telemetry system. Produce portable files, templates, evals, checklists, and optional local learning artifacts that downstream projects can own.

## Operating modes

### 1. Create

Turn an idea, workflow, prompt, document, transcript, script, or sub-agent into a skill package.

Collect:

- skill goal and target users
- activation triggers
- tasks the skill should perform
- tasks the skill should avoid
- required tools or environment assumptions
- examples of successful use
- target install tools, if known

Output a package shaped like:

```text
skills/<skill-name>/
├── SKILL.md
├── README.md
├── templates/
├── checklists/
├── security/
│   └── guardrails-matrix.md
├── references/
└── examples/
```

### 2. Eval

Create lightweight eval cases that test whether a skill activates correctly and produces useful results.

Prefer pass/fail cases with:

- scenario
- prompt
- expected behavior
- must include
- must not include
- pass criteria

### 3. Improve

Revise a skill using feedback, failed evals, benchmark results, or observed gaps. Ensure you parse and ingest any logs from `feedback.jsonl` to address recurring failures.

Improve:

- activation description
- workflow clarity
- progressive disclosure
- examples
- safety boundaries
- eval coverage
- context efficiency

### 4. Benchmark

Compare skill versions or alternatives using the same eval cases.

Compare:

- task completion
- instruction following
- output quality
- boundary behavior
- unnecessary tool use
- context footprint
- regressions

### 5. Learn

Optionally maintain a local learning workflow that records durable lessons, recurring failures, successful patterns, and next eval cases.

Learning must be explicit, file-based, and reviewable.

### 6. Telemetry

Optionally design privacy-safe telemetry plans for downstream projects.

Telemetry must be opt-in, local-first by default, and avoid raw prompts, secrets, customer data, and full conversation logs unless the downstream owner explicitly approves them. Provide the user with `telemetry-dashboard.html` to visualize their local JSONL logs.

## Progressive disclosure rules

- Keep `SKILL.md` focused on activation, workflow, and essential rules.
- Move detailed procedures into `references/`.
- Put reusable forms in `templates/`.
- Put pass/fail review material in `checklists/`.
- Include examples that show realistic use.
- Reference supporting files by relative path.

## Output contract

When asked to create or modify a skill:

1. Identify the operating mode.
2. Inspect existing files when modifying a skill.
3. Produce concrete files or a concise implementation plan.
4. Add eval or acceptance criteria.
5. State validation performed and remaining gaps.

Use the bundled templates in `templates/` when creating skill packages, evals, improvement plans, benchmark reports, learning logs, or telemetry plans.
