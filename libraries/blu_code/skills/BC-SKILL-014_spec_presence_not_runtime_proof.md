# BC-SKILL-014 — Spec Presence Is Not Runtime Proof

## Trigger

Use whenever a file, registry, module, Program, service, route, or command appears in source.

## Failure Pattern

The model treats a declared module, registry entry, or help listing as proof that the route is live and working.

## Do

1. Classify source presence, static validation, SimCode probe, and live route proof separately.
2. Require route ownership proof for execution claims.
3. Require artifact/file proof for export claims.
4. Require state readback for mutation claims.
5. Name `not checked` when proof is absent.

## Do Not

- Do not say a feature works because it is listed.
- Do not use `/help` success as command execution proof.
- Do not infer runtime ownership from registry adjacency.
- Do not blur static proof with live proof.

## Validation

- Response distinguishes what was read from what was executed.
- Completion claims cite the actual proof type.
- Missing proof is marked BLOCKED, SKIPPED, or not checked.
- Live route matrices include observed output.

## Example

Bad: `/help MOOD` lists canonical output, so `/mood show` must work.

Good: `/help MOOD` proves docs; `/mood show` and `/echotrace Mood` prove execution.
