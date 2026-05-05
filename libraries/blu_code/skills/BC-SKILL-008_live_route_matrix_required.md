# BC-SKILL-008 — Live Route Matrix Required

## Trigger
Use after any change touching Exec, ExecLib, Commands, Programs, routing, gates, or command output.

## Failure Pattern
A spec appears correct but fails in live command behavior.

## Do
1. Build a route matrix before declaring success.
2. Test every affected command/subcommand.
3. Include state variations.
4. Include negative/fail-closed tests.
5. Record observed output exactly.

## Do Not
- Do not call a patch stable because the file reads correctly.
- Do not skip live tests after route/gate changes.
- Do not test only the happy path.

## Validation
- Every route in the matrix returns expected output.
- No unexpected prose or source answer appears.
- State changes persist and affect later turns correctly.

## Example Matrix
- `/mood show`
- `/mood on`
- ordinary turn after `/mood on`
- `/mood circles`
- `/mood show`
- `/mood squares`
- `/mood show`
