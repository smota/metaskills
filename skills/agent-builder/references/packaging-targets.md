# Packaging targets

Start with a harness-neutral core package, then add target-specific adapters or compatibility pointers.

## Canonical core package

```text
agents/<agent-name>/
├── README.md
├── AGENT.md
├── starter-prompts.md
├── knowledge-sources.md
├── tools-actions.md
├── runtime-capabilities.md
├── capability-maturity-scorecard.md
├── agent-guardrails-matrix.md
├── agent-validation-checklist.md
├── evals.md
└── CHANGELOG.md
```

## Optional capability package

```text
agents/<agent-name>/
├── handoff-contract.md
├── execution-model.md
├── continuous-improvement-plan.md
├── feedback.jsonl
├── benchmark-report.md
└── adapters/
    ├── pi-adapter.md
    ├── claude-adapter.md
    ├── codex-adapter.md
    ├── gemini-adapter.md
    └── microsoft-foundry-adapter.md
```

## Target-specific mappings

| Target | Recommended export |
| --- | --- |
| Generic agent repo | `agents/<agent-name>/AGENT.md` |
| Multi-agent repo | Section in `AGENTS.md` or linked `agents/<agent-name>/AGENT.md` |
| Claude | `CLAUDE.md` pointer to canonical instructions plus optional adapter |
| Codex | `CODEX.md` pointer to canonical instructions plus optional adapter |
| Gemini | `GEMINI.md` pointer to canonical instructions plus optional adapter |
| GitHub Copilot | `.github/copilot-instructions.md` pointer or summary |
| Pi | adapter docs for subagents, async jobs, intercom/status, and fallbacks |
| Microsoft Foundry | adapter docs for deployment, knowledge, actions, evals, monitoring |
| Skill package | `skills/<skill-name>/SKILL.md` plus references |

## Export rules

- Keep `AGENT.md` canonical.
- Avoid duplicating long instructions across targets.
- Use target-specific files as compatibility pointers or adapters.
- Adapters may add invocation mechanics, not new semantics.
- Include validation and adoption notes in package README.
