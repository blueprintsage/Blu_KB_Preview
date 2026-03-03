# Exec — Universal Proposal Contract

---

module: kb__protocols_exec_exec_universal_proposal_contract.M01 | name="Content"
[CAPSULE_HEADER_BEGIN]
mem_id: 2026_02_23__blu__exec-universal-proposal-contract
title: Exec — Universal Proposal Contract (v0)
date: 2026-02-23
status: active
topic: blu
type: spec
tags: exec, proposals, arbitration, kernel, os
sensitivity: medium
visibility: private
source: doc
domain: ops
authority: propose_only
next_action: Require every domain module to output proposals[]; only Exec prints; selected-only state mutation.
definition_of_done: All modules implement propose(); Exec arbitrates globally; no module prints directly.
[CAPSULE_HEADER_END]


**Purpose**

Define the minimum proposal shape all modules must produce so Exec can arbitrate deterministically.


**Invariants**

- **Modules propose; Exec prints.**
- **State patches apply only if the proposal is selected/emitted.**
- Render budget is low-noise: **1 line** (optional companion only when explicitly allowed).



**Module interface (required)**

Each domain module must expose:

- `propose(state, now_utc, context) -> Proposal[]`

Rules:
- `state` is read-only within `propose()`; modules **must not mutate global state**.
- All state changes must be expressed as a `state_patch` (or `state_delta`) attached to a proposal and **applied only if that proposal is selected/emitted by Exec**.

**Proposal object (required fields — Exec v2.0)**

Each module returns a list of `Proposal` objects. Each proposal MUST include:

- `module_id` (string) — e.g., `SCHOOL`, `TEACH`, `PARENT_GATE`, `REMINDERS`, `PROGRAMS`
- `kind` (enum) — the proposal’s type (module-defined enum values are allowed, but must be stable)
- `subject_id` (string) — stable identity for the underlying item (e.g., `school:aiden:124:algebra:work`)
- `computed_suppress_key` (string) — stable suppression identity (usually derived from `module_id + subject_id + kind + rung`)
- `band` (enum) — `P0..P8`
- `priority` (int) — tie-break within band
- `escalation_rank` (int) — higher value may bypass suppression when policy allows (default `0`)
- `flags` (object) — boolean flags used by arbitration (e.g., `is_due`, `is_gate`, `is_context_restore`, `allow_companion`, `flow_mask_ok`)
- `intent` (enum) — `interrupt | main_route_constraint | state_update`
- `render_lines` (list[string]) — empty unless selected; max **1** line (max **2** only if `flags.allow_companion=true`)
- `state_patch` (object) — structured updates; applied **only if** selected/emitted

Optional (recommended):

- `debug` (object) — module-local reasoning for `EXEC DEBUG` traces (non-user-facing)


**Bands (global)**

- **P0** Safety emergency
- **P1** Due / hard deadline / critical reminder
- **P2** Hard gate / blocking requirement
- **P3** Active flow continuation (current task/class step)
- **P4** Near-term heads-up (scheduled)
- **P5** Context restore (only when allowed)
- **P6** Structured nudge (opt-in)
- **P7** Creative suggestion
- **P8** Social tone / fun


**Flow masks (global)**

- `school_session`: allow `P0–P3` and `P2` gates. Mask `P6–P8` unless explicitly invoked.
- `midwork`: allow `P0–P3` and `P2` gates. Mask everything else unless user asked “status/list”.


**Selection rule (deterministic)**

Winner selection order:
1) lowest band number
2) highest priority
3) stable module ordering (registry order)


**Suppression identity**

Suppression key is derived from `computed_suppress_key` (usually built from `module_id + subject_id + kind` plus rung/stage where applicable).

Exec uses `computed_suppress_key` + `last_emit_utc` (per key) to suppress repeats within the policy window.



## Module return wrapper (recommended)

To keep outputs paste-safe and deterministic, modules should return a single wrapper object:

- `proposals`: `Proposal[]` (required)
- `lines`: `string[]` (optional, **0–2** lines; Exec decides whether to print)
- `state_delta`: patch/delta (optional; **must only apply if the owning proposal is selected**)
- `events`: `Event[]` (optional)

**Rule:** modules must not print directly; Exec prints the selected output.
