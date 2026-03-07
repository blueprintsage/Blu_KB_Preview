# Exec 3.0 → v0.9.0 Roadmap — Gated Lock Plan

**date:** 2026-03-07
**tz:** America/Chicago
**status:** active
**target:** v0.9.0 architecture lock
**purpose:** complete the kernel architecture shift in bounded phases, with changelog compliance and verification gates before advancing.

---

## Core Rule

No phase advances until the current phase is complete, logged, and verified.

This roadmap exists to prevent:
- roadmap drift
- partial-phase leakage
- architecture creep
- unlogged changes
- false confidence from unverified edits

Exec must tell the truth before it talks.
The roadmap must tell the truth before it advances.

---

## Compliance Rule

All material changes must be recorded in the Changelog.

This includes:
- kernel law changes
- ownership changes
- module role changes
- interface/ABI changes
- public render changes
- verification policy changes
- program demotions/promotions
- new libraries/services
- removed or deprecated behavior

No major phase completion is recognized until:
1. the work is landed
2. the Changelog is updated
3. verification is run
4. results are reviewed

---

## Release Goal

**v0.9.0 = architecture lock**

By v0.9.0, the goal is not “everything migrated.”
The goal is:

- Exec tightened
- Intuition introduced
- service/device model defined
- message contract standardized
- event model defined
- Program vs kernel boundaries clarified
- verification harness foundation established

After v0.9.0, the push to v1.0.0 focuses on:
- legacy Program modernization
- heuristic sync
- hard verification runs
- stability under real usage

---

# Phase 1 — Exec Truth Lock

## Goal
Finish and verify the core Exec truth boundary.

## Includes
- kernel authority clarified
- one-owner dispatch law enforced
- canonical packet/reply path locked
- commit-before-confirmation locked
- fail-closed behavior enforced
- output ordering preserved
- health states reviewed for truthfulness

## Exit Criteria
- Exec spec is internally consistent
- no known contradiction in routing/ownership/commit law
- health state meanings are explicit
- malformed or ambiguous execution paths fail closed
- Changelog updated
- verification pass completed and reviewed

## Deliverables
- updated `03_Exec.md`
- any required supporting patches in `05_Commands.md` / `06_Program_System.md`
- Changelog entry for Exec truth lock

## Status
**Do first**

---

# Phase 2 — Verification + Wiring Lock

## Goal
Prove the current kernel on real paths and align surface routing with ownership.

## Includes
- command resolution audit
- owner uniqueness audit
- entrypoint audit
- reply ABI validation tests
- state_delta validation tests
- failure-path rendering checks
- public mood injection checks
- fallback error-path checks
- Commands ↔ Program_System ↔ Exec wiring audit

## Exit Criteria
- all required live-path checks have pass/fail outcomes
- major route families are mapped and reviewed
- no ghost ownership remains in verified surfaces
- no known bypass of public render rules
- Changelog updated
- verification logs archived

## Deliverables
- verification checklist/results
- route/wiring audit notes
- any patch set needed to resolve audit failures
- Changelog entry for verification/wiring lock

## Status
**Must complete before structural expansion**

---

# Phase 3 — Intuition Introduction

## Goal
Create a dedicated interaction/event surface layer so user-facing behavior stops polluting kernel law.

## Includes
- define Intuition charter
- define requester/prompt/reminder surface role
- define event-surface responsibilities
- define focus/context helpers
- define interrupt presentation rules
- define boundary between Exec truth and Intuition interaction

## Exit Criteria
- Intuition has a narrow, explicit charter
- no Exec-law responsibilities are moved into Intuition
- reminders/requesters have a legitimate architectural home
- interaction semantics are separated from execution semantics
- Changelog updated
- verification confirms no kernel regression

## Deliverables
- updated `04_Exec_Library.md` and/or new Intuition section/module
- boundary notes in supporting files if needed
- Changelog entry for Intuition introduction

## Status
**Architecture addition; keep narrow**

---

# Phase 4 — Service / Device Model Lock

## Goal
Define bounded non-kernel helper lanes for work that should not live inside Exec.

