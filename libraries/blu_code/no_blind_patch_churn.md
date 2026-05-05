# No blind patch churn

Date: 2026-05-04
Trigger: Blu repeatedly proposed patches across Exec, ExecLib, MoodLib, RibbonLib, PersonaLib, and Commands without locking a single recovery strategy.

## Mistake

Blu treated a live broken kernel as a patch target and kept changing layers without first anchoring source truth, rollback state, or one selected strategy.

## Verified symptom

Admin became stuck with overwritten build copies and no known-good current copy, while Mood behavior continued to regress.

## Rule

When a kernel subsystem breaks:
1. Stop patching.
2. Identify the active source files.
3. Preserve a baseline.
4. Decide whether the task is:
   - root rewrite
   - control fix
   - rollback/recovery
   - diagnostic only
5. Deliver complete files or a complete archive when replacements are requested.

Do not mix root fixes and control fixes in the same unmanaged sequence.
