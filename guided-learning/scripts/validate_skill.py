from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

import yaml


OPEN_SPEC_FIELDS = {
    "name",
    "description",
    "license",
    "compatibility",
    "metadata",
    "allowed-tools",
}

NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
REFERENCE_PATTERN = re.compile(r"\[[^\]]+\]\((references/[^)]+)\)")
REQUIRED_HEADINGS = [
    "## Mode gate comes first",
    "## Reconstruct the minimum learning state every learning turn",
    "## Core learning loop",
    "## Teaching invariants",
    "## Choose one primary pedagogical action",
]


def split_frontmatter(text: str) -> tuple[dict[str, object], str]:
    if not text.startswith("---\n"):
        raise ValueError("SKILL.md must start with YAML frontmatter")

    closing = text.find("\n---\n", 4)
    if closing == -1:
        raise ValueError("SKILL.md frontmatter is not closed with ---")

    raw = text[4:closing]
    body = text[closing + 5 :]
    data = yaml.safe_load(raw)
    if not isinstance(data, dict):
        raise ValueError("SKILL.md frontmatter must be a YAML mapping")
    return data, body


def validate_frontmatter(skill_root: Path, frontmatter: dict[str, object]) -> list[str]:
    errors: list[str] = []

    unknown = sorted(set(frontmatter) - OPEN_SPEC_FIELDS)
    if unknown:
        errors.append(f"non-portable frontmatter fields: {', '.join(unknown)}")

    name = frontmatter.get("name")
    if not isinstance(name, str) or not name:
        errors.append("frontmatter.name must be a non-empty string")
    else:
        if len(name) > 64:
            errors.append("frontmatter.name exceeds 64 characters")
        if not NAME_PATTERN.fullmatch(name):
            errors.append("frontmatter.name must use lowercase letters, digits, and single hyphens")
        if name != skill_root.name:
            errors.append(f"frontmatter.name {name!r} does not match directory {skill_root.name!r}")

    description = frontmatter.get("description")
    if not isinstance(description, str) or not description.strip():
        errors.append("frontmatter.description must be a non-empty string")
    elif len(description) > 1024:
        errors.append("frontmatter.description exceeds 1024 characters")

    metadata = frontmatter.get("metadata")
    if metadata is not None:
        if not isinstance(metadata, dict):
            errors.append("frontmatter.metadata must be a mapping")
        else:
            for key, value in metadata.items():
                if not isinstance(key, str) or not isinstance(value, str):
                    errors.append("frontmatter.metadata keys and values must be strings")
                    break

    return errors


def validate_skill_body(skill_root: Path, text: str, body: str) -> list[str]:
    errors: list[str] = []
    lines = text.splitlines()

    if len(lines) > 500:
        errors.append(f"SKILL.md has {len(lines)} lines; open specification recommends 500 or fewer")

    heading_positions: list[int] = []
    for heading in REQUIRED_HEADINGS:
        position = body.find(heading)
        if position == -1:
            errors.append(f"missing required core section: {heading}")
        else:
            heading_positions.append(position)

    if len(heading_positions) == len(REQUIRED_HEADINGS) and heading_positions != sorted(heading_positions):
        errors.append("critical SKILL.md sections are not ordered for long-context resilience")

    for target in REFERENCE_PATTERN.findall(body):
        target_path = skill_root / target
        if not target_path.is_file():
            errors.append(f"missing referenced file: {target}")
        if target_path.parent != skill_root / "references":
            errors.append(f"reference path should remain one level deep: {target}")

    return errors


def validate_reference_directory(skill_root: Path) -> list[str]:
    errors: list[str] = []
    references = skill_root / "references"
    if not references.is_dir():
        return ["references directory is missing"]

    for path in sorted(references.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        if not text.strip():
            errors.append(f"empty reference file: {path.name}")
        for target in REFERENCE_PATTERN.findall(text):
            errors.append(
                f"reference file {path.name} links to another local reference {target}; keep reference loading one level deep"
            )

    return errors


def validate_evals(skill_root: Path) -> list[str]:
    errors: list[str] = []
    eval_dir = skill_root / "evals"

    activation_path = eval_dir / "activation.json"
    scenarios_path = eval_dir / "scenarios.json"

    if not activation_path.is_file():
        errors.append("evals/activation.json is missing")
    else:
        activation = json.loads(activation_path.read_text(encoding="utf-8"))
        if not isinstance(activation, list) or not activation:
            errors.append("activation evals must be a non-empty JSON list")
        else:
            for item in activation:
                if not {"id", "should_activate", "prompt", "reason"}.issubset(item):
                    errors.append("activation eval entry is missing required fields")
                    break

    if not scenarios_path.is_file():
        errors.append("evals/scenarios.json is missing")
    else:
        scenarios = json.loads(scenarios_path.read_text(encoding="utf-8"))
        if not isinstance(scenarios, list) or not scenarios:
            errors.append("scenario evals must be a non-empty JSON list")
        else:
            for item in scenarios:
                if not {"id", "setup", "user_turn", "must", "must_not"}.issubset(item):
                    errors.append("scenario eval entry is missing required fields")
                    break

    return errors


def validate(skill_root: Path) -> list[str]:
    skill_file = skill_root / "SKILL.md"
    if not skill_file.is_file():
        return ["SKILL.md is missing"]

    text = skill_file.read_text(encoding="utf-8")
    frontmatter, body = split_frontmatter(text)

    errors = []
    errors.extend(validate_frontmatter(skill_root, frontmatter))
    errors.extend(validate_skill_body(skill_root, text, body))
    errors.extend(validate_reference_directory(skill_root))
    errors.extend(validate_evals(skill_root))
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate the portable guided-learning Agent Skill")
    parser.add_argument(
        "skill_root",
        nargs="?",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="Path to the guided-learning skill directory",
    )
    args = parser.parse_args()

    errors = validate(args.skill_root.resolve())
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print("guided-learning skill validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())