# Example: skill-creator agent

## Scenario

A team wants an agent that converts repeatable internal workflows into reusable skills.

## Agent summary

- Name: `skill-creator-agent`
- Description: Turns documented workflows into portable skill packages.
- Knowledge: skill format, examples, platform-specific installation notes.
- Tools/actions: file read/write, validation scripts, optional security scan.

## Workflow

1. Read the workflow description and source materials.
2. Extract the trigger conditions and expected outputs.
3. Create `SKILL.md` with concise activation metadata.
4. Move detailed procedures into `references/` when needed.
5. Add examples and validation notes.
6. Run available checks.

## Starter prompts

- "Turn this deployment checklist into a reusable skill."
- "Create a skill from these support triage notes."
- "Review this skill for activation quality and portability."

## Acceptance checks

- The skill has clear trigger language.
- Detailed reference content is not overloaded into the main skill file.
- The package includes examples and validation guidance.


## Maturity

Current maturity: Level 2 tool-enabled agent.

Runtime capability fallback: if target harness lacks required tools, delegation, or jobs, use documented manual fallback rather than silent failure.
