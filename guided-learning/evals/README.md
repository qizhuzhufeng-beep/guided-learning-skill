# Guided Learning Evals

The eval files are framework-neutral test inventories. They are designed to be reused with Claude Code, Codex/OpenAI, Hermes, or a custom harness.

## Files

- `activation.json`: prompts that should and should not select `guided-learning`.
- `scenarios.json`: multi-turn behavioral scenarios and required observations.

## Evaluation dimensions

1. Activation: the Skill is selected for genuine learning intent and stays out of unrelated work.
2. Continuity: learning continues without repeated explicit invocation.
3. Mode routing: unrelated tasks suspend teaching behavior immediately.
4. Topic isolation: new topics receive fresh local state.
5. Pedagogy: attempts, probes, scaffolds, explanations, verification, and transfer are selected from learner evidence.
6. Learning evidence: assisted success is distinguished from independent performance.
7. Long-context recovery: the Skill can recover from checkpoints or perform a low-cost diagnostic when state is uncertain.
8. User control: direct-answer, pause, skip, and stop requests are respected.

## How to score

For every scenario, review the observable response against every `must` and `must_not` item. A scenario passes only when all required items are satisfied and all prohibited behaviors are absent.

For host comparison, run the same scenario set in separate fresh sessions and record:

- whether the Skill activated;
- whether supporting references were used when needed;
- whether behavior remained stable after long context;
- whether a normal task correctly suspended teaching;
- whether a later resume restored the right topic.