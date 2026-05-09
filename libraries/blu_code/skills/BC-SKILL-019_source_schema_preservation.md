# BC-SKILL-019 — Source Schema Preservation

## Trigger
Modifying repo-local structured artifacts, skill cards, indexes, manifests, changelogs, archives, registries, or any artifact with an established local format/style.

## Failure Pattern
Existing artifacts are rewritten into a generalized schema, normalized template, representative replacement, or abstracted format that does not match the local source style.

The semantic content may remain similar while the artifact identity is silently replaced.

## Do
Preserve the exact repo-local structure, style, headings, field order, naming pattern, numbering behavior, and operational cadence unless explicitly instructed to replace them.

Use neighboring artifacts as schema truth.

Treat local format/style as part of the artifact itself.

Patch minimally.

Validate numbering, references, archive completeness, and package integrity before publishing replacements.

## Do Not
Do not modernize, normalize, summarize, or re-template existing artifacts.
Do not rewrite operational field-manual style into generalized metadata/spec style.
Do not generate “close enough” replacements.
Do not rebuild indexes or archives from memory.
Do not infer numbering without checking the actual source set.
Do not replace artifact identity with semantically similar structure.

## Validation
The modified artifact still matches local format/style.
Existing file identities are preserved.
Referenced files exist.
No duplicate IDs or numbering collisions are introduced.
Archive contents match changelog claims.
Package structure remains intact.
A side-by-side comparison with neighboring artifacts shows schema continuity.

## Example
Bad:
Rewriting BluCode cards into metadata-heavy spec blocks with a different structure and cadence.

Bad:
Generating replacement archives that omit required files such as `INDEX.md`.

Good:
Creating a new BluCode card using the same operational field-manual structure, numbering style, and section ordering as the surrounding cards.