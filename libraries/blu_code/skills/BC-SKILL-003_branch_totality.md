# BC-SKILL-003 — Branch Totality

## Trigger

Use when a component has multiple paths, dependency calls, optional features, or error handling.

## Failure Pattern

The code has a happy path but leaves a missing `else`, unknown state, or implicit fallthrough where GPT/completion can improvise the rest.

## Do

1. Make every decision total: success path, alternate path, blocked path, or failure path.
2. Use nested branches when needed; complexity is allowed if every branch terminates.
3. Name the branch taken in trace output when the lane is deterministic.
4. Return a packet for every terminal branch.

## Do Not

- Do not rely on comments, examples, or surrounding prose to define missing branches.
- Do not allow a failed dependency to fall through to a synthesized answer.
- Do not treat `unknown` as success.
- Do not continue after a terminal branch.

## Validation

- Each conditional has a defined terminal behavior.
- Unexpected inputs return explicit failure or unsupported-command packets.
- Trace/diag can identify the branch taken.
- No branch requires ordinary completion to finish the response.

## Example

Good shape: `IF input valid THEN execute owned step ELSEIF dependency blocked THEN return BLOCKED ELSE fail closed`.

The exact words do not need to appear in the file; the behavior must be total.
