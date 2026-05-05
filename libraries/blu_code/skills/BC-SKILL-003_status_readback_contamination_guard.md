# BC-SKILL-003 — Status-Readback Contamination Guard

## Trigger
Use when a command prints valid-looking but wrong status prose copied by pattern from another command.

## Failure Pattern
The model generalizes from another command’s readback template and fabricates a plausible output.

## Do
1. Identify similar command families with readback output.
2. Add explicit forbidden outputs for the affected command.
3. State that the affected command is not a status query when relevant.
4. Add a test that blocks the fabricated readback pattern.
5. Revalidate the command across modes/states.

## Do Not
- Do not treat plausible prose as successful command execution.
- Do not rely on absence of source-grounding as proof of correct routing.
- Do not share readback templates across commands unless authorized.

## Validation
- The command never prints borrowed readback phrasing.
- The command output matches its exact contract.
- Mode/state changes do not alter the command’s output class.

## Example
Bad:
`Mood display is currently set to smart.`

Good:
`[MOOD] Steady 💙`
