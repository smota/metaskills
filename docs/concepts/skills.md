# Skills

A skill is a reusable capability, procedure, workflow, or prompt package that another agent can activate.

## Use a skill when

- a workflow should be repeated across projects
- activation triggers matter
- examples, checklists, templates, or references help execution
- the asset should install as a self-contained package

## Typical package

```text
skills/<skill-name>/
├── SKILL.md
├── README.md
├── templates/
├── checklists/
├── references/
└── examples/
```

## Current native skills

- [`agent-builder`](../../skills/agent-builder/)
- [`skill-creator`](../../skills/skill-creator/)
