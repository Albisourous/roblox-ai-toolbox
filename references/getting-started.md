Read when: creating your first Roblox place or choosing an AI-assisted workflow.

# Roblox AI toolbox: Getting started

## Start with one small place

Install Roblox Studio from the official setup page: https://create.roblox.com/docs/studio/setup. Sign in, open a template such as Baseplate, and press Play to see the empty place from a player's view. Add one simple goal, one obstacle, and a clear finish. Keep the first version small enough to test in a few minutes.

Save the work as an experience in Studio. An experience can contain one or more places. Keep it private while you learn and test. Publishing permissions and menu labels can change, so verify the current steps in Creator Docs: https://create.roblox.com/docs/studio/publishing/publish-experiences-and-places.

You can work in Studio, connect an AI agent through an MCP server, or move code into files and Git. Start with the path that feels clear. You can change later.

## Choose how the agent reaches Studio

### Studio's built-in MCP server

In Studio, open Assistant, choose Manage MCP Servers, and enable "Enable Studio as MCP server." Then connect an MCP-capable AI client and ask it to inspect the open place before making a small change. Menu names and support can change. Verify the current setup in Creator Docs before relying on this workflow: https://create.roblox.com/docs.

This path keeps the place and its DataModel visible in Studio. The agent may be able to inspect or edit objects through tools, but the available tools depend on the client and Studio version. Confirm what the agent can do before asking it to publish or change live settings.

### Roblox's open-source Studio MCP server

Roblox also publishes an open-source server: https://github.com/Roblox/studio-rust-mcp-server. Its README provides release downloads and setup steps. The README lists release downloads for Windows and macOS. Other clients may need manual configuration. Read the README for current downloads and client support.

For total beginners, Roblox's open-source server is a good starting point because its README walks through setup. Download only from the official repository. Restart Studio and the AI client after setup, then check that the client lists Studio tools before asking for edits. Follow the server README if your system or client differs.

### Files and Git with Rojo

When scripts grow beyond a few files, keep source code in a project folder and use Git to track changes. Rojo connects files to the Roblox DataModel: https://github.com/rojo-rbx/rojo. Its README links to the current documentation and supported workflows.

Rokit manages command-line tools for a project: https://github.com/rojo-rbx/rokit. Install Rokit using the current instructions in its README. In a project, `rokit init` creates its tool configuration and `rokit add <tool-name>` adds a tool. Start with Rojo, StyLua, and Selene. Check each tool's current README for the package name and install options. Wally packages can be added with `rokit add wally`, as shown in Wally's README: https://github.com/UpliftGames/wally.

StyLua formats Luau: https://github.com/JohnnyMorganz/StyLua. Selene checks Luau for common errors: https://github.com/Kampfkarren/selene. The tools change over time. Follow their READMEs rather than copying a version number from an old tutorial.

Studio alone is enough for a small prototype. Move to files and Git when source files, review, or repeatable builds make the project easier to manage.

## A short glossary

| Term | Meaning |
|---|---|
| Experience or universe | The overall Roblox game and its connected places. |
| Place | One map or scene inside an experience. |
| DataModel | The tree of services and objects that make up a running place. |
| Server and client | The server owns shared game state. Each client handles one player's view and input. |
| Script, LocalScript, ModuleScript | Code that runs on the server, on a client, or can be shared as a module. Check execution context in Creator Docs. |
| RemoteEvent and RemoteFunction | Messages between a client and server. Validate every client request on the server. |
| DataStore | Roblox storage for data that should persist between sessions. Verify current limits and behavior in Creator Docs. |
| Game Pass | A product that usually grants a permanent entitlement. Verify current purchase behavior in Creator Docs. |
| Developer Product | A repeatable purchase, often used for consumable items. Its receipt must be granted safely by the server. |
| Robux | Roblox's virtual currency. Prices, fees, and rules can change. Verify current Creator Docs. |
| Creator Hub | The web dashboard for managing experiences, settings, analytics, and publishing. |
| Open Cloud | Roblox APIs for approved external tools. Verify current API scopes and endpoint behavior in Creator Docs. |
| Rojo | A tool that syncs a filesystem project with Studio. |

## Ask an agent for one clear change

Give the agent a goal, say whether the work runs on the server or client, describe the expected behavior, and ask for a short manual test checklist. Make one request per feature. Ask it to inspect the project structure before editing.

Example prompts:

> Add a finish line to this place. Detect completion on the server, show a result card on the client, and list three manual test steps.

> Add a jump tutorial for first-time players. Use one short visual hint, hide it after the first jump, and tell me which files you changed.

> Save a player's best score. Keep the server authoritative, handle storage errors, and give me a checklist for first play, rejoin, and a failed save. Check current DataStore guidance in Creator Docs.

> Add one cosmetic Game Pass to the shop. Do not change gameplay power. Show the current price safely, verify ownership on the server, and explain how to test without assuming the creator account is a new player.

## Build the first complete loop

- Prototype the core loop with placeholder art. Make the goal clear before adding a large map.
- Add save data only for progress players need between sessions. Handle failed reads and writes. Verify current DataStore rules in Creator Docs.
- Add one optional monetization item only after the game works without it. Keep competitive play fair and check current policy.
- Test controls, text size, and safe areas on a phone. Studio emulation is useful, but it cannot replace a device check.
- Publish privately and test a fresh join. Verify the current publish steps and eligibility in Creator Docs.
- Invite a few people to play. Watch where they stop, ask what they expected, and fix the biggest problem.
- Open the experience to the public only after the first session, save flow, purchase flow, and release settings pass.

## Avoid common first-project mistakes

- Trusting the client: treat every client message as a request. The server must validate the player, item, amount, and game state.
- Ignoring storage errors: DataStore requests can fail. Use `pcall`, bounded retries, and a clear fallback. Verify the current API guidance in Creator Docs.
- Granting purchases twice: deduplicate receipts durably and retry safely. See the monetization reference.
- Publishing with debug flags on: check test masks, free-for-testing settings, and temporary controls before release.
- Designing only for desktop: phone players need large targets, readable text, and controls that do not cover the action.
- Rebuilding an engine feature: search Creator Docs and engine APIs before adding custom physics, UI, persistence, or messaging.
