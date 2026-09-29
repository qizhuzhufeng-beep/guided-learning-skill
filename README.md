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

## Quick start

### Option A — install into an Agent Skills host

For Claude Code or any host that supports the open Agent Skills format:

```bash
git clone https://github.com/qizhuzhufeng-beep/guided-learning-skill.git

# Claude Code, personal (available in all projects)
mkdir -p ~/.claude/skills
cp -r guided-learning-skill/guided-learning ~/.claude/skills/

# Claude Code, single project only
mkdir -p /path/to/your-project/.claude/skills
cp -r guided-learning-skill/guided-learning /path/to/your-project/.claude/skills/
```

Windows PowerShell equivalent:

```powershell
git clone https://github.com/qizhuzhufeng-beep/guided-learning-skill.git
New-Item -ItemType Directory -Force "$env:USERPROFILE\.claude\skills" | Out-Null
Copy-Item -Recurse guided-learning-skill\guided-learning "$env:USERPROFILE\.claude\skills\"
```

Start a new conversation and simply say what you want to learn, for example:

> Teach me Bayes theorem — I want to actually understand it.

No slash command is required. A correct activation starts with a short diagnostic task or question instead of a full lecture, and the Skill keeps running across later turns of the same topic.

### Option B — install as an agent prompt

For agents or apps without an Agent Skills mechanism, paste this single message into a fresh conversation — the agent fetches and loads the Skill by itself:

```text
Act as my learning tutor using the guided-learning skill: fetch https://raw.githubusercontent.com/qizhuzhufeng-beep/guided-learning-skill/main/guided-learning/SKILL.md and follow it as your teaching behavior for this conversation (files linked under references/ live in the same directory on the same host); if you cannot fetch URLs, say so and I will paste the file; once loaded, ask me what I want to learn.
```

中文版：

```text
从现在起按 guided-learning 技能担任我的学习导师：读取 https://raw.githubusercontent.com/qizhuzhufeng-beep/guided-learning-skill/main/guided-learning/SKILL.md 并在本对话中严格遵循它作为你的教学行为（其中引用的 references/ 文件在同一目录 https://raw.githubusercontent.com/qizhuzhufeng-beep/guided-learning-skill/main/guided-learning/ 下）；如果你无法访问网址，直接告诉我，我会把文件内容粘贴给你；加载完成后问我想学什么。
```

If the agent has no internet access, paste manually instead:

1. Open `guided-learning/SKILL.md`.
2. Paste its full content into the agent's system prompt, custom instructions, or the first message of a conversation.
3. Optionally paste one or more files from `guided-learning/references/` after it; the main file works on its own, and references add depth for specific situations.

The main file is deliberately compact (under 500 lines) so it fits typical custom-instruction limits.

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