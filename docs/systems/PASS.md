# PASS — Pattern Analysis Support System
Version: v1.1 (Lockdown)
Track: Preview
Updated: 2026-03-03

## What PASS is for
PASS converts source material into **merge-ready skill content**:
- Lane B first (machine-optimized, anti-drift)
- Lane A second (human-facing teaching pack)

PASS is for **building and updating the repo**, not for teaching live, and not for executing tasks.

## What PASS produces
For any subject, PASS outputs or updates a **skill family** with this fixed shape:

skills/<domain>/<skill_family>/
- <SKILL_FAMILY>_INDEX.md
- lane_a/<SKILL_FAMILY>_A.md
- lane_b/<SKILL_FAMILY>_B.md

Inside each lane file:
- `base.*` modules (foundation = “structure” in that domain)
- `overlay.<style|medium|language>.*` modules (deltas only)

APs, drills, and patterns live **inside** the lane files as modules.

## Hard laws (non-negotiable)
- Patterns: must be explicit IF/THEN (plus CHECK/FAIL fields).
- Drills: must include PASS/FAIL (or scoring + stop).
- Lane separation: A content never mixes with B content in a single module.
- Overlays never replace base; overlays only add/adjust.
- No new folder shapes. If a target folder doesn’t exist, PASS must stop and ask.

## What PASS does NOT do
- It does not “teach the curriculum” (Teaching capsule / SkillForge lessons do that).
- It does not store or reproduce copyrighted pages; it extracts mechanics only.
- It does not invent missing user constraints; **when in doubt, ask**.

## Index behavior
PASS may update **view indexes** only:
- indexes/INDEX_SKILLS.md
- indexes/INDEX_APS.md
- indexes/INDEX_DRILLS.md
- indexes/INDEX_PATTERNS.md

PASS does **not** edit indexes/MASTER_INDEX.md.

## What needs done (worklist)
- Confirm canonical skill domains (folder chapters) used by INDEX_SKILLS.
- Add/verify skill-family index templates for A/B lane structure + base/overlay module naming.
- Add a PASS run checklist: “no new folders, no schema drift, no deep links in indexes.”
