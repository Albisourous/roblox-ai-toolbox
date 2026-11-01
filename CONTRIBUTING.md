# Contributing to the Roblox AI toolbox

Submit a reusable lesson with evidence. Keep it generic enough to help a game repo you have never seen. Do not include a game title, place name, account identifier, private URL, or project-specific config key.

## Add a learning

Use one line in the format from [the learning loop](references/learning-loop.md):

```text
- [area] lesson. Evidence: what happened. Status: observed | verified <docs URL>. Added: YYYY-MM-DD. Harvested: no
```

Choose one allowed area from `templates/LEARNINGS.md`. Keep the lesson short. State what happened in the evidence field. Use `observed` for a result from one project. Use `verified` only with a current Creator Docs URL that supports the platform claim.

Before opening a change:

1. Search the matching Roblox AI toolbox reference for a duplicate.
2. Remove private data and generalize any project detail.
3. Verify volatile APIs, limits, and policies against current Creator Docs.
4. Run `python3 scripts/validate.py`.
5. Run `python3 -m unittest discover -s tests`.

Do not include credentials, player data, user IDs, private links, or Robux revenue. A passing check does not make sensitive data safe to publish. Follow the repository maintainer's contribution and release process.
