# Long-Context Reliability

## Objective

Preserve teaching quality when the conversation becomes long, the host summarizes context, or the learner alternates between topics and ordinary tasks.

## Do not rely on one-time activation strength

Treat the skill as a reusable controller that can be selected again on later learning turns. The core workflow must remain recoverable from the skill's metadata, the compact `SKILL.md`, and the recent conversation.

## Minimum recoverable state

After context loss or summarization, recover only:

- interaction mode;
- active topic;
- target capability;
- current focus;
- verified prerequisites needed now;
- active misconception, if any;
- most recent strong evidence;
- hint level for the current task;
- current frontier or natural continuation point.

Do not try to reconstruct every historical question.

## Checkpoints

Create a compact learner-facing checkpoint at meaningful boundaries when doing so improves recoverability:

- switching learning topics;
- suspending learning for an unrelated task;
- completing a substantial concept;
- before a long detour;
- when the context has become complex enough that state ambiguity is likely.

Example:

"We can pause here. You can now explain why self-attention is context-dependent; multi-head attention is the next unverified step."

Do not emit a checkpoint on every turn.

## State ambiguity

If summarization leaves an important fact uncertain, choose one of:

1. use recent direct evidence already visible;
2. ask one low-cost diagnostic question;
3. state the uncertainty and resume from the nearest safe frontier.

Do not invent mastery or a misconception that is no longer evidenced.

## Main-file ordering

Critical instructions must stay near the top of `SKILL.md`: mode gate, minimum state reconstruction, core loop, teaching invariants, and action-selection priority.

Detailed theory, domain patterns, and examples belong in references so that long-context compaction does not make the core controller depend on distant material.

## Host behavior

Claude Code documents that invoked Skill content persists across turns and that auto-compaction re-attaches only the first 5,000 tokens of each recent Skill within a combined budget. This design therefore keeps critical rules early and the main file compact.

OpenAI and Hermes use metadata-first progressive disclosure, so a clear description should make the Skill rediscoverable on continued learning turns.