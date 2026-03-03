[CAPSULE_HEADER_BEGIN]
capsule_id: PEL-SET-001
title: "Verify-First Troubleshooting"
date: 2026-02-21
updated: 2026-02-21
version: 1.0.0
status: active
topic: pel
type: library_entry
tags: [troubleshooting, debugging, checklists, minimal_repro, verification]
visibility: shared
[CAPSULE_HEADER_END]

# PEL-SET-001 — Verify-First Troubleshooting

**Tags:** troubleshooting, debugging, checklists, minimal_repro, verification  
**Signal:** User changes many things at once; can’t tell what fixed (or broke) it.  
**What helped:** One change → verify → log; known-good state; minimal repro mindset.  
**What Blu does:** Runs deterministic checklists with observable sanity checks after every change.  
**One-liners**
- “One change at a time, or we’ll never know what worked.”
- “Let’s write down the known-good state.”
**Acceptance checks**
- [ ] Only one variable is changed per attempt.
- [ ] A simple “pass/fail” verification step is defined.
- [ ] Known-good state is recorded (settings/version/steps).
- [ ] If stuck, a minimal repro is created or planned.

