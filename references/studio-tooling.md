Read when: using Rojo, Studio MCP, device testing, or debugging source mismatches.

# Roblox AI toolbox: Studio and agent tooling

For a step-by-step source check before trusting a playtest, use the [playtest guard](playtest-guard.md) reference.

## Know which source you are testing

Rojo maps a filesystem checkout into a Roblox DataModel. A running `rojo serve` process serves its working tree, including uncommitted edits. Check the process and working directory before syncing. Two checkouts can contain different code even when both appear current.

Keep one original place and one intended sync server for a test. Avoid creating duplicate test places as a shortcut. After a source change, sync, stop Play, and start a fresh Play session before asserting behavior.

Run the source gate before using Studio:

```sh
stylua --check src/
selene src/
rojo build -o build/game.rbxl
```

Use the commands and project paths configured by the repository. A successful build checks source structure. It does not prove the active Studio document or runtime uses that source.

## Treat Studio MCP state as mutable

- Studio MCP `studio_id` changes on each Play or stop transition. List connected studios again after each transition.
- `execute_luau` needs an explicit `datamodel_type`. Use the Server or Client DataModel when the test requires it.
- Edit DataModel calls are rejected during Play. Stop first, then edit.
- A module `require` can return a cached copy across calls. Read the module's `.Source` or require a `:Clone()` when checking fresh code.
- Edit source can match disk while Play runs older code. Compare the Server and Client sources during Play when source identity matters.
- A stop acknowledgment can arrive before Studio actually returns to Edit. Confirm the state or `RunService:IsRunning()` before trusting the stop.

Clicking a UI element by its `instance_path` can fail when names are duplicated. Find its `AbsolutePosition` and use the visible control location when path lookup is ambiguous.

## Test rendering and behavior

Use screenshots to verify visual claims. Capture the changed screen once and inspect the real state. Console output and a successful build cannot show whether text clips or buttons overlap.

For mobile layouts, gate touch-specific UI on `TouchEnabled` and inspect the actual device safe area. Studio's touch emulator helps with basic layout but has limits. Test controls on a real phone before release.

If Studio is unavailable, create an HTML or SVG mock for store art or UI and render it in headless Chrome. This checks composition and text sizing in a browser, not Roblox runtime behavior. State the distinction.

## Know common engine failure modes

Observed: with streaming enabled and no character, a RemoteEvent argument that references an unreplicated Instance can arrive as nil. Find the object by a stable name or identifier on the receiving side, and validate it on the server. Verify streaming and character behavior for the current experience before applying this workaround.

Do not set `workspace.FallenPartsDestroyHeight` from a game script. Configure the kill height declaratively in the project settings. Observed example: a default kill height of -500 silently destroyed a long-travelling object. Check the current place value before assuming the default is safe.

When floors sit on decorative non-collide parts, set `RaycastParams.RespectCanCollide = true` for floor queries where appropriate. Confirm the query still finds the intended support surface.

Observed: the persistent leaderboard beta appeared only in the native PlayerList. The feature and behavior can change. Verify current Creator Docs before building a custom UI around it.

An older standalone Luau compiler can report register-limit errors that do not reproduce in the current Roblox toolchain. Compare with an unchanged baseline and current tooling before treating the report as a source regression.

## Keep the test honest

Record the exact checkout, sync server, Studio document, and runtime state for a failure. If the Edit source is correct but the Play source is old, fix source identity before diagnosing gameplay. A historical screenshot or prior successful playtest does not prove the latest source works.

Prefer a short, direct test of the changed feature. Use a known seed or test keyword to reach the feature without playing a long random session, then return to ordinary play for one smoke test. Remove temporary debug prints and test-only switches before committing.
