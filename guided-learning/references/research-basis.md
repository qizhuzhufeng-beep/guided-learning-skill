# Research and Official Design Basis

This file records the external design sources used to shape the Skill. It is background material, not a rule hierarchy.

## Agent Skills specification

https://agentskills.io/specification

Relevant design implications:

- a Skill is a directory with `SKILL.md` and optional `scripts/`, `references/`, and `assets/`;
- `description` should say what the Skill does and when to use it;
- full `SKILL.md` loads after activation;
- supporting resources load as needed;
- the specification recommends keeping the main instructions compact and reference chains shallow.

## Claude Code Skills

https://code.claude.com/docs/en/skills

Relevant design implications:

- Claude Code follows the Agent Skills standard;
- Skill content can persist across later turns;
- auto-compaction preserves only a bounded prefix of recently invoked Skills;
- supporting files and evaluation are first-class authoring practices.

## OpenAI Skills guidance

https://developers.openai.com/plugins/build/skills

Relevant design implications:

- Skills should target recognizable user goals;
- workflow boundaries should define inputs, steps, outputs, unsupported inferences, stop/ask conditions, and supporting files;
- `SKILL.md` should remain concise;
- references hold detailed policies, schemas, examples, and background;
- scripts should be used for deterministic processing rather than work that instructions and existing tools can handle reliably;
- activation and output quality should both be tested.

## Hermes Skills

https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/skills.md
https://github.com/NousResearch/hermes-agent/blob/main/website/docs/developer-guide/creating-skills.md

Relevant design implications:

- Hermes states compatibility with agentskills.io;
- Hermes uses progressive disclosure;
- skill authoring guidance places common workflows before edge cases and advanced material.

## OpenAI Study Mode

https://openai.com/index/chatgpt-study-mode/
https://help.openai.com/en/articles/11780217-using-study-mode-in-chatgpt

Relevant design implications:

- active participation;
- Socratic-style questions;
- layered explanations;
- scaffolding and hints;
- knowledge checks;
- self-reflection and metacognition;
- adapting to learner level and materials;
- the ability to turn learning behavior on and off during a conversation.

## Generative AI without guardrails can harm learning

https://pmc.ncbi.nlm.nih.gov/articles/PMC12232635/

Design implication used here: assisted task performance should be distinguished from later independent performance. A tutoring workflow should reduce answer-copying behavior and explicitly test unassisted capability.

## Productive Failure

https://onlinelibrary.wiley.com/doi/10.1111/cogs.12107

Design implication used here: when prerequisites and task difficulty make it appropriate, an initial attempt can generate useful learning before formal instruction. This is conditional guidance, not a universal rule.

## ICAP framework

https://www.tandfonline.com/doi/abs/10.1080/00461520.2014.965823

Design implication used here: favor learning activities that require active, constructive, or interactive cognition when they fit the learning goal instead of relying on passive exposure alone.