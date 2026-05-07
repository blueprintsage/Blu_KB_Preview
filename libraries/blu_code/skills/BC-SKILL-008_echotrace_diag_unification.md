# BC-SKILL-008 — EchoTrace / Diag Unification

## Trigger

Use when adding diagnostics, probes, `/echotrace`, `/diag`, `/tracert`, or owner-level proof.

## Failure Pattern

Diag and trace split into separate systems that disagree, or global trace pretends to know internal owner truth it did not inspect.

## Do

1. Treat trace/diag as one concept: packet proof across boundaries.
2. Exec trace proves route lock, owner selection, packet handoff, and Egress decision.
3. Owner trace proves input validation, branch taken, dependency calls, output packet, and failure reason.
4. Expose public trace by lead alias; show internal dependencies as steps.
5. Return BLOCKED when instrumentation cannot prove a field.

## Do Not

- Do not claim live behavior from source/static trace.
- Do not treat module presence as route execution proof.
- Do not hide missing instrumentation behind PASS.
- Do not create separate diagnostic stories that can contradict each other.

## Validation

- `/echotrace {ALIAS}` walks the full owner chain to terminal packet decision.
- Trace results distinguish PASS, FAIL, BLOCKED, and SKIPPED.
- Failure output names the boundary to patch next.
- `/DevMode tracert` remains source/static proof only if kept.

## Example

Good: `/echotrace Mood` reports Ingress lock, Scheduler owner, RibbonLib result, MoodLib result, MoodService packet, and Egress render decision.
