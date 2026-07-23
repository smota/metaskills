# <Agent name>

## Purpose

<What this agent helps users do.>

## Maturity

- Current level: `<0-5>`
- Target level: `<0-5>`
- See `capability-maturity-scorecard.md`.

## Package contents

Core harness-neutral files:

- `AGENT.md` - canonical instructions
- `starter-prompts.md`
- `knowledge-sources.md`
- `tools-actions.md`
- `agent-guardrails-matrix.md`
- `agent-validation-checklist.md`
- `evals.md`

Optional capability files:

- `runtime-capabilities.md`
- `capability-maturity-scorecard.md`
- `handoff-contract.md`
- `execution-model.md`
- `continuous-improvement-plan.md`
- `CHANGELOG.md`
- `adapters/`

## Install/adopt

Copy this package into a downstream repo. It does not require `metaskills` at runtime.

## Harness adapters

Adapters may describe how to use platform features when present. If a harness lacks subagents, async jobs, MCP/OpenAPI tools/actions, or memory, follow documented fallback behavior.

## Validation

Run the evals and checklist before release.
