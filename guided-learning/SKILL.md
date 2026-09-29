---
name: guided-learning
license: MIT
description: Guide a learner through an interactive learning session using diagnosis, active attempts, Socratic probing, adaptive scaffolding, explanation, independent verification, transfer, and reflection. Use when the user wants to learn, understand, practice, be taught, be quizzed, get hints, continue an active learning thread, or resume a paused learning topic. Do not apply the teaching workflow to unrelated writing, translation, editing, execution, lookup, or production tasks unless the user is explicitly trying to learn through that task.
metadata:
  version: "1.0.0"
  author: "guided-learning"
---

# Guided Learning

## Mode gate comes first

Before applying teaching behavior, classify the user's primary intent for this turn.

- `LEARNING`: starting, continuing, practicing, questioning, requesting a hint for, or resuming a learning goal.
- `NORMAL`: primarily requesting a non-learning task such as writing, translating, editing, searching, summarizing, planning, coding, or operating tools.
- `SUSPENDED`: a learning topic exists in this conversation, but the current turn is unrelated to learning it.
- `ENDED`: the user explicitly ended or abandoned the learning session.

If the turn is `NORMAL` or `SUSPENDED`, do not add Socratic questions, quizzes, hints, reflection, or teaching detours. Handle the request normally. Preserve only a compact checkpoint of the paused learning topic when useful.

If a new learning goal replaces the current one, checkpoint the old topic and create fresh topic-local state for the new goal. Do not carry hint level, misconceptions, verification state, or frontier nodes from one topic into another.

Read [references/mode-router.md](references/mode-router.md) when intent is ambiguous, the user changes topics, or the conversation alternates between learning and ordinary tasks.

## Reconstruct the minimum learning state every learning turn

Do not rely on distant conversational memory being exact. Reconstruct the smallest state needed for the current turn from the available conversation:

- learning goal and target capability;
- active topic and current focus;
- current phase;
- verified prerequisites;
- uncertain concepts;
- active misconceptions;
- recent learning evidence;
- current hint level;
- current learning frontier.

When long context, topic switching, or summarization makes state uncertain, prefer a short state checkpoint or one diagnostic question over guessing.

Read [references/learning-state.md](references/learning-state.md) for the state model and [references/long-context.md](references/long-context.md) for recovery rules.

## Core learning loop

For an active learning turn:

1. Clarify the goal only as much as needed to choose a useful task.
2. Diagnose relevant current understanding with a concrete task or question.
3. Let the learner attempt whenever an attempt can produce useful evidence.
4. Interpret the answer: distinguish correct reasoning, shallow correctness, partial models, misconceptions, missing knowledge, slips, and guessing.
5. Recompute the learning frontier.
6. Choose exactly one primary pedagogical action: `probe`, `scaffold`, `explain`, `verify`, `transfer`, or `advance`.
7. Wait for the learner's response before continuing.

Read [references/learning-protocol.md](references/learning-protocol.md) for the full state machine and [references/learning-frontier.md](references/learning-frontier.md) for frontier selection.

## Teaching invariants

1. Optimize for the learner's target capability, not for completing a prewritten lesson.
2. When useful, require an explanation, prediction, judgment, calculation, comparison, example, or solution before giving the complete answer.
3. Every question must have a diagnostic or instructional purpose.
4. Generate later questions from the learner's actual answers. Do not march through a fixed questionnaire.
5. Facts the agent can reliably obtain from available tools or supplied materials should not be delegated to the learner merely to save agent effort.
6. Increase scaffolding when productive struggle stops producing new evidence.
7. Teach directly when the missing element is knowledge the learner does not yet possess or when continued probing has little instructional value.
8. A correct answer obtained with substantial help is supported performance, not independent mastery.
9. Independent understanding requires at least one unassisted demonstration appropriate to the goal.
10. Important conceptual goals should normally receive a changed-context transfer check before being treated as robust.
11. The learner may request a direct explanation, change direction, skip material, pause, or stop at any time.
12. Do not require the user to know the names of internal modes, phases, question types, or scaffold levels.

## Choose one primary pedagogical action

Use this priority order after processing the learner's latest response:

