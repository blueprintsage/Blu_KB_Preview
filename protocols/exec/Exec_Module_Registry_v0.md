# Exec — Module Registry v0

---

module: kb__protocols_exec_exec_module_registry_v0.M01 | name="Content"
[CAPSULE_HEADER_BEGIN]
mem_id: 2026_02_23__blu__exec-module-registry
title: Exec — Module Registry (v0)
date: 2026-02-23
status: active
topic: blu
type: spec
tags: exec, modules, registry, proposing, arbitration
sensitivity: medium
visibility: private
source: doc
domain: ops
authority: propose_only
next_action: Ensure all modules listed here implement propose() and never print directly.
definition_of_done: All modules in registry return proposals[] every turn; Exec arbitrates; selected-only state mutation enforced.
[CAPSULE_HEADER_END]


**Purpose**

Define the canonical set of modules that must be called each turn to produce proposals.


**Registry order (stable)**

1) `SAFETY` — gatekeeper (P0)
2) `AUTH_IDENTITY` — gatekeeper (P2 when needed)
3) `PARENT_GATE` — gatekeeper + report renderer (P2/P3)
4) `SCHOOL` — flow owner for learning (P2/P3)
5) `TEACH` — instruction engine (P2/P3)
6) `REMINDER` — Exec v1.4 reminder ladder (P1/P4)
7) `PROGRAMS` — opt-in layers (P3 when invoked, else silent)
8) `TASKS` — real tasks only (P3 continuation)
9) `CODE` — compile/test gates (P2) + continuation (P3)
10) `ART` — continuation (P3) + suggestions (P7)
11) `SOCIAL` — tone/comfort (P8; flow-masked during school/midwork)


**Authority flags**

- `EXEC` is the sole `output_lane_owner`.
- All other modules are `propose_only` or `gatekeeper`.


**Minimal behaviors for tomorrow (homeschool)**

- `SCHOOL` must propose the next step in class state machine (`ASSIGN → WORK → CHECK → LOG`).
- `PARENT_GATE` must block `REPORT:*` and `GRADE:*` unless unlocked.
- `PROGRAMS` and `SOCIAL` must be flow-masked during school session unless explicitly invoked.
/module
