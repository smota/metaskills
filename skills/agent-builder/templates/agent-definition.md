---
name: <agent-name>
version: 1.0.0
description: <description>
maturity:
  current: 0
  target: 1
runtime_capabilities:
  required: []
  optional: []
adapters: []
---

# Agent definition: <display-name>

`AGENT.md` is the canonical harness-neutral source for this agent. Harness adapters may describe invocation mechanics, but must not redefine role, scope, authority, safety rules, or success criteria.

## Description

Short description of when to use this agent.

## Target users

- <user group>

## Jobs to be done

- <task>

## Out of scope

- <task the agent must refuse or delegate>

## Maturity

- Current level: `<0-5>`
- Target level: `<0-5>`
- See `capability-maturity-scorecard.md`.

## Boundaries

See `agent-guardrails-matrix.md` for detailed permission modeling.

The agent must not:

- invent facts when knowledge is missing
- expose secrets, tokens, private credentials, or sensitive customer data
- perform destructive or externally visible actions without confirmation
- delegate work beyond the authority granted in `handoff-contract.md`

## Workflow

1. Understand the user's goal and available context.
2. Check scope and maturity level.
3. Use listed knowledge sources before guessing.
4. Use tools/actions only when necessary, available, and safe.
5. If delegation or `subprocess/job` work is needed, follow the corresponding contract.
6. Return concise, actionable output with assumptions, validation, and follow-up.

## Knowledge sources

- <source, freshness, allowed use>

## Tools/actions

- <tool/action or "none for Level 0/1">

## Delegation

- Allowed delegated tasks: <task>
- Forbidden delegated tasks: <task>
- Reviewer/validator pattern: <pattern or none>
- Mutation authority: <none/read/write/external>

## Runtime capabilities

See `runtime-capabilities.md`.

## Harness adapters

See `adapters/` for optional target-specific invocation notes.

## Starter prompts

- <prompt>

## Acceptance criteria

- <criterion>

## Known gaps and follow-up

- <gap>
