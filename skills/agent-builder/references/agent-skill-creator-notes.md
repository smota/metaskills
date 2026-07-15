# agent-skill-creator notes

Source component: [`../../../components/agent-skill-creator`](../../../components/agent-skill-creator)

Ideas to use as implementation/reference:

- accept plain English, files, links, scripts, or transcripts as source material
- uncover implicit requirements before writing final instructions
- generate reusable assets rather than one-off chat responses
- include validation, security review, and eval guidance
- think across platforms and export targets
- keep detailed reference material outside the main activation file when it grows too large

Recommended adaptation:

1. Use `agent-skill-creator` as a submodule/component reference, not as vendored source.
2. Keep `agent-builder` native to this repo under `skills/agent-builder`.
3. If improvements are needed upstream, branch inside `components/agent-skill-creator` and send PRs there.
4. Update the parent submodule pointer only after selecting a known-good upstream commit.
