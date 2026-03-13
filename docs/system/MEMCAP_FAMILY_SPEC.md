# MEMCAP_FAMILY_SPEC_v1
Date: 2026-03-12  
Status: Canon Draft v1  
Scope: Blu repo / continuity architecture

## 1. Purpose

This document defines the **memcap family** for Blu.

It exists to solve a specific problem:

one memcap format is not enough to serve all continuity needs.

Different continuity tasks need different output shapes:
- fast next-chat restart
- project-specific handoff
- human-readable long-form review
- archive-grade preservation

This spec separates those roles cleanly.

---

## 2. Core Relationship to MMU

### 2.1 MMU role
MMU is for:
- **per-session continuity**
- thread separation
- salience handling
- return-to-task behavior
- active memory hygiene inside a live chat

### 2.2 Memcap role
Memcaps are for:
- **explicit continuity transfer**
- cross-chat carry-forward
- project handoff
- archival snapshots
- readable state preservation outside chat

### 2.3 Core law
**MMU handles live session continuity.  
Memcaps handle intentional continuity transfer.**

This is the main separation after the MMU patch.

---

## 3. Memcap Family

The memcap family has four types:

1. **Normal Memcap**
2. **Project Memcap**
3. **Raw Dump Memcap**
4. **Cold Store Memcap**

Each has a different purpose and should not be treated as interchangeable.

---

## 4. Normal Memcap

### 4.1 Purpose
Default next-chat handoff.

### 4.2 Use when
Use a Normal Memcap when the goal is:
- restart the next chat fast
- preserve current priorities
- carry key state forward without dragging the whole session

### 4.3 Output style
- compact
- practical
- operational
- low-noise

### 4.4 Must include
- date
- active projects
- active non-project threads if still relevant
- important changes this session
- locked decisions
- next actions
- files needed next time if relevant

### 4.5 Should avoid
- long narrative retelling
- excessive emotional detail
- redundant project deep dives
- full vent replay

### 4.6 Target size
Short to medium.

### 4.7 Summary label
**Normal = routine carry**

---

## 5. Project Memcap

### 5.1 Purpose
Scoped continuity handoff for one project.

### 5.2 Use when
Use a Project Memcap when the goal is:
- continue a specific project later
- preserve technical/project state
- separate project continuity from the rest of the chat

Examples:
- Dungeon Forge
- PASS
- SkillForge
- School
- Teach

### 5.3 Output style
- structured
- scoped
- technical
- low-noise

### 5.4 Must include
- project identity
- current project state
- locked decisions
- created artifacts
- unresolved items
- blockers
- next tasks
- source files needed next time

### 5.5 Should avoid
- unrelated side threads
- personal vent material unless it materially affected the project
- broad life recap
- extra chat flavor not relevant to continuation

### 5.6 Target size
Medium.

### 5.7 Summary label
**Project = scoped carry**

---

## 6. Raw Dump Memcap

### 6.1 Purpose
Human-readable long-form session carry.

### 6.2 Use when
Use a Raw Dump Memcap when:
- a person wants to read the session outside chat
- high nuance retention matters
- emotional tone and sequence matter
- a fuller recall is wanted without relying on the chat UI

This is the best fit for:
- V-readable session carry
- long-form external review
- “give me the whole arc in one readable block”

### 6.3 Output style
- long-form
- chronological or semi-chronological
- readable prose
- detail-preserving

### 6.4 Must include
- session context
- major threads in order
- important exchanges or paraphrases
- emotional/relational context where relevant
- major decisions made
- artifacts created
- unresolved items
- next actions

### 6.5 Should avoid
- meaningless filler
- literal full transcript recreation
- over-compression that strips context
- aggressive cleanup that destroys nuance

### 6.6 Target size
Medium to long.

### 6.7 Summary label
**Raw Dump = readable full carry**

---

## 7. Cold Store Memcap

### 7.1 Purpose
Archive-grade preservation format.

### 7.2 Use when
Use a Cold Store Memcap when:
- preserving an end-of-phase state
- storing a milestone snapshot
- creating a long-horizon archival record
- consolidating one or more memcaps into a preserved artifact

### 7.3 Important correction
Cold Store is **not** the default memcap.

It should be treated as:
- milestone preservation
- archive snapshot
- derived archival synthesis

not routine next-chat carry.

### 7.4 Output style
- structured
- stable
- archival
- lower-frequency
- preservation-oriented

### 7.5 May be built from
- Normal Memcap
- Project Memcap
- Raw Dump Memcap
- direct milestone synthesis

### 7.6 Must include
- preservation date
- scope
- milestone identity
- stable decisions
- active state at archive time
- known unresolved areas
- source artifacts or dependency references
- status note indicating archived vs active project state

### 7.7 Should avoid
- chatty filler
- unstable speculative claims
- temporary vent noise
- pretending archive state is live active state later

