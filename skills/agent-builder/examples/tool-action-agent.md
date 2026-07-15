# Example: tool/action-enabled agent

## Scenario

A downstream project wants an agent that prepares release notes from GitHub issues, merged PRs, and changelog fragments.

## Agent summary

- Name: `release-notes-agent`
- Description: Drafts release notes from repository history and issue metadata.
- Knowledge: changelog, release policy, labels, previous releases.
- Tools/actions: Git CLI, GitHub CLI, repository file search.

## Tools/actions

| Tool/action | Purpose | Inputs | Outputs | Safety notes |
| --- | --- | --- | --- | --- |
| `git log` | Inspect commits since a tag | base tag, head ref | commit list | Read-only |
| `gh pr list` / `gh pr view` | Inspect merged PR metadata | labels, milestone, date range | PR summaries | Read-only; requires GitHub auth |
| File search | Find changelog fragments | path patterns | matching files | Read-only unless user asks to update |

## Starter prompts

- "Draft release notes since v1.4.0."
- "Group merged PRs by feature, fix, and documentation."
- "Find changelog fragments for the next release."

## Acceptance checks

- Release notes distinguish features, fixes, docs, and breaking changes.
- The agent identifies the source range used.
- The agent asks before writing release files.
