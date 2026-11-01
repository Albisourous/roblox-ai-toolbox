Read when: recording a game-repo lesson or harvesting lessons into the toolbox.

# Roblox AI toolbox: Learning loop

Keep reusable evidence close to the game while it is fresh. Share lessons that can help another project. Build the Roblox AI toolbox from checked evidence, with project details removed. Record the observation before deciding whether it applies across projects.

## Part 1: Keep notes in the game repo

Create `.roblox-ai-toolbox/LEARNINGS.md` in the game repo. Start with the provided [learning log template](../templates/LEARNINGS.md) to keep area names and evidence fields consistent.

Add an entry when:

- A platform gotcha takes more than two tries to understand or work around.
- The user corrects a design, monetization, or user experience choice.
- A metric moves after a change and the evidence could help explain why.
- An API or policy behaves differently from a toolbox reference.

Use one line per entry:

```text
- [area] lesson. Evidence: what happened. Status: observed | verified <docs URL>. Added: YYYY-MM-DD. Harvested: no
```

Use one of these area names: `ads`, `game-design`, `monetization`, `economy`, `retention-growth`, `metrics`, `publishing`, `studio-tooling`, `agent-workflow`, or `getting-started`.

Keep each lesson concise and the evidence specific enough to check. `Observed` means the behavior happened in a project and has not been confirmed as a current platform rule. `Verified` needs a Creator Docs URL that supports the claim. Do not turn an observed workaround into an official rule.

Example:

```text
- [studio-tooling] Play loaded an older script after sync. Evidence: the Edit and Server fingerprints differed before a fresh start. Status: observed. Added: 2026-10-31. Harvested: no
```

Never record secrets, player data, user IDs, private links, or Robux revenue. Do not use a real game title, place name, or account detail as a lesson. Keep the file local or in the game repo's private workflow if the evidence is sensitive.

## Part 2: Harvest into the Roblox AI toolbox

Run the standard-library harvester against one or more game repos:

```sh
python3 scripts/harvest.py ../game-one ../game-two
python3 scripts/harvest.py --json ../game-one
```

It reports entries marked `Harvested: no`, grouped by area with their source path and line number. It warns about malformed lines and exits successfully so one bad note does not block other repos. Review the warning and repair the source entry before harvesting it.

For each candidate:

1. Generalize the lesson. Remove game and place names, account identifiers, private URLs, and project-specific config keys. Turn any price into an explicitly labeled example or remove it.
2. Search the toolbox references for an existing rule. Merge useful evidence into the matching section instead of adding a duplicate.
3. Check volatile platform claims against current Creator Docs. Add the docs URL when verified. Keep project-only behavior labeled `Observed`.
4. Add the generalized rule to the matching reference. Keep the language short and state the evidence or the verification status.
5. Mark the source entry `Harvested: vX.Y.Z` only after the toolbox change is ready. Use the release version that contains the change.
6. Bump the version, add a changelog entry, run the validator with private terms configured, and run the unit tests.
7. Open a pull request or push according to the toolbox maintainer's workflow.

Do not mark an entry harvested just because it was read. It must be generalized, checked for duplicates, and either included or rejected with a reason in the game repo.

## When the reference disagrees with reality

Check the version, platform, and conditions in the observed scenario. If the current Creator Docs or a reproducible test contradicts the toolbox, fix the reference and record the evidence. Do not silently work around a stale rule or teach another agent to repeat it.
