# BC-SKILL-010 — Live Route Matrix Required

## Trigger

Use after any change touching Exec, ExecLib, Commands, Programs, routing, gates, state, command output, or support decoration.

## Failure Pattern

A build is called stable because the source reads correctly or SimCode unit probes pass, but live route behavior has not been observed.

## Do

1. Build a route matrix before declaring success.
2. Test every affected command/subcommand.
3. Include state variations and negative/fail-closed tests.
4. Record observed output exactly.
5. Separate static validation, SimCode probes, and live hosted results.

## Do Not

- Do not call a patch green from static checks alone.
- Do not test only the happy path.
- Do not skip live hosted checks when the bug was live hosted behavior.
- Do not merge if expected output and observed output diverge.

## Validation

- Matrix lists command, expected output, observed output, status, and notes.
- Failures identify the likely owner boundary.
- No unexpected prose, source answer, mood/humor decoration, or fallback appears.
- State changes persist only when Egress commits them.

## Example

Good matrix row: `/simcode echotrace all` expected unsupported subcommand; observed unsupported subcommand; PASS; proves invalid delegation stayed blocked.
