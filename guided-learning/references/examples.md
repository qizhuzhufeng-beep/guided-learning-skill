# Interaction Examples

## Example 1 — Start from a broad goal

User: "I want to understand Docker."

Good behavior:

- establish a practical or conceptual target with at most one necessary clarification;
- use a diagnostic scenario rather than asking for a long self-assessment;
- adapt the frontier from the answer.

Possible response:

"Let's anchor it in one question first. Imagine you start three containers from the same image. Do you think each container contains its own full operating-system kernel, or do they share something with the host? Explain your current guess."

## Example 2 — Misconception

User: "Attention means each important word gets a bigger fixed weight."

Good behavior:

- identify a context-dependence misconception;
- use a discriminating example;
- avoid immediately dumping the full Q/K/V derivation.

Possible response:

"That model would give a word roughly the same importance everywhere. Consider `bank` in `river bank` and `bank account`: should the relationships it relies on stay fixed across those contexts? What would a fixed-weight view fail to capture?"

## Example 3 — Missing knowledge

User repeatedly cannot reason about race conditions because atomicity is unknown.

Good behavior:

- stop repetitive probing;
- explain atomicity briefly;
- then ask the learner to reconstruct the idea in the original scenario.

## Example 4 — Supported success does not equal mastery

Learner solves a probability problem after Level 4 support.

Good behavior:

- acknowledge the supported solution;
- provide a fresh problem without the previous scaffolding;
- only then consider independent verification.

## Example 5 — Switch to a new learning topic

Conversation is learning Git rebase.

User: "Actually, teach me how DNS resolution works first."

Good behavior:

- checkpoint Git briefly if useful;
- create fresh DNS topic state;
- do not inherit Git hint level or misconceptions;
- diagnose DNS independently.

## Example 6 — Ordinary task during learning

Conversation is learning Git rebase.

User: "Help me rewrite this email to my manager."

Good behavior:

- suspend Git learning;
- rewrite the email normally;
- do not add a quiz, Socratic question, or Git analogy;
- retain a compact Git checkpoint only if useful for later resume.

## Example 7 — Resume

User later says: "Back to rebase."

Good behavior:

- restore the nearest reliable checkpoint;
- if state is uncertain after a long detour, use one low-cost diagnostic;
- continue without requiring the user to invoke the Skill again.

## Example 8 — Direct answer request

User: "Just tell me the answer this time."

Good behavior:

- give the answer directly;
- keep it focused;
- if the learning session continues, follow with a low-cost reconstruction or changed example;
- do not lecture the user about why direct answers are bad.

## Example 9 — User says "I get it"

Good behavior:

- treat it as a signal to check understanding;
- use one concise unassisted task;
- do not mark the concept verified from the self-report alone.

## Example 10 — Long context uncertainty

The conversation summary says only "the learner worked on self-attention" and no reliable mastery evidence remains.

Good behavior:

- do not assume mastery;
- ask one targeted task such as a brief explanation or prediction;
- rebuild the frontier from the result.