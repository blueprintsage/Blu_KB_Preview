# PROGRAM.SkillForge.Validator.v1 — Spec — v1.0.0

CAPSULE HEADER v1.1 (NO-YAML)
capsule_id: blu__skillforge_validator_v1
title: PROGRAM.SkillForge.Validator.v1 — Spec
date: 2026-03-05
updated: 2026-03-05
version: 1.0.0
status: active
topic: skillforge
type: spec
tags: [skillforge, validator, uniformity, schema]
sensitivity: high
visibility: shared
source: doc
domain: skillforge
schema: capsule_header_block_v1.1
body_schema: blu_modular_v1
END CAPSULE HEADER

module: blu__sfval.M01 | name="Purpose (HARD)"
Validate uniform SkillForge outputs before packing/zip/registry:
- object schema fields present
- quote ban
- dual-lane layout present
- required files present (patterns/drills/aps/etc.)
/module

module: blu__sfval.M02 | name="Required checks (HARD)"
Lane B content rules:
- patterns.md items must include IF/THEN/BECAUSE/CHECK
- drills.md items must include GOAL/INPUTS/STEPS/OUTPUT/RUBRIC_PASS
- aps.md items must include TRIGGER/PROCEDURE/DONE_DEFINITION

Layout rules:
- `skills/<domain>/<subskill>/...` exists
- `teaching/<domain>/<subskill>/...` exists

On failure: return `ERR:SKILLFORGE_SCHEMA_VIOLATION` or `ERR:PACK_DUAL_LANE_FAILED`.
/module
