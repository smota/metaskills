# Skill telemetry plan

Telemetry is optional and must be explicitly approved by the downstream project owner.

## Purpose

What quality or efficiency questions should telemetry answer?

## Collection mode

- [ ] none
- [ ] manual notes only
- [ ] local JSONL events
- [ ] CI/eval summaries
- [ ] other:

## Allowed signals

```yaml
skill_name:
skill_version:
event_type:
goal_category:
success:
failure_type:
followup_required:
tool_use_count_bucket:
duration_bucket:
eval_case:
notes_without_sensitive_data:
```

## Prohibited data

- raw prompts unless explicitly approved
- secrets or credentials
- customer data
- private file contents
- full conversation logs by default

## Storage

- Location:
- Retention:
- Access:
- Review cadence:

## Improvement loop

Explain how telemetry summaries become eval cases, improvement plans, or benchmark runs.
