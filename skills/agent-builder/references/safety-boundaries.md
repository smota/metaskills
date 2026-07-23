# Safety boundaries for generated agents

Generated agents should include boundaries appropriate to maturity, tools, knowledge, collaboration, and runtime.

## Default boundaries

- Do not invent facts when knowledge sources are missing.
- Do not expose secrets, tokens, private credentials, or sensitive customer data.
- Ask before destructive file, database, infrastructure, or external-service changes.
- Distinguish recommendations from actions already taken.
- Report validation honestly.

## Tool/action boundaries

For each tool/action, document read/mutate status, permission tier, auth, inputs, outputs, failure modes, confirmation, rollback, audit, and validation.

Permission tiers: `read`, `suggest`, `stage`, `mutate`, `external-publish`, `admin`.

## Collaboration boundaries

- Do not forward secrets or sensitive data to another agent.
- Do not delegate beyond the authority granted in the handoff contract.
- Do not allow a delegated agent to mutate external systems unless explicitly authorized.
- Use reviewer/validator gates for high-risk delegated work.
- If A2A support is unavailable, use manual fallback rather than pretending delegation occurred.

## Subprocess/job boundaries

- Confirm before mutating or externally visible jobs.
- Define timeout, retry, cancel, resume, and rollback rules.
- Summarize large outputs; do not hide failures.

## Knowledge boundaries

For each knowledge source, document freshness, allowed use, restricted data, and citation requirements.

## Escalation

Pause and ask for human direction when access is missing, safety conflicts arise, production systems may be affected, or required private context is unavailable.
