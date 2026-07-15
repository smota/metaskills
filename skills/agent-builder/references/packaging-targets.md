# Packaging targets

Start with a tool-neutral package, then add target-specific pointers or exports.

## Canonical package

```text
agents/<agent-name>/
├── README.md
├── AGENT.md
├── starter-prompts.md
├── knowledge-sources.md
├── tools-actions.md
└── evals.md
```

## Target-specific mappings

| Target | Recommended export |
| --- | --- |
| Generic agent repo | `agents/<agent-name>/AGENT.md` |
| Multi-agent repo | Section in `AGENTS.md` or linked `agents/<agent-name>/AGENT.md` |
| Claude | `CLAUDE.md` pointer to canonical instructions |
| Codex | `CODEX.md` pointer to canonical instructions |
| Gemini | `GEMINI.md` pointer to canonical instructions |
| GitHub Copilot | `.github/copilot-instructions.md` pointer or summary |
| Skill package | `skills/<skill-name>/SKILL.md` plus references |

## Export rules

- Avoid duplicating long instructions across targets.
- Keep one canonical source where possible.
- Use target-specific files as compatibility pointers.
- Include validation and adoption notes in the package README.
