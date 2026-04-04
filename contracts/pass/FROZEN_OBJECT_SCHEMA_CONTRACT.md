# Frozen Object Schema Contract
updated: 2026-04-03
tz: America/Chicago
status: canon
version: 1.0

## Purpose
Define the locked external PASS object shape used after harvest.
This is the normalization target for Stage 3+.
This contract is media-agnostic.
Different ingest lenses are allowed upstream, but all kept outputs must normalize here.

## Object families
- pattern
- drill
- ap

## Global laws
- One kept object = one top-level object file.
- One kept object = one primary conceptual home.
- Variants attach to the parent object through `variants[]`.
- Tags widen applicability; they do not change ownership.
- Cross-links must be typed.
- PASS may not invent one-off object shapes to save malformed findings.
- If a kept finding cannot normalize to this contract, it must be rejected or remain a partial-stage result.

## Required common fields
- object_id
- object_type
- name
- category
- subcategory
- stage_binding
- lane_fit
- foundation_role
- tags[]
- cross_links[]
- reference
- confidence
- variants[]

## Allowed values
### object_type
- pattern
- drill
- ap

### stage_binding
- 0 design
- 1 skeleton
- 2 block
- 3 rough
- 4 final

### lane_fit
- teach
- skill
- both
- teaching_foundation

### foundation_role
- foundation
- specialization

### confidence
- low
- medium
- high

## reference object
Required fields:
- source_id
- source_title
- author
- publish_date
- media_type
- locator
- evidence_type

Allowed evidence_type:
- text
- image
- mixed

## cross_links[] entry shape
Each entry must include:
- rel
- target_object_id

Allowed rel values:
- foundation_of
- variant_of
- prerequisite_for
- supports
- related_to
- teaches
- skill_pair
- teaching_foundation_for

## Pattern required body fields
- pattern_rule.if
- pattern_rule.then
- pattern_rule.else (optional)
- do[]
- dont[]
- checklist[]

## Drill required body fields
- practice_task
- target_skill
- success_check[]

Optional drill body fields:
- setup
- instructions[]
- common_failures[]
- do[]
- dont[]
- checklist[]

## AP status
AP remains provisional at the content level, but APs must still normalize into the same outer shape.

AP required body fields:
- objective
- steps_or_flow
- notes

## Variants
`variants[]` is optional but, when present, each entry must include:
- name
- lane_fit
- tags[]
- use_when

Variant body then follows the parent family:
- pattern variant -> pattern-like payload
- drill variant -> drill-like payload
- ap variant -> ap-like payload

## Failure rule
If Stage 3 cannot normalize harvested findings to this contract, PASS must stop and label the run as partial-stage rather than claiming full compilation success.