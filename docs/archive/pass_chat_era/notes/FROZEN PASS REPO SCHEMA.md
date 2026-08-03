# FROZEN PASS REPO SCHEMA — PASTE BLOCK

## Frozen external object contract
Every normalized PASS output must resolve to the same external shape regardless of source type.

### Required objects
- pattern
- drill
- AP
- reference
- tags
- cross-links
- category
- subcategory
- stage_binding

### Optional objects
- variant
- modernization

## Frozen stage scaffold
`stage_binding` must use the canonical scaffold exactly:
- 0 design
- 1 skeleton
- 2 block
- 3 rough
- 4 final

## Frozen placement law
- Place extracted material where it conceptually belongs, not merely where it came from.
- Preserve source provenance through tags, references, and cross-links.
- Store foundational concepts in foundation-capable category/subcategory locations even when the source came from a narrow variant or source-specific bucket.
- Foundations are canonical reusable lanes from which variants emerge.
- Variants must inherit from foundations without duplicating the foundational object.
- Cross-domain reusable knowledge must not remain trapped inside a narrow source or variant bucket when a broader foundation exists.

## Frozen duplicate / merge law
- PASS output shape may not drift.
- Duplicate merges must preserve tags, provenance, and cross-links without inventing a new schema.

## Frozen index patch format
PASS must emit:
- subcategory index patch
- category index patch

Index patches must be:
- additive
- path-explicit
- concrete file-entry based when required
- not vague folder-only references

## Frozen repo-ready workflow
PASS repo integration must remain reducible to:
1. drop files
2. apply local index patches
3. add changelog entry
4. push

## Required repo-ready artifacts
PASS ingestion output must include:
- standardized library objects
- local index patches
- changelog-ready patch text

## Repo-drop bundle template
A repo-ready PASS run should package:
- source record
- normalized object files
- subcategory index patch
- category index patch
- changelog-ready run summary
- reject log
- zip bundle

## Stability law
- PASS internal logic may evolve.
- PASS external output shape may not drift.
- Uniform PASS outputs are required for dynamic SkillForge assembly and School sequencing.
- PASS must optimize for repeatable repo integration, not one-off packaging.

## Ownership boundary
- PASS owns conceptual placement and ingestion outputs.
- SkillForge consumes placed library objects but does not relocate them.
- School sequences placed library objects but does not redefine conceptual ownership.