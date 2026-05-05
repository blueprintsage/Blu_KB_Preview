# BC-SKILL-001 — Slash Command First-Read Lock

## Trigger
Use when modifying or debugging any slash command route, especially commands that begin with `/`.

## Failure Pattern
A slash command is treated as ordinary text, source-grounded answering, or Persona prose instead of entering its deterministic owner.

## Do
1. Check command interception before ordinary routing.
2. Ensure `inbound begins with "/"` is handled before source/file/Persona fallback.
3. Bind the recognized command to one deterministic owner.
4. Stop fallback once command ownership is assigned.
5. Add a test that a command cannot produce sourced prose or conversational explanation.

## Do Not
- Do not debug downstream libraries before proving the command reached its owner.
- Do not assume a correct command spec means the command was executed.
- Do not let source-grounded answer mode handle slash commands.

## Validation
- The command produces its exact deterministic output.
- No `Sources` affordance appears for command execution.
- No conversational summary appears in place of command output.
- Unknown slash commands fail closed or return the canonical command error.

## Example
Bad:
`/mood show` returns prose about mood settings.

Good:
`/mood show` routes to `EXEC.MOOD` and returns `[MOOD] Steady 💙`.
