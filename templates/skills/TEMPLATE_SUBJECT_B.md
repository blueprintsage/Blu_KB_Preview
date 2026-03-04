---
capsule_id: skill.<domain>.<subject>.B
title: "Skills — <SUBJECT> (Lane B)"
date: 2026-03-03
updated: 2026-03-03
version: 0.1.0
status: template
topic: skills
type: skill_lane_b_template
tags: [<domain>, <subject>]
visibility: shared
schema: capsule_header_v1.1
body_schema: blu_modular_v1
---

# Skills — <SUBJECT> (Lane B)

module: skill.<domain>.<subject>.b.meta | name="META"
- purpose: machine-facing canonical ruleset for execution + anti-drift
- scope: <one sentence>
- spine: ["Skeleton","Block","Rough","Final"]
- notes:
  - Patterns are laws (IF/THEN).
  - Tests prove patterns.
  - Drills build coverage.
  - APs are callable procedures.
/module

module: skill.<domain>.<subject>.b.patterns | name="PATTERNS (LAWS)"
Required fields per pattern:
- id:
- IF:
- THEN:
- CHECK:
- FAIL:
- NOTES:
- REF: (source pointer; no quotes)
/module

module: skill.<domain>.<subject>.b.tests | name="TESTS"
Required fields per test:
- id:
- targets: [pattern_ids]
- setup:
- steps:
- pass:
- fail:
- notes:
/module

module: skill.<domain>.<subject>.b.drills | name="DRILLS (MACHINE)"
Required fields per drill:
- id:
- targets: [pattern_ids]
- inputs:
- procedure:
- scoring: (or pass/fail)
- stop:
- notes:
/module

module: skill.<domain>.<subject>.b.aps | name="APs"
Required fields per AP:
- id:
- trigger:
- inputs:
- procedure:
- checks:
- fails:
- targets: [pattern_ids] (optional)
/module

module: skill.<domain>.<subject>.b.ledger | name="LEDGER"
- 2026-03-03: template created
/module
