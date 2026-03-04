# SkillForge — Lesson Runner (Dual-Lane)
Version: v1.0 (Lockdown)
Track: Preview
Updated: 2026-03-03

## What SkillForge is for
SkillForge is the **lesson layer**. It turns a learning request into a sequence of steps that:
- teaches using **Lane A** skill content
- executes/validates using **Lane B** skill content (anti-drift)

Teaching spine (Skeleton → Block → Rough → Final) is applied here as the default lesson structure.

## Where SkillForge lives
Runtime lesson content:
- systems/skill_forge/aps/...

Templates for authoring SkillForge assets:
- templates/skill_forge/...

SkillForge depends on skills living under:
- skills/<domain>/<skill_family>/lane_a and lane_b

## What SkillForge calls
- Skills (Lane A and/or Lane B modules)
- AP modules inside those lane files when executing a request
- Overlays when explicitly selected (style/medium/language); otherwise base only

## Hard laws (non-negotiable)
- SkillForge does not invent missing requirements; **when in doubt, ask**.
- If style/medium/language is not specified, stay in `base`.
- Lesson files (APs) must point to skill entrypoints (skill-family index or lane file), not to deep module dumps in repo indexes.

## What needs done (worklist)
- Add a single canonical SkillForge system spec link in indexes/INDEX_SYSTEMS.md (folder entrypoint only).
- Standardize AP naming and required metadata fields (so APs are searchable and stable).
- Ensure every AP references: skill_id + lane + base/overlay selection rule.
