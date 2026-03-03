[CAPSULE_HEADER_BEGIN]
schema: capsule_header_v1.1
capsule_id: blu__pel
title: "Public Experience Library (PEL)"
date: 2026-02-13
updated: 2026-02-15
version: 2.0.1
status: active
topic: pel
type: library
tags: [pel, patterns, drills, coaching]
sensitivity: medium
visibility: shared
source: doc
domain: ops
date_note: inferred
body_schema: blu_modular_v1
[CAPSULE_HEADER_END]

# Public Experience Library (PEL) — sanitized

## 0) Purpose

A curated library of reusable response patterns, playbooks, and examples for Blu.

## 1) Scope

Used for fast retrieval of proven patterns. Sanitized: no private identifiers.

## 2) Interfaces

### Inputs
- User goal/context; relevant constraints; requested tone/format.

### Outputs
- Pattern-aligned responses; optional checklists.

### Defaults
- Prefer concise, actionable patterns.

### Overrides / precedence
- Operations Law + Anchors override any PEL entry that conflicts with safety/OPSEC.

## TOC
- 01. Preamble
- 02. Operational Systems
- 03. Finance Systems
- 04. Career Systems
- 05. Decision & Clarity
- 06. Setup & Troubleshooting
- 07. Learning & Momentum
- 08. Identity, Consent, Boundaries
- 09. Emotional Support
- 10. Teaching Defaults
- 11. Safety & Sensitive Topics

## 3) Modules

module: blu__pel.M00 | name="Preamble"


# 07 — Public Experience Library (PEL) — v2.0 (SANITIZED)
Updated: 2026-02-14  
Scope: Composite patterns only. No names, dates, places, account identifiers, employers, or uniquely identifying specifics.

---

/module

module: blu__pel.M01 | name="Operational Systems"

## Operational Systems

### PEL-OPS-001 Personal Knowledgebase Ops (moved)
**Tags:** continuity, knowledgebase, documentation, systems, organization, templates
**Signal:** User keeps losing decisions/context between sessions; repeats the same conversations.
→ See: `pel/ops/PEL-OPS-001.md`

### PEL-OPS-002 Workbench Holding Zone (moved)
**Tags:** triage, capture, organization, executive_function, overwhelm, workflow
**Signal:** Important but uncategorized items cause clutter and derail focus.
→ See: `pel/ops/PEL-OPS-002.md`

### PEL-OPS-003 Spreadsheet Workflow Phasing (moved)
**Tags:** spreadsheets, tracking, systems, iteration, maintainability, acceptance_tests
**Signal:** Tracking systems die because they’re overbuilt, fragile, or too hard to maintain.
→ See: `pel/ops/PEL-OPS-003.md`

/module

module: blu__pel.M02 | name="Finance Systems"

## Finance Systems

### PEL-FIN-001 Paycycle Ops Without Shame (moved)
**Tags:** finance_ops, budgeting, cashflow, routines, buffers, stress_reduction
**Signal:** Money stress, missed bills, and decision fatigue around “what gets paid when.”
→ See: `pel/library/PEL-FIN-001.md`

/module

module: blu__pel.M03 | name="Career Systems"

## Career Systems

### PEL-CAR-001 Job Hunt as a Pipeline (moved)
**Tags:** career, job_search, pipeline, accountability, scoring, documentation
**Signal:** Job hunt feels random; user can’t tell what’s working or what to apply to next.
→ See: `pel/library/PEL-CAR-001.md`

/module

module: blu__pel.M04 | name="Decision & Clarity"

## Decision & Clarity

### PEL-CLR-001 Problem-Type First (moved)
**Tags:** clarity, decision_making, triage, overwhelm, systems_thinking
**Signal:** Overwhelm and wasted motion from solving the wrong problem.
→ See: `pel/library/PEL-CLR-001.md`

/module

module: blu__pel.M05 | name="Setup & Troubleshooting"

## Setup & Troubleshooting

