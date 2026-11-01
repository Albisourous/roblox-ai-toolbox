Read when: preparing a Roblox release, updating a live listing, or changing Open Cloud assets.

# Publishing and compliance

## Check release state

Before publishing, review release flags and test-only state:

- Debug generators and test shortcuts are off.
- Test ownership masks and fake entitlements are empty.
- Free purchase bypasses are off.
- Local debug edits are either committed to the intended working tree or removed.
- The running sync tool serves the checkout you reviewed.
- The current build passes its source checks.

Confirm the Studio window holds the live cloud experience, not a local file. The File menu should show "Download a Copy" for a cloud place, and `game.PlaceId` should be nonzero. If either check disagrees, stop and identify the open document before publishing.

After publish, verify the asset's Updated time through the public details endpoint: `https://economy.roblox.com/v2/assets/<placeId>/details`. Allow about a minute for the value to change. Players already in old servers can continue running old code. Rejoin after a minute to test the new version.

Publishing, syncing source, and updating a repository are separate operations. A source commit or sync does not prove that the cloud place was published. Capture the published asset time and run a live smoke test.

## Separate maturity from age eligibility

Content maturity and eligibility for Kids or Select are separate checks. Answer the current questionnaire accurately. Do not repeat a completed questionnaire just to change a different publishing gate.

Current Kids and Select eligibility rules are volatile. Check Creator Docs before deciding that a game can reach a particular audience: https://create.roblox.com/docs/production/publishing/kids-and-select

Review voice chat and camera access. Turn them off when the game does not need them. Confirm the experience page, platform support, localization, and maturity settings before making the experience public.

## Prepare the listing

Keep a release listing kit with:

- A recognizable icon that stays legible when circularly cropped for a pass.
- Five distinct thumbnails that show the main activity and social play.
- A title with words players search for and the game's brand.
- A short description whose first lines explain the activity.
- Correct genre, device support, maturity, and localized text.

Check current Creator Hub limits and image requirements before upload. Do not use unrelated game names or misleading keywords. Ask someone unfamiliar with the game to read the title and first lines of the description.

## Use Open Cloud safely

Open Cloud can create or patch game passes and developer products, including icons, when the key has the right scopes. The source experience confirms that game-pass and developer-product writes require `game-pass:write` and `developer-product:write`. Verify current scope names and endpoint behavior in Creator Docs before use.

Any script that can mutate a live experience must default to dry run. Require an explicit `--apply` flag for writes. Print the target universe, asset, and changed fields before applying. Read back the result after a mutation and stop if it differs from the intended value.

Observed: universe boolean fields accepted a PATCH, while a description PATCH returned 200 without changing the description. A success status alone did not prove that the text changed. Paste description text in Creator Hub when the API path does not apply it, then verify the visible result.

Use an unauthenticated public endpoint to check readiness only when it exposes the needed public data. The source material uses `develop.roblox.com` universe and badge endpoints as examples. Confirm current endpoint behavior and do not treat a public response as proof of write access.

## Close the release loop

Publish only after the release flags, source checks, listing, and compliance review are complete. Confirm the right place is open, publish from Studio, verify the asset Updated time, then join a fresh server. Check the main loop, store, leaderboard, and any changed platform integration.

Keep a short release record with version or commit, place, publish time, checks, and smoke-test result. If any step is unverified, say so. Never claim a live release from a local build alone.
