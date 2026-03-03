# Programs — Registry Canon (v1)

---

module: kb__protocols_programs_program_registry_canon_v1.M01 | name="Content"
[CAPSULE_HEADER_BEGIN]
mem_id: 2026_02_28__blu__program-registry-canon-v1
title: Programs — Registry Canon (v1)
date: 2026-02-28
status: active
topic: blu
type: spec
tags: programs, registry, canon
sensitivity: medium
visibility: private
source: doc
domain: ops
authority: propose_only
definition_of_done: One canonical registry path is defined; all references use program_id from that file.
[CAPSULE_HEADER_END]

## Canonical registry path

- Canonical registry: `templates/docs/Program_Registry.md`

## Rules

- `program_id` is the **stable identifier** and must never be reused for a different program.
- Defaults are defined only in the canonical registry.
- Any secondary “list of programs” must link to the canonical registry and must not redefine defaults.
