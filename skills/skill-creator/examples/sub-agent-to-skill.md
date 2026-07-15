# Example: sub-agent to skill

## Source sub-agent traits

- Role: database migration reviewer
- Tools: file search, SQL parser, test runner
- Prompt: review migrations for safety, rollback, and data risk

## Converted skill traits

- Activation description focuses on when migration review is needed.
- Tool assumptions are documented as optional downstream capabilities.
- Detailed SQL review rubric moves to `references/sql-migration-rubric.md`.
- Eval cases cover destructive statements, missing rollback, and safe additive changes.

## Conversion rule

A sub-agent often describes a persona. A skill should describe a reusable capability, activation triggers, workflow, supporting references, and validation.
