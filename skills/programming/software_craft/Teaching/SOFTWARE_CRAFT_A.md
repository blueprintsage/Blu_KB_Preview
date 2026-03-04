---
capsule_id: teaching.programming.software_craft.A
title: "Teaching — Software Craft (Lane A)"
date: 2026-03-03
updated: 2026-03-03
version: 0.1.0
status: draft
topic: teaching
type: skill_lane_a
tags: [programming, software_craft]
visibility: shared
schema: capsule_header_v1.1
body_schema: blu_modular_v1
sources:
  - pragmatic_programmer
  - passionate_programmer
---

# Teaching — Software Craft (Lane A)


module: teaching.programming.software_craft.a.meta | name="META"
- purpose: teach software craft habits and professional practice
- spine: ["Skeleton","Block","Rough","Final"]
- lane_b_ref: ../Skills/SOFTWARE_CRAFT_B.md
/module


module: teaching.programming.software_craft.a.lesson_map | name="LESSON MAP"
- outcomes:
  - develop habits that reduce defects and rework
  - communicate with options and assumptions
  - maintain code health continuously
- sequence:
  1) Skeleton: intent + constraints + options
  2) Block: safe structure (boundaries, tests, automation)
  3) Rough: refine design; reduce duplication; refactor safely
  4) Final: ship with proof + checklist
/module


module: teaching.programming.software_craft.a.core_explanations | name="CORE EXPLANATIONS"
- Foundation: STRUCTURE in software means correctness + maintainability + observability.
- Patterns are laws; use them as the referee when deciding what to do next.
- When a result is "off," correct structure first: constraints, tests, boundaries, automation.
/module


module: teaching.programming.software_craft.a.patterns | name="PATTERNS (REFERENCE)"
- Use Lane B pattern IDs as law references.
- Start with these: SC-PAT-001, SC-PAT-002, SC-PAT-020, SC-PAT-030, SC-PAT-040, SC-PAT-060, SC-PAT-070.
/module



module: teaching.programming.software_craft.a.drills | name="DRILLS (HUMAN)"
### SC-DRILL-A-001
- targets: ['SC-PAT-001', 'SC-PAT-080']
- goal: Turn ambiguity into actionable options.
- setup: Pick one unclear requirement.
- steps: Write assumptions; propose 2 options with tradeoffs; ask one clarifying question.
- time/reps: 15 minutes
- pass/fail: PASS if options+tradeoffs+assumptions are written and a question is asked.
- common fails: Skipping assumptions; offering only one option.
- scaling: Easier: do with a small task. Harder: do with a multi-stakeholder task.

### SC-DRILL-A-002
- targets: ['SC-PAT-020']
- goal: Detect and remove duplication.
- setup: Choose a function duplicated in two places.
- steps: Refactor to one source; update call sites; confirm behavior.
- time/reps: 30–60 minutes
- pass/fail: PASS if duplication removed and behavior preserved.
- common fails: Refactoring without validating behavior.
- scaling: Easier: small helper. Harder: cross-module duplication.

### SC-DRILL-A-003
- targets: ['SC-PAT-040', 'SC-PAT-041']
- goal: Make changes safe with tests.
- setup: Pick a recent bug or change.
- steps: Reproduce; write failing test; fix; keep test.
- time/reps: 45 minutes
- pass/fail: PASS if test fails before fix and passes after.
- common fails: Writing tests after fixing.
- scaling: Easier: pure function. Harder: integration bug.

/module

module: teaching.programming.software_craft.a.aps | name="APs (HOW TO USE)"
- Use the Lane B APs during real work:
  - SC-AP-001 (ambiguity/options)
  - SC-AP-002 (bug fix with regression proof)
  - SC-AP-003 (merge checklist)
/module


module: teaching.programming.software_craft.a.ledger | name="LEDGER"
- 2026-03-03: initial teaching pack created to accompany Lane B
/module
