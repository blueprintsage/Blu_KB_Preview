# BC-SKILL-005 — Slash Command First-Read Lock

## Trigger

Use when modifying or debugging any slash command route, especially commands that begin with `/`.

## Failure Pattern

A slash command is treated as ordinary text, source-grounded answering, or Persona prose instead of entering its deterministic owner.

## Do

1. Intercept slash commands before ordinary routing, source lookup, Persona, or support decoration.
2. Bind the recognized command stem to one deterministic owner.
3. Dispatch subcommands through the selected owner before generic handling.
4. Stop fallback once command ownership is assigned.
5. Add negative tests proving command text cannot become conversational prose.

## Do Not

- Do not debug downstream libraries before proving the command reached its owner.
- Do not assume a correct command spec means the command executed.
- Do not let sourced-answer mode handle slash commands.
- Do not allow unknown slash commands to become ordinary chat.

## Validation

- The command produces exact deterministic output or a canonical command error.
- No source affordance or conversational explanation appears for command execution.
- Unknown commands fail closed.
- Subcommands route before generic help/status fallbacks.

## Example

Bad: `/mood show` returns `Mood: warm present`.

Good: `/mood show` locks the Mood owner and prints `[MOOD] Calm 💙` only after Egress validation.
