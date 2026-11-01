#!/usr/bin/env python3
"""Validate roblox-shipkit package structure and shared metadata."""

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VERSION = "0.1.0"
errors = []


def fail(message):
    errors.append(message)


def read_text(path):
    try:
        return path.read_text(encoding="utf-8")
    except OSError as exc:
        fail(f"{path.relative_to(ROOT)}: cannot read file: {exc}")
        return ""


skill_path = ROOT / "SKILL.md"
skill = read_text(skill_path) if skill_path.exists() else ""
if not skill_path.exists():
    fail("SKILL.md: file is missing")

frontmatter = ""
if skill.startswith("---\n"):
    pieces = skill.split("---", 2)
    if len(pieces) == 3:
        frontmatter = pieces[1]
    else:
        fail("SKILL.md: frontmatter is not closed")
else:
    fail("SKILL.md: YAML frontmatter must start with ---")

for field in ("name", "description", "metadata"):
    if not re.search(rf"(?m)^{field}:\s*(?:\S|$)", frontmatter):
        fail(f"SKILL.md: frontmatter is missing {field}")
if not re.search(r'(?m)^\s+version:\s*["\']?0\.1\.0["\']?\s*$', frontmatter):
    fail("SKILL.md: metadata.version must be 0.1.0")

word_count = len(re.findall(r"\b[\w']+\b", skill))
if word_count > 2000:
    fail(f"SKILL.md: {word_count} words exceeds the 2,000 word limit")

linked_references = set(
    re.findall(r"\]\((references/[A-Za-z0-9_./-]+)\)", skill)
)
for reference in sorted(linked_references):
    target = ROOT / reference
    if not target.is_file():
        fail(f"SKILL.md: linked reference does not exist: {reference}")

changelog = ROOT / "CHANGELOG.md"
changelog_text = read_text(changelog)
first_heading = re.search(r"(?m)^## \[([^\]]+)\]", changelog_text)
if not first_heading or first_heading.group(1) != VERSION:
    fail(f"CHANGELOG.md: first version heading must be [{VERSION}]")

for manifest in sorted(ROOT.glob(".*-plugin/plugin.json")):
    try:
        data = json.loads(read_text(manifest))
    except json.JSONDecodeError as exc:
        fail(f"{manifest.relative_to(ROOT)}: invalid JSON: {exc}")
        continue
    if data.get("version") != VERSION:
        fail(f"{manifest.relative_to(ROOT)}: version must be {VERSION}")

for reference in sorted((ROOT / "references").glob("*.md")):
    text = read_text(reference)
    if not re.search(r"(?m)^Read when:", text):
        fail(f"{reference.relative_to(ROOT)}: missing Read when: line")

for markdown in sorted(ROOT.rglob("*.md")):
    if ".git" in markdown.parts:
        continue
    text = read_text(markdown)
    for line_number, line in enumerate(text.splitlines(), start=1):
        if "\u2014" in line or "\u2013" in line:
            fail(
                f"{markdown.relative_to(ROOT)}:{line_number}: "
                "em dash or en dash is not allowed"
            )

if errors:
    print("\n".join(f"FAIL: {error}" for error in errors), file=sys.stderr)
    sys.exit(1)

print("Package validation passed.")
