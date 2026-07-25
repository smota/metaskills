# Harness adapters

MetaSkills aims to be harness-agnostic but capability-aware.

## Core idea

- `AGENT.md` is canonical and portable.
- Adapters explain how to use harness capabilities when present.
- Adapters must not redefine role, scope, authority, safety, or success criteria.
- Missing capability must have fallback.

## Examples

| Semantic need | Harness capability | Fallback |
| --- | --- | --- |
| Research delegation | subagent single/parallel | manual handoff checklist |
| Review gate | reviewer/validator agent | human review checklist |
| Long-running work | async subprocess/job runner | user-run command plus resume notes |
| Tool call | MCP/OpenAPI action | manual procedure |
| Feedback loop | telemetry or local memory | redacted feedback notes and changelog |

## Adapter files

Typical generated agent packages may include:

```text
adapters/
├── pi-adapter.md
├── claude-adapter.md
├── codex-adapter.md
├── gemini-adapter.md
└── microsoft-foundry-adapter.md
```

## Design rule

Harness power is optional acceleration, not lock-in. A generated agent should still be understandable and useful as files even when target runtime features are unavailable.
