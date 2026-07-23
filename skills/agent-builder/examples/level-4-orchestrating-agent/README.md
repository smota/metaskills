# Level 4 orchestrating agent fixture

Current maturity: Level 4 orchestrating agent.
Target maturity: Level 5 learning agent.

## Package shape

```text
agents/repo-change-orchestrator/
├── README.md
├── AGENT.md
├── runtime-capabilities.md
├── handoff-contract.md
├── execution-model.md
├── tools-actions.md
├── agent-guardrails-matrix.md
├── agent-validation-checklist.md
├── evals.md
└── adapters/
    ├── pi-adapter.md
    └── claude-adapter.md
```

## Collaboration contract

- Delegable tasks: codebase reconnaissance, plan review, implementation review.
- Forbidden delegation: secret handling, production deploy approval, final user decision.
- Status states: queued, running, blocked, needs-human, complete, failed, cancelled.

## Subprocess/job contract

- Jobs: tests, lint, build, security scan.
- Mutating jobs: none by default.
- Timeout/retry/resume behavior documented in `execution-model.md`.

## Fallback behavior

- No A2A/subagents: use manual handoff checklist.
- No async job runner: user runs command and provides output.
- No MCP/OpenAPI tools/actions: use manual procedure.

## Validation

- Handoff envelope has input/output schema.
- Job failure produces structured `error/fallback`.
- Adapter docs do not override `AGENT.md`.
