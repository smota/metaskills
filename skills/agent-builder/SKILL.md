---
name: agent-builder
description: >-
  Use when a user wants to build, design, refine, validate, or package an AI
  agent, copilot, coding assistant, skill-building assistant, tool-enabled
  agent, orchestrating agent, or reusable agent definition for another project.
  Triggers include build an agent, create an agent, agent builder, design a
  copilot, make an AI assistant, agent instructions, agent with tools, agent
  with knowledge, agent-to-agent collaboration, subprocess/job execution,
  starter prompts, package an agent, validate an agent.
---

# Agent Builder

Use this skill to turn a plain-language goal into a portable agent definition that another project can adopt.

The skill is harness-neutral by default and harness-capability-aware when a target environment provides subagents, async jobs, MCP/OpenAPI tools/actions, memory, or deployment features.

## Non-goals

Do not turn this repository into a hosted agent platform, management system, job runner, queue, or runtime. Produce files, instructions, templates, contracts, adapters, and validation guidance that downstream projects can copy, install, or adapt.

## Workflow

### 1. Understand

Collect minimum information needed:

- goal and target users
- current maturity level and target maturity level
- target harnesses or deployment environments
- jobs to perform, refuse, or delegate
- expected inputs and outputs
- knowledge sources and freshness expectations
- tools/actions needed, if any
- runtime capabilities needed: A2A, subagents, subprocess/job execution, async follow-up, MCP/OpenAPI, memory, audit/logs
- acceptable fallback when a capability is unavailable or unknown
- security, privacy, compliance, and mutation authority boundaries

Ask only for missing decisions that materially affect safety or usefulness.

### 2. Configure

Draft a harness-neutral agent package with:

- canonical `AGENT.md`
- maturity scorecard
- runtime capability matrix
- knowledge source contract
- tools/actions contracts with MCP/OpenAPI schemas
- handoff contract for Level 4+ collaboration
- execution model for Level 4+ subprocess/job work
- adapter docs for target harnesses
- starter prompts
- evals and acceptance criteria
- continuous-improvement artifacts for Level 5

### 3. Review

Check level-aware fit:

- Level 0 must not require tools/actions.
- Level 2 must include schemas and safe fallbacks for tools/actions.
- Level 3 mutating actions must include confirmation, rollback, and audit notes.
- Level 4 orchestration must include handoff, runtime capability, and subprocess/job contracts.
- Level 5 must include feedback, evals, benchmark, and changelog workflow.
- Adapters must not redefine canonical `AGENT.md` semantics.

### 4. Package

Preferred package:

```text
agents/<agent-name>/
├── README.md
├── AGENT.md
├── starter-prompts.md
├── knowledge-sources.md
├── tools-actions.md
├── runtime-capabilities.md
├── capability-maturity-scorecard.md
├── agent-guardrails-matrix.md
├── agent-validation-checklist.md
├── evals.md
├── CHANGELOG.md
├── handoff-contract.md              # Level 4+
├── execution-model.md               # Level 4+
├── continuous-improvement-plan.md    # Level 5
└── adapters/                         # optional harness capability mapping
```

## Included templates

Use files under `templates/`, including maturity scorecard, runtime capabilities, handoff contract, execution model, tools/actions, MCP/OpenAPI schema starters, adapters, evals, benchmark, feedback, and changelog templates.

## Validation

Use `references/validation-rubric.md` and `checklists/` before committing or sharing. Report gaps and follow-up honestly.
