# BC-SKILL-011 — One-Seam Fix Discipline

## Trigger
Use when repeated patches are causing regressions or confusion.

## Failure Pattern
Multiple layers are changed at once, making the real failure harder to isolate.

## Do
1. Identify the single most likely seam.
2. Change only that seam.
3. Test before touching adjacent layers.
4. If the test fails, inspect actual active files/output before another change.
5. Stop patching when the diagnosis changes.

## Do Not
- Do not patch Exec, ExecLib, Persona, Commands, and Programs together unless the route matrix requires it.
- Do not change libraries when the command is not reaching them.
- Do not change render logic when dispatch is wrong.

## Validation
- The patch scope matches the diagnosed seam.
- Test result confirms or falsifies the seam.
- No unrelated subsystem behavior changes.

## Example
Bad:
Fix MoodLib when `/mood show` is being captured by source answering.

Good:
Fix first-read command routing first.
