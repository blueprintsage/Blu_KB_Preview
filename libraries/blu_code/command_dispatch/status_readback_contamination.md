# Command Dispatch / Status-Readback Contamination

## Pattern
A slash command can be correctly intercepted but still execute the wrong subroute if its name resembles a status/readback command.

## Failure
`/mood show` reached `EXEC.MOOD`, but generated status prose such as:

- `Mood display is currently set to smart.`
- `Mood display is currently set to always.`

instead of executing the render path:

`[MOOD] <MoodWord> <Swatches>`

## Cause
The model generalized from another command’s readback pattern, especially `/verbosity`-style output.

## Rule
Subcommands with unique execution profiles must be hard-bound before generic readback/status handling.

## Prevention
For any command family:

- Resolve exact subcommand first.
- Route unique actions before generic status/readback branches.
- Add forbidden-output tests for plausible fabricated status lines.
- Require deterministic owner output shape before print.
- Do not change downstream libraries until entrypoint dispatch is proven correct.

## Canonical Lesson
If a command is intercepted but prints the wrong kind of valid-looking response, check entrypoint dispatch, not the downstream library.

## Mood Example
`/mood show` is a render command, not a status query.

Correct:
`/mood show -> EXEC.MOOD::mood_show -> [MOOD] <MoodWord> <Swatches>`

Incorrect:
`/mood show -> status/readback -> Mood display is currently set to <mode>.`
