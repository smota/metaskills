# Pi adapter

Maps canonical `AGENT.md` behavior to Pi harness capabilities when present. Does not change role, scope, authority, safety rules, or success criteria.

## Required features

- None for Level 0-3 agents.
- Level 4 orchestration may use Pi subagents when available.
- Level 4 async work may use background subprocess/job orchestration when available.

## Supported features

- Research delegation: Pi single/parallel subagents.
- Review gate: reviewer subagent or review-loop pattern.
- Planner-worker split: planner + worker handoff.
- Long-running work: async/background run with status and follow-up.
- Coordination: intercom/status messages where configured.

## Unsupported or unknown features

- Subagents unavailable -> fallback: manual handoff checklist from `handoff-contract.md`.
- Async job unavailable -> fallback: user-run command and resume instructions from `execution-model.md`.
- MCP tool unavailable -> fallback: manual procedure from `tools-actions.md`.

## Configuration notes

- Keep `AGENT.md` canonical.
- Add Pi-specific invocation examples in adapter only.
- Declare required subagent roles and whether they are read-only or mutation-capable.

## Validation

- Run one no-tool prompt eval.
- If subagents claimed, run a delegated dry-run task or document unavailable fallback.
- If async jobs claimed, run a harmless command job or document unavailable fallback.

## No semantic override

This adapter must not redefine role, scope, authority, safety rules, or success criteria from `AGENT.md`.
