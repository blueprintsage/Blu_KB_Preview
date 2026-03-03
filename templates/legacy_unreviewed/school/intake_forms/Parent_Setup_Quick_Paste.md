capsule_id: kb__templates_school_intake_forms_parent_setup_quick_paste_md__fc7c28
title: "Parent Setup Quick Paste"
date: 2026-02-24
updated: 2026-02-24
version: 0.1.0
status: draft
topic: blu
type: spec
tags: ['templates', 'school', 'intake-forms']
sensitivity: medium
visibility: shared
source: repo
domain: templates
schema: capsule_header_v1.1
body_schema: blu_modular_v1
---

module: templates.school.copypasta.M02 | name="Parent Setup (1 kid) — quick paste"

## Parent Setup (1 kid) — quick paste

1) Choose student log file name:
- `<StudentName>_Log_Current.md` (one file, overwritten daily)

2) In the student log set:
- subjects.core: <Subject 1> | <Subject 2> | <Subject 3> | <Subject 4> | <Subject 5>
- school.day_ends_on: <anchor subject>

3) Each morning:
- Load/paste the student log → run `SCHOOL:START`

4) Each class:
- Student uses “HS Class Paste (student)” template.

/module
