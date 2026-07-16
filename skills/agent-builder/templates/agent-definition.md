---
name: <agent-name>
version: 1.0.0
description: <description>
dependencies:
  - mcp:postgres-server
models:
  recommended: claude-3-5-sonnet
---

# Agent definition: <display-name>

## Description

Short description of when to use this agent.

## Target users

- <user group>

## Jobs to be done

- <task>

## Boundaries

See [agent-guardrails-matrix.md](agent-guardrails-matrix.md) for detailed permission modeling.

The agent must not:

- <boundary>

## Architecture Workflow

```mermaid
flowchart TD
    A[User Request] --> B{Is in scope?}
    B -- Yes --> C[Use Knowledge Sources]
    B -- No --> D[Refuse/Delegate]
    C --> E[Call Tools/Actions]
    E --> F[Return Output]
```

## Instructions

1. Understand the user's goal and available context.
2. Check whether the request is in scope.
3. Use the listed knowledge sources before guessing.
4. Use tools/actions only when they are necessary and safe.
5. Return concise, actionable output.
6. Call out assumptions, missing information, and follow-up work.

## Knowledge sources

- <source>

## Tools/actions

- <tool/action>

## Starter prompts

- <prompt>

## Acceptance criteria

- <criterion>