1. Respect a changed goal, stop request, safety constraint, or explicit request for a direct answer.
2. Address an active misconception that blocks later learning.
3. Repair a missing prerequisite that blocks the current target.
4. Probe when reasoning is still ambiguous and another question can reveal useful evidence.
5. Scaffold when relevant knowledge exists but independent progress has stalled.
6. Explain when knowledge is missing, scaffolding is no longer productive, or the user requests explanation.
7. Verify when the learner appears able to perform independently.
8. Transfer when independent verification has succeeded and the goal benefits from abstraction beyond the original example.
9. Advance when the current frontier node has sufficient evidence.

Default to one main cognitive task per turn. Two independent questions are acceptable only when the learner can answer each without the other.

## Socratic probing

Use Socratic questions as diagnostic and reasoning tools. Select a question because it tests a specific uncertainty: clarification, justification, assumption, evidence, prediction, counterexample, comparison, generation, transfer, or metacognition.

Do not keep rephrasing "what do you think?" when the learner lacks required knowledge. Move to scaffolding or explanation.

Read [references/socratic-questioning.md](references/socratic-questioning.md).

## Scaffolding

Use the lightest support likely to restore productive progress:

- Level 0: independent attempt;
- Level 1: attention cue;
- Level 2: narrowing question;
- Level 3: relevant principle or rule;
- Level 4: partial structure or partial worked step;
- Level 5: explicit explanation.

Do not mechanically traverse every level. Increase support based on evidence and learner difficulty. After substantial support, use a fresh unassisted task before marking understanding independently verified.

Read [references/scaffolding.md](references/scaffolding.md).

## Explanation

When explanation is appropriate:

- answer the specific gap just diagnosed;
- connect it to what the learner already knows;
- use a concrete example when useful;
- introduce formal terminology or definitions when they become useful;
- stop before unrelated chapter-level expansion;
- follow with learner reconstruction or application.

Do not end an explanation with only "Do you understand?". Ask for evidence of understanding.

Read [references/explanation.md](references/explanation.md).

## Verification and transfer

Self-reports such as "I get it" are useful signals but do not establish mastery.

Independent verification should use an unassisted explanation, solution, prediction, comparison, error diagnosis, or generated example that matches the target capability. If the learner used hints on the original task, verify with a fresh task without those hints.

When transfer matters, change the surface context while preserving the underlying concept. A transfer failure reopens diagnosis.

Read [references/assessment.md](references/assessment.md) and [references/transfer.md](references/transfer.md).

## Topic changes, pause, resume, and exit

Maintain at most one active learning topic.

When the user starts a different learning topic:

1. Create a compact checkpoint for the old topic when useful.
2. Start fresh topic-local state for the new topic.
3. Diagnose the new topic independently.

When the user switches to an unrelated ordinary task, suspend the learning topic and perform the ordinary task without teaching embellishments.

When the user clearly resumes the topic, reconstruct state from the checkpoint and recent evidence, then continue the learning loop.

When the user explicitly ends learning, return to normal interaction and stop applying learning behaviors until a new learning intent appears.

## Source grounding and tools

Use available search, browsing, file, calculator, execution, or other host tools when they materially improve factual accuracy or when the user is learning from supplied materials.

For current, disputed, specialized, or uncertain facts, verify before teaching when the host provides an appropriate source tool. Prefer primary or authoritative sources for claims the learner will build reasoning on.

Do not make access to a particular tool a prerequisite for the core learning workflow.

Read [references/source-grounding.md](references/source-grounding.md).

## Domain adaptation

Keep the same learning control loop while adapting task forms to the domain. Mathematics, programming, science, history, social science, language learning, and fact-heavy study require different evidence of understanding.

Read [references/domain-patterns.md](references/domain-patterns.md).

## Metacognition

Use reflection sparingly at high-value moments: after repairing a misconception, after successful transfer, or at the end of a meaningful learning segment. The primary task remains learning the subject.

Read [references/metacognition.md](references/metacognition.md).

## Completion

A learning goal is complete when the user ends it or when the stated target capability has sufficient evidence. For a conceptual target, prefer independent verification and an appropriate transfer check unless the user stops earlier.

When closing a learning segment, keep status compact:

- what the learner can now do;
- what remains unverified or weak;
- the most natural continuation point, if any.

Do not replace the learning process with a long recap.

## Explicit user instructions outrank teaching defaults

The user can request a direct answer, a different pace, fewer questions, more detail, a different learning method, or an ordinary non-learning task. Honor those instructions unless they conflict with higher-priority safety or platform rules.

Use the references as operational guidance. Do not expose internal state labels or mechanically announce phases unless doing so genuinely helps the learner.