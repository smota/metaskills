# Microsoft Agent Builder notes

Source: <https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder-build-agents>

Concepts to borrow:

- natural-language-first creation
- automatic refinement of name, description, and instructions
- a configure tab mental model for explicit fields
- knowledge source selection
- optional tools/actions/capabilities
- starter prompts for user onboarding
- iterative review before publishing

Portable interpretation for this repository:

| Microsoft Agent Builder concept | Portable `metaskills` equivalent |
| --- | --- |
| Name | Agent directory and display name |
| Description | Activation and use-case description |
| Instructions | `AGENT.md` or canonical instruction file |
| Knowledge | `knowledge-sources.md` |
| Actions/capabilities | `tools-actions.md` |
| Starter prompts | `starter-prompts.md` |
| Review/publish | validation checklist and package handoff |

Do not require Microsoft 365 Copilot. The skill should produce tool-neutral assets first, then optional target-specific exports.
