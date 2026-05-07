# BC-SKILL-006 — Dependency Chain Stop Rule

## Trigger

Use when a Program/service/library calls another component.

## Failure Pattern

A parent continues after a child dependency failed, returned partial data, returned malformed data, or was not actually called.

## Do

1. Declare dependency names and expected packet fields.
2. Call dependencies only after the parent input contract passes.
3. Validate dependency packets before using their data.
4. Stop the parent chain if a required dependency fails or is BLOCKED.
5. Record the dependency result in trace/diag.

## Do Not

- Do not infer dependency output from spec text.
- Do not use stale state when same-turn proof is required.
- Do not skip a dependency because the expected result seems obvious.
- Do not convert dependency failure into a smooth user answer.

## Validation

- Parent trace shows every required dependency call.
- Missing or invalid dependency output blocks the parent packet.
- Optional dependencies have explicit alternate branches.
- Failure reason names the dependency boundary.

## Example

Remind example: `IF Time packet passes THEN DateLib/ReminderLib may compute due state ELSE Remind returns failure/BLOCKED and stops.`
