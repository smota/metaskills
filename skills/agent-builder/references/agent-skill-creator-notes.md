# agent-skill-creator notes

Source component: [`../../../components/agent-skill-creator`](../../../components/agent-skill-creator)

Component metadata: [`../../../components/agent-skill-creator.metaskills.md`](../../../components/agent-skill-creator.metaskills.md)

Mode: `reference-only`

Ideas to use as implementation/reference:

- accept plain English, files, links, scripts, or transcripts as source material
- uncover implicit requirements before writing final instructions
- generate reusable assets rather than one-off chat responses
- include validation, security review, and eval guidance
- think across platforms and export targets
- keep detailed reference material outside the main activation file when it grows too large

Recommended adaptation:

1. Use `agent-skill-creator` as a pinned reference-only submodule, not as vendored source.
2. Keep `agent-builder` native to this repo under `skills/agent-builder`.
3. Keep templates and required install content inside `skills/agent-builder/` so `npx skills add <repo> --skill agent-builder` installs a complete package.
4. If improvements are needed upstream, branch inside `components/agent-skill-creator` and send PRs there.
5. Update the parent submodule pointer only after selecting a known-good upstream commit.

Because this is `reference-only`, the `agent-builder` skill must not require the submodule at runtime or during installation.
