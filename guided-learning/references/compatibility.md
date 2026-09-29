# Cross-Agent Compatibility

## Portable core

The Skill is authored against the Agent Skills open specification:

- required `SKILL.md` with `name` and `description`;
- `references/` for detailed guidance;
- `scripts/` only for deterministic validation or processing;
- no required MCP server;
- no required host memory;
- no required hook, subagent, or host-specific frontmatter.

## Claude Code

Claude Code follows the Agent Skills standard and adds optional capabilities such as invocation controls, dynamic context injection, subagent execution, and other frontmatter extensions. The portable Skill does not require them.

Claude Code documents that invoked Skill content remains in the conversation across later turns. It also documents that auto-compaction re-attaches the first 5,000 tokens of each recent Skill within a shared budget. Keep critical control rules early in `SKILL.md`.

## OpenAI / Codex

OpenAI Skills use metadata-first activation and support `SKILL.md`, `references/`, `scripts/`, and `assets/`. The `description` should state the user goal and activation conditions. Detailed procedures belong in the body and supporting files.

This Skill requires no plugin or MCP dependency.

## Hermes

Hermes documents compatibility with the agentskills.io standard and uses progressive disclosure: metadata first, full Skill when needed, then individual reference files. Hermes-specific metadata and automation fields are intentionally omitted from the portable core.

## Invocation syntax

Do not treat `/guided-learning` as a portable protocol requirement. Different hosts expose explicit invocation differently. The portable requirement is one user-visible learning Skill with metadata that also permits automatic discovery.

## Tool differences

Search, browsing, file access, calculators, execution, and other tools vary by host. Use them when available and appropriate, while preserving a complete text-only learning loop when unavailable.

## Optional host enhancements

Host-specific adapters may later improve quality, but they must not change the pedagogical semantics of:

- mode routing;
- state reconstruction;
- frontier selection;
- scaffolding;
- independent verification;
- transfer;
- exit behavior.