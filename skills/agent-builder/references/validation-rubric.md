# Agent validation rubric

Score each item as pass, partial, or fail.

## 1. Scope

- The agent has a single clear primary job.
- Target users are identified.
- Out-of-scope work is explicit.

## 2. Instructions

- Instructions describe concrete behavior.
- The agent has a repeatable workflow.
- Follow-up question rules are clear.
- Refusal and delegation boundaries are clear.

## 3. Knowledge

- Knowledge sources are named.
- Freshness expectations are documented.
- Missing-knowledge behavior is defined.

## 4. Tools/actions

- Each tool/action has a purpose.
- Inputs, outputs, permissions, and failure modes are documented.
- The agent asks before destructive or externally visible actions.

## 5. User experience

- Starter prompts match real use cases.
- Outputs are concise and actionable.
- The agent explains assumptions and gaps.

## 6. Portability

- The canonical instructions are tool-neutral.
- Target-specific files point back to canonical instructions.
- The package can be copied into a downstream repo without this repo running as a service.
