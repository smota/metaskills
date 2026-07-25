# Getting started

Use this guide from an adopting project: the repository where you want MetaSkills available.

## Install

List available skills:

```bash
npx skills add https://github.com/smota/metaskills --list --full-depth
```

Install a skill:

```bash
npx skills add https://github.com/smota/metaskills --skill agent-builder --full-depth
npx skills add https://github.com/smota/metaskills --skill skill-creator --full-depth
```

Non-interactive target example:

```bash
npx skills add https://github.com/smota/metaskills --skill agent-builder --agent claude-code --full-depth -y
```

## Use

1. Ask your coding agent to use the installed skill by name.
2. Review generated files before committing them.
3. Keep generated agents, skills, toolsets, and local changes in your adopting project.

## Update

Re-run the same install command from the adopting project root:

```bash
npx skills add https://github.com/smota/metaskills --skill agent-builder --full-depth
```

Then review the diff:

```bash
git status
git diff
git diff --check
```

Preserve project-owned changes:

- local `AGENT.md` decisions
- local knowledge sources
- local tool auth notes
- local runtime capability choices
- local eval history and feedback logs

Accept upstream updates when they improve reusable templates, checklists, references, examples, or adapters.

## Record upstream version

In generated package README or changelog, record:

- upstream repo: `https://github.com/smota/metaskills`
- installed skill: `agent-builder` or `skill-creator`
- version or commit used
- local changes made after install

## Validate before commit

```bash
git diff --check
```

For JSON templates:

```bash
python -m json.tool path/to/file.json
```

## Need to choose what to install?

See [Choose an asset](./choose-an-asset.md).
