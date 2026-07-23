# Agent build review checklist

- [ ] Package keeps `AGENT.md` canonical and harness-neutral.
- [ ] No hosted runtime, daemon, queue, or service was added.
- [ ] Current and target maturity levels are justified by evidence.
- [ ] Level 0 agents do not fail because tools/actions are absent.
- [ ] Level 2+ tools/actions include schema, auth, permission tier, failure, fallback, validation.
- [ ] Level 4+ orchestration includes runtime capabilities, handoff contract, and execution model.
- [ ] Delegation scope, authority, statuses, and failure handling are explicit.
- [ ] Subprocess/job contracts include confirmation, timeout, retry, cancel, resume, rollback.
- [ ] Adapters do not override canonical semantics.
- [ ] Missing harness capability has safe fallback.
- [ ] Secrets/sensitive data restrictions are present.
- [ ] Evals cover success, refusal, missing capability, and failure paths.
