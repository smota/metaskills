# Gemini adapter

Use Gemini project files as thin compatibility pointers to canonical `AGENT.md`.

## Required features

- `AGENT.md` readable in target repo.
- Optional `GEMINI.md` pointer or concise summary linked to canonical instructions.

## Supported features

- Instruction loading through `GEMINI.md` or project guidance.
- Tool/action use when target harness exposes tools.
- Knowledge-grounded operation when sources are provided.

## Unsupported or unknown features

- No subagent/A2A support -> fallback: manual handoff checklist.
- No async subprocess/job support -> fallback: user-run command and resume notes.
- No MCP/OpenAPI tool support -> fallback: manual procedure from `tools-actions.md`.

## Configuration notes

- Keep canonical behavior in `AGENT.md`.
- Add Gemini-specific prompt or context-size notes here only.
- Document missing capability states in `runtime-capabilities.md`.

## Validation

- Confirm `GEMINI.md` points to `AGENT.md`.
- Run starter prompt without optional tools.
- Run missing knowledge or missing tool fallback eval.

## No semantic override

This adapter must not redefine role, scope, authority, safety rules, or success criteria from `AGENT.md`.
