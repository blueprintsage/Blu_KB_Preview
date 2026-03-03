## Unreleased

- Added PASS:GUT Protocol v1 + PASS:GUT ART smoke; added DP-WRI-004 drills; added PAT-ART palette/light/material/value/ornament patterns; added Exec v2 smokes/tags.
- Added PASS:GUT Protocol v1 + PASS:GUT ART smoke/regression seed; added ART patterns + creative writing drills; added Exec v2 smokes/tags.
- Scope lock enforcement: stay-in-scope + Parking Lot (max 1–2 bullets); “felt missing” diagnostic.
- RC gate: tags + smoke tests required; fixed regression seeds + sim report required for RC/Release.
- Art Stack: medium-first gate, Discovery Mode, Light Box/Onion Skin, DRAW_4STEP_CORE (S0–S3), FINISH_STACK (Step 4).
- School reliability: class lock, answer gate (3 attempts), refusal→0, schedule autopilot.

# Changelog

## 2026-02-26
- Merged repo-safe PDF GUT mechanics pack (Death Gate Cycle → writing patterns/APs/drills + comics dialogue economy).
- Added Comics Layout Layering System v1.1 and Skill Forge Sequential Page Integrity drills.
- Updated Lexicon: “kernel capsules”.

## 0.8.2 — 2026-02-25

### Reminders (Hosted Mode)
- Hosted chat note: automatic “tick-on-inbound” is not guaranteed by the host runtime; use `TICK` / `REMINDERS:TICK` (or `TICK NOW ...`) to force evaluation.
- Added deterministic evaluation command: `TICK NOW YYYY-MM-DD HH:MM TZ America/Chicago`.
- Added staged pre-alerts: **T-60**, **T-10**, then **DUE** (priority: DUE > T-10 > T-60).
- Standardized reminder output to a personable chat-style alert (no fenced blocks), while preserving “emit-first, then stop” behavior.

### School Engine (Day 125 regression fix)
- Added **Completion Gate**: prevent class switching/advancing while a class block is pending; require explicit user choice to resolve state.
- Added **Practice vs Graded** separation: formal score/letter outputs only after explicit submission intent.
- Hardened submission intent: only the current message may trigger graded mode; banned “external submission proof” references.

### Release engineering
- Adopted repo-facing vocabulary: `artifact_role = release|preview`.
- Prepared migration plan to store canonical version + changelog in repo files (this file + `VERSION.md`) to prevent header mismatches.


## 0.8.4-phase2 — 2026-02-28
- Exec v2.0: added formal Exec state schema + debug trace spec + golden regression pack scaffolding.
- Exec v2.0: normalized Universal Proposal Contract (required `propose(state, now_utc, context)` signature; required proposal fields incl. `computed_suppress_key`, `escalation_rank`, `flags`).

## 0.8.4-phase3 — 2026-02-28
- Programs: define canonical Program Registry and Program ABI contract (modules propose; Exec prints; selected-only state deltas).
- Exec: universal module wrapper now documents `lines/state_delta/events` alongside proposals.


## 0.8.4-phase4 — 2026-02-28
- Parent Gate: canonical TTL/session unlock semantics; `PARENT:LOCK` immediate relock; no “spent keyfile” persistence assumptions.
- Wizards/templates: updated Parent Gate key policy text to reference canonical TTL spec.

## 0.8.4-phase5 — 2026-02-28
- Release ops: added v0.8.4 burn-in suite and promote checklist to support repeatable promotion.
