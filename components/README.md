# Components

External component repositories belong here as Git submodules.

Each subdirectory under `components/` should be an independently maintained repository with its own history, branches, and PR workflow. The parent `metaskills` repository records the exact commit that should be used.

Each component should also have a sibling metadata file:

```text
<component-name>.metaskills.md
```

The metadata file declares how this repo uses the submodule:

- `reference-only` — pinned prior art or reference material; not imported or run
- `development-companion` — used for upstream-compatible development and PRs
- `tool-provider` — scripts, CLIs, schemas, or tests are intentionally called from the submodule

Current components:

- [`agent-skill-creator`](./agent-skill-creator) — see [`agent-skill-creator.metaskills.md`](./agent-skill-creator.metaskills.md)

See [`../docs/submodules.md`](../docs/submodules.md) for the full workflow.
