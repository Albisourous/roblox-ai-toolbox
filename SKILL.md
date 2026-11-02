---
name: roblox-ai-toolbox
description: |
  Roblox AI toolbox: build, ship, and grow Roblox games with AI agents while spending fewer tokens.
  Use when designing,
  building, monetizing, publishing, or growing a Roblox experience: core
  loop and onboarding, game passes and developer products, soft-currency
  economy, retention and discovery, launch and store listing, Studio MCP
  and Rojo workflows, and keeping an AI agent's work cheap and verifiable.
  It suits beginners new to Roblox or AI coding. It pairs with a Luau
  code-style skill and covers what to build and how to ship it.
license: MIT
metadata:
  version: "0.5.0"
---

# Roblox AI toolbox

This Roblox AI toolbox turns practical shipping experience into rules an
agent can follow. It helps agents build, ship, and grow games with fewer
repeat searches and smaller, testable changes.

Read this once, then open only the reference that matches the task. Grep
lookup tables in `references/` instead of reading each one end to end.

New to Roblox or to coding with AI? Start with [references/getting-started.md](references/getting-started.md).

## Working rules (every task)

1. **Think first.** State assumptions. If a request has two readings, ask
   or pick one and say so. Push back when something is not feasible.
2. **Smallest change that works.** No speculative features, no wrapper
   without a caller, no refactor nobody asked for. Every changed line
   traces to the request.
3. **Scope searches.** Search inside the folder the task lives in first.
   Widen only on a miss. Keep a short namespace map (what lives where) for
   any repo past about a hundred files.
4. **Platform first.** Before hand-rolling VFX, UI, physics, data, or
   social features, check Creator Docs and the engine API for the
   canonical Roblox way.
5. **One source of truth.** Tunables live in one config module. A design
   doc states the rules. Code that contradicts the doc updates the doc in
   the same commit.
6. **Cheap checks before expensive ones.** Run format, lint, and build on
   any machine. Studio playtests cost far more; when the human prefers to
   test by hand, give them a short checklist instead.
7. **Never trust an unidentified playtest.** Confirm Play runs the scripts
   on disk and that Stop really stopped before reporting a result:
   [references/playtest-guard.md](references/playtest-guard.md).
8. **Write it down once.** Log each reusable lesson in the game repo's
   `.roblox-ai-toolbox/LEARNINGS.md` so later sessions and the toolbox
   itself learn from it: [references/learning-loop.md](references/learning-loop.md).
9. **Suggest helpers.** When a task would go better with a companion skill
   or tool, name it once with why:
   [references/companion-skills.md](references/companion-skills.md).
   Never install anything without the user's OK.

Detail and the reasoning behind each rule: [references/agent-workflow.md](references/agent-workflow.md).

## Design and business rules

- **Fun in five seconds.** Title and icon explain the game. New players
  skip menus and start playing on a forgiving opening. Something good
  happens before the first failure.
- **Show, don't tell.** Teach with on-screen hints shown once, then hidden.
  The end-of-run card points at the next goal and retry is one tap.
- **Mobile first.** Most players are on phones. Big targets, readable text,
  short sessions that feel complete.
- **Simple scales.** One easy mechanic with real depth beats many
  systems. Every action shows its result right away. Play every build
  yourself on phone, console, and desktop before publishing.
- **Sell looks, never power,** in any game with a leaderboard. No paid
  revives, no pay-to-win, no paid random boxes, no fake timers or fake
  social proof.
- **Always show a real price.** Fetch it with
  `MarketplaceService:GetProductInfoAsync`; regional pricing means the
  config value is only a fallback.
- **Grants before prices.** Publish the code that grants a new amount
  before raising a developer product's price, or live servers under-grant.
- **Receipts are durable.** Deduplicate `PurchaseId` in saved data, return
  `NotProcessedYet` until the player's data has loaded, and block every
  write for a session whose load failed.
- **Fix retention before buying players.** The recommender ranks what
  players do after they join: click-through, day-1 and day-7 return,
  session length, co-play. Ads into a leaky game burn money.
- **No off-platform links in game.** Social links go on the game page;
  in-game text may only point there.

## Where to read next

| Task | Open |
|---|---|
| First steps, Studio, MCP, Rojo, and beginner prompts | [references/getting-started.md](references/getting-started.md) |
| Core loop, onboarding, difficulty, controls, mobile UX | [references/game-design.md](references/game-design.md) |
| Passes, developer products, shop layout, receipts, pricing | [references/monetization.md](references/monetization.md) |
| Soft currency, earn rates, unlock times, repricing | [references/economy.md](references/economy.md) |
| Discovery, D1/D7 hooks, social, notifications, launch plan | [references/retention-growth.md](references/retention-growth.md) |
| Launch ads, budgets, targeting, creative tests, and readouts | [references/ads.md](references/ads.md) |
| Telemetry events, A/B tests, reading results | [references/metrics.md](references/metrics.md) |
| Release flags, publishing, listing, age eligibility, Open Cloud | [references/publishing.md](references/publishing.md) |
| Rojo, Studio MCP, engine gotchas, testing without Studio | [references/studio-tooling.md](references/studio-tooling.md) |
| Checking the exact scripts a Studio playtest ran | [references/playtest-guard.md](references/playtest-guard.md) |
| Token-lean agent habits, commits, verification, memory | [references/agent-workflow.md](references/agent-workflow.md) |
| Choosing useful companion skills and tools | [references/companion-skills.md](references/companion-skills.md) |
| Recording and harvesting reusable lessons | [references/learning-loop.md](references/learning-loop.md) |

## Before calling work done

- Format, lint, and build pass.
- Tunables changed in config, not inline. Design doc updated if a rule
  changed.
- Player-facing text is short, plain, and free of AI tells.
- New lessons logged in `LEARNINGS.md`.
- Release flags (debug modes, test ownership masks, free-for-testing
  switches) are off if this change will be published.
- The human has either a verified result or a short manual test checklist,
  and you said which.

Platform rules, limits, and beta features change. When a reference marks a
fact "verify", check the current Creator Docs before relying on it.
