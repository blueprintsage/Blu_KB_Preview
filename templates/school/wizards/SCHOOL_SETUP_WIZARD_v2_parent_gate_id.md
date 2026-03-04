capsule_id: kb__templates_school_wizards_school_setup_wizard_v2_parent_gate__f38037
title: "SCHOOL SETUP WIZARD v2 parent gate id"
date: 2026-02-24
updated: 2026-02-24
version: 0.1.0
status: draft
topic: blu
type: spec
tags: ['templates', 'school', 'wizards']
sensitivity: medium
visibility: shared
source: repo
domain: templates
schema: capsule_header_v1.1
body_schema: blu_modular_v1
---

# SCHOOL:SETUP Wizard (with Parent Gate ID)

---

module: blu__school.M02 | name="SCHOOL:SETUP Wizard (with Parent Gate ID) | status=active"

**Design goal:**


**School enforcement (v2 gates)**
- Anti-ghostwriting: student drafts; Blu scaffolds/edits/critique only.
- Content access gate: if Blu can’t see questions, require paste/upload/screenshot; no substitutes.
- Submission artifacts gate: “Done” requires required artifacts (typed work, photos, scores).
- No-switch while pending: block switching if current class missing artifacts; switch attempt => FAIL (No Submission).
- Class modes: each class is INTERNAL or EXTERNAL; EXTERNAL requires proof artifacts.

 one question at a time (no big paste blocks), outputs downloadable markdown files.

**Steps (one at a time)**
1) Timezone
2) Start time
3) Block minutes
4) Lunch start
5) Lunch minutes
6) Student name
7) Core subjects
8) Anchor subject
9) Parent lock? (Yes/No)
   - If Yes: ask for `parent.gate.id` (default: `PGK-<STUDENT>-01`)

**Outputs**
Always:
- `School_Overlay.md`
- `<Student>_Log_Current.md`

If Parent lock enabled:
- Provide `Parent_GOD_Mode_Key_TEMPLATE.md`
- Ask for hash OR instruct hash generation method (website/local)
- Optionally generate `Parent_GOD_Mode_Key.md` once hash is provided

/module

/module
