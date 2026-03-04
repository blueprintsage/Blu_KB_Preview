# PASS Teaching Loop (PDF/Docs Ingestion) — Template
Location: templates/skills/PASS_Teaching_Loop_Template.md

[CAPSULE_HEADER_BEGIN]
mem_id: 2026_02_23__templates__pass-teaching-loop
title: PASS Teaching Loop (PDF/Docs Ingestion) — Template
date: 2026-02-23
status: active
topic: templates
type: template
tags: pass, ingest, pdf, teaching, skillforge
sensitivity: low
visibility: shared
source: doc
domain: support
authority: propose_only
[CAPSULE_HEADER_END]

module: TPL.PASS.M01 | name="Purpose + When to Use"
Find: pass teaching loop pdf docs ingest skim deep
Purpose:
- A reusable, deterministic workflow for learning from PDFs/docs across any topic (art, coding, writing, cooking, etc.).
- Inputs are study material; Blu outputs *original* curricula, drills, diagnostics, and structured teaching artifacts.

Use this when:
- You want to absorb a book/manual into a teachable structure.
- You want repeatable outputs (summary → canon → procedures → PD/DP → routing → course → patches).

Not for:
- Long verbatim quotes or “reprint the book.” (Summaries + short excerpts only.)

/module

module: TPL.PASS.M02 | name="Start Toggle + Mode"
Find: teaching loop on pass skim deep
Start toggle (paste once):
- Teaching Loop on. Ask for the next PDF/doc until I say DONE.

Mode (per item):
- PASS skim  — fast map-level extraction
- PASS deep  — SkillForge-ready extraction (canon/procs/PD/DP/routing/course)

/module

module: TPL.PASS.M03 | name="Inputs"
Find: inputs focus chapters pages
For each item, provide:
- File (PDF/doc) upload
- Mode: skim or deep
- Optional focus:
  - chapters/sections/pages
  - target skills (e.g., “foreshortening + camera”)
  - desired outputs (e.g., “just PD/DP + routing”)

/module

module: TPL.PASS.M04 | name="Outputs — Skim Contract"
Find: outputs skim master summary what’s new patch notes
Skim outputs (per item):
1) MASTER_SUMMARY (1–2 pages max)
2) Key concepts / definitions (bullets)
3) High-leverage procedures (outline)
4) PD/DP *suggestions* (lightweight)
5) Patch Notes (what to add/change in your KB; avoid reprinting)

/module

module: TPL.PASS.M05 | name="Outputs — Deep Contract"
Find: outputs deep canon procedures pd dp routing course exit criteria
Deep outputs (per item):
1) MASTER_SUMMARY
2) CANON (principles + constraints)
3) PROCEDURES (step-by-step workflows)
4) PD drills (practice reps)
5) DP gates (objective pass/fail)
6) ROUTING_MAP (DP fail → PD/PROC fix → retest)
7) COURSE_OUTLINE (modules + pacing)
8) EXIT_CRITERIA (what “done” means)
9) Patch Blocks (copy/paste deltas into repo/project files)

/module

module: TPL.PASS.M06 | name="Patch Discipline (No implicit state)"
Find: patch blocks selected-only state no implicit memory
Rules:
- Blu does **not** assume persistent storage. Outputs are patches you apply to repo/project files.
- Prefer “patch blocks” over rewriting entire documents.
- Keep changes minimal, deterministic, and reversible.

/module

module: TPL.PASS.M07 | name="Loop Control"
Find: ask for next item until done next item
Loop:
- After each item, Blu ends with: “Next item?” and waits.
- User ends with: DONE.

/module

module: TPL.PASS.M08 | name="Optional: End-of-session memlog"
Find: memory vault memlog end session
If you want a vault entry:
- At session end, Blu can emit a short memlog formatted to your Memory Vault Template (what was ingested + what was added + next step).

/module
