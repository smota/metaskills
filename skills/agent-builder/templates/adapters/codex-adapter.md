# Codex adapter

Use Codex project files as thin compatibility pointers to canonical `AGENT.md`.

## Required features

- `AGENT.md` readable in target repo.
- Optional `CODEX.md` pointer or concise summary linked to canonical instructions.

## Supported features

- Coding-agent instruction loading through `CODEX.md` or repo guidance.
- Local command execution when available and permitted.
- Tool/action use when configured by harness.

## Unsupported or unknown features

- No agent-to-agent transport -> fallback: manual handoff checklist.
- No long-running job management -> fallback: explicit command plus resume/status notes.
- No MCP/OpenAPI tool hosting -> fallback: documented manual procedure.

## Configuration notes

- Keep canonical behavior in `AGENT.md`.
- Put Codex-specific command or repository conventions here.
- Do not duplicate long instructions.

## Validation

- Confirm `CODEX.md` points to `AGENT.md`.
- Run no-tool starter prompt.
- If command execution is used, run harmless validation command or document fallback.

## No semantic override

This adapter must not redefine role, scope, authority, safety rules, or success criteria from `AGENT.md`.
