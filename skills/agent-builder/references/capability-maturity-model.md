# Capability maturity model

Use this model to choose how much agent capability to design now. Not every agent needs every platform feature.

| Level | Name | Capability | Required assets | Common next step |
| --- | --- | --- | --- | --- |
| 0 | Prompt agent | Role, scope, refusal rules, output style | `AGENT.md`, starter prompts | Add knowledge sources |
| 1 | Knowledge agent | Source-aware answers, freshness rules, citations, missing-context behavior | `knowledge-sources.md`, evals | Add read tools/actions |
| 2 | Tool-enabled agent | Read-oriented `tools/actions` with MCP/OpenAPI schemas and safe invocation rules | `tools-actions.md`, schemas, runtime capabilities | Add guarded mutation |
| 3 | Action agent | Mutating actions with confirmation, rollback, audit expectations | guardrails matrix, validation plan | Add delegation/jobs |
| 4 | Orchestrating agent | Agent-to-agent handoff, delegation, `subprocess/job` execution, async follow-up | handoff contract, execution model, adapters | Add learning loop |
| 5 | Learning agent | Feedback, evals, regression checks, benchmark history, continuous improvement | feedback shape, benchmark report, changelog | Tighten metrics and rollout |

## Rules

- Level 0 is valid. Do not force tools/actions into a prompt-only agent.
- Level 2 requires schemas and failure handling for every tool/action.
- Level 3 requires confirmation and rollback notes for mutating work.
- Level 4 claims require handoff, runtime capability, and subprocess/job contracts.
- Level 5 requires evals, feedback classification, improvement workflow, and changelog discipline.
- If runtime support is missing or unknown, state fallback behavior instead of pretending support exists.

## Upgrade guidance

1. Identify current level from evidence, not aspiration.
2. Pick one target level for next release.
3. Add only contracts needed for that level.
4. Validate current level before adding advanced adapters.
5. Record gaps and follow-up in the generated package.
