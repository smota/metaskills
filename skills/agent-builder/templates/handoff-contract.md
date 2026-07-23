# Agent-to-agent handoff contract

## Allowed delegation

- `<task type>` may be delegated to `<role>` when `<condition>`.

## Forbidden delegation

- `<task type>` must not be delegated because `<reason>`.

## Handoff envelope

```yaml
task: ""
context: ""
constraints:
  - ""
expected_output:
  format: ""
  must_include:
    - ""
deadline: ""
priority: normal
authority:
  read: true
  write: false
  mutate_external: false
secrets_policy: "do not forward secrets, tokens, private credentials, or sensitive customer data"
```

## Status states

- queued
- running
- blocked
- needs-human
- complete
- failed
- cancelled

## Output schema

```yaml
status: complete | failed | blocked | needs-human
summary: ""
changed_files: []
validation: []
risks: []
error: ""
fallback: ""
```

## Failure behavior

- If agent-to-agent transport is unavailable, use manual handoff checklist.
- If delegated agent lacks authority, pause and ask human.
- If delegated work requires mutation, require explicit confirmation.
- If child output is incomplete, mark status `blocked` or `failed`; do not silently proceed.
