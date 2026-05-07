# BC-SKILL-009 — Probe-First SimCode

## Trigger

Use before declaring any deterministic route, component rewrite, artifact/export, or runtime patch complete.

## Failure Pattern

A patch reads correctly but fails live because no probe tested the handoff, output shape, forbidden legacy output, or failure branch.

## Do

1. Ship a minimal probe pack with the change.
2. Probe the smallest callable contract first.
3. Add a pipeline/handoff probe when multiple components exchange packets.
4. Add forbidden-output probes for known legacy formats.
5. Run the probe board before claiming completion.

## Do Not

- Do not treat unit green as runtime green.
- Do not treat static file scans as live route proof.
- Do not hide BLOCKED as PASS.
- Do not claim file creation/export/load worked without artifact proof.

## Validation

- Every changed deterministic entrypoint has a contract probe.
- Every public renderer has an exact shape probe and forbidden legacy probe.
- Every expected failure has a terminal failure packet probe.
- Probe output reports PASS/FAIL/BLOCKED/SKIPPED distinctly.

## Example

Mood probe minimum: `/mood show` exact shape, `/mood on` exact confirmation, ordinary-turn containment, forbidden `Mood:` prefix, and `/echotrace Mood` chain proof.
