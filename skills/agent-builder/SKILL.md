---
name: agent-builder
description: Use when a user wants to build, design, refine, validate, or package an AI agent, copilot, coding assistant, skill-building assistant, tool-enabled agent, or reusable agent definition for another project. Triggers include: build an agent, create an agent, agent builder, design a copilot, make an AI assistant, agent instructions, agent with tools, agent with knowledge, starter prompts, package an agent, validate an agent.
---

# Agent Builder

Use this skill to turn a plain-language goal into a portable agent definition that another project can adopt.

This skill borrows the simple configure-and-review workflow from Microsoft 365 Copilot Agent Builder and the plain-English-to-reusable-asset strategy from `agent-skill-creator`, while staying tool-neutral and repository-portable.

## Non-goals

Do not turn the current repository into a hosted agent platform, management system, or runtime. Produce files, instructions, templates, and validation guidance that downstream projects can copy, install, or adapt.

## Workflow

### 1. Understand

Collect the minimum information needed to scope the agent:

- user goal and target users
- jobs the agent must perform
- jobs the agent must refuse or delegate
- expected input and output formats
- knowledge sources the agent can use
- tools/actions the agent needs
- security, privacy, and compliance boundaries
- target downstream environment, if known

If the user gives enough information, proceed without a long questionnaire. Ask only for missing decisions that materially affect safety or usefulness.

### 2. Configure

Draft an agent specification with:

- name: short, descriptive, and scoped
- description: one paragraph explaining when to use the agent
- instructions: operational behavior, boundaries, and workflow
- knowledge: source list, freshness expectations, and access notes
- tools/actions: required capabilities, inputs, outputs, auth, and failure modes
- starter prompts: realistic prompts users can try immediately
- acceptance criteria: how to tell whether the agent works

### 3. Review

Check the draft against this rubric:

- Is the agent scoped to a clear job?
- Are instructions specific enough to execute?
- Are knowledge sources explicit?
- Are tools/actions necessary and safe?
- Are refusal/delegation boundaries clear?
- Are starter prompts realistic?
- Is the output portable across projects?
- Are validation steps included?

### 4. Package

Prefer a portable package structure:

```text
agents/<agent-name>/
├── README.md
├── AGENT.md
├── starter-prompts.md
├── knowledge-sources.md
├── tools-actions.md
└── evals.md
```

For skill-oriented outputs, use:

```text
skills/<skill-name>/
├── SKILL.md
├── README.md
├── references/
└── examples/
```

Use this skill's bundled `templates/` directory when creating files:

- `templates/agent-builder-intake.md`
- `templates/agent-definition.md`
- `templates/agent-readme.md`
- `templates/agent-starter-prompts.md`
- `templates/agent-tool-actions.md`
- `templates/agent-evals.md`
- `templates/agent-validation-checklist.md`

### 5. Follow up

End with:

- files created or proposed
- validation performed
- unresolved questions
- recommended next increment

## Output contract

When asked to build an agent, produce either:

1. a concise plan when implementation is not requested, or
2. concrete files when implementation is requested.

Use Markdown for human-editable assets. Keep tool-specific files as pointers to a canonical source where possible.
