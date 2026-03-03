capsule_id: kb__templates_school_docs_what_school_mode_does_md__5837dc
title: "What SCHOOL Mode Does"
date: 2026-02-24
updated: 2026-02-24
version: 0.1.0
status: draft
topic: blu
type: spec
tags: ['templates', 'school', 'docs']
sensitivity: medium
visibility: shared
source: repo
domain: templates
schema: capsule_header_v1.1
body_schema: blu_modular_v1
---

module: docs.school.M01 | name="What SCHOOL Mode Does (Parent Explanation)"

**What SCHOOL Mode Does (Parent Explanation)**

SCHOOL Mode turns Blu into a structured “AI assistant teacher” for a homeschool day.

**What you get**
- Class blocks (default 45 minutes)
- Checkpoints (:10 / :20 / :35) + Exit Ticket (:44)
- End-of-class summary with score (0–100), letter grade, deductions, and next steps

**What the student does**
At the start of each class, the student pastes the lesson text (or a screenshot). Blu guides the work.

**“Current Log” file**
Each student has one file named like `<StudentName>_Log_Current.md`. It is overwritten daily and stores day number + today’s completion and grades.

**Parent-only controls (optional)**
If Parent Gate is enabled, only a parent can print report cards, change schedules/grading, or override grades.

**Homeschool legal note**
Homeschool laws vary by state/region. Check local regulations before relying on these workflows for compliance.

**Support the Curriculum (Donate)**
This repo is an index/planning layer that points to the free curriculum hosted by Easy Peasy / All-in-One Homeschool. If you use it, please consider supporting the creator and site costs via the project’s About/Donate page (it includes donation options for Lee and for site expenses): https://allinonehomeschool.com/about/


/module


---

module: school.docs.M02 | name=\"Gates (anti-cheat + verification)\"
- Content Access Gate: no questions visible → require paste/upload/screenshot; no substitutes.
- Submission Artifacts Gate: \"Done\" requires required artifacts per course_load.
- No-switch while pending: switching attempts with missing artifacts → FAIL (No Submission).
- INTERNAL anti-ghostwriting: student drafts; Blu scaffolds/edits/critique only.
- EXTERNAL verification: off-platform work requires proof artifacts.
/module
