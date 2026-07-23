# Harness adapters

Adapters map harness-neutral agent semantics to platform-specific capabilities. They must not override `AGENT.md`.

## Adapter rule

- `AGENT.md` owns role, scope, authority, safety, and success criteria.
- Adapter files own invocation mechanics, capability mapping, setup notes, and fallback behavior.
- Missing capability must be explicit: `available`, `unavailable`, or `unknown`.

## Included adapters

- `pi-adapter.md` - subagents, review loops, async jobs, intercom/status when present.
- `claude-adapter.md` - `CLAUDE.md` pointer and Claude project guidance.
- `codex-adapter.md` - `CODEX.md` pointer and coding-agent command guidance.
- `gemini-adapter.md` - `GEMINI.md` pointer and Gemini project guidance.
- `microsoft-foundry-adapter.md` - Foundry/Copilot-style deployment mapping.

## Required validation per adapter

- Confirms canonical pointer to `AGENT.md`.
- Lists supported, unsupported, and unknown capabilities.
- Provides fallback for each missing capability.
- Includes at least one validation check.
