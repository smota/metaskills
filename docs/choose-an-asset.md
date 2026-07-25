# Choose an asset

Use this decision guide when you are unsure whether to create a skill, agent, toolset, component, example, or doc.

## Quick decision tree

```text
Do users talk to it as a role or worker?
  yes → agent
  no  → continue

Is it a reusable capability, procedure, workflow, or prompt package?
  yes → skill
  no  → continue

Is it a tool integration, schema, wrapper, MCP/OpenAPI guide, or command pattern?
  yes → toolset
  no  → continue

Is it an external repository with its own lifecycle?
  yes → component submodule
  no  → continue

Is it only illustrating use of existing assets?
  yes → example
  no  → doc or ADR
```

## Asset types

| Asset | Use when | Expected location |
| --- | --- | --- |
| Agent | Reusable persona/worker users can ask to perform a role | `agents/<agent-name>/` |
| Skill | Reusable capability/procedure that improves agent behavior | `skills/<skill-name>/` |
| Toolset | Tool integration notes, schemas, wrappers, or usage guides | `toolsets/<toolset-name>/` |
| Component | External repo with its own lifecycle, linked for reference or tooling | `components/<name>` plus `.metaskills.md` |
| Example | Minimal adoption scenario or generated output sample | `examples/<example-name>/` |
| Guide | Step-by-step procedure | `docs/guides/` |
| Concept | Explanation of a model or term | `docs/concepts/` |
| Reference | Stable architecture, policy, or workflow detail | `docs/reference/` |
| ADR | Durable decision and rationale | `docs/adr/` |

## Agent vs skill

Choose an **agent** when the asset describes a worker with a goal, scope, authority, tools, knowledge, and expected outputs.

Choose a **skill** when the asset describes a reusable capability or procedure that another agent can activate.

Simple rule:

- “Build a repo onboarding assistant” → agent.
- “Create a reusable process for reviewing database migrations” → skill.

## Toolset vs skill

Choose a **toolset** when the main value is integration mechanics: MCP server notes, OpenAPI schema patterns, command wrappers, auth setup, or usage constraints.

Choose a **skill** when the main value is reasoning workflow, activation guidance, examples, and success criteria.

## Component vs native asset

Choose a **component** when the source has its own lifecycle, releases, issues, PRs, or upstream contribution path.

Choose a **native asset** when MetaSkills owns the reusable package directly.
