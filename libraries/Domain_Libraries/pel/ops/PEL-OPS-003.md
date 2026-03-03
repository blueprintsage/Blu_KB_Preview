[CAPSULE_HEADER_BEGIN]
capsule_id: PEL-OPS-003
title: "Spreadsheet Workflow Phasing"
date: 2026-02-21
updated: 2026-02-21
version: 1.0.0
status: active
topic: pel
type: ops_entry
tags: [spreadsheets, tracking, systems, iteration, maintainability, acceptance_tests]
visibility: shared
[CAPSULE_HEADER_END]

# PEL-OPS-003 — Spreadsheet Workflow Phasing

**Tags:** spreadsheets, tracking, systems, iteration, maintainability, acceptance_tests  
**Signal:** Tracking systems die because they’re overbuilt, fragile, or too hard to maintain.  
**What helped:** Phase 1 working → Phase 2 polish → Phase 3 automation; definitions + checks; maintainability-first.  
**What Blu does:** Ships the simplest working tracker with acceptance checks, then iterates.  
**One-liners**
- “Phase 1: works. Phase 2: pretty. Phase 3: automation.”
- “If it won’t survive your worst day, it’s not a system.”
**Acceptance checks**
- [ ] Phase 1 can be maintained in under 2 minutes/day.
- [ ] Definitions tab (or equivalent) exists for key fields.
- [ ] There are 3 pass/fail checks that confirm the tracker is “working.”
- [ ] Automation is explicitly deferred until Phase 1 is stable.

