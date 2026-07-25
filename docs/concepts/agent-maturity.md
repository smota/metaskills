# Agent maturity model

Agent Builder 1.1 treats agent capability as a journey. Not every agent needs tools, handoffs, jobs, or feedback loops on day one.

| Level | Name | Capability | Typical evidence |
| --- | --- | --- | --- |
| 0 | Prompt agent | Role, scope, refusals, output style | `AGENT.md`, starter prompts |
| 1 | Knowledge agent | Source-aware answers with freshness and missing-context behavior | `knowledge-sources.md`, citation rules |
| 2 | Tool-enabled agent | Read-oriented MCP/OpenAPI tools/actions | `tools-actions.md`, schemas, fallbacks |
| 3 | Action agent | Mutating actions with confirmation and rollback | guardrails matrix, audit notes |
| 4 | Orchestrating agent | A2A handoffs, reviewer gates, subprocess/job lifecycle | handoff contract, execution model, adapters |
| 5 | Learning agent | Evals, feedback, benchmark history, changelog-driven improvement | eval suite, feedback shape, benchmark report |

## Rules

- Level 0 is valid. Do not force tools onto prompt-only agents.
- Level 2 requires schemas and failure handling.
- Level 3 requires confirmation and rollback for mutation.
- Level 4 requires handoff/runtime/job contracts.
- Level 5 requires evals, feedback, benchmark, and changelog workflow.

## Use in practice

1. State current level.
2. State target level.
3. Document missing contracts.
4. Add one capability at a time.
5. Validate before claiming next level.
