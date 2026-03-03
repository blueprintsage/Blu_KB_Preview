capsule_id: kb__index_global_conventions_md__f457fc
title: "Global Conventions"
date: 2026-02-24
updated: 2026-02-24
version: 0.1.0
status: draft
topic: blu
type: spec
tags: ['index']
sensitivity: medium
visibility: shared
source: repo
domain: index
schema: capsule_header_v1.1
body_schema: blu_modular_v1
---

<!--
Global Conventions (canonical)
Extracted from legacy Interim repo index into a single edit point.
Paste-safe: no YAML front matter.
-->

# Global Conventions

## ID & Naming
- **Domain Pack ID:** `DP-<AREA>-###` (e.g., `DP-VID-001`)
- **Pattern ID:** `PAT-<AREA>-###` (e.g., `PAT-CORE-001`)
- **Schema blocks** are written as bullet fields with required/optional markers.
- **Checks** must be observable and testable.
- **Failure-modes** are formatted: `Symptom → Likely cause → Fix`.
- **Knobs** are user-invokable toggles that map to direct edits.

## Universal Output Spine (default)
1) **Goal / Title (1 line)**  
2) **Deliverable** (the thing itself, or the plan to produce it)  
3) **Schema** (fields + constraints)  
4) **Checks** (2–7)  
5) **Failure-modes** (3–10)  
6) **Knobs** (6–12)  
7) **Next step** (one minimal move)

## Universal Knob Categories (starter set)
- Length (shorter/longer)
- Tone (more formal / warmer / more intense)
- Specificity (more concrete / more abstract)
- Structure (bullets / narrative / table)
- Pace (faster / slower)
- Risk (safer / edgier within policy)
- Focus (more on X, less on Y)
- Detail (add examples / remove examples)

---

---

module: gc.M99 | name="Maintenance"
## Maintenance
- Canonical source: `index/Global_Conventions.md`
- Edit conventions here; keep other files linking to this.
/module

*Last updated:* 2026-02-15
