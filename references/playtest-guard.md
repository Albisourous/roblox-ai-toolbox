Read when: checking that Studio Play used current scripts or actually stopped.

# Roblox AI toolbox: Playtest guard

Studio can run older scripts than the files on disk. A stop request can also report success while Studio remains in Play. Either mistake can make an invalid run look correct. Compare script fingerprints and confirm Studio state before using playtest results.

## Fingerprint the changed scripts

The toolbox includes `scripts/fingerprint.luau` and `scripts/fingerprint.py`. The Luau version prints each script's full instance path, byte length, and 32-bit FNV-1a hash. The Python version prints the same length and hash for files on disk. Both normalize CRLF line endings to LF before computing the length and hash.

Use the Python script on the files that changed:

```sh
python3 scripts/fingerprint.py path/to/changed-script.luau
```

Pass every changed file in one call when a feature spans several modules.

Run the Luau script with the Studio MCP client's execution tool in the Edit DataModel. Tool names and access can vary by client and Studio version. Verify current Creator Docs and the MCP client documentation before relying on a specific tool or source access.

Match each file to its Studio instance using the project's sync map. For Rojo, check the project file and its mappings. The path can change when Studio copies a script into a runtime service. Match copied scripts by name and compare the content fingerprint, not only the path.

## Before counting a Play result

1. Stop any old Play session and confirm Studio is in Edit.
2. Fingerprint every changed script in Edit and compare with the disk output.
3. Start Play and fingerprint the Server DataModel.
4. Fingerprint the Client DataModel.
5. Compare each changed script with the Edit and disk fingerprints. Account for expected path changes when Studio copies a script at runtime.

If a changed script differs in either Play DataModel, the run is invalid. Do not count UI checks, console output, or assertions from it. A matching Edit fingerprint alone does not show what Play loaded. A value read through `require` is not proof either, because a required module can remain cached from an earlier load.

If there is a mismatch, keep it unexplained until the source of the difference is visible. Check which checkout the sync process serves, whether a second sync server is connected, and whether Studio reconnected to an older session. Record which checks you could not perform.

## Confirm that Play stopped

After the stop command:

1. Read Studio's state and confirm it reports Edit.
2. Check `RunService:IsRunning()` and confirm it returns `false`.
3. If Studio still reports Play, press Studio's own Stop button in the window running the experience.
4. Check the state and running value again.
5. Fingerprint Edit against disk one more time. Studio source can differ after a stop even when it matched before Play.

The Studio instance ID can change during Play and stop transitions. If a tool reports that the instance is disconnected, list connected Studio instances again and use the current ID. Do not treat a "Game Stopped" response as proof of the final state.

## Report the evidence

For each tested change, report the checkout and sync server, Studio state, and whether Edit, Server, Client, and disk fingerprints match. If a hash differs, name the script and DataModel. Separate verified state from anything you could not inspect. Do not say that the playtest passed while a changed script is mismatched or Studio remains in Play.

The fingerprint scripts are included in this Roblox AI toolbox under the MIT License. They provide source identity evidence, not proof that the game behaves correctly. Use a short functional test after the identity check.
