# Contributing

## Validate before committing

```bash
python guided-learning/scripts/validate_skill.py
python -m pytest -q
```

The validator and tests require PyYAML.

## Commit convention

Follow Conventional Commits. English, imperative mood, one logical change per commit.

```text
type(scope): subject, imperative, <= 72 chars, no trailing period
```

- Types: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`
- Scope: the area touched — `readme`, `skill`, `validator`, `evals`, `tests`, `license`, ...
- Body (optional): bullet points, one change per bullet; state the why when the what is not self-evident.

Example:

```text
docs(readme): add quick start install guide

- Option A: install into Agent Skills hosts (bash and PowerShell)
- Option B: paste SKILL.md as a prompt for hosts without skills support
```
