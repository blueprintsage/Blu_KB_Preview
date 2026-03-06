# Programs — ABI Contract (v1)

---

module: kb__protocols_programs_program_abi_v1.M01 | name="Content"
[CAPSULE_HEADER_BEGIN]
mem_id: 2026_02_28__blu__program-abi-v1
title: Programs — ABI Contract (v1)
date: 2026-02-28
status: active
topic: blu
type: spec
tags: programs, abi, exec, state_delta, events
sensitivity: medium
visibility: private
source: doc
domain: ops
authority: propose_only
definition_of_done: All Program modules conform to this ABI; Exec is the only printer and state applier.
[CAPSULE_HEADER_END]

## Purpose

Standardize how **Programs** (opt-in layers) interact with Exec so behavior is deterministic and promotable.

## Core invariants

- **Programs never print directly.** They only return data.
- **Exec is the only component that prints and applies state.**
- Programs may be **flow-masked** (e.g., during School) unless explicitly invoked by the user.

## Module return shape

A Program module call returns a `ProgramResult` object:

- `lines` (optional): `string[]` with **0–2** short, user-facing lines (not printed by the Program; Exec decides).
- `proposals`: `Proposal[]` in the **Exec Universal Proposal Contract** shape.
- `state_delta` (optional): JSON Patch (or equivalent) describing intended state changes. Must be empty unless tied to a specific proposal.
- `events` (optional): `Event[]` for logging/telemetry.

### Contract rules

1) **No side effects:** Program code must not mutate global state directly.
2) **Selected-only mutation:** `state_delta` may only be applied when Exec selects the proposal that owns it.
3) **Silence by default:** when a Program is OFF or flow-masked, it returns `proposals=[]` and no `lines`.

## Suggested fields for program proposals

- `kind`: `program_notice | program_action | program_gate`
- `priority_band`: typically **P3** (when invoked); otherwise silent.
- `suppress_key`: include `(program_id, stage, due_id)` to dedupe.
