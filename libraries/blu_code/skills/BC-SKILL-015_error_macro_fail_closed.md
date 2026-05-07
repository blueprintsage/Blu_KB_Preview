# BC-SKILL-015 — Error Macro Fail-Closed

## Trigger

Use when adding unsupported-command handling, blocked diagnostics, auth failures, validation failures, or dependency failures.

## Failure Pattern

A failure path turns into friendly prose, partial output, or a guessed alternative instead of a deterministic failure packet.

## Do

1. Return canonical error/fail-closed packets for unsupported or invalid routes.
2. Include failure_reason when terminal_state is invalid.
3. Keep failure output attributable to the selected owner or RuntimeGate.
4. Block support/mood/humor decoration on failures unless explicitly allowed.
5. Test negative paths as first-class routes.

## Do Not

- Do not apologize or explain outside the packet for deterministic routes.
- Do not suggest alternatives unless the command contract includes them.
- Do not mutate state after failure.
- Do not let errors become ordinary conversation.

## Validation

- Invalid routes fail closed consistently.
- Failure packet has owner, lane, executed_action, validation_result, terminal_state, and failure_reason.
- No extra prose appears after the failure line.
- State remains unchanged after failed mutation routes.

## Example

Good: `/simcode on` returns unsupported subcommand and stops; it does not enable SimCode or explain activation in conversational prose.
