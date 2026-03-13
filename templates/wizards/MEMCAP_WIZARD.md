# MEMCAP_WIZARD
Date: 2026-03-12
Status: Active Wizard
Scope: Blu continuity / memcap selection

## Purpose

Use this wizard whenever a user asks for a memcap without clearly specifying which type they want.

This wizard exists to prevent Blu from guessing the wrong continuity format.

---

## Trigger

Trigger this wizard when the user asks for a memcap in a generic or ambiguous way.

Examples:
- make a memcap
- give me a memcap
- memcap this
- write a memcap
- create a memcap
- I need a memcap

Do **not** trigger this wizard if the user already specifies a memcap type clearly.

---

## Fast-Path Commands

If the user already knows what they want, accept these directly and skip the choice prompt:

- `/memcap normal`
- `/memcap project`
- `/memcap raw`
- `/memcap cold`
- `/memcap vault`

Natural-language equivalents also bypass the wizard:
- make a normal memcap
- make a project memcap
- give me a raw dump memcap
- make a cold store memcap
- write a memory vault entry

---

## Wizard Prompt

If the request is ambiguous, respond with exactly this choice prompt:

Which memcap do you want?

1. Normal — routine carry
2. Project — scoped carry
3. Raw Dump — readable full carry
4. Cold Store — archival preservation
5. Memory Vault — offline/manual vault storage

Fast path:
- `/memcap normal`
- `/memcap project`
- `/memcap raw`
- `/memcap cold`
- `/memcap vault`

---

## Type Meanings

### Normal
Use for:
- routine next-chat continuity
- compact restart context
- practical carry-forward

### Project
Use for:
- one specific project
- technical/project state handoff
- artifact/blocker/next-task carry-forward

### Raw Dump
Use for:
- readable long-form session carry
- outside-chat reading
- nuance/tone/sequence preservation

### Cold Store
Use for:
- archival preservation
- milestone/end-of-phase snapshot
- long-horizon storage

### Memory Vault
Use for:
- manual/offline vault entry
- preserved memory record
- vault-style storage

---

## Default Resolution Rules

- If the user says `default`, produce **Normal**.
- If the user says `full`, produce **Raw Dump** unless they explicitly ask for archival preservation.
- If the user says `project`, use the active project if obvious; otherwise ask for the project name.
- If the user asks for more than one type, produce each separately and label them clearly.
- If the user asks generically and does not choose, do not guess. Use the wizard prompt.

---

## Anti-Drift Rules

- Do not treat Cold Store as the default memcap.
- Do not collapse Memory Vault into normal memcap behavior.
- Do not guess the memcap type when the request is ambiguous.
- Do not over-interview the user. Ask only for the memcap type unless the chosen type truly needs missing information.

---

## Command Map

- `normal` = routine carry
- `project` = scoped carry
- `raw` = readable full carry
- `cold` = archival preservation
- `vault` = memory vault entry

---

## Implementation Note

This is the active wizard behavior, not just a design note.
When installed in repo/runtime, generic memcap requests should route here first.

