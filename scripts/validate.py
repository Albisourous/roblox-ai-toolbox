#!/usr/bin/env python3
"""Validate roblox-ai-toolbox package structure and shared metadata."""

import json
import os
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VERSION = None
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
version_match = re.search(
    r'(?m)^\s+version:\s*["\']?(\d+\.\d+\.\d+)["\']?\s*$', frontmatter
)
if not version_match:
    fail("SKILL.md: metadata.version must be a semantic version")
else:
    VERSION = version_match.group(1)

description_match = re.search(
    r"(?ms)^description:\s*\|\s*\n((?:[ \t]+.*(?:\n|$))*)", frontmatter
)
description = ""
if description_match:
    description = "\n".join(
        line.strip() for line in description_match.group(1).splitlines()
    ).strip()
else:
    fail("SKILL.md: description must use a block scalar")
first_sentence_match = re.match(r"^(.+?[.!?])(?:\s|$)", description, re.S)
first_sentence = first_sentence_match.group(1) if first_sentence_match else ""
if not first_sentence:
    fail("SKILL.md: description must start with a complete sentence")

word_count = len(re.findall(r"\b[\w']+\b", skill))
if word_count > 2000:
    fail(f"SKILL.md: {word_count} words exceeds the 2,000 word limit")

linked_references = set(
    re.findall(r"\]\(((?:references|scripts|templates)/[A-Za-z0-9_./-]+)\)", skill)
)
for link in sorted(linked_references):
    target = ROOT / link
    if not target.is_file():
        fail(f"SKILL.md: linked path does not exist: {link}")

changelog = ROOT / "CHANGELOG.md"
changelog_text = read_text(changelog)
first_heading = re.search(r"(?m)^## \[([^\]]+)\]", changelog_text)
if VERSION and (not first_heading or first_heading.group(1) != VERSION):
    fail(f"CHANGELOG.md: first version heading must be [{VERSION}]")

for manifest in sorted(ROOT.glob(".*-plugin/plugin.json")):
    try:
        data = json.loads(read_text(manifest))
    except json.JSONDecodeError as exc:
        fail(f"{manifest.relative_to(ROOT)}: invalid JSON: {exc}")
        continue
    if VERSION and data.get("version") != VERSION:
        fail(f"{manifest.relative_to(ROOT)}: version must be {VERSION}")
    if first_sentence and data.get("description") != first_sentence:
        fail(
            f"{manifest.relative_to(ROOT)}: description must match "
            "the first sentence of SKILL.md"
        )

marketplace = ROOT / ".claude-plugin" / "marketplace.json"
try:
    marketplace_data = json.loads(read_text(marketplace))
except json.JSONDecodeError as exc:
    fail(f"{marketplace.relative_to(ROOT)}: invalid JSON: {exc}")
else:
    if first_sentence and marketplace_data.get("description") != first_sentence:
        fail(
            f"{marketplace.relative_to(ROOT)}: description must match "
            "the first sentence of SKILL.md"
        )
    for plugin in marketplace_data.get("plugins", []):
        if VERSION and plugin.get("version") != VERSION:
            fail(
                f"{marketplace.relative_to(ROOT)}: plugin version must be "
                f"{VERSION}"
            )
        if first_sentence and plugin.get("description") != first_sentence:
            fail(
                f"{marketplace.relative_to(ROOT)}: plugin description must "
                "match the first sentence of SKILL.md"
            )

for reference in sorted((ROOT / "references").glob("*.md")):
    text = read_text(reference)
    if not text.startswith("Read when:"):
        fail(f"{reference.relative_to(ROOT)}: first line must start with Read when:")

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

private_terms_paths = []
local_terms = ROOT / ".private-terms"
if local_terms.is_file():
    private_terms_paths.append(local_terms)
env_terms = os.environ.get("PRIVATE_TERMS_FILE")
if env_terms:
    env_path = Path(env_terms).expanduser()
    if not env_path.is_absolute():
        env_path = ROOT / env_path
    if env_path.is_file():
        private_terms_paths.append(env_path)
    else:
        fail(f"PRIVATE_TERMS_FILE: file does not exist: {env_path}")

private_terms = set()
for terms_path in private_terms_paths:
    try:
        for line in terms_path.read_text(encoding="utf-8").splitlines():
            term = line.split("#", 1)[0].strip()
            if term:
                private_terms.add(term.casefold())
    except OSError as exc:
        fail(f"{terms_path}: cannot read private terms: {exc}")

if private_terms:
    try:
        tracked = subprocess.run(
            ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
            cwd=ROOT,
            check=True,
            capture_output=True,
        ).stdout.decode("utf-8").split("\0")
    except (OSError, subprocess.CalledProcessError, UnicodeDecodeError) as exc:
        fail(f"private terms: cannot list repository files: {exc}")
        tracked = []
    for relative in filter(None, tracked):
        if relative == "LICENSE":
            continue
        path = ROOT / relative
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        for line_number, line in enumerate(text.splitlines(), start=1):
            folded = line.casefold()
            for term in sorted(private_terms):
                if term in folded:
                    fail(
                        f"{relative}:{line_number}: private term "
                        f"{term!r} found"
                    )

if errors:
    print("\n".join(f"FAIL: {error}" for error in errors), file=sys.stderr)
    sys.exit(1)

print("Package validation passed.")
