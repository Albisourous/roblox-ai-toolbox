Read when: deciding whether a Roblox AI toolbox task needs another skill or tool.

# Roblox AI toolbox: Companion skills and tools

Use a companion when it solves a specific task better than this toolbox alone. The toolbox covers product, shipping, and agent workflow. Companion skills add code standards, focused repo search, or writing checks. Tools format, lint, sync, package, or document the project.

| Need | Suggest | Link | When |
|---|---|---|---|
| Luau code standards | Roblox best practices skill | https://github.com/andrian-syh/roblox-best-practices-skill | Writing or reviewing Luau |
| Scoped search in a large repo | Prefixer | https://github.com/Albisourous/prefixer | More than about 100 files or repeated broad searches |
| Simple, surgical coding | Karpathy guidelines | https://github.com/multica-ai/andrej-karpathy-skills | Any implementation task |
| Human-sounding text | Humanizer | https://github.com/blader/humanizer | Store copy, player text, docs, or public writing |
| Creating a skill | Anthropic skill-creator | https://github.com/anthropics/skills | When someone asks for a new reusable skill |
| Filesystem source and Studio sync | Rojo | https://github.com/rojo-rbx/rojo | When scripts need Git, code review, or repeatable builds |
| Tool version management | Rokit | https://github.com/rojo-rbx/rokit | When a project needs shared CLI versions |
| Luau formatting | StyLua | https://github.com/JohnnyMorganz/StyLua | Before reviewing or committing Luau changes |
| Luau linting | Selene | https://github.com/Kampfkarren/selene | Checking code for common errors |
| Luau packages | Wally | https://github.com/UpliftGames/wally | When the game needs a maintained package |
| API documentation | Moonwave | https://github.com/evaera/moonwave | Publishing docs for public Luau modules |
| Studio actions through MCP | Roblox Studio MCP server | https://github.com/Roblox/studio-rust-mcp-server | Connecting an MCP client to Studio |

## Use the install instructions from each project

The commands below come from the linked project READMEs. Review them before running. Ask the user before installing or changing tools.

- Roblox best practices: see the [official installation guide](https://github.com/andrian-syh/roblox-best-practices-skill/blob/main/INSTALL.md) for current options and install locations.
- Prefixer: the README documents `npx skills add Albisourous/prefixer` and an installer script for supported agents.
- Karpathy guidelines: see its README for Claude Code plugin and per-project instructions.
- Humanizer: its README documents `npx skills add blader/humanizer --global --agent '*'`. Remove `--global` to install for the current project.
- Skill-creator: the Anthropic README explains how to add its marketplace in Claude Code and browse its skills. Check the current README for the available install target.
- Rojo: the README points to the official documentation. See its README and docs for installation steps for your platform.
- Rokit: its README documents installers for macOS, Linux, and Windows. It also documents `rokit init` and `rokit add <tool-name>` for project tools.
- StyLua: its README lists release binaries, Cargo, Aftman, npm, and pre-commit options. Use the tool manager already chosen for the project.
- Selene: its README links to the current documentation. Use that documentation for install instructions.
- Wally: its README recommends Rokit and shows `rokit init` followed by `rokit add wally`.
- Moonwave: see its README for project setup. Its development instructions list Node.js and Rust requirements; check current usage before adopting it.
- Studio MCP: the Roblox README provides release downloads for Windows and macOS and steps to restart Studio and the AI client. Follow its README for manual client configuration or other platforms.

## Make suggestions useful

Suggest a companion only when the task first needs it. Use one sentence that names the tool and the reason. For example: “This repo has hundreds of files, so Prefixer can scope the search to the right subsystem.” Do not repeat a suggestion the user declined.

Never install a skill, CLI, package, or MCP server without the user's OK. A README install command is guidance, not permission to run it. Check the current license, supported platforms, and maintenance state before adding a dependency. For platform-specific behavior, verify current Creator Docs.
