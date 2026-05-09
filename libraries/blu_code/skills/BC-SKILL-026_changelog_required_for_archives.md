# BC-SKILL-026 — Changelog Required for Archives

## Trigger

Use whenever Blu creates a new archive, patch package, release package, kernel package, BluCode package, Error_Macros package, or any artifact that contains changed kernel/governance source.

## Failure Pattern

The assistant ships an `EVIDENCE.zip`, manifest, summary, or final-chat explanation instead of including the required `CHANGELOG.md` in the archive.

This loses release continuity and makes later package comparison harder.

## Do

1. Include `CHANGELOG.md` in every newly generated archive that contains changed kernel/governance source.
2. Use the repository changelog template when it is present in the active source tree.
3. If the template is not present in the provided source, include a conservative `CHANGELOG.md` with:
   - package name
   - date
   - source baseline
   - changed files
   - change summary
   - validation performed
   - known limitations
4. Treat an evidence bundle as supplemental only.
5. Validate the generated archive contains `CHANGELOG.md` before linking it.
6. If multiple archives are produced, each archive must carry its own changelog.

## Do Not

- Do not substitute `EVIDENCE.zip` for `CHANGELOG.md`.
- Do not rely on the chat response as the changelog.
- Do not claim release/package completion if the required changelog is missing.
- Do not invent use of a repo template if the template was not present in the accessible source.

## Validation

- Archive inventory contains `CHANGELOG.md`.
- `CHANGELOG.md` lists the baseline/source archive.
- `CHANGELOG.md` lists all modified source files.
- `CHANGELOG.md` states validation performed and known limitations.
- Evidence artifacts, if any, are separate from and subordinate to the changelog.

## Example

Good: `PATCHED_KERNEL.zip` contains `CHANGELOG.md`, changed kernel files, and optional validation notes.

Bad: `PATCHED_KERNEL.zip` is delivered with only an external `EVIDENCE.zip` and no changelog inside the patched archive.