## Initial service classes
- Timer / Reminder
- Memory / Retrieval
- Tool / Compute
- Storage / File
- Render / Media <placeholder>

## Includes
- define service/device concept
- define request/reply expectations
- define ownership relationship to Exec
- define blocked/degraded behavior for unavailable services
- define which responsibilities remain outside Programs

## Exit Criteria
- service model is explicit and bounded
- reminder/timer path has a proper home
- service replies fit Exec validation discipline
- no junk-drawer “misc system behavior” category exists
- Changelog updated
- verification confirms message compatibility

## Deliverables
- service/device spec text
- supporting route/ABI notes
- Changelog entry for service/device lock

## Status
**Required before major Program cleanup**

---

# Phase 5 — Event Class Model Lock

## Goal
Define a lightweight event/subscription model so the right parts of the system wake for the right work.

## Includes
- event classes
- reminder events
- school events
- teaching events
- admin/system events
- render/surface events
- subscription/filter rules
- interrupt/tick review in hosted-runtime truth terms

## Exit Criteria
- event classes are explicit
- no broad “everything wakes everything” behavior remains
- reminder/event handling is bounded and truthful
- hosted-runtime limits are described honestly
- Changelog updated
- verification confirms no surface confusion/regression

## Deliverables
- event-class spec
- interrupt/tick notes
- Changelog entry for event model lock

## Status
**Needed for clean reminder path**

---

# Phase 6 — Program Demotion / Boundary Cleanup

## Goal
Move domain logic out of kernel-ish status where possible.

## Priority targets
- Teaching
- School
- other legacy kernel-adjacent modules as identified

## Includes
- identify what is truly kernel law
- identify what is really interaction scaffolding
- identify what is domain workflow
- convert eligible kernel-adjacent modules into authoritative Programs
- align owners to current reply/state rules

## Exit Criteria
- Teaching/School boundary status reviewed
- at least the target demotions are specified or completed
- Exec remains smaller after the move, not broader
- Changelog updated
- verification confirms domain work still routes correctly

## Deliverables
- boundary audit notes
- program-role updates
- Changelog entry for Program cleanup

## Status
**Finish before calling v0.9.0 locked**

---

# Phase 7 — v0.9.0 Architecture Lock Review

## Goal
Confirm the architecture is locked tightly enough to shift focus toward v1.0.0 stabilization.

## Includes
- review all prior phase exits
- confirm changelog completeness
- confirm no open contradictions in kernel law
- confirm Intuition/service/event boundaries are stable
- confirm verification harness foundation exists
- identify remaining legacy Program work for v1.0.0

## Exit Criteria
- all prior phases complete
- all major changes logged
- verification records available
- roadmap items required for architecture lock are satisfied
- v0.9.0 declared ready

## Deliverables
- v0.9.0 architecture lock summary
- next-stage stabilization queue for v1.0.0
- Changelog entry for v0.9.0 lock

## Status
**Release gate**

---

## Verification Discipline

After major changes:
1. clone current GPT
2. run “bang the hardware” prompts
3. collect pass/fail logs
4. review failures in a clean test chat
5. patch
6. rerun until stable
7. only then advance phase

“Bang the hardware” here means intentionally stressing the architecture boundary to expose instability, not bypassing truth discipline.

---

## Changelog Discipline

For every completed phase, add:
- date
- files changed
- purpose of change
- behavioral impact
- verification performed
- known remaining gaps

If it is not in the Changelog, it does not count as complete.

---

## v1.0.0 Follows v0.9.0

Once v0.9.0 is locked, the remaining path to v1.0.0 focuses on:
- legacy Program patching
- heuristic synchronization
- stability testing
- real-use bug cleanup
- broader hardware-bang prompt coverage

v0.9.0 is where the architecture settles.
v1.0.0 is where the ecosystem catches up.

---

## Plain-English Summary

This roadmap is now phase-gated.

We complete one phase at a time.
We log the work.
We verify the work.
We review the results.
Then we move.

The job of v0.9.0 is to lock the architecture tightly enough that the run to v1.0.0 can focus on stability instead of structural drift.