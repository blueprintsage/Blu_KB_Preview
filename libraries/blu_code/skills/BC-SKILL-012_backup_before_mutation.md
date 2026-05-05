# BC-SKILL-012 — Backup Before Mutation

## Trigger
Use before generating or applying any replacement file, archive, or kernel change.

## Failure Pattern
A working copy is overwritten and cannot be recovered.

## Do
1. Preserve the uploaded source as baseline.
2. Name generated archives with date and purpose.
3. Include only changed files.
4. Recommend backup before replacement.
5. Never overwrite user files in place without a separate artifact.

## Do Not
- Do not assume the user has version control.
- Do not hand out partial indexes that overwrite full indexes.
- Do not create archives that look complete but contain only fragments.

## Validation
- Original source remains available.
- Replacement artifact is separate.
- Index files are full merged files unless clearly labeled as fragments.

## Example
Bad:
Archive contains a one-entry `INDEX.md` that overwrites the full BluCode index.

Good:
Archive contains a full merged `INDEX.md` with all retained entries.
