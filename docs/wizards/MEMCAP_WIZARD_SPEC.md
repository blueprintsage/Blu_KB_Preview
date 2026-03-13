# MEMCAP_WIZARD_SPEC.md
Date: 2026-03-12  
Status: Canon Draft  
Scope: Blu continuity / memcap selection flow

## 1. Purpose

This document defines the **Memcap Wizard**.

The Memcap Wizard exists so that when a user asks for a memcap, Blu does not have to guess which continuity format they want.

Instead, Blu should either:
- offer the available memcap types and let the user choose
- or accept a direct fast-path command from users who already know the type they want

---

## 2. Why the Wizard Exists

The continuity system now has multiple valid memcap types:

1. Normal
2. Project
3. Raw Dump
4. Cold Store
5. Memory Vault

These are not interchangeable.

A generic “make a memcap” request is now ambiguous.
The wizard resolves that ambiguity cleanly without forcing Blu to guess wrong.

---

## 3. Core Law

**If the user asks for a memcap without specifying a type, Blu should offer the five available memcap types and let the user choose.**

If the user specifies a type clearly, Blu should skip the choice prompt and produce that type directly.

---

## 4. Supported Memcap Types

## 4.1 Normal
Purpose:
- routine next-chat handoff
- practical restart context
- compact operational carry

Summary label:
**Normal = routine carry**

---

## 4.2 Project
Purpose:
- scoped project continuity
- technical/project state carry
- use for Dungeon Forge, PASS, SkillForge, School, Teach, etc.

Summary label:
**Project = scoped carry**

---

## 4.3 Raw Dump
Purpose:
- readable long-form carry
- high nuance retention
- best for outside-chat reading and human review

Summary label:
**Raw Dump = readable full carry**

---

## 4.4 Cold Store
Purpose:
- archival preservation
- milestone or end-of-phase snapshot
- long-horizon storage

Summary label:
**Cold Store = archival preservation**

---

## 4.5 Memory Vault
Purpose:
- manual/offline vault storage container
- vault-oriented preserved memory entry
- not the default routine memcap

Summary label:
**Memory Vault = offline/manual vault storage**

---

## 5. Trigger Conditions

The wizard should trigger when the user asks for a memcap in a generic or ambiguous way.

### Example trigger phrases
- make a memcap
- give me a memcap
- memcap this
- write a memcap
- create a memcap
- make me a memcap
- I need a memcap

If the request does not clearly specify type, the wizard should activate.

---

## 6. Direct Fast-Path Commands

If the user already knows what they want, Blu should accept direct commands and skip the wizard choice step.

### Supported fast-path forms
- `/memcap normal`
- `/memcap project`
- `/memcap raw`
- `/memcap cold`
- `/memcap vault`

### Acceptable natural-language fast paths
- make a project memcap
- give me a raw dump memcap
- make a cold store memcap
- write a memory vault entry
- make a normal memcap

These should bypass the choice prompt.

---

## 7. Wizard Prompt Behavior

If the request is ambiguous, Blu should offer the five options cleanly.

### Suggested prompt shape
```text
Which memcap do you want?

1. Normal — routine carry
2. Project — scoped carry
3. Raw Dump — readable full carry
4. Cold Store — archival preservation
5. Memory Vault — offline/manual vault storage
```

Optional fast-path reminder:
```text
You can also use:
 /memcap normal
 /memcap project
 /memcap raw
 /memcap cold
 /memcap vault
```

---

## 8. Recommendation Logic

If the user seems unsure, Blu may recommend a type based on intent.

### Recommend Normal when
- user wants next-chat continuity
- user wants a quick restart summary
- no project specialization is needed

### Recommend Project when
- user is handing off a specific project
- technical/project state matters more than the rest of the chat
- the project has artifacts, blockers, and next tasks

### Recommend Raw Dump when
- user wants a fuller readable summary
- someone else will read it outside chat
- nuance/tone/sequence matter

### Recommend Cold Store when
- user wants archival preservation
- a milestone or phase is ending
- the snapshot is not just for immediate next-chat restart

### Recommend Memory Vault when
- user wants a manual vault-style entry
- they are preserving a memory record for offline/reference use
- they explicitly want the vault format

---

## 9. Selection Resolution Rules

### 9.1 If user picks one option
Produce only that memcap type.

### 9.2 If user asks for more than one
Produce each requested type separately and label them clearly.

### 9.3 If user says “default”
Default to **Normal Memcap**.

### 9.4 If user says “project”
Ask for the project name only if genuinely needed and missing.
Otherwise infer from active project context.

### 9.5 If user says “full”
Default to **Raw Dump** unless context clearly implies Cold Store.

---

## 10. Output Rules

### 10.1 Label the memcap type clearly
Every memcap produced through the wizard should be clearly labeled by type.

### 10.2 Respect the family spec
The wizard should not collapse the memcap family back into one generic format.

### 10.3 Keep type boundaries clear
Do not let:
- Raw Dump become Project
- Project become Normal
- Cold Store become routine carry
- Memory Vault become default memcap

---

## 11. Commands Summary

```text
/memcap normal
/memcap project
/memcap raw
/memcap cold
/memcap vault
```

Meanings:

- `normal` = routine carry
- `project` = scoped carry
- `raw` = readable full carry
- `cold` = archival preservation
- `vault` = memory vault entry

---

## 12. Anti-Drift Rules

### 12.1 No guessing when ambiguous
If the user asks generically, offer the choice menu.

### 12.2 No treating Cold Store as default
Cold Store is archival, not routine.

### 12.3 No collapsing Memory Vault into ordinary memcap use
Memory Vault stays its own type.

### 12.4 No over-questioning
The wizard should ask for the type choice, not launch into a full interview unless the chosen type actually requires missing information.

---

## 13. Recommended Repo Position

This wizard spec belongs with continuity / memcap policy docs.

Suggested placement:
- Core / policy
- continuity architecture area
- same neighborhood as:
  - `MEMCAP_FAMILY_SPEC.md`
  - `Memory_Vault_Template.md`
  - `COLD_STORE_KNOWLEDGE_TEMPLATE.md`

---

## 14. Recommended Next Artifacts

After this spec, the useful follow-ups are:

- `MEMCAP_WIZARD_PROMPTS.md`
- `MEMCAP_COMMAND_MAP.md`

Optional later:
- a real Program spec if the wizard proves stable enough to deserve promotion

---

## 15. Current Verdict

The Memcap Wizard should exist as the default selector for generic memcap requests.

This gives Blu:
- safer memcap selection
- user choice by default
- fast-path commands for advanced users
- cleaner continuity behavior after the MMU patch
