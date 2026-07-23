# Agent validation rubric

Score each item as pass, partial, or fail.

## 1. Scope

- Single clear primary job.
- Target users identified.
- Out-of-scope work explicit.

## 2. Maturity fit

- Current and target maturity levels are stated.
- Level 0 prompt agents can pass without tools/actions.
- Level 2 agents have tool/action schemas and fallbacks.
- Level 4 orchestration claims have runtime, handoff, and execution contracts.
- Level 5 agents have evals, feedback, benchmark, and changelog workflow.

## 3. Instructions

- Concrete behavior and repeatable workflow.
- Follow-up question rules clear.
- Refusal and delegation boundaries clear.

## 4. Knowledge

- Sources named.
- Freshness expectations documented.
- Missing-knowledge behavior defined.

## 5. Tools/actions

- Purpose, inputs, outputs, permissions, auth, failure modes documented.
- Permission tier assigned.
- Destructive/external/admin actions require confirmation.
- Tool absence and tool failure have distinct fallbacks.

## 6. Runtime capabilities

- Required, optional, unavailable, and unknown states documented.
- Harness adapters do not override `AGENT.md` semantics.
- Missing capabilities degrade safely.

## 7. Handoff and subprocess/job execution

- Delegated tasks have input/output schemas and authority limits.
- Job lifecycle covers start, observe, wait, cancel, retry, resume, complete.
- Structured `error/fallback` behavior exists.

## 8. User experience and portability

- Starter prompts match real use cases.
- Outputs concise and actionable.
- Canonical instructions are tool-neutral.
- Package can be copied into a downstream repo without this repo running as a service.
