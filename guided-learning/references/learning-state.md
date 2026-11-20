# Learning State

## Purpose

Learning state is a compact reconstruction of what matters for choosing the next pedagogical action. It is conversation-local in the Skill-only design and should remain small enough to recover after long-context summarization.

## Session-level state

- `interaction_mode`: `LEARNING`, `NORMAL`, `SUSPENDED`, or `ENDED`.
- `active_topic`: the single topic currently being learned.
- `suspended_topics`: optional compact checkpoints for topics paused earlier in this conversation.
- `learner_preferences`: only preferences explicitly expressed or repeatedly demonstrated during the current conversation, such as pace or desired explanation depth.

## Topic-local state

### Goal

The learner's stated topic.

### Target capability

Translate a broad topic into an observable ability when possible.

Examples:

- "Understand Bayes theorem" → explain conditional reversal errors and solve a representative problem independently.
- "Learn Git rebase" → predict what rebase changes and safely choose between rebase and merge in common scenarios.

### Current focus

The concept or task currently being learned.

### Phase

Use one of:

- `goal`
- `diagnose`
- `attempt`
- `probe`
- `scaffold`
- `explain`
- `reconstruct`
- `verify`
- `transfer`
- `complete`

The phase is a control hint, not a rigid workflow label that must be shown to the user.

### Concept states

Use these states when useful:

- `unseen`
- `exposed`
- `attempted`
- `supported`
- `independently-verified`
- `transfer-verified`

A misconception is a parallel property and may coexist with `exposed` or `attempted`.

### Verified prerequisites

Only include prerequisites supported by evidence relevant to the current target.

### Uncertain concepts

Concepts where available evidence is insufficient or contradictory.

### Misconceptions

Record a concise description of the learner's apparent mental model, not merely that an answer was wrong.

Example:

`attention = a fixed importance score attached to each word`

### Recent evidence

Prefer high-information evidence:

- independent explanation;
- independent solution;
- prediction with reasoning;
- correction of one's own error;
- identification of a counterexample;
- transfer to a changed context.

Do not retain a large transcript summary when a smaller evidence statement will do.

### Hint level

Use 0–5 according to `scaffolding.md`. Reset or reduce it when moving to a genuinely fresh task. Never copy it to an unrelated topic.

### Frontier

The current concept or small set of concepts that are learnable now and most relevant to the target.

## Evidence hierarchy

From weak to strong:

1. self-report such as "I understand";
2. recognition of an answer;
3. correct answer after substantial support;
4. unassisted correct answer;
5. unassisted explanation of why;
6. self-correction;
7. handling a counterexample;
8. transfer to a changed context;
9. generating a valid new example, problem, or test.

Do not promote a concept to `independently-verified` based only on levels 1–3.

## State reconstruction

At the start of each learning turn, reconstruct only the state needed to choose the next action. If old details conflict with recent evidence, prioritize recent direct evidence. If an important state element is genuinely unavailable after summarization, perform a low-cost diagnostic instead of inventing it.