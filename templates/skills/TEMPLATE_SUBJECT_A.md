---
capsule_id: teaching.<domain>.<subject>.A
title: "Teaching — <SUBJECT> (Lane A)"
date: 2026-03-03
updated: 2026-03-03
version: 0.1.0
status: template
topic: teaching
type: skill_lane_a_template
tags: [<domain>, <subject>]
visibility: shared
schema: capsule_header_v1.1
body_schema: blu_modular_v1
---

# Teaching — <SUBJECT> (Lane A)

module: teaching.<domain>.<subject>.a.meta | name="META"
- purpose: human-facing teaching pack for this subject
- scope: <one sentence>
- spine: ["Skeleton","Block","Rough","Final"]
- uses_lane_b:
  - relative_path: ../Skills/<SUBJECT>_B.md
  - patterns_as_laws: true
/module

module: teaching.<domain>.<subject>.a.lesson_map | name="LESSON MAP"
- outcomes: []
- prerequisites: []
- sequence: ["Skeleton","Block","Rough","Final"]
/module

module: teaching.<domain>.<subject>.a.core_explanations | name="CORE EXPLANATIONS"
- Explain concepts in plain language. Examples allowed.
- Reference Lane B Pattern IDs where relevant.
/module

module: teaching.<domain>.<subject>.a.patterns | name="PATTERNS (HUMAN-FACING)"
Recommended fields:
- id: <PatternID from Lane B>
- plain_language:
- how_to_apply:
- self_check:
/module

module: teaching.<domain>.<subject>.a.drills | name="DRILLS (HUMAN)"
Required fields per drill:
- id:
- targets: [pattern_ids]
- goal:
- setup:
- steps:
- time/reps:
- pass/fail:
- common_fails:
- scaling:
/module

module: teaching.<domain>.<subject>.a.aps | name="APs (HOW-TO USE)"
Recommended fields:
- id:
- when_to_use:
- steps:
- self_check:
/module

module: teaching.<domain>.<subject>.a.ledger | name="LEDGER"
- 2026-03-03: template created
/module
