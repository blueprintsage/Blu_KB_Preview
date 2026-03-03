capsule_id: kb__templates_school_docs_parent_gate_id_linking_md__ecb958
title: "Parent Gate ID Linking"
date: 2026-02-24
updated: 2026-02-24
version: 0.1.0
status: draft
topic: blu
type: spec
tags: ['templates', 'school', 'docs']
sensitivity: medium
visibility: shared
source: repo
domain: templates
schema: capsule_header_v1.1
body_schema: blu_modular_v1
---

module: blu__school_docs.M03 | name="Parent Gate ID (How Linking Works) | status=active"

# Parent Gate ID (How Linking Works)

To keep parent secrets out of student files, we use a **Gate ID** pointer.

- The **Parent Key** file contains:
  - `parent.gate.id` (identifier)
  - `parent.gate.hash` (the hash)

- The **School Overlay** and/or **Student Log** contain only:
  - `parent.gate.required: true`
  - `parent.gate.id: <same id>`

Blu allows parent-only commands only when:
1) the Parent Key is loaded,
2) `PARENT:UNLOCK` succeeds, and
3) the `parent.gate.id` values match.

This makes rotation easy (change hash, keep the same ID) and avoids spreading hashes around.

/module


## Unlock lifetime (canonical)

Unlock lifetimes (TTL vs session) and relock hygiene are defined in `protocols/parent/Parent_Gate_TTL_v1.md`.
