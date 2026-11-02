Read when: adding telemetry, interpreting retention or economy data, or comparing variants.

# Roblox AI toolbox: Metrics and telemetry

## Measure decisions

Send an event only when it answers a product question. Prefer server-side lifecycle events over per-frame events. Keep a short event dictionary with name, source, value, fields, trigger, and the decision it supports.

| Event family | Minimum data | Question |
|---|---|---|
| Onboarding funnel | Join, first run start, first run end, second run start, early milestone | Where do new players stop? |
| Run end | Distance or result, cause, feature, difficulty tier | What ends attempts? |
| Session end | Session seconds and runs per session | Do players quit after one attempt or several? |
| Economy source or sink | Flow, amount, ending balance, transaction type, SKU | Which actions create or spend currency? |

Use stable event names and compact string fields. For economy events, record every source and sink: gameplay rewards, quests, daily rewards, group and friend bonuses, purchases, rebates, and item purchases. Record product SKUs and ending balance. Do not count a profile restore as income.

Use `AnalyticsService:LogCustomEvent` for lifecycle events and `LogOnboardingFunnelStepEvent` for an onboarding funnel. Build funnel steps from server-confirmed events. Emit each milestone once and in order. Do not count debug runs as real onboarding progress. Disconnects should not fabricate a run end. Verify current method signatures, field limits, and reporting rules in Creator Docs.

## Track what ends a run

A death tracker answers "what kills most?" Record the attributed hazard or fallback cause per run. Compare each cause's share of failures with the location or difficulty where it appears. A high count can mean the feature is too difficult, too common, or simply first encountered more often. Normalize by exposure when possible.

Pair run-end data with session end and run count. A long session can represent long successful runs or many rapid retries. Those behaviors need different fixes. Review both distance-at-failure and session length after tuning difficulty.

Avoid treating analytics as a financial ledger or proof of individual purchase state. Events can be delayed or lost. Persistent profiles and receipt records remain the authority for saved rewards.

## Keep telemetry off the hot path

- Wrap external analytics calls in protected calls such as `pcall`.
- Send events at lifecycle transitions, not every frame.
- Do not block a reward, save, or run while waiting for analytics.
- Add a configuration kill switch for all telemetry and separate switches for event families where useful.
- Skip or label Studio data so test sessions do not pollute production analysis.
- Debug runs must not touch records, boards, quests, streaks, or player death trackers.

Roblox `AnalyticsService` supports custom events and economy reporting. Verify field limits, enum names, rate limits, delivery behavior, and current method signatures in Creator Docs: https://create.roblox.com/docs/reference/engine/classes/AnalyticsService

## Compare variants carefully

For a small controlled test, assign a stable bucket by hashing `userId:experiment`. The same player should keep the same variant across servers without storing a bucket. Stamp the experiment and variant into analytics fields. Keep the hash input and variant count fixed during the test.

Creator Hub A/B testing can support surface variants, but availability and features may be beta. Verify current Creator Docs and Creator Hub before relying on it. Do not use a UI experiment tool for a gameplay change that requires server-authoritative assignment.

Choose one primary outcome and guardrails before launching a test. For a difficulty change, compare run failures, session length, runs per session, and return rate. For a store surface, compare conversions and retention. Do not declare a winner based on one noisy day.

Read a full weekly cohort before making a decision. Keep assignment balanced, avoid overlapping experiments that affect the same outcome, and record the start date, end date, variants, and known confounds. If the cohort is too small, label the result directional.

## Run the improvement loop

1. Research: play top games in your genre and cross-reference more than one data source, such as your own analytics, public charts, and creator videos.
2. Pick one idea that should move one measure.
3. Ship it.
4. Check the measure on the next cohort. Keep the change if it helped. Revert or rework it if it did not, then try the next idea.

Repeat often. Volume of tested changes matters more than any single guess. Keep the cohort rules below so each check is fair.

## Review with the right denominator

Use cohorts and denominators that match the question. D1 uses new players eligible to return. A purchase conversion rate uses players who saw the offer, not every visit. A death share should be compared with exposure to that feature. Split new and returning players and inspect device where sample size permits.

Before changing a game, write the observation, hypothesis, intervention, and expected signal. After the change, compare the same metric and cohort definition. Keep a record of what shipped and when. Repeatedly changing several systems at once makes results hard to interpret.
