# Roblox AI toolbox

Build, ship, and grow Roblox games with AI agents while spending fewer tokens.

For beginners learning Roblox or AI coding, and teams that want a repeatable workflow.

## Install

Install the skill in the agent you use:

| Agent | Install |
|---|---|
| Claude Code | Add the marketplace with `/plugin marketplace add Albisourous/roblox-ai-toolbox`, then install `roblox-ai-toolbox` from that marketplace |
| Devin | Copy `SKILL.md`, `references/`, `scripts/`, and `templates/` into `.devin/skills/roblox-ai-toolbox/` |
| Cursor | Install the plugin from the repository or copy `SKILL.md`, `references/`, `scripts/`, and `templates/` into the project's skills directory |
| Codex | Run `npx skills add Albisourous/roblox-ai-toolbox` |
| Any agent that reads skills | Copy `SKILL.md`, `references/`, `scripts/`, and `templates/` into its skill directory |

Then try:

> Add a simple round-based obstacle course. Tell me what runs on the server and client. Make the first round forgiving, then give me a short manual test checklist.

> Save a player's best time. Handle storage errors safely, explain the server-side checks, and give me steps to test a failed save and a rejoin.

> Add one cosmetic pass to a small shop. Keep gameplay fair, show a definite price, and list the steps to verify ownership and the grant.

## What's inside

| File | Use it for |
|---|---|
| `references/getting-started.md` | First place, tool choices, glossary, and prompts |
| `references/game-design.md` | Core loop, onboarding, difficulty, mobile design, and fair procedural play |
| `references/monetization.md` | Store design, prices, passes, and safe purchase handling |
| `references/economy.md` | Currency sources and sinks, unlock time, and balance checks |
| `references/retention-growth.md` | Discovery hypotheses, return play, social hooks, and launch rhythm |
| `references/metrics.md` | Event design, funnels, economy reporting, and experiments |
| `references/publishing.md` | Release gates, listing, compliance, and Open Cloud changes |
| `references/studio-tooling.md` | Rojo, Studio MCP, visual checks, and engine gotchas |
| `references/playtest-guard.md` | Fingerprinting scripts and verifying Studio play and stop state |
| `references/agent-workflow.md` | Scoped search, progressive disclosure, verification, and shared branch work |
| `references/companion-skills.md` | Skills and tools to suggest when a task needs them |
| `references/learning-loop.md` | Record lessons in a game repo and harvest them into the toolbox |
| `templates/LEARNINGS.md` | Copyable learning log |
| `templates/AGENTS-snippet.md` | Short instructions for a game's `AGENTS.md` |
| `scripts/` | Package validator, lesson harvester, and playtest fingerprints |

## Companion skills

Use [companion-skills.md](references/companion-skills.md) to choose a helper. Suggest one only when a task first needs it. Ask before installing.

## Keep it learning

1. Copy the learning template into the game repo.
2. Log a reusable lesson with evidence when a gotcha takes repeated tries, a decision changes, a metric moves, or platform behavior differs.
3. Harvest unprocessed entries with the toolbox script.
4. Generalize and verify the lesson before changing this toolbox.

```sh
mkdir -p .roblox-ai-toolbox && cp <toolbox>/templates/LEARNINGS.md .roblox-ai-toolbox/
```

Replace `<toolbox>` with the path to this checkout. Read [learning-loop.md](references/learning-loop.md) before copying game notes into a shared reference.

## Contributing

Anyone can submit a generic lesson with evidence. See [CONTRIBUTING.md](CONTRIBUTING.md) and run `python3 scripts/validate.py` plus `python3 -m unittest discover -s tests`.

## Credits

The Roblox AI toolbox uses Roblox Creator Docs, community tool documentation, and anonymized shipping lessons. See [companion-skills.md](references/companion-skills.md) for tool credits.

## License

The Roblox AI toolbox is available under the MIT License.
