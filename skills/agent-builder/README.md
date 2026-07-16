# agent-builder skill

The `agent-builder` skill helps users create practical, portable agents from plain-language goals.

It is inspired by Microsoft 365 Copilot Agent Builder's simple flow — describe, configure, add knowledge, add actions, review — and uses `agent-skill-creator` as an implementation/reference component for turning workflows into reusable agent assets.

## Use cases

- design a new AI agent for a downstream project
- convert a workflow into agent instructions
- define knowledge sources and tool/action requirements
- create starter prompts and validation criteria
- package an agent definition for reuse

## Inputs

Useful inputs include:

- agent goal
- target users
- workflows the agent should support
- source documents or repositories
- tools/actions the agent can call
- output format preferences
- safety or compliance boundaries

## Outputs

The recommended output package is:

```text
agents/<agent-name>/
├── README.md
├── AGENT.md
├── starter-prompts.md
├── knowledge-sources.md
├── tools-actions.md
└── evals.md
```

## References

- [`references/microsoft-agent-builder-notes.md`](./references/microsoft-agent-builder-notes.md)
- [`references/agent-skill-creator-notes.md`](./references/agent-skill-creator-notes.md)
- [`references/output-schema.md`](./references/output-schema.md)
- Component submodule in the source repo: [`../../components/agent-skill-creator`](../../components/agent-skill-creator)

## Included templates

The installable skill package includes its own templates under [`templates/`](./templates/):

- `agent-builder-intake.md`
- `agent-definition.md`
- `agent-evals.md`
- `agent-guardrails-matrix.md`
- `agent-readme.md`
- `agent-starter-prompts.md`
- `agent-tool-actions.md`
- `agent-validation-checklist.md`
- `mcp-tool-schema.json`
- `openapi-tool-schema.yaml`

These templates live inside the skill package so installers such as `npx skills add <repo> --skill agent-builder` install a complete, self-contained skill.

## Validation

Use the included templates and the checklists in [`checklists/`](./checklists/) to review generated agent packages before committing or sharing them.
