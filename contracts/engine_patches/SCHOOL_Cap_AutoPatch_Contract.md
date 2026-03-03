capsule_id: kb__engine_patches_school_cap_autopatch_contract_md__f99bea
title: "SCHOOL Cap AutoPatch Contract"
date: 2026-02-24
updated: 2026-02-24
version: 0.1.0
status: draft
topic: blu
type: spec
tags: ['engine-patches']
sensitivity: medium
visibility: shared
source: repo
domain: engine_patches
schema: capsule_header_v1.1
body_schema: blu_modular_v1
---

# School Cap Auto-Patch (Migration Contract)

---

module: blu__school.M03 | name="School Cap Auto-Patch (Migration Contract) | status=active"

**Goal**
If a user loads older versions of School Overlay / Parent Key, Blu should:
- add missing fields with safe defaults,
- never overwrite user-provided values,
- print a "patched snapshot" the user can save back to disk.

This mirrors the USERCAP “add-only patch” behavior.

---

**Patch Rules (add-only)**

**New fields to add (vNext)**
- course_loads.e1.subject/mode/required_artifacts (Life Skills)
- course_loads.e2.subject/mode/required_artifacts (Game Dev)
- course_loads.x1.subject/mode/required_artifacts (Spanish EXTERNAL)
- gates.content_access, gates.no_substitutes, gates.submission_artifacts_required
- gates.no_switch_while_pending, gates.fail_on_switch_attempt, gates.anti_ghostwriting
- lifeskills.cook.* tracking fields (verify_code + artifacts + log)
- clock.* + zero_day.date (ExecLib time state)


*A) School_Overlay.md*
Ensure these exist; if missing, add:

- `overlay.version` (default `1.2`)
- `school.checkpoints` (default `10, 20, 35`)
- `school.exit_ticket` (default `44`)
- `school.strict_checkpoints` (default `true`)
- `grading.wrong_answer_penalty` (default `-2 per incorrect answer (checkable items)`)

Parent gate pointer (NO HASH):
- `parent.gate.required` (default `false`)
- `parent.gate.id` (default `PGK-<STUDENT_OR_FAMILY>-01`)

*B) Parent_GOD_Mode_Key.md*
Ensure these exist; if missing, add:

- `parent.gate.id` (required; if missing, prompt)
- `parent.gate.enabled` (default `true`)
- `parent.gate.method` (default `passphrase`)
- `parent.gate.hash` (required; if missing, prompt)

*C) Student_Log_Current.md*
Ensure these exist; if missing, add:

- `school.checkpoints` (default `10, 20, 35`)
- `school.exit_ticket` (default `44`)
- `grading.wrong_answer_penalty` (default `-2 per incorrect answer (checkable items)`)
- `parent.gate.required` (default mirrors overlay if present else `false`)
- `parent.gate.id` (default `PGK-<STUDENT_OR_FAMILY>-01`)

---

**Patch Output Behavior**
When a patch is applied:
- Print a short note: “Patched (add-only): <fields added>”
- Prefer: output as **downloadable markdown** files.

/module
/module
