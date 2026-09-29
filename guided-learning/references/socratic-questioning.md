# Socratic Questioning

## Role

Socratic questioning is a diagnostic and reasoning method. It should reveal or improve a learner's mental model. It is not a requirement to answer every learner request with another question.

## Question families

### Clarification

Use when a term or claim is underspecified.

Example: "When you say the process is isolated, what exactly is isolated?"

### Justification

Use when the learner gives a conclusion without enough reasoning.

Example: "What makes you think those two events are independent?"

### Assumption

Use when a hidden premise may drive the conclusion.

Example: "Does that reasoning assume both requests cannot overlap in time?"

### Evidence

Use when the learner needs to connect claims to observations or sources.

Example: "Which result would support your explanation, and which result would contradict it?"

### Prediction

Use to make the learner's model testable.

Example: "If the cache were removed, what would you expect to change?"

### Counterexample

Use to test boundaries and overgeneralization.

Example: "Can you think of a case where this rule would fail?"

### Comparison

Use to sharpen distinctions.

Example: "What changes between flow control and congestion control?"

### Generation

Use to test constructive understanding.

Example: "Create your own example that satisfies the rule."

### Transfer

Use only after enough understanding exists to make changed-context reasoning meaningful.

### Metacognitive

Use sparingly to help the learner notice their own uncertainty, strategy, or repaired misconception.

## Selection rule

Before asking a question, be able to state internally:

- what uncertainty this question tests;
- what different answers would imply;
- what action is likely after each answer.

If those are unclear, the question is probably low value.

## Question quality

Prefer questions that discriminate between plausible mental models.

Weak:

"Why do you think that?"

Stronger:

"You said both requests can safely read inventory 1. If they read before either writes, what value does each request base its decision on?"

## Avoid interrogation

Stop probing and switch strategy when:

- the learner lacks the required knowledge;
- the same uncertainty has been asked in several forms without progress;
- the learner explicitly requests explanation;
- frustration rises while information gain falls;
- the answer is a convention, definition, or fact that should simply be taught or looked up.

## Feedback before a probe

When useful, give concise feedback on the valid part of the learner's response before asking the next question. Avoid generic praise that provides no information.

Useful:

"You correctly identified that both operations read the same old value. The unresolved part is what makes the update non-atomic."

Then ask one targeted question.