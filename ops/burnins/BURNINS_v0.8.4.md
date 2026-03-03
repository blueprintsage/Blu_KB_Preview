# v0.8.4 Burn-ins (Phase 5) --- module: kb__ops_burnins_burnins_v0_8_4.M01 | name="Burn-ins"
[CAPSULE_HEADER_BEGIN]
mem_id: 2026_02_28__blu__burnins-v0-8-4
title: v0.8.4 Burn-ins (Phase 5)
date: 2026-02-28
status: draft
topic: blu
type: checklist
tags: burnin, release, exec, reminders, parent_gate, softkick
sensitivity: medium
visibility: private
source: roadmap
domain: ops
authority: canon
[CAPSULE_HEADER_END]

## Rules
- Run in this order.
- Record PASS/FAIL and any deviations.
- Prefer deterministic replay (`TICK NOW ...`) where available.

## Burn-in A — Reminders ladder + suppression
PASS if:
- m60 → m10 → DUE eligibility in correct order.
- Suppression prevents accidental duplicate emits inside window.
- DUE persists until DONE / MOVE / PAUSE / DELETE.

## Burn-in B — DUE persistence actions
PASS if each action clears DUE as expected:
- DONE clears
- MOVE reschedules
- PAUSE stops ticking
- DELETE removes

## Burn-in C — Parent Gate TTL lifecycle
PASS if:
- TTL unlock expires and protected commands are blocked after expiry.
- Session unlock stays valid until `PARENT:LOCK`.
- `PARENT:LOCK` cancels any unlock immediately.

## Burn-in D — SOFTKICK paste-safe output
PASS if:
- Every SOFTKICK output is exactly one fenced ```text block
- No trailing chars after closing fence

## Burn-in E — Program Registry canonical routing
PASS if:
- `program_id` resolves via canonical registry
- disabled programs cannot run
- programs do not print directly (Exec is print lane)

[/module]

## Burn-in F — Fixed regression seed sweep (run-first)
PASS if:
- All fixed seeds in `tests/REGRESSION_SEEDS_v1.md` pass (50/50).
- Any failure is reproducible on immediate rerun (seed-deterministic).

## Burn-in G — Exec 2.0 smokes (if Exec touched)
PASS if:
- All required tests in `tests/SMOKES_EXEC_v2.md` pass.
- SIM TAG coverage recorded using `tests/SIM_TAGS_EXEC_v2.md`.
