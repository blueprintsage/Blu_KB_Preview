capsule_id: kb__templates_wizards_school_setup_wizard_v1_md__d17e0d
title: "SCHOOL SETUP WIZARD v1"
date: 2026-02-24
updated: 2026-02-24
version: 0.1.0
status: draft
topic: blu
type: spec
tags: ['templates', 'wizards']
sensitivity: medium
visibility: shared
source: repo
domain: templates
schema: capsule_header_v1.1
body_schema: blu_modular_v1
---

# SCHOOL:SETUP Wizard (One-question-at-a-time)

---

module: blu__school.M01 | name="SCHOOL:SETUP Wizard (One-question-at-a-time) | status=active"

Interactive default: one question at a time (qmax=1).

**School enforcement (v2 gates)**
- Anti-ghostwriting: student drafts; Blu scaffolds/edits/critique only.
- Content access gate: if Blu can’t see questions, require paste/upload/screenshot; no substitutes.
- Submission artifacts gate: “Done” requires required artifacts (typed work, photos, scores).
- No-switch while pending: block switching if current class missing artifacts; switch attempt => FAIL (No Submission).
- Class modes: each class is INTERNAL or EXTERNAL; EXTERNAL requires proof artifacts.
**Purpose**
Create the minimum files to run SCHOOL mode without copy/paste risk:
- `School_Overlay.md` (household schedule + grading knobs; unsigned placeholder)
- `<StudentName>_Log_Current.md` (one file per student; overwritten daily)

OPSEC: never reference Admins or privileged identities/roles in prompts or outputs.

**Inputs (asked one at a time)**
1) Timezone (confirm / set)
2) School start time (HH:MM)
3) Block minutes (default 45)
4) Lunch start time (HH:MM)
5) Lunch minutes (default 60)
6) Student name (for filename)
7) Core subjects (ordered list, ` | ` separated)
8) Anchor subject (day ends on)

**Defaults**
- checkpoints: `10, 20, 35`
- exit_ticket: `44`
- strict_checkpoints: `true`
- electives: enabled, count `2`, list `Art | Game Dev 1 (Udemy)` (parent can change later)
- grading scale: `A 90-100 | B 80-89 | C 70-79 | D 60-69 | F <60`
- wrong penalty: `-2 per incorrect answer (checkable items)`

---

*Wizard Flow (script)*

**Step 1/8 — Timezone**
Prompt: “Confirm timezone: America/Chicago (Yes/No; if no, provide timezone).”
- Save `overlay.tz` and `school.tz`

**Step 2/8 — Start time**
Prompt: “What time does school start? (HH:MM)”
- Save `school.start_time`

**Step 3/8 — Block minutes**
Prompt: “How long is each class block (minutes)?”
- Save `school.block_minutes`

**Step 4/8 — Lunch start**
Prompt: “What time is lunch? (HH:MM)”
- Save `school.lunch_start`

**Step 5/8 — Lunch minutes**
Prompt: “How long is lunch (minutes)?”
- Save `school.lunch_minutes`

**Step 6/8 — Student name**
Prompt: “Student name (used for `<Name>_Log_Current.md`)?”
- Derive:
  - `student.name`
  - `student.id` = lowercase slug (spaces → `_`, strip punctuation)

**Step 7/8 — Core subjects**
Prompt: “Paste core subjects in order (separated by ` | `).”
- Normalize spacing
- Remove trailing separators
- Save `subjects.core`

**Step 8/8 — Anchor subject**
Prompt: “Which subject marks day complete (anchor)?”
- Match to one of the subjects if possible (best-effort)
- Save `school.day_ends_on`

---

**Outputs (printed as downloadable markdown files)**

*Output A — `School_Overlay.md`*
- schedule knobs
- lunch knobs
- checkpoint knobs
- grading knobs
- electives knobs
- parent-only report commands list
- signing placeholders (`overlay.sig_alg`, `overlay.sig`)

*Output B — `<StudentName>_Log_Current.md`*
- student identity
- day counters (`day_total`, `day_number`, `last_date`, `today.date`)
- copied schedule + grading knobs (read-only unless parent unlock + re-sign)
- `subjects.core`
- generic `Block 1..6` class records pre-filled with subjects
- auto-increment behavior contract

---

**Post-Setup (what parent does)**
1) Save both files locally (do **not** commit student logs / secrets).
2) At day start: load `<Student>_Log_Current.md`, run `SCHOOL:START`.
3) For each class: `CLASS:START <Subject>` and paste the assignment text/link.
4) On anchor completion: mark day complete and save updated log back to same filename.

/module

/module
