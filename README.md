# Guided Learning — Portable Agent Skill

This package implements a single cross-agent `guided-learning` Skill for interactive learning through diagnosis, active attempts, Socratic probing, adaptive scaffolding, direct explanation when needed, independent verification, transfer, and selective metacognition.

## Design goals

- One user-visible Skill.
- One explicit activation can carry an entire learning thread; later learning turns should remain discoverable from the Skill metadata.
- Learning behavior stops immediately for unrelated ordinary tasks.
- New learning topics receive fresh topic-local state.
- Long-context recovery uses compact checkpoints and low-cost re-diagnosis rather than invented state.
- The portable core depends only on the open Agent Skills format.
- Claude Code, Codex/OpenAI, and Hermes host-specific features are optional enhancements.

## Package layout

```text
guided-learning/
├── SKILL.md
├── references/
├── scripts/
└── evals/
```

The top-level `tests/` directory validates the package itself.

## Validate

From this package root:

```bash
python guided-learning/scripts/validate_skill.py
pytest -q
```

The validator checks:

- portable Agent Skills frontmatter;
- directory/name agreement;
- description limits;
- compact main-file size;
- critical-section ordering for long-context resilience;
- direct reference integrity;
- eval data shape.

## Host use

Install or expose the `guided-learning/` directory through the host's Agent Skills mechanism.

- Claude Code follows the Agent Skills standard and supports project, personal, synced, and plugin Skill locations.
- OpenAI/Codex supports open-standard Agent Skills and discovers skills from configured capability directories or packaged Skill environments.
- Hermes documents agentskills.io compatibility and loads Skills progressively.

Explicit invocation syntax differs by host. Treat the product contract as one visible `guided-learning` Skill, not a requirement that every host use the same slash character.

## Runtime contract

The Skill uses conversation-local state. It does not require MCP, a database, cloud memory, hooks, subagents, or external services.

Long-term cross-session learning history is intentionally outside this Skill-only implementation.

## Research and official sources

See `guided-learning/references/research-basis.md`.