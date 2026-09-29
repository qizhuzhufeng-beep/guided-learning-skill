# Learning Frontier

## Definition

The learning frontier is the concept or small set of concepts that:

1. have enough prerequisite support to be learnable now;
2. are relevant to the learner's target capability;
3. provide the highest value for the next learning action.

It is a reasoning model, not a requirement to construct a literal graph.

## Dependency types

Consider dependencies such as:

- factual prerequisite;
- procedural prerequisite;
- conceptual prerequisite;
- vocabulary prerequisite;
- representational prerequisite;
- misconception repair required before proceeding.

## Priority order

When several frontier candidates exist, prefer:

1. a blocking misconception already evidenced;
2. a missing prerequisite blocking the current target;
3. the concept currently being formed, to preserve local continuity;
4. the nearest next concept on the path to the target capability;
5. enrichment or optional extensions.

## Recompute triggers

Recompute after:

- every meaningful learner answer;
- a new misconception;
- evidence that a presumed prerequisite is missing;
- independent verification;
- transfer success or failure;
- a user-requested topic change;
- a direct request to skip or deepen a concept.

## Temporary dependency detours

If the learner needs a short prerequisite to understand the active topic, treat it as a temporary frontier node and return to the parent topic once repaired.

Example:

`self-attention → dot-product meaning → self-attention`

Do not create a new top-level topic for every prerequisite.

## Topic replacement

If the new subject has its own independent target, checkpoint the old topic and create fresh topic-local state.

## Avoid over-modeling

Do not spend learner-facing time drawing a large curriculum graph unless the learner requests it or the map itself helps. The frontier primarily guides the agent's choice of next action.