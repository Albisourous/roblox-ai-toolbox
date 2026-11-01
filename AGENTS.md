# Roblox AI toolbox repository instructions

This repository contains the Roblox AI toolbox skill, references, templates, and small validation tools. `SKILL.md` is the entry point. References hold details that agents should read only when relevant.

## Layout

- `SKILL.md`: routing and short working rules.
- `references/`: product guidance, workflow, and verified playtest procedure.
- `templates/`: copyable learning and game-repo instructions.
- `scripts/`: package validation, learning harvest, and source fingerprints.
- `tests/`: standard-library unit tests.

## Invariants

- Keep public text generic. Never add a game title, place or user ID, private link, or project-specific config key.
- Use plain text and ASCII hyphens. Do not use em or en dashes.
- Keep `SKILL.md` below 2,000 words. Put detail in references.
- Bump the version and changelog for a reusable guidance change.
- Keep `metadata.version`, the first `CHANGELOG.md` version, plugin manifests, and the marketplace plugin version in sync.
- The first sentence of the SKILL description must match each plugin description.
- Every linked reference, script, or template in `SKILL.md` must exist.

## Before pushing

Run `python3 scripts/validate.py` and `python3 -m unittest discover -s tests`. Keep `.private-terms` local and ignored. Add sensitive search terms only when the maintainer asks, and never commit that file.

## Harvest lessons

Follow [the Roblox AI toolbox learning loop](references/learning-loop.md). Keep source notes in each game repo, generalize evidence, check for duplicates, verify platform claims, then mark the source entry with the toolbox version that contains it.
