# Capsule Header Template (Markdown-only — NO YAML)
Date: 2026-02-23
Location: templates/docs/Capsule_Header_Template.md

> Use this header block at the top of any capsule.  
> It is **plain Markdown text** with **no YAML front matter**.

---

## Capsule Header Block (copy/paste)

[CAPSULE_HEADER_BEGIN]
mem_id: YYYY_MM_DD__topic__short-slug
title: ...
date: YYYY-MM-DD
status: draft|active|locked
topic: blu|finance|career|learning|workbench|other
type: note|decision|playbook|template|log|handoff|spec|summary
tags: tag1, tag2
sensitivity: low|medium|high
visibility: private|shared|public

# optional / indexing
source: chat|call|doc|import
domain: writing|game_dev|visual|video|finance|ops|support|other

# optional / authority (added for Exec)
# propose_only = module proposes only (never renders)
# output_lane_owner = sole renderer/arbiter (Exec)
# gatekeeper = can hard-block until resolved
authority: propose_only|output_lane_owner|gatekeeper

# optional / linking
related: capsule_id_1; capsule_id_2
supersedes: capsule_id_old
superseded_by: capsule_id_new

# optional / execution
next_action: ...
definition_of_done: ...
review_after: YYYY-MM-DD

# optional / publish safety
redaction_level: none|light|heavy
notes_public: ...
[CAPSULE_HEADER_END]

---

## Recommended body structure (after header)

## Context
- Why this exists

## Decisions / Findings
- ...

## Playbook / Steps
1) ...
2) ...

## Checks
- [ ] ...

## Next
- next_action repeated (optional)

---

## Example: Exec capsule (output lane owner)

[CAPSULE_HEADER_BEGIN]
mem_id: 2026_02_23__blu__exec-kernel-v14-canon
title: Exec Kernel v1.4 — Canon Spec
date: 2026-02-23
status: locked
topic: blu
type: spec
tags: exec, kernel, arbitration, suppression, escalation, ops
sensitivity: medium
visibility: shared
source: doc
domain: ops
authority: output_lane_owner
next_action: Integrate universal proposal contract (v2) without modifying v1.4 canon.
definition_of_done: All domains propose; Exec remains sole output lane; v1.4 unchanged.
review_after: 2026-03-23
notes_public: Deterministic arbitration kernel for interrupts/reminders; defines suppression, escalation, and DUE semantics.
redaction_level: light
[CAPSULE_HEADER_END]