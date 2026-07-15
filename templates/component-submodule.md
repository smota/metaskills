# Component submodule template

Use this checklist when adding an external repository as a `metaskills` component.

## Component

- Name:
- Upstream repository:
- Local path: `components/<name>`
- Purpose:
- Owner/upstream maintainers:

## Add command

```bash
git submodule add <repo-url> components/<name>
git commit -m "Add <name> component submodule"
```

## Adoption notes

Document how downstream projects should use this component:

- expected inputs
- expected outputs
- supported tools or runtimes
- setup requirements
- validation command

## Update workflow

1. Make changes inside `components/<name>`.
2. Commit and push to the component repository.
3. Open and merge a PR in the component repository.
4. Pull the merged component commit locally.
5. Commit the updated submodule pointer in `metaskills`.
