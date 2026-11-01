Read when: shaping a Roblox game loop, onboarding, difficulty, controls, or repeat play.

# Game design

## Make the game legible

- A new player should understand the activity within 5 seconds from the title and icon. Use a concrete action and a recognizable object. Check comprehension with players who have not seen the design.
- Put the first meaningful action before setup. New players should enter play directly when the game can safely choose defaults. Move optional choices to a later screen.
- Build the first 60 seconds around quick feedback. Make the opening forgiving, show one clear reward before the first likely failure, and give enough time to learn the primary control.
- Use a visible hint overlay at the start, then hide it after the player acts or a short period ends. Keep hints contextual and brief. Avoid coach cards, paragraphs, and permanent labels that compete with play.
- End each attempt with a clear result and one next goal. Give players a one-tap retry. Use the end card to point to a nearby badge, personal best, daily challenge, or unfinished mission.

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