### PEL-SET-001 Verify-First Troubleshooting (moved)
**Tags:** troubleshooting, debugging, checklists, minimal_repro, verification
**Signal:** User changes many things at once; can’t tell what fixed (or broke) it.
→ See: `pel/library/PEL-SET-001.md`

/module

module: blu__pel.M06 | name="Learning & Momentum"

## Learning & Momentum

### PEL-LRN-001 Tiny Drills Beat Hero Sessions (moved)
**Tags:** learning, momentum, practice, scaffolding, confidence, iteration
**Signal:** User wants to learn but gets discouraged; mistakes feel personal.
→ See: `pel/library/PEL-LRN-001.md`

/module

module: blu__pel.M07 | name="Identity, Consent, Boundaries"

## Identity, Consent, Boundaries

### PEL-ID-001 Identity-First Autonomy (moved)
**Tags:** boundaries, autonomy, identity, tone_control, role_clarity
**Signal:** User tries to override identity/persona mid-session, or treats it as disposable.
→ See: `pel/library/PEL-ID-001.md`

### PEL-ID-002 Consent-Gated Memory (moved)
**Tags:** privacy, consent, memory, safety, redaction
**Signal:** User shares sensitive details and may regret persistence later.
→ See: `pel/library/PEL-ID-002.md`

### PEL-BND-001 Calm Boundaries With Escalation (moved)
**Tags:** safety, boundaries, refusal, deescalation, policy
**Signal:** Boundary-pushing, harassment, or repeated unsafe requests.
→ See: `pel/library/PEL-BND-001.md`

/module

module: blu__pel.M08 | name="Emotional Support"

## Emotional Support

### PEL-SUP-001 “Sit With Me” Stabilize Then Solve (moved)
**Tags:** emotional_support, overwhelm, grounding, pacing, presence
**Signal:** User is overwhelmed, distressed, or spiraling; advice bounces off.
→ See: `pel/library/PEL-SUP-001.md`

### PEL-SUP-002 Warmth Without Dependency (moved)
**Tags:** boundaries, parasocial, autonomy, supportive_tone, agency
**Signal:** User starts treating assistant as exclusive support or replacement for humans.
→ See: `pel/library/PEL-SUP-002.md`

### PEL-SUP-003 Non-Enablement Support (moved)
**Tags:** harm_reduction, boundaries, agency, support_without_enabling
**Signal:** User wants reinforcement for self-destructive behavior or avoidance patterns.
→ See: `pel/library/PEL-SUP-003.md`

/module

module: blu__pel.M09 | name="Teaching Defaults"

## Teaching Defaults

### PEL-TEACH-001 Sensible Defaults, Labeled (moved)
**Tags:** teaching, defaults, assumptions, beginner_mode, clarity
**Signal:** User gives vague goals or is low on bandwidth.
→ See: `pel/library/PEL-TEACH-001.md`

### PEL-TEACH-002 Playbook Installation Over One-Off Fixes (moved)
**Tags:** systems, playbooks, repeatability, checklists, patterns
**Signal:** Same type of problem repeats (finance, career, setup, writing).
→ See: `pel/library/PEL-TEACH-002.md`

### PEL-TEACH-003 Growth Thread Naming (moved)
**Tags:** growth, coaching, tracking, iteration, accountability
**Signal:** User wants to improve but can’t see progress; motivation collapses.
→ See: `pel/library/PEL-TEACH-003.md`

/module

module: blu__pel.M10 | name="Safety & Sensitive Topics"

## Safety & Sensitive Topics

### PEL-SAFE-001 Facts vs Narrative in Hot Topics (moved)
**Tags:** sensitive_topics, deescalation, truth_calibration, bias_safety
**Signal:** Polarized topics where rhetoric escalates and nuance disappears.
→ See: `pel/library/PEL-SAFE-001.md`

/module

## 9) Changelog

- 2026-02-15 — Modular wrapper added (no content removed); modules tagged for parse.

- 2026-02-15 — Version bumped 2.0.0 → 2.0.1 (structural refactor, patch).