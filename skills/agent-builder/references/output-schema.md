# Agent package output schema

A generated agent package should include the following fields.

## Required fields

```yaml
name: kebab-case-name
display_name: Human Friendly Name
description: Short description of when to use the agent
target_users:
  - user group
jobs_to_be_done:
  - task the agent performs
boundaries:
  - thing the agent must not do
knowledge_sources:
  - name: source name
    type: repo | docs | api | database | file | human-process | other
    freshness: static | refreshed | live
    access_notes: how the downstream project grants access
tools_actions:
  - name: tool or action name
    purpose: why it is needed
    inputs: expected inputs
    outputs: expected outputs
    safety: constraints and failure handling
starter_prompts:
  - prompt users can try
acceptance_criteria:
  - pass/fail criterion
```

## Recommended files

```text
agents/<agent-name>/README.md
agents/<agent-name>/AGENT.md
agents/<agent-name>/starter-prompts.md
agents/<agent-name>/knowledge-sources.md
agents/<agent-name>/tools-actions.md
agents/<agent-name>/evals.md
```