### 7.8 Target size
Medium to long, but more structured than Raw Dump.

### 7.9 Summary label
**Cold Store = archival preservation**

---

## 8. Family Summary

```text
Normal     = routine carry
Project    = scoped carry
Raw Dump   = readable full carry
Cold Store = archival preservation
```

---

## 9. Trigger / Selection Guide

### Use a Normal Memcap when:
- ending a regular chat
- wanting quick restart context
- preserving active priorities only

### Use a Project Memcap when:
- a project needs to move to another chat
- technical state matters more than broad session context
- multiple projects exist and one needs isolated carry-forward

### Use a Raw Dump Memcap when:
- a person wants the session readable outside chat
- high-fidelity human review matters
- nuance/tone/order matter

### Use a Cold Store Memcap when:
- a milestone is complete
- a phase should be archived
- a stable preservation record is desired

---

## 10. Required Cross-Type Rules

### 10.1 Do not confuse archive with active state
Archive is not active by default.

### 10.2 Do not promote temporary emotion into stable state automatically
Emotional intensity may be described in Raw Dump, but should not automatically become persistent state in Normal or Project memcaps.

### 10.3 Do not force one format to do every job
If a user wants full readability, use Raw Dump.
If a user wants project handoff, use Project Memcap.
If a user wants fast restart, use Normal.

### 10.4 Keep file/source requirements explicit
If a new chat will need files re-uploaded, say so.

### 10.5 Cross-chat carry-forward should be explicit
Do not assume MMU is responsible for cross-chat continuity.

---

## 11. Inclusion / Exclusion Rules

### 11.1 Carry forward
Carry forward:
- locked decisions
- active project state
- next tasks
- blockers
- file dependencies
- relevant portrait continuity
- major thread identity if still active

### 11.2 Allow to decay
Allow to decay:
- temporary vent heat
- repetitive argument details
- transient frustration unless materially relevant
- one-off side chatter
- stale speculative interpretations

### 11.3 Special rule for side threads
If a side thread is not the active continuity target, it should be summarized, not replayed in full, unless Raw Dump is explicitly requested.

---

## 12. Recommended Template Structure Per Type

### 12.1 Normal Memcap structure
- MEMCAP / date
- active projects
- active threads
- key changes this session
- locked decisions
- next actions
- needed files / caveats

### 12.2 Project Memcap structure
- PROJECT MEMCAP / date / project
- current state
- locked decisions
- artifacts created
- blockers
- unresolved items
- next tasks
- required files next time

### 12.3 Raw Dump Memcap structure
- RAW DUMP / date / scope
- session context
- major threads in sequence
- key emotional/relational context
- decisions made
- artifacts created
- unresolved items
- next actions

### 12.4 Cold Store structure
- COLD STORE / date / scope
- milestone identity
- archived state summary
- stable decisions
- unresolved issues
- source artifact references
- archive status note

---

## 13. Repo / Template Changes Required

### 13.1 Keep the Cold Store template
Do not remove it.

### 13.2 Reposition the Cold Store template
Relabel it as:
- archive-grade
- milestone preservation
- not default

### 13.3 Add new templates
The repo should add:
- `Normal_Memcap_Template`
- `Project_Memcap_Template`
- `Raw_Dump_Memcap_Template`

### 13.4 Add usage guidance
The repo should include a short usage guide:
- when each memcap type is used
- which one is default
- which one is archival
- how they relate to MMU

---

## 14. Changelog Requirements

Because the MMU patch and memcap-family update affect continuity behavior, changelogs must be explicit.

### 14.1 Required changelog fields
Every memcap/template policy update should record:
- date
- artifact/template changed
- what changed
- why it changed
- operational impact
- whether it affects default behavior

### 14.2 Required notes for this family spec rollout
The changelog should explicitly state:
- Cold Store is no longer treated as the default memcap
- Normal Memcap becomes the default routine handoff
- Project Memcap becomes the scoped project handoff
- Raw Dump Memcap becomes the readable long-form carry
- Memcaps now serve as the official cross-chat continuity layer
- MMU is now explicitly per-session, not cross-chat by default

### 14.3 Failure mode to avoid
Do not leave changelogs vague, or future continuity work will drift again.

---

## 15. Rollout Order

Recommended rollout sequence:

1. update MMU patch changelogs properly
2. add this family spec to repo
3. update Cold Store template labeling
4. add Normal Memcap template
5. add Project Memcap template
6. add Raw Dump Memcap template
7. update usage notes / README if needed

---

## 16. Current Verdict

The memcap system should no longer rely on one template trying to do every job.

Blu should use a memcap family:

- Normal for routine carry
- Project for scoped carry
- Raw Dump for readable full carry
- Cold Store for archival preservation

This is the cleanest match for the new MMU patch and the way continuity is actually being used.
