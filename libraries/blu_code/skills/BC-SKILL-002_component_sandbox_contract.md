# BC-SKILL-002 — Component Sandbox Contract

## Trigger

Use when creating or rewriting any Program, service, library, renderer, or deterministic support component.

## Failure Pattern

A component has fuzzy boundaries: it reads ambient state, mutates state directly, prints directly, continues after failure, or depends on hidden fallback behavior.

## Do

1. Give every component one owned job, one entry boundary, and one terminal boundary.
2. Validate input before doing owned work.
3. Call declared dependencies only through packet bridges.
4. Return a success packet, explicit failure packet, or BLOCKED packet.
5. Stop after returning; never continue into prose or another owner by implication.

## Do Not

- Do not print directly from a component.
- Do not mutate state directly; propose state_delta for Egress/Exec commit.
- Do not call undeclared dependencies.
- Do not use partial success as permission to continue.

## Validation

- Every callable entrypoint has input requirements, output packet fields, and failure reasons.
- Invalid input stops inside the component and returns a failure packet.
- Dependency failure stops the parent chain unless an explicit alternate branch exists.
- State changes appear only as proposed deltas.

## Example

Bad: Reminder parses time, writes memory, and prints confirmation.

Good: Reminder parses input, calls Time/Date/Reminder libs as needed, returns a terminal packet plus state_delta, and stops.
