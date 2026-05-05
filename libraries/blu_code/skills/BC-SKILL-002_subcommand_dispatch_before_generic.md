# BC-SKILL-002 — Subcommand Dispatch Before Generic Handling

## Trigger
Use when a command family has multiple subcommands with different behavior.

## Failure Pattern
A specific subcommand is recognized but handled by a generic branch.

## Do
1. Parse the exact subcommand first.
2. Dispatch unique subcommands before generic status/readback/default handlers.
3. Keep state-setting commands separate from render/read/execute commands.
4. Give special subcommands their own entrypoint.
5. Add tests for every subcommand.

## Do Not
- Do not let `show`, `status`, `list`, or empty subcommand share a handler unless their behavior is identical.
- Do not allow fallthrough from exact-match branches.
- Do not infer subcommand meaning from similar command families.

## Validation
- Each subcommand maps to exactly one entrypoint.
- `show` cannot enter state-setting or status-readback branches.
- State commands commit state and print confirmation only.
- Render commands render only their deterministic output.

## Example
Bad:
`/mood show` prints the current mode.

Good:
`/mood show` force-renders the mood line.
