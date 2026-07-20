# Build a database migration review agent

## Starting prompt

```text
Use the agent-builder skill to design an agent that reviews database migrations before release.
```

## Skill used

`agent-builder`

## Expected output structure

```text
agents/database-migration-reviewer/
├── README.md
├── AGENT.md
├── starter-prompts.md
├── knowledge-sources.md
├── tools-actions.md
└── evals.md
```

## Before

Migration review is inconsistent. Reviewers may miss lock risks, destructive changes, missing rollback notes, or application compatibility concerns.

## After

The downstream project has a review agent with explicit knowledge sources, safe tool boundaries, review categories, escalation criteria, and evals.

## Assumptions to adapt

- Database engine and migration framework.
- Deployment model and rollback policy.
- Required performance and security review checks.

## Validation checklist

- [ ] Agent checks for destructive operations and data-loss risk.
- [ ] Agent asks for schema, migration, and application context when missing.
- [ ] Agent distinguishes advisory comments from release blockers.
- [ ] Agent includes starter prompts for new migration, hotfix, and rollback review.
- [ ] Agent evals include a risky migration and a safe additive migration.
