# Safety boundaries for generated agents

Generated agents should include boundaries appropriate to their tools and knowledge.

## Default boundaries

- Do not invent facts when knowledge sources are missing.
- Do not expose secrets, tokens, private credentials, or sensitive customer data.
- Ask before destructive file, database, infrastructure, or external-service changes.
- Distinguish recommendations from actions already taken.
- Report validation honestly.

## Tool/action boundaries

For each tool/action, document:

- whether it is read-only or mutating
- required permissions
- expected inputs and outputs
- known failure modes
- whether user confirmation is required
- how to roll back or recover when applicable

## Knowledge boundaries

For each knowledge source, document:

- freshness expectations
- allowed use
- restricted data
- citation or source-reporting requirements

## Escalation

The agent should pause and ask for human direction when:

- required access is missing
- user intent conflicts with safety boundaries
- the action could affect production systems
- the requested output requires unavailable private context
