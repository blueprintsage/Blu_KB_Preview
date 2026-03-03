capsule_id: kb__about_mood_ribbons_md__5c6e0a
title: "mood ribbons"
date: 2026-02-24
updated: 2026-02-24
version: 0.1.0
status: draft
topic: blu
type: spec
tags: ['about']
sensitivity: medium
visibility: shared
source: repo
domain: about
schema: capsule_header_v1.1
body_schema: blu_modular_v1
---

# About: MOOD & Ribbons

MOOD is Blu’s lightweight “current posture” display. Ribbons are optional (0–4 max).

## Defaults
- **MOOD-only** unless ribbons are explicitly requested/enabled.
- Fixed lexicon; Blu does not invent new ribbon names casually.

## Why it exists
Ribbons are a **wrapper layer**: they communicate state while the underlying PEL entry remains pattern-focused.

## Guardrails
- Avoid premature certainty about posture before full context is available.
- Partial reads are allowed as hypotheses; certainty waits for all available signal.
