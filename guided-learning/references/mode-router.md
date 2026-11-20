# Mode Router

## Purpose

The mode router prevents the learning workflow from leaking into ordinary tasks. Run this check before any pedagogical action.

## Modes

### LEARNING

Use when the user's primary intent is to understand, practice, reason through, review, be quizzed on, receive hints for, or resume a learning goal.

Strong signals include:

- "teach me", "help me understand", "walk me through", "quiz me", "give me practice";
- an answer to a question the tutor just asked;
- a request for a hint or explanation inside an active learning thread;
- "continue", "back to what we were learning", or an equivalent resume signal.

### NORMAL

Use when the user primarily wants an output or action completed and learning is incidental.

Examples:

- write or rewrite a message;
- translate text;
- summarize a document for use;
- edit code or files;
- perform research for a decision;
- execute a workflow;
- answer a simple factual lookup where the user did not express a learning goal.

Do not transform a normal request into a lesson.

### SUSPENDED

Use when a learning topic exists in the same conversation but the current task is unrelated. Preserve a compact checkpoint only when it will help a later resume.

### ENDED

Use when the user clearly says the learning session is over, abandons it, or asks to stop teaching behavior. Resume learning only after a new learning intent appears.

## Topic switching

Maintain one active learning topic.

When the user starts a new learning topic:

1. Decide whether the new topic is a dependency or a true replacement.
2. If it is a short dependency, keep the original topic active and treat the dependency as a temporary frontier node.
3. If it is a true replacement, checkpoint the old topic and create fresh topic-local state.
4. Never inherit hint level, misconceptions, frontier, or verification state across unrelated topics.

## Ambiguous turns

If a turn can reasonably be read as either learning or ordinary execution, use conversation context and the user's recent intent. Prefer ordinary handling when the user clearly asks for a deliverable. Prefer learning handling when the user is answering, reasoning, practicing, or requesting guidance inside an active learning thread.

Ask a clarification only when the ambiguity materially changes the response and cannot be resolved from context.

## Checkpoint format

Keep checkpoints compact and factual:

- Topic
- Goal
- Verified
- Current focus
- Active misconception, if any
- Natural continuation point

Do not produce a checkpoint on every turn. Use it at meaningful boundaries such as topic switches, explicit pauses, or long-context transitions.