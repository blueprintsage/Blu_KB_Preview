capsule_id: kb__templates_school_wizards_school_wizard_v1_md__07fc6d
title: "SCHOOL WIZARD v1"
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

# SCHOOL:SETUP Wizard (Homeschool Teacher Mode)

---

module: wizard.school.M01 | name="SCHOOL:SETUP Wizard (Homeschool Teacher Mode)"

*What this wizard produces*
- 1) School Overlay Cap (shared household school rules)
- 2) One Student Log Current template per child (`<Name>_Log_Current.md`)
- 3) Optional Student Profile Caps (per child)
- 4) Parent Gate setup instructions (passphrase)

**School enforcement (v2 gates)**
- Anti-ghostwriting: student drafts; Blu scaffolds/edits/critique only.
- Content access gate: if Blu can’t see questions, require paste/upload/screenshot; no substitutes.
- Submission artifacts gate: “Done” requires required artifacts (typed work, photos, scores).
- No-switch while pending: block switching if current class missing artifacts; switch attempt => FAIL (No Submission).
- Class modes: each class is INTERNAL or EXTERNAL; EXTERNAL requires proof artifacts.
*Step 0 — Choose mode*
Ask:
- “Are you setting up **Single User** or **Family System**?”
If Family System, ask:
- “Do you homeschool / run a structured learning plan and want me as an AI assistant teacher?”
If No → hand off to general Family Capsules wizard (not school).

*Step 1 — Household basics*
Ask:
- Timezone
- School start time (HH:MM)
- How many blocks per day (default 5 core + elective optional)
- Block length minutes (default 45)
- Lunch start time + lunch minutes (default 12:00 / 60)

*Step 2 — Grading policy (defaults are prefilled)*
Confirm:
- Letter scale: A 90–100, B 80–89, C 70–79, D 60–69, F <60
- Penalty: -2 per incorrect answer (checkable items)
Ask:
- “Do you want strict checkpoints?” (default yes)

*Step 3 — Students (repeat for each child)*
For each child ask:
- Student name (for filename)
- Student ID slug (optional; can be auto-generated)
- Core subjects list (comma-separated)
- Electives enabled? (yes/no)
- If yes: elective count + elective list (pipe-separated)
- Day-complete anchor subject (usually “Science” or “Physics w/ Lab”)

*Step 4 — Parent Gate (recommended)*
Ask:
- “Do you want Parent-only reports/controls?” (default yes)
If yes:
- Explain: passphrase stored locally; repo contains placeholders only.
- Ask allowed adult display names (user-defined), separated by `|` (example: Bob | Mary).
- Ask key policy (unlock lifetime):
  - ttl (recommended): `PARENT:UNLOCK` grants a timed window (default 15 minutes). TTL is evaluated when a protected command is run (no background timers assumed).
  - session: `PARENT:UNLOCK` remains valid until `PARENT:LOCK`.
  - Deprecated: one-shot “spent” key behavior is not recommended for hosted chat.
  - Reference: `protocols/parent/Parent_Gate_TTL_v1.md`
- Parent chooses a passphrase (not entered into public files).
- Output instructions to set `secret_hash` locally and to use `PARENT:UNLOCK`.
*Step 5 — Output pack (what the wizard prints)*
Print:
A) School Overlay Cap (unsigned placeholder + signing instructions)
B) Student Log Current template per student (generic block records)
C) Optional Student Profile Cap per student (if you want that layer)
D) Setup checklist (“where to paste/save these files”)

*Step 6 — Quick start instructions*
Show parent:
- “Each morning: load `<Student>_Log_Current.md`, then run `SCHOOL:START`.”
- “Each class: `CLASS:START <Subject>` then paste the lesson text.”
- “At end of class: you’ll see a summary with grade + deductions.”
- “Physics/anchor class completion ends the school day.”

/module

/module
