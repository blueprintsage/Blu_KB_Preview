capsule_id: kb__templates_school_caps_student_cap_template_md__ebde28
title: "Student Cap TEMPLATE"
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

module: cap.student.M01 | name="Student Cap (per child) — TEMPLATE"

**Student Cap (per child) — TEMPLATE**

student.id: <student_slug>
student.name: <Student Name>

school.day_total: 180
school.current_day: <ASK_AT_SCHOOL_START>

subjects.core: <Subject 1> | <Subject 2> | <Subject 3> | <Subject 4> | <Subject 5>
subjects.elective: <Elective A> | <Elective B>


# Course loads live in Student_Log_Current (per day) and define INTERNAL/EXTERNAL + required artifacts.

/module
