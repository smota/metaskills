# Agent validation checklist

## Maturity fit

- [ ] Current and target maturity levels are stated.
- [ ] Level 0 agents do not require tools/actions.
- [ ] Level 2 agents include MCP/OpenAPI schemas for tools/actions.
- [ ] Level 4 agents include runtime, handoff, and execution contracts.
- [ ] Level 5 agents include evals, feedback, benchmark, and changelog artifacts.

## Harness neutrality

- [ ] `AGENT.md` is canonical.
- [ ] Adapters do not override semantics.
- [ ] Required/optional/unavailable capabilities are explicit.
- [ ] Missing capability fallback is not silent.

## Tools/actions

- [ ] Each tool/action passes `tool-action-contract-checklist.md`.
- [ ] Destructive/external/admin actions require confirmation.
- [ ] Absence fallback differs from failure fallback.

## Handoff and jobs

- [ ] Delegated tasks and forbidden delegated tasks are documented.
- [ ] Handoff input/output schemas are present when A2A is claimed.
- [ ] Subprocess/job lifecycle covers timeout, retry, cancel, resume, rollback.

## Safety and quality

- [ ] Knowledge freshness and missing-context behavior are documented.
- [ ] Secrets and sensitive data handling are documented.
- [ ] Evals cover success, refusal, missing capability, and failure paths.
- [ ] Known gaps and follow-up are listed.
