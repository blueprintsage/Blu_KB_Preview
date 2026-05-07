# BC-SKILL-013 — Full-File Replacement Discipline

## Trigger

Use when patch placement is risky, files are small enough to replace, or the user asks for a complete rewrite.

## Failure Pattern

Small text patches land in the wrong section, duplicate blocks, leave stale residue, or create contradictory contracts.

## Do

1. Read the target structure before editing.
2. Prefer full-file replacement for small/medium deterministic specs with heavy structural change.
3. Remove stale blocks instead of layering exceptions around them.
4. Run duplicate-owner and forbidden-token scans after replacement.
5. Include a diff/manifest summary.

## Do Not

- Do not regex-patch unknown structure.
- Do not leave deprecated owner names near active route maps.
- Do not preserve old examples that contradict new architecture.
- Do not claim full rewrite when only fragments changed.

## Validation

- No duplicate owners, stale route maps, or contradictory examples remain.
- File headings and metadata still match the project style.
- Validation report includes removed residue.
- Downstream indexes are updated when filenames change.

## Example

Bad: Patch around `EXEC.MOOD` in three places.

Good: Replace the relevant Exec section and remove every stale `EXEC.MOOD` owner reference.
