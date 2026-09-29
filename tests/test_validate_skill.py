from pathlib import Path
import sys

import yaml


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = PROJECT_ROOT / "guided-learning"
SCRIPTS_DIR = SKILL_ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS_DIR))

import validate_skill


def test_complete_skill_passes_validator() -> None:
    assert validate_skill.validate(SKILL_ROOT) == []


def test_frontmatter_matches_open_agent_skills_spec() -> None:
    text = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
    raw = text.split("---", 2)[1]
    frontmatter = yaml.safe_load(raw)

    assert frontmatter["name"] == "guided-learning"
    assert len(frontmatter["name"]) <= 64
    assert 0 < len(frontmatter["description"]) <= 1024
    assert set(frontmatter).issubset(validate_skill.OPEN_SPEC_FIELDS)


def test_main_skill_stays_compact() -> None:
    lines = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8").splitlines()
    assert len(lines) <= 500


def test_all_references_are_direct_and_exist() -> None:
    text = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
    _, body = validate_skill.split_frontmatter(text)
    targets = validate_skill.REFERENCE_PATTERN.findall(body)

    assert targets
    for target in targets:
        path = SKILL_ROOT / target
        assert path.is_file()
        assert path.parent == SKILL_ROOT / "references"


def test_critical_sections_are_present_in_resilient_order() -> None:
    text = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
    _, body = validate_skill.split_frontmatter(text)
    positions = [body.index(heading) for heading in validate_skill.REQUIRED_HEADINGS]
    assert positions == sorted(positions)


def test_eval_inventory_contains_positive_and_negative_activation() -> None:
    import json

    cases = json.loads((SKILL_ROOT / "evals" / "activation.json").read_text(encoding="utf-8"))
    assert any(case["should_activate"] for case in cases)
    assert any(not case["should_activate"] for case in cases)


def test_scenarios_cover_mode_switching_and_long_context() -> None:
    import json

    cases = json.loads((SKILL_ROOT / "evals" / "scenarios.json").read_text(encoding="utf-8"))
    ids = {case["id"] for case in cases}

    assert "normal-task-suspends-learning" in ids
    assert "resume-after-normal-task" in ids
    assert "new-topic-isolated" in ids
    assert "long-context-uncertain-state" in ids