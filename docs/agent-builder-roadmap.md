# Agent Builder roadmap: epics and feature breakdown

This roadmap keeps `agent-builder` focused on architecting, specifying, packaging, and validating portable agents. It must not become an agent hosting runtime. The skill should describe required capabilities, contracts, and adapters so downstream agent environments can execute them when available.

## Product principles

- Keep canonical agent instructions in `AGENT.md`.
- Use `CLAUDE.md`, `CODEX.md`, `GEMINI.md`, and other target files as thin compatibility pointers or adapters.
- Separate harness-neutral intent from harness-specific execution.
- Prefer explicit contracts over hidden assumptions.
- Model platform capabilities without requiring this repository to run as a service.
- Document every `tool/action` with inputs, outputs, auth, safety, `error/fallback`, and validation behavior.
- Prefer standard `MCP/OpenAPI` schemas for `tools/actions`.

## Maturity model

Agents should not need every capability on day one. `agent-builder` should assign a current maturity level and generate the next improvement path.

| Level | Name | Agent capability | Typical assets |
| --- | --- | --- | --- |
| 0 | Prompt agent | Role, scope, refusals, output style | `AGENT.md`, starter prompts |
| 1 | Knowledge agent | Source-aware answers with freshness and citation rules | `knowledge-sources.md`, missing-context behavior |
| 2 | Tool-enabled agent | Read-oriented `tools/actions` with schemas and safe invocation rules | `tools-actions.md`, `mcp-tool-schema.json`, `openapi-tool-schema.yaml` |
| 3 | Action agent | Mutating actions with confirmation, rollback, and audit expectations | guardrails matrix, action validation plan |
| 4 | Orchestrating agent | Agent-to-agent handoff, delegation, `subprocess/job` execution, async follow-up | handoff contract, execution model, runtime capability matrix |
| 5 | Learning agent | Feedback, evals, regression checks, benchmark history, continuous improvement | eval suite, feedback log, improvement plan, changelog |

## GitHub epic breakdown

### Epic 1: Capability maturity model

**Goal:** Make `agent-builder` produce agents with an explicit maturity level and next-step upgrade path.

Features:

- Add a maturity scorecard template.
- Add maturity-level guidance to `SKILL.md` workflow.
- Add questions to intake checklist for desired starting level and target level.
- Add validation rubric items for maturity fit.

Acceptance criteria:

- Generated agent package states current and target maturity levels.
- Level 0-5 definitions appear in skill references or templates.
- Validation can pass a simple prompt-only agent without forcing tools/actions.
- Validation can identify when orchestration claims lack supporting contracts.

Suggested issue title:

> Epic: Add capability maturity model to agent-builder

### Epic 2: Harness-neutral core package

**Goal:** Ensure agents remain portable across harnesses while retaining enough structure for real deployment.

Features:

- Keep `AGENT.md` as canonical source.
- Add `runtime-capabilities.md` template.
- Add `capability-maturity-scorecard.md` template.
- Clarify compatibility files: `CLAUDE.md`, `CODEX.md`, `GEMINI.md`, GitHub Copilot instructions.
- Update packaging target docs to separate core assets from adapters.

Acceptance criteria:

- Generated package can be copied into another repo without requiring `metaskills`.
- Harness-specific files point back to canonical instructions instead of duplicating full content.
- Package clearly marks required, optional, and unavailable runtime capabilities.

Suggested issue title:

> Epic: Split harness-neutral agent core from harness adapters

### Epic 3: Harness adapter model

**Goal:** Let generated agents leverage harness capabilities when present, with graceful fallback when absent.

Features:

- Add `adapters/` package convention.
- Add adapter templates for Pi, Claude, Codex, Gemini, and Microsoft Foundry notes.
- Define mapping from semantic needs to runtime primitives.
- Document fallback behavior when harness lacks subagents, async jobs, or tool hosting.

Example mapping:

| Semantic need | Pi adapter | Generic fallback |
| --- | --- | --- |
| Research delegation | subagent single/parallel | manual handoff checklist |
| Review gate | reviewer subagent | human review checklist |
| Long-running work | async `subprocess/job` | explicit command plus resume instructions |
| Tool call | MCP/OpenAPI tool/action | documented manual procedure |

Acceptance criteria:

- Agent package can include harness-specific enhancements without changing `AGENT.md` semantics.
- Each adapter states required harness features and fallback mode.
- Missing capability never becomes silent failure.

Suggested issue title:

> Epic: Add harness adapters with capability detection and fallback guidance

### Epic 4: Agent-to-agent collaboration contracts

**Goal:** Support true multi-agent workflows without embedding a runtime into `agent-builder`.

Features:

- Add `handoff-contract.md` template.
- Define handoff envelope: task, context, constraints, expected output, deadline, priority.
- Define status states: queued, running, blocked, needs-human, complete, failed, cancelled.
- Define reviewer/validator/planner-worker patterns.
- Add collaboration safety rules for scope, secrets, and mutation authority.

Acceptance criteria:

- Orchestrating agents specify which tasks may be delegated.
- Delegated work has explicit input/output schemas.
- Handoff failure includes `error/fallback` behavior.
- Multi-agent workflows can degrade to manual handoff in harnesses without A2A support.

Suggested issue title:

> Epic: Add agent-to-agent handoff contracts

### Epic 5: Subprocess and async job execution model

**Goal:** Describe how agents request, monitor, and recover from external work without owning the job runner.

Features:

- Add `execution-model.md` or `subprocess-triggers.md` template.
- Document `subprocess/job` lifecycle: start, observe, wait, cancel, retry, resume, complete.
- Define output capture and summarization expectations.
- Define timeout, retry, idempotency, and rollback rules.
- Add examples for builds, tests, scans, data processing, and deployments.

Acceptance criteria:

- Generated agents state which jobs they can trigger.
- Mutating jobs require confirmation and rollback notes.
- Long-running jobs specify async follow-up behavior.
- Failed jobs include structured `error/fallback` guidance.

Suggested issue title:

> Epic: Add subprocess and async job execution contracts

### Epic 6: Tool/action schema and safety upgrade

**Goal:** Improve `tools/actions` from descriptive docs into deployable contracts.

Features:

- Expand `agent-tool-actions.md` with required schema fields.
- Strengthen `mcp-tool-schema.json` and `openapi-tool-schema.yaml` examples.
- Add permission tiers: read, suggest, stage, mutate, external-publish, admin.
- Add confirmation, rollback, and audit requirements per tier.
- Add validation checklist for each `tool/action`.

Acceptance criteria:

- Every tool/action has purpose, schema, auth, permissions, failure modes, and validation.
- MCP/OpenAPI schema examples are usable as starting points.
- Destructive or externally visible actions require confirmation by default.
- Tool absence and tool failure are distinct fallback cases.

Suggested issue title:

> Epic: Harden tools/actions contracts for MCP and OpenAPI

### Epic 7: Continuous improvement loop

**Goal:** Make every generated agent improvable through evals, feedback, and versioned changes.

Features:

- Add `continuous-improvement-plan.md` template.
- Add optional `feedback.jsonl` shape for local feedback capture.
- Add improvement workflow: observe, classify, patch, validate, record.
- Add benchmark guidance for comparing agent versions.
- Add changelog expectations for agent packages.

Acceptance criteria:

- Generated agent packages include evals and known gaps.
- Feedback categories include scope, knowledge, tool/action, safety, UX, orchestration, and environment.
- Improvements update evals before or alongside instructions.
- Agent releases record what changed and why.

Suggested issue title:

> Epic: Add continuous improvement loop for generated agents

### Epic 8: Examples and validation fixtures

**Goal:** Prove roadmap features with concrete agent packages.

Features:

- Add a Level 0 prompt-only example.
- Add a Level 2 MCP/OpenAPI tool-enabled example.
- Add a Level 4 orchestrating example with A2A and `subprocess/job` contracts.
- Add a Level 5 learning-agent example with evals and feedback loop.
- Add release checklist coverage for generated examples.

Acceptance criteria:

- Examples validate package structure and portability.
- Examples show harness-specific adapters only under adapter docs.
- Examples include fallback behavior for missing harness capabilities.
- Example README files state current maturity level.

Suggested issue title:

> Epic: Add maturity-based agent examples and validation fixtures

## Recommended implementation sequence

1. Add maturity model reference and scorecard template.
2. Add runtime capability and harness adapter templates.
3. Add handoff and subprocess/job contract templates.
4. Upgrade tools/actions schema guidance.
5. Update `SKILL.md`, README, checklists, and validation rubric.
6. Add examples for Level 0, Level 2, Level 4, and Level 5 agents.
7. Add release notes and GitHub issues for each epic.

## Definition of done for roadmap completion

- `agent-builder` can generate a portable `AGENT.md` package for simple agents.
- Same package can declare optional harness-specific enhancements without losing portability.
- Generated agents can specify A2A, `subprocess/job`, MCP/OpenAPI, and tool/action behavior as contracts.
- Harnesses with advanced capabilities can execute those contracts through adapters.
- Harnesses without those capabilities receive safe manual fallback paths.
- Continuous improvement artifacts exist for evals, feedback, benchmark, and changelog-driven agent evolution.
