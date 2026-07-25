# Component submodule workflow

Use Git submodules when a component is built from an existing repository and should keep its own history, branches, releases, issues, and pull requests.

In this repository, external component repositories live under `components/`.

## When to use a submodule

Use a submodule for a component when:

- the source already exists in another Git repository
- changes should be proposed back to that repository with normal PRs
- the component has an independent release or ownership model
- `metaskills` should reference a known-good commit without absorbing the full source history

Do not use a submodule for small native files that belong directly in `skills/`, `agents/`, `toolsets/`, or `examples/`. Templates should live with the skill, agent, or toolset that owns them so installable/reusable assets stay self-contained.

## Component modes

Every submodule should have a companion metadata file named:

```text
components/<component-name>.metaskills.md
```

Use one of these modes.

### `reference-only`

Use when the external repo is prior art, documentation, or an inspectable reference. The parent repo pins a known commit, but does not run or import the submodule.

Good for:

- workflow inspiration
- architecture examples
- upstream documentation
- concepts borrowed by a native skill, agent, or toolset

### `development-companion`

Use when contributors are expected to patch the external repo from this workspace and send PRs upstream.

Good for:

- making upstream-compatible changes
- testing a component in context
- updating the parent submodule pointer after upstream merges

### `tool-provider`

Use when native assets in this repo intentionally call scripts, CLIs, schemas, or tests from the submodule.

Good for:

- validation scripts
- code generators
- test harnesses
- reusable CLI utilities

This mode creates stronger coupling. Document required commands, failure modes, and whether downstream users must initialize submodules.

## Add an existing component repository

```bash
mkdir -p components
git submodule add https://github.com/<org>/<repo>.git components/<repo>
git commit -m "Add <repo> component submodule"
git push origin main
```

This creates or updates `.gitmodules` and records the exact component commit in the parent repository.

Then add component metadata:

```bash
cat > components/<repo>.metaskills.md <<'EOF'
# <repo> component

Mode: `reference-only`

Upstream repository: <https://github.com/<org>/<repo>>

Used by:

- <native skill/agent/toolset path>

## Purpose

Describe why this component is linked.

## Not used for

- runtime imports
- generated code copied into native assets
- required downstream installation content
EOF

git add components/<repo>.metaskills.md
```

## Clone with components

Preferred:

```bash
git clone --recurse-submodules https://github.com/smota/metaskills.git
```

If already cloned:

```bash
git submodule update --init --recursive
```

## Work on a component

```bash
cd components/<repo>
git checkout -b <feature-branch>
# make changes
git add .
git commit -m "Describe component change"
git push origin <feature-branch>
```

Open a PR against the component repository. The component keeps its normal review and merge process.

## Update `metaskills` after the component PR merges

```bash
cd components/<repo>
git checkout main
git pull origin main

cd ../..
git add components/<repo>
git commit -m "Update <repo> component"
git push origin main
```

The parent commit updates the submodule pointer to the merged component commit.

## Pull latest parent and component pointers

```bash
git pull origin main
git submodule update --init --recursive
```

## Update all component submodules

Use intentionally, because this moves every component pointer to the latest remote-tracking commit configured for that submodule:

```bash
git submodule update --remote --merge
git status
```

Review, test, and commit the updated pointers in the parent repository.

## Rules of thumb

- Give every component a `.metaskills.md` metadata file with a declared mode.
- Commit component changes inside the component repo first.
- Push component branches to the component remote and open PRs there.
- Commit parent pointer changes in `metaskills` only after deciding which component commit should be referenced.
- Keep native metaskills assets outside `components/`.
- Keep external repos inside `components/` as submodules instead of copied source.
- For installable assets such as `npx skills add <repo> --skill <name>`, keep required templates and references inside the install unit.
