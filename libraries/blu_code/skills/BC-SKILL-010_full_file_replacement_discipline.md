# BC-SKILL-010 — Full-File Replacement Discipline

## Trigger
Use when the user cannot or should not manually patch code fragments.

## Failure Pattern
Fragment edits are unclear, placed incorrectly, or overwrite good source.

## Do
1. Provide full replacement files when requested.
2. State exact files included.
3. Avoid partial snippets unless explicitly asked.
4. Preserve unrelated content.
5. Include a manifest and clear backup instruction.

## Do Not
- Do not say “add this somewhere.”
- Do not provide fragments after the user asked for full files.
- Do not mix patch strategies midstream.
- Do not include extra files outside the locked scope.

## Validation
- User can replace files without manual merging.
- Archive contains only intended files.
- Manifest matches actual contents.

## Example
Bad:
“Paste this block near validation.”

Good:
Archive contains full `03_Exec.md` based on the user’s uploaded file.
