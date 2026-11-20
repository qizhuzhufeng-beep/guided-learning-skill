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

The top-level `tests/` directory validates the package itself. Package notes: [cross-agent compatibility](guided-learning/references/compatibility.md) and [research and design basis](guided-learning/references/research-basis.md).

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

### Option B — let your agent install it for you

If you already use a coding agent (Claude Code, Codex CLI, and similar), skip the manual steps. Send it this message in a fresh conversation, approve the writes when it asks for permission, and it will install the Skill by itself and then walk you through your first use:

```text
Set up the guided-learning skill on my machine from this repository: https://github.com/qizhuzhufeng-beep/guided-learning-skill.git — clone it, install the guided-learning/ directory into your skills directory (for Claude Code: ~/.claude/skills/), confirm the skill is discoverable, then teach me step by step how to use it, starting with what to say first.
```

中文版：

```text
为我在本机配置 guided-learning 学习技能：仓库是 https://github.com/qizhuzhufeng-beep/guided-learning-skill.git —— 克隆仓库，把其中的 guided-learning/ 目录安装到你的技能目录（Claude Code 是 ~/.claude/skills/），确认你能发现这个技能，然后手把手教我怎么用，从第一句话怎么说开始。
```

The agent clones the repository, copies `guided-learning/` into the skills directory, verifies the installation, and teaches you how to start. Note that skills are discovered when a session starts, so open a new conversation after installing.

