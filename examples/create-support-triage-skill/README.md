# Create a support triage skill

## Starting prompt

```text
Use the skill-creator skill to turn our support triage workflow into a reusable skill for coding agents.
```

## Skill used

`skill-creator`

## Expected output structure

```text
skills/support-triage/
├── SKILL.md
├── README.md
├── templates/
├── checklists/
├── references/
└── examples/
```

## Before

Support analysis depends on individual maintainers remembering how to classify reports, request logs, avoid private data, and escalate urgent bugs.

## After

The workflow is packaged as an installable skill with intake questions, severity criteria, privacy boundaries, response templates, and eval cases.

## Assumptions to adapt

- Severity labels and service-level expectations.
- Required logs and redaction policy.
- Escalation path for security or customer-impacting issues.

## Validation checklist

- [ ] Skill avoids asking for secrets or sensitive customer data.
- [ ] Skill distinguishes bug, question, feature request, and incident.
- [ ] Skill includes templates for first response and escalation notes.
- [ ] Skill defines pass/fail evals for ambiguous and urgent tickets.
- [ ] Skill documents what a downstream project must customize.
