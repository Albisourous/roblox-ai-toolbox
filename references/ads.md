Read when: running Roblox ads for a launch or relaunch.

# Roblox AI toolbox: Launch ads

## Why use ads at launch

A new experience has little player behavior data. A paid campaign can bring in an early audience so you can measure whether players understand the first session, how long they play, and whether they return. Start with [retention-growth.md](retention-growth.md), which explains why you must fix the first session before buying reach.

Roblox's Ads Manager documentation says the `Plays` objective can provide initial traffic that helps an experience get considered for Recommended For You. The same page says ad campaigns do not affect its ranking there. Use paid traffic to measure a launch. Treat Home recommendation impressions as a signal to watch, not a promised result.

## Before you spend

Use this release gate before starting a campaign:

- A new player can finish the first session on a phone.
- Onboarding makes the first action clear and does not block play.
- No known bug prevents players from starting or completing the core loop.
- Analytics events are live. You can inspect session starts, quits, and return play. See [metrics.md](metrics.md).
- Two or three distinct thumbnails are ready to compare. Check the listing and release steps in [publishing.md](publishing.md).

Use [game-design.md](game-design.md) to review the first minute, controls, and mobile layout. If the first session still loses players, fix it before you pay for more visits.

## Set a budget you can afford

One creator's launch routine used about $10 per day for 10 days, about $100 total. For competitive genres or games that need full servers, the creator sometimes spent $15 to $20 per day. Treat both figures as examples, not Roblox requirements or performance guarantees.

The creator used 10 days to give the campaign time to evaluate. Set a total limit before launch and decide what results would justify continuing.

## Keep the first campaign broad

The current [Ads Manager documentation](https://create.roblox.com/docs/production/promotion/ads-manager) confirms these labels:

- `Daily Budget` sets the campaign's maximum spend per day.
- `Plays` is the objective for reaching players likely to start a session.
- `Budget & Duration` contains campaign budget and timing options.
- `Advanced Targeting` is optional. It can narrow delivery by location, age, gender, genre, or device type.

For a broad test, set `Daily Budget`, select the `Plays` objective, and leave `Advanced Targeting` unset or use its broadest available options. The creator described using all regions and all devices. The current documentation does not confirm those exact choice labels, so check current Ads Manager labels. The page calls the objective `Plays`, not "maximize plays." Start broad and let delivery find players. Use campaign data before narrowing the audience; there is no secret targeting trick.

## Compare a few thumbnails

Run two or three different thumbnails at the same time. Compare click-through rate (CTR) for each one, then replace or remove a clear loser after the campaign has data. A thumbnail that earns clicks still needs a game that keeps those players. Read CTR alongside cost per play (CPP), retention, and session length.

## Launch playbook

| Time | What to do |
|---|---|
| Day 1 | Let the campaign learn. Do not pause it or change its settings. Watch CTR and CPP. Join the game and follow real players for a few minutes. Note where they hesitate, get lost, or leave. |
| Days 2 to 4 | Compare the thumbnails. Replace or remove weak ones. Fix bugs you observed, then check that the first session still works on a phone. |
| Day 5 and later | Make an honest call. If the unofficial benchmarks look weak and players leave early, stop spending and fix the core game. If results look healthy and Home recommendation impressions appear, keep the campaign running while you watch organic traffic. Stop ads when organic traffic keeps servers active. |

## Keep improving while ads run

Keep a short daily fix list from player feedback, and ship useful updates while the campaign runs. In one solo creator's launch, ad-driven players had weaker metrics and less favorable like ratios than later organic players. Treat that as an anecdote and compare your own cohorts before drawing conclusions.

The same creator reported that extra campaigns after two weeks of weak Home recommendation impressions did not help, and metrics climbed after ads were turned off. Roblox's documentation says ads do not change Recommended For You ranking, so this timing does not show that turning ads off improves ranking. Use player feedback and cohort results to choose fixes, and judge organic traffic on its own.

## Read benchmarks with retention

One creator used CTR around 2.5% or higher and CPP around $0.008 or lower as personal targets. These are unofficial examples, not platform benchmarks. Results vary by genre, region, creative, and time. Roblox currently labels the metric `CPP (Cost-per-play)` in Ads Manager.

Compare those campaign numbers with D1, D7, and session length from [metrics.md](metrics.md). Strong clicks with poor return play point to a game problem. Do not increase spend just to improve a dashboard number.

## Mistakes to avoid

- Buying reach before the first session works on mobile.
- Changing settings every day while the campaign is learning.
- Narrowing the audience before you have evidence about who enjoys the game.
- Running one thumbnail, so you have nothing useful to compare.
- Spending past day 5 when retention and session length show that players leave early.
