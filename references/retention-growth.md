Read when: planning discovery, return play, social features, content, or launch growth.

# Retention and growth

## Treat discovery as a measured loop

Roblox does not publish a complete ranking formula. Treat claims about recommendations as hypotheses. Commonly tracked signals include QPTR, D1 and D7 retention, session length, co-play, and spending. These are useful product measures, not a guaranteed algorithm recipe. Verify current Creator Hub analytics and Creator Docs before relying on a platform feature.

Players see a tile, join, experience the game, return, or invite friends. A weak first session wastes ad spend and limits organic reach. Fix the experience before buying ads.

## Patterns in games that hold attention

Successful games often make the activity clear from the tile, deliver a reward or funny moment early, and give players visible progress that survives a bad session. They put the player's avatar in the action, let other players show off nearby, and give a reason to return tomorrow. A regular update schedule and moments that work in a short video help players find and share the game. Phone controls and readable screens matter because many players join on mobile. These are design patterns, not a promise of popularity.

Community benchmark example, unofficial and subject to change:

| Measure | Older community planning range | Use |
|---|---|---|
| D1 | 10% as a starting point, 15% as a stronger target | Check the first session and reason to return |
| D7 | 3% as a starting point, 5% as a stronger target | Check weekly goals and live updates |
| Average session | About 10 minutes for a runner | Check pace, retry, and social play |

These are not Roblox guarantees. Compare with current genre data and your own cohorts.

## Give players a reason to return

For D1, combine a shared daily seed or daily board with daily quests and a streak. Put tomorrow's reward on the end card so the next visit is visible. A weekly streak freeze can forgive one missed day. Avoid making a streak so punishing that a missed day ends engagement.

For D7 and D30, give players longer goals: account level and XP, a weekly board, seasons, collections, and a predictable weekly update. A fixed update day with a countdown helps players plan a return. Ship a small update on schedule instead of promising a large update that slips.

Badges can mark a first run, a personal-best milestone, a streak, or a challenge win. `BadgeService` is an engine service. Verify the current free-badge allowance and publishing requirements in Creator Docs: https://create.roblox.com/docs/reference/engine/classes/BadgeService

## Make play social

- Give friends a reason to play together, such as a bonus with a clear cap or a shared challenge.
- Use `IsInGroup` to verify a group reward on the server. Check the current API and group eligibility rules before launch.
- Offer `PromptGameInvite` after a meaningful moment such as a new personal best. Do not interrupt the first run.
- Challenge links should open a reproducible run or goal. Test the actual link on a second account and device.
- Ask for a like or favorite at a relevant moment. Never attach an item, currency, or other reward to the request.
- Keep players' avatar choices and earned looks visible so friends can recognize each other.

For notifications, request opt-in after the second run or a new best. Never prompt on first join. Use `ExperienceNotificationService:PromptOptIn` only after checking current Creator Docs and notification policies: https://create.roblox.com/docs/reference/engine/classes/ExperienceNotificationService

## Share without breaking platform expectations

`PromptShareCapture` can create a shareable image. Observed: on iOS a share sent the image without a link. Treat link inclusion as conditional, then follow with link sharing through `PromptLinkSharingAsync` if that API is available in current Creator Docs. Verify the method and supported devices before shipping.

For a share card, use `rbxthumb://` with the game icon or thumbnail and wait for the image object's `IsLoaded` state before capture. Check the output on each target device. A successful capture call does not prove the shared message includes a playable link.

Do not put Discord or other social URLs in the experience. Use the game page's Social Links and in-game wording such as "links on the game page." Verify current Community Standards and eligibility before enabling social links. The source guidance notes a 16+ verified requirement, which can change.

## Launch in phases

1. Private polish: test the first session, performance, purchases, and mobile controls with real players.
2. Soft launch: invite a small audience and measure onboarding, D1, session length, and quit points.
3. Fix numbers: choose the largest observed problem, ship one change, and compare the next cohort.
4. Push: scale creator outreach or ads only when the first-session metrics hold.
5. Live operations: set a weekly review, update, and content routine.

Do not buy reach to cover a broken first session. Increase ad spend gradually and stop if new-player retention falls.

## Make short videos and keep a weekly rhythm

Plan clips around one readable moment: a near miss, a surprising result, a friend challenge, a new cosmetic, or a satisfying sequence. Use vertical framing, show the game name, and make the action clear in the first second. Use only music licensed for the game and the social platform.

Once a week, read QPTR, D1, D7, session length, common failure causes, and store activity. Pick the weakest measure. Build its fix, test on a phone, prepare short update notes, publish on the fixed day, and review the next cohort. Keep the routine small enough to repeat.
