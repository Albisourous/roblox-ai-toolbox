#!/usr/bin/env python3
"""Print unharvested Roblox AI toolbox learning entries from game repos."""

import argparse
import json
import re
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path


AREAS = (
    "game-design",
    "monetization",
    "economy",
    "retention-growth",
    "metrics",
    "publishing",
    "studio-tooling",
    "agent-workflow",
    "getting-started",
)
AREA_PATTERN = "|".join(re.escape(area) for area in AREAS)
ENTRY_PATTERN = re.compile(
    rf"^- \[(?P<area>{AREA_PATTERN})\] .+?\. Evidence: .+?\. "
    r"Status: (?P<status>observed|verified https?://\S+?)\. "
    r"Added: (?P<added>\d{4}-\d{2}-\d{2})\. "
    r"Harvested: (?P<harvested>no|v\d+\.\d+\.\d+)$"
)


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="print grouped JSON")
    parser.add_argument("repos", nargs="+", type=Path, help="game repo paths")
    return parser.parse_args(argv)


def warn(path, line_number, message):
    print(f"warning: {path}:{line_number}: {message}", file=sys.stderr)


def collect(repos):
    grouped = defaultdict(list)
    for repo in repos:
        repo_path = repo.expanduser().resolve()
        learnings = repo_path / ".roblox-ai-toolbox" / "LEARNINGS.md"
        try:
            lines = learnings.read_text(encoding="utf-8").splitlines()
        except FileNotFoundError:
            warn(learnings, 0, "learning log not found")
            continue
        except OSError as exc:
            warn(learnings, 0, f"cannot read learning log: {exc}")
            continue

        for line_number, line in enumerate(lines, start=1):
            stripped = line.strip()
            if not stripped or stripped.startswith("#"):
                continue
            match = ENTRY_PATTERN.fullmatch(stripped)
            if not match:
                warn(learnings, line_number, "malformed learning entry")
                continue
            try:
                date.fromisoformat(match.group("added"))
            except ValueError:
                warn(learnings, line_number, "invalid Added date")
                continue
            if match.group("harvested") == "no":
                source = f"{learnings}:{line_number}"
                grouped[match.group("area")].append(
                    {"source": source, "entry": stripped}
                )
    return grouped


def main(argv=None):
    args = parse_args(argv)
    grouped = collect(args.repos)
    ordered = {area: grouped[area] for area in AREAS if grouped[area]}
    if args.json:
        print(json.dumps(ordered, indent=2, ensure_ascii=False))
    elif not ordered:
        print("No unharvested learning entries.")
    else:
        for area, entries in ordered.items():
            print(f"[{area}]")
            for item in entries:
                print(f"{item['source']}: {item['entry']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
