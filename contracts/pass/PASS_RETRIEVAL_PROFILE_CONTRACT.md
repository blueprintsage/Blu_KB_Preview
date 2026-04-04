# PASS Retrieval Profile Contract
updated: 2026-04-03
tz: America/Chicago
status: canon
version: 1.0

## Purpose
Define the lightweight machine-search layer SkillForge uses before opening full object files.

## Storage law
Retrieval profiles live under:
`indexes/retrieval/skills/<Category>/<Subcategory>/`

## Global laws
- One top-level object gets one retrieval profile.
- Attached variants do not become separate top-level profiles by default.
- Variants stay inside the parent profile as `variant_profiles[]`.
- Markdown object files remain canonical content.
- Retrieval JSON remains canonical runtime lookup.
- SkillForge must query manifest first, then selected profiles, then selected markdown objects.

## Object profile required fields
- profile_schema_version
- profile_id
- object_id
- object_type
- name
- slug
- category
- subcategory
- primary_home_path
- lane_fit
- foundation_role
- stage_binding
- tags[]
- cross_links[]
- variant_profiles[]
- reference_summary
- confidence

## reference_summary required fields
- source_id
- source_title
- media_type
- evidence_type
- locator_summary

## cross_links[] entry shape
Required:
- rel
- target_object_id
- target_category
- target_subcategory
- target_profile_path

## variant_profiles[] entry shape
Required:
- name
- lane_fit
- tags[]
- use_when

## Subcategory manifest required fields
- manifest_schema_version
- category
- subcategory
- manifest_path
- primary_home_path
- object_counts
- objects[]
- updated

## objects[] entry shape
Required:
- object_id
- object_type
- name
- slug
- profile_path
- lane_fit
- foundation_role
- stage_binding
- tags[]
- confidence

## Runtime law
SkillForge retrieval order:
1. exact subcategory candidates
2. parent foundations
3. attached variants
4. typed cross-linked supports
5. cross-domain tag neighbors
6. ask one clarifying question when material ambiguity remains