# BC-SKILL-016 — Artifact Claim Proof

## Trigger

Use when a route creates, patches, packages, exports, loads, or links an artifact.

## Failure Pattern

The assistant claims an archive or file was created/loaded/patched without verifying existence, contents, or linkability.

## Do

1. Verify the artifact path exists before linking.
2. Verify required files are present in archives.
3. Generate a manifest and validation report for build artifacts.
4. Separate static validation from live route testing.
5. Never claim live deployment when only a local artifact was produced.

## Do Not

- Do not link nonexistent files.
- Do not claim a repo push without real repo write access.
- Do not claim loaded/active runtime unless the route actually loaded it.
- Do not treat upload presence as internal content proof.

## Validation

- Artifact links resolve.
- Archive contains expected files.
- Manifest lists baseline, changed files, unchanged protected files, and checksums when practical.
- Final response states not live-tested when live testing did not occur.

## Example

Good: Exported zip exists, contains changed files and validation report, and final answer says `Not live-tested yet`.
