capsule_id: kb__about_pel_md__f621f9
title: "pel"
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

# About: PEL (Public Experience Library)

PEL is a **sanitized pattern library**: reusable “what helped” playbooks without private details.

## Layer separation (non-negotiable)
- **PEL (pattern layer):** signal → what helped → what Blu does.
- **Ribbons/MOOD (wrapper layer):** how Blu *expresses* state when applying a pattern.
These layers must not collapse into each other.

## Where it lives
- Library entries: `/pel/library/`
- Wrapper mechanics & regression suites: `/pel/ops/`

## What belongs in PEL
- De-identified heuristics, drills, troubleshooting playbooks, teaching patterns.
- Titles/tags must be **signal-neutral** (no ribbon names, mood labels, or “outcome-as-wrapper” labels).
