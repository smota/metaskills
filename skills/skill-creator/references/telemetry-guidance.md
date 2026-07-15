# Telemetry guidance

Telemetry is optional. A skill must remain useful without telemetry.

## Allowed by default

- manual maintainer notes
- eval pass/fail summaries
- benchmark aggregate results
- local counters that do not include sensitive content

## Require explicit approval

- raw prompts
- raw model outputs
- full transcripts
- user identifiers
- repository-private file excerpts
- customer data

## Recommended event shape

```json
{"skill_name":"example","skill_version":"abc123","event_type":"eval","success":true,"failure_type":null,"duration_bucket":"short","notes_without_sensitive_data":"passed boundary case"}
```

## Review questions

- What decision will this data support?
- Can the same decision be made from eval summaries instead?
- Is sensitive information excluded?
- Is retention documented?
- Can users opt out?
