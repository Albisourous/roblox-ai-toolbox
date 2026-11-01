Read when: an agent must change a Roblox game with fewer searches, tokens, and risky iterations.

# Roblox AI toolbox: Agent workflow

## Think before coding

Use the Karpathy guidelines as a compact review: think before coding, choose the simplest solution, make surgical edits, and define a measurable goal. Credit: https://github.com/multica-ai/andrej-karpathy-skills and Andrej Karpathy's post.

- State assumptions. If two interpretations change the implementation, ask before choosing.
- Prefer the smallest change that meets the request. Do not add speculative abstractions.
- Touch only files needed for the task. Keep existing style and remove only dead code your change creates.
- Define success before editing. A bug fix should have a reproducing test or a narrow verification. A design change should name the player behavior and metric it should improve.

## Scope searches

Read a namespace map before searching a large repository. Search the likely directory first, then widen on a miss. Credit: https://github.com/Albisourous/prefixer

Use targeted `rg` searches and read only matching sections. Do not dump a whole repository or every large document into context. If a search misses, check whether the namespace map is stale before assuming the code is absent.

## Use progressive disclosure

Keep the always-read skill short. Put detailed procedures, platform APIs, and examples in linked references. Use a lookup table or search query to find a specific rule instead of repeatedly reading every reference. Keep common commands near the top and rare troubleshooting lower in the reference.

Search Creator Docs and engine APIs before hand-rolling a Roblox feature. Use established engine behavior when it fits. Verify API names, permissions, platform limits, and policy in current Creator Docs.

## Make a bounded change

Read the design document and relevant code before editing. If code contradicts a design decision, update the design document in the same change. Keep tunable values in the project's single configuration source.

Use a tracker document for multi-item work. Give each change one clear item and one commit. Keep tests and notes tied to that item. Assign new tracker rows the next number after the current maximum.

Record new operational gotchas in persistent project memory or a knowledge file. A gotcha that lives only in a chat will be rediscovered by the next agent.

## Verify cheaply first

Run formatting, lint, and a build on any machine before spending time in Studio. Then test only the changed flow. If the human prefers manual playtests, leave a short checklist with exact steps and expected results instead of running a long agent playtest.

Use a deterministic debug seed or feature keyword to reach a specific procedural feature quickly. Verify the normal random flow afterward if the change affects general generation. Remove temporary debug prints and test shortcuts before commit.

For visual work, use screenshots. For server state, inspect the server DataModel. Do not infer visual success from a passing build or gameplay success from source text.

## Protect shared branches and live services

When agents share one branch, check for concurrent changes before integrating. Fetch immediately before a push. If commits are cited by hash, merge them so those references stay valid. Never overwrite another agent's work with a stale checkout.

Scripts that touch live services must default to dry run and require `--apply` for mutation. Print what will change. Use available APIs to check public state before asking a human to inspect it. Ask only for decisions or access you cannot obtain yourself.

Keep secrets out of shell output, logs, tests, and commits. Do not publish or deploy outside the requested release path.

## Humanize public text

Run the humanizer checklist on player-facing copy, store text, release notes, and public documentation. Remove staged openers, repeated closers, fake contrasts, forced triads, filler, and inflated claims. Keep technical names and supported facts intact.

Before committing, review the diff against the task. Run the narrowest relevant checks after the final edit. Report exactly what passed, what remains unverified, and any decision needed from the human.
