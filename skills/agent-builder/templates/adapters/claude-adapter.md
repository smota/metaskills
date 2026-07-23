# Claude adapter

Use Claude project files as thin compatibility pointers to canonical `AGENT.md`.

## Required features

- `AGENT.md` readable in target repo.
- Optional `CLAUDE.md` pointer or short summary that links back to canonical instructions.

## Supported features

- Instruction loading through `CLAUDE.md` or project guidance.
- Tool/action use when target environment exposes tools.
- Skills when target environment supports skill activation.

## Unsupported or unknown features

- No subagent support -> fallback: manual handoff checklist.
- No async subprocess/job support -> fallback: user-run commands and resume notes.
- No MCP/OpenAPI action support -> fallback: manual procedure in `tools-actions.md`.

## Configuration notes

- Keep long-form behavior in `AGENT.md`.
- `CLAUDE.md` should say: “Use `agents/<agent-name>/AGENT.md` as canonical instructions.”
- Document any Claude-specific tools in this adapter, not in canonical semantics.

## Validation

- Confirm `CLAUDE.md` points to `AGENT.md`.
- Run starter prompt without optional tools.
- Run one missing-capability fallback eval.

## No semantic override

This adapter must not redefine role, scope, authority, safety rules, or success criteria from `AGENT.md`.
