# Day 125 — Completion Gate Regression (2026-02-25)

## Summary
A regression was observed where a student could advance to the next class without completing the current work. A grading command produced an official-looking grade for partial completion.

## Patch Direction
### Completion Gate (per class/task)
Add state:
- active_class
- active_task_id
- task_status: active|submitted|graded|complete
- advance_policy: require_complete (default ON)

Rule:
- If task_status != complete, block switching classes.
- Allow: HINT / CHECK / SUBMIT / PAUSE.

### Separate Practice vs Graded Mode
Add mode:
- practice: generated problems; no official grades
- graded: only explicit student submissions count

Rule:
- GRADE:* only grades explicit submissions in graded mode.

## Burn-In Tests
1) Attempt switch class before complete → blocked.
2) Practice problems present → GRADE:ALL returns "Ungraded: practice-only".
3) Explicit submission → graded with rubric.
