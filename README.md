# roblox-shipkit

Roblox game design and shipping guidance for coding agents. It covers game loops, fair monetization, economy balance, retention, metrics, publishing, Studio tools, and efficient agent workflow.

## Install

Use the skill installer supported by your agent:

| Agent | Install |
|---|---|
| Claude Code | Add the marketplace with `/plugin marketplace add Albisourous/roblox-shipkit`, then install `roblox-shipkit` from that marketplace |
| Devin | Copy `SKILL.md` and `references/` into `.devin/skills/roblox-shipkit/` |
| Cursor | Install the plugin from the repository or copy the skill files into the project's skills directory |
| Codex | Run `npx skills add Albisourous/roblox-shipkit` |
| Any agent that reads skills | Copy `SKILL.md` and `references/` into its skill directory |

The skill's `SKILL.md` is the entry point. It routes agents to the reference that fits the task.

## What's inside

| Reference | Use it for |
|---|---|
| `references/game-design.md` | Core loop, onboarding, difficulty, mobile design, and fair procedural play |
| `references/monetization.md` | Store design, prices, passes, and safe purchase handling |
| `references/economy.md` | Currency sources and sinks, unlock time, and balance checks |
| `references/retention-growth.md` | Discovery hypotheses, return play, social hooks, and launch rhythm |
| `references/metrics.md` | Event design, funnels, economy reporting, and experiments |
| `references/publishing.md` | Release gates, listing, compliance, and Open Cloud changes |
| `references/studio-tooling.md` | Rojo, Studio MCP, visual checks, and runtime source identity |
| `references/agent-workflow.md` | Scoped search, progressive disclosure, verification, and shared branch work |

## Companion skills

These skills cover adjacent work. roblox-shipkit adds shipping, product design, and workflow guidance alongside Luau code standards.

- [Roblox best practices](https://github.com/andrian-syh/roblox-best-practices-skill) for Luau and Roblox code standards.
- [Prefixer](https://github.com/Albisourous/prefixer) for namespace maps and scoped repository search.
- [Studio playtest guard](https://github.com/Albisourous/roball-studio-runtime-identity) for verifying runtime source and Studio state.
- [Karpathy guidelines](https://github.com/multica-ai/andrej-karpathy-skills) for simplicity and goal-driven coding.
- [Humanizer](https://github.com/blader/humanizer) for clear player-facing and public text.

## Credits and license

The guidance draws on lessons from shipping a Roblox game and public Roblox Creator Docs. Companion skills are credited above. This package is available under the MIT License.
