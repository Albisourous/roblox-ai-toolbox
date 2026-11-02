Read when: pricing earnable items, setting rewards, or balancing a soft-currency economy.

# Roblox AI toolbox: Economy

## Model sources and sinks

List every way currency enters and leaves the game before choosing prices. Sources include repeatable play, first-time milestones, daily rewards, quests, group rewards, friend bonuses, and purchases. Sinks include cosmetics, upgrades, crafting, and other spending. Track one-time grants separately from repeatable earnings.

Keep leaderboard score separate from spendable currency. If a player can buy score or a score multiplier, the board stops measuring the intended skill. A paid pack should not be counted as gameplay income.

For every transaction, record the SKU, amount, transaction type, and ending balance. Use the same SKU for every path that buys the same item. Record discounted purchases separately if the discount changes the amount. This makes sources, sinks, and inflation visible.

## Estimate earnings before setting prices

Build earning scenarios from active play time, not calendar time. Estimate a short-run player, a typical player, and a skilled player. For each scenario, state assumptions about run length, time between runs, pickups, completion rate, and bonuses.

Use this formula for a repeatable run reward:

`currency per active hour = average currency per run * 3600 / (run seconds + between-run seconds)`

Do not add daily quests, streaks, group rewards, or purchases into a solo repeatable baseline. Estimate those separately. Label these estimates as assumptions until production data replaces them.

Measure p25, median, and p75 currency per active hour. These percentiles show how the economy serves slower, typical, and faster earners. Include new and returning players separately. Measure actual active time and actual banked rewards. Distance alone does not prove pickup rate or time played.

## Show unlock time from zero

Create an unlock table with item price, amount needed from zero, and estimated runs and active minutes for each earning scenario. Round up to complete runs. State that goals are alternatives, because spending on one item delays another.

Use the table to check the first earned item, common mid-tier goals, and the largest goal. A first earned cosmetic around 60 to 90 active minutes is one shipped-game planning example, not a platform standard. Choose a target based on playtest data and the game's session length. New players should get some early choice without making the entire catalog immediate.

Keep a free starting option and avoid progression that feels like a second job. If a player must wait several days, make the wait clear and offer a meaningful activity during it. Calendar-based release gates should not be confused with playtime needed to earn an item.

## Keep paid value consistent

Calculate currency per Robux for each pack. The rate should rise as pack size grows. Clearly state a first-purchase bonus and make it one-time. Do not imply that an item has an exact Robux equivalent when the player buys indivisible currency and keeps a leftover balance.

Prices should reflect the expected unlock time and the value of the item. Do not raise prices because a few skilled players earn quickly. Compare retention and satisfaction along with purchase conversion. A higher short-term spend rate can still harm lifetime value if it makes progression feel unfair.

## Pace progression before launch

Test progression on a fresh account. A creator or long-used tester account already owns the unlocks and skips the walls a new player hits. Play the first session as a new player and write down what unlocks at each minute.

Track every progression milestone as a funnel: first upgrade bought, second upgrade, first zone or tier reached, first capacity upgrade. Low conversion at one step means that step is confusing, introduced at the wrong time, or too expensive. In one observed launch, roughly three in five new players bought the first progression item and about one in four ever upgraded capacity; making the early items cheaper coincided with day-1 retention climbing from the single digits into the mid-teens.

Pair the funnel with paid playtester grinds. Give two or three testers a small Robux payment and a fixed report format - minutes played, what they unlocked, where they felt stuck, and anything blocking progress - then have them play for a few hours. Their notes plus the funnel give a hypothesis for the largest wall. Fix the early game first, then smooth the mid and late game. Finish this before a discovery push, not after: in the same launch a week of poor early retention while featured capped the peak.

## Calibrate after release

Read a full week of player cohorts before changing the economy. Compare active-hour earnings, runs per session, time to first purchase, unlock completion, D1 and D7 retention, payer conversion, and revenue per new player. Split new players from returning players. Use small samples as directional evidence, not a proven optimum.

Change one price band or reward family at a time. Record the hypothesis, date, affected cohort, and success measure. Keep the previous values available for rollback.

## Prevent documentation drift

Keep economy values in one source of truth and link design tables to it where practical. After any repricing, search every document for old amounts and update stale examples, store text, and release notes.

Add an automated check for economy invariants. Examples include prices divisible by a chosen denomination, minimum rewards, monotonic pack value, no duplicate item identifiers, and consistency between catalog price and discount calculation. These checks should assert rules, not freeze every balance choice forever.

Before a price change, test buying, granting, equipping, rejoining, and any rebate path. A static check cannot prove that a Roblox purchase prompt or receipt works.
