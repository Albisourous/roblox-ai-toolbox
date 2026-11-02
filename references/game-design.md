Read when: shaping a Roblox game loop, onboarding, difficulty, controls, or repeat play.

# Roblox AI toolbox: Game design

## Make the game legible

- A new player should understand the activity within 5 seconds from the title and icon. Use a concrete action and a recognizable object. Check comprehension with players who have not seen the design.
- Put the first meaningful action before setup. New players should enter play directly when the game can safely choose defaults. Move optional choices to a later screen.
- Build the first 60 seconds around quick feedback. Make the opening forgiving, show one clear reward before the first likely failure, and give enough time to learn the primary control.
- Use a visible hint overlay at the start, then hide it after the player acts or a short period ends. Keep hints contextual and brief. Avoid coach cards, paragraphs, and permanent labels that compete with play.
- End each attempt with a clear result and one next goal. Give players a one-tap retry. Use the end card to point to a nearby badge, personal best, daily challenge, or unfinished mission.

## Check the idea before building

Ideas are cheap. Most of a game's result comes from the idea and how well it is executed, with data-driven tuning doing the rest. Before committing, check the idea against these questions:

- Is it easy to consume? A young player should get it without reading.
- Does one simple mechanic offer depth and replayability?
- Does it work on phone, console, and desktop?
- Does it have mass-market appeal, and do players already want this fantasy?
- Is the core fantasy strong? A well-built world that sells the premise, such as a tiny avatar in a giant room, does a lot of the work.
- Is there a curiosity hook and a reason to come back tomorrow, such as a new item to unlock or roll?
- Can players show off what they own or built to others nearby?

One creator who studies top games for a living reported that most front-page games share a simple core mechanic, a reason to return, and a social flex element. Treat that as a pattern to test, not a formula.

## Keep it simple, with depth

Many players are young children. Pick one simple mechanic that keeps producing new decisions. A single building mechanic becomes deep when other players can raid the result, because each loss sends the player back to find a better layout. A single random roll becomes deep when players keep asking what comes next and how far it can go.

Every feature needs a clear cause and effect: press a button, see the result in the game right away. Players do not care how many systems a game has. They leave when they cannot tell how it works. A feature list that impresses developers often confuses players. Simple scales.


Prototype one mechanic in a rough Studio test. For example, use an `AlignPosition` part that chases the player and see whether dodging it feels fun. Tune movement early, including running, double jump, or dodge, and let the core verb suggest the theme. Then build a round loop around that action.

Plan real time for hit detection. It often takes more work than a quick prototype suggests. Once rounds work, add long-term progression: upgrades bought with earned cash and unlockable tools that change how rounds play, so attempts do not feel repetitive. Add lobby extras after that. A leaderboard or practice area supports the game better than an unrelated obby.

Playtest with friends, other developers, or your community at every stage, even when the game looks rough. Use their feedback to decide what to tune before adding more content. If you add random unlocks, let players earn them with soft currency. Do not sell random boxes for Robux. See [monetization.md](monetization.md).

## Play your own game

Polish is usually the gap between a copy that stalls and the game it copied. Play every build yourself before publishing, on each device you support. Look for small friction: a proximity prompt that does not trigger, unpolished UI, a system that breaks after a respawn. Fix friction before adding content.

- Test with a gamepad, not only touch and keyboard. In one case study about 30% of players were on console, console onboarding felt unclear, and fixing it raised D1.
- Join on a fresh account to see what a new player sees. Your creator account may skip onboarding or own items a new player lacks.
- Play top games in your genre yourself, since videos hide how the controls feel. Note what they do in the first minute.

A short intro cutscene that sets up the fantasy is a common pattern in top games. One creator reported that adding one cut the share of players who left right away from about 22% to about 15%. Treat that as an anecdote. Keep it short, keep the first action close behind it, and compare your own cohorts. See [metrics.md](metrics.md).

## Teach, then test

Introduce one mechanic in a safe setting before combining it with other mechanics. The first exposure should have room to react. Later sections can increase speed, complexity, or consequence.

Use a simple progression:

| Stage | Purpose | Design check |
|---|---|---|
| Introduce | Show one new hazard or action | Can a first-time player identify it before danger? |
| Practice | Repeat it with low pressure | Does a mistake teach what to change? |
| Combine | Pair it with a known mechanic | Can the player still read the safe route? |
| Test | Raise pressure or vary timing | Does success reflect skill rather than surprise? |

Do not introduce several unfamiliar hazards at once. When a player fails, show the cause. If a dodge that avoids one hazard sends the player into another, change the layout. Track deaths by cause and location, then tune the point where a mechanic first appears.

## Keep controls small

- Each control must earn its place. Fewer verbs are easier to learn and to map across keyboard, touch, and gamepad.
- Map each device to the same intent where possible. Avoid device-specific mechanics that change the required skill.
- Set large touch targets, keep text readable at phone size, and respect safe areas and cutouts.
- Test on a real phone. A desktop window resized to a narrow shape does not reproduce touch input, device safe areas, or platform UI.
- If the game uses its own boards and the native player list overlaps the HUD, hide the default list. `StarterGui:SetCoreGuiEnabled(Enum.CoreGuiType.PlayerList, false)` is an engine API. Verify current behavior in Creator Docs: https://create.roblox.com/docs/reference/engine/classes/StarterGui

## Make each session feel complete

Most players use phones, so short sessions should still deliver a goal, result, and reward. Let progress survive a failed attempt when that fits the game. Use frequent feedback, clear milestones, and a retry that does not require navigating through several menus.

Show the player's avatar or chosen appearance during play. Let nearby players see each other's looks, scores, or progress in a shared space or board. Self-expression and visible ownership give players something to talk about and make clips easier to recognize.

Design moments that read in a short vertical video. A clear opening, visible risk, near miss, surprising result, or friend challenge works better than an unexplained long sequence. Keep the main action visible and avoid relying on text that disappears in a small crop.

## Make procedural play fair

Seeded deterministic generation can support fair challenges and replayable leaderboards. The same seed should produce the same layout for every player and every retry.

- Keep the generator pure. Give it a seeded `Random` object and return data describing the layout.
- Do not call `math.random` or create Roblox Instances inside the generator.
- Build or spawn the returned data outside the generator.
- Test many seeds for reachable paths, fair spacing, and valid entry and exit conditions.
- Store the seed with a record so another player can reproduce the run.

Determinism only helps if the server controls the seed and validates results. Do not trust a client report as proof of a leaderboard score.

## Keep tuning coherent

Put gameplay tunables in one central configuration module. Avoid scattering magic values through builders, UI, and server logic. Write the design document alongside code when a change alters a stated rule, mechanic, or balance target. Keep the numbers and behavior aligned.

Before adding a mechanic, ask whether it improves the core loop enough to justify another control, tutorial, UI state, and test case. Remove verbs that do not earn their place. Test the smallest version with players before expanding content.

For each change, define the player behavior it should improve and the signal that would show improvement. Use a manual test on a phone for touch changes. Use seeded cases to test procedural difficulty. Use a screenshot for a visual claim. A build passing does not show that the game reads well.
