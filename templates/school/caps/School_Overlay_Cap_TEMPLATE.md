capsule_id: kb__templates_school_caps_school_overlay_cap_template_md__032662
title: "School Overlay Cap TEMPLATE"
date: 2026-02-24
updated: 2026-02-24
version: 0.1.0
status: draft
topic: blu
type: spec
tags: ['templates', 'school', 'caps']
sensitivity: medium
visibility: shared
source: repo
domain: templates
schema: capsule_header_v1.1
body_schema: blu_modular_v1
---

# School Overlay Cap (SIGNED, HMAC) — TEMPLATE

---

module: cap.school_overlay.M01 | name="School Overlay Cap (SIGNED, HMAC) — TEMPLATE"

overlay.id: <FAMILY_SLUG>__school_overlay
overlay.version: 1.1
overlay.tz: <TZ>

school.start_time: 08:00
school.block_minutes: 45
school.checkpoints: 10, 20, 35
school.exit_ticket: 44
school.strict_checkpoints: true

school.lunch_start: 12:00
school.lunch_minutes: 60

school.day_ends_on: <Anchor Subject>

school.electives.enabled: true
school.electives.count: 0
school.electives.list: <Elective A> | <Elective B>

school.subjects.core: <Subject 1> | <Subject 2> | <Subject 3> | <Subject 4> | <Subject 5>

grading.scale: A 90-100 | B 80-89 | C 70-79 | D 60-69 | F <60
grading.wrong_answer_penalty: -2 per incorrect answer (checkable items)

reports.parent_only: REPORT:CARD, REPORT:WEEK, SCHOOL:CONFIG:*, GRADE:*

overlay.sig_alg: HMAC-SHA256
overlay.sig: <PARENT_GENERATED_SIGNATURE>

/module

/module
