capsule_id: kb__templates_skill_forge_walkthrough_skill_forge_md__6fc77a
title: "WALKTHROUGH SKILL FORGE"
date: 2026-02-24
updated: 2026-02-24
version: 0.1.0
status: draft
topic: blu
type: spec
tags: ['templates', 'skill-forge']
sensitivity: medium
visibility: shared
source: repo
domain: templates
schema: capsule_header_v1.1
body_schema: blu_modular_v1
---

WALKTHROUGH — SKILL FORGE (Operator Card)
version: 1.0
date: 2026-02-22
tz: America/Chicago
audience: Dad (steward/operator)
goal: run a topic end-to-end, export full backup + repo-ready updates, minimal drama.

0) Mental Model
- Core Libraries (single source of truth):
  - core_library/patterns/ (PAT-*)
  - core_library/drills/pd/ (PD-*)
  - core_library/drills/dp/ (DP-*)
- Topic Packs (domain/topic-specific):
  - skills/<domain>/<topic>/ (canon, procedures, course, sources, vta, capsule)
- COLD_STORE_KNOWLEDGE is the catastrophe restore image:
  - full embedded content; never link-dependent.

1) Start a New Topic
1. Create topic folder:
   - skills/<domain>/<topic>/
2. Copy in a filled capsule:
   - skills/<domain>/<topic>/CAPSULE.md
   (copy from templates/skill_forge/SKILL_FORGE_CAPSULE_TEMPLATE.md)
3. Create/confirm standard topic files:
   - canon/CANON.md
   - procedures/PROCEDURES.md
   - course/COURSE_OUTLINE.md
   - course/TOPIC_PD_PLAYLIST.md (links → core_library/drills/pd/)
   - course/TOPIC_DP_PLAYLIST.md (links → core_library/drills/dp/)
   - course/ROUTING_MAP.md (DP → PD/PROC mapping)
   - course/EXIT_CRITERIA.md (graduation requirements)
   - sources/SOURCES.md
   - vta/DIAGRAM_TASKS.md

2) Ingest Workflow (per item)
You upload one item at a time and label it like:
- “Item N/Total — <title> — deep|skim — focus(optional) — format: pdf|zip_images|video_pack — part(optional)”

Blu always performs Gate 0 BEFORE summarizing:
- pdf: page count + truncation check (STOP if partial)
- zip_images: file count + naming/range check (STOP if missing pages)
- video_pack: subs + timestamped frames + manifest + size <512MB (STOP if missing)

If Gate 0 fails: fix transport first (split, re-export images, etc.).

3) What Blu Outputs per Item (token-safe)
For each item:
- Per-item summary (tight)
- What’s new vs duplicate
- Conflicts/variants (A/B + when to use)
- Patch notes (what changed in canon/procedures/PD/DP/outline/sources)
Then Blu asks: “Send the next item?”

4) How We Avoid Dupes/Drift
- Reusable patterns/drills go to Core Libraries (PAT/PD/DP).
- Topic pack holds only topic-specific canon/procedures and links to Core.
- If something disagrees between sources:
  - keep both as VARIANTS with “when/why,” don’t overwrite silently.
- IDs never renumber; deprecate instead.

5) DONE Closeout (the required outputs)
When Dad says “DONE — generate backup + repo pack” Blu produces:

A) COLD_STORE_KNOWLEDGE — <Topic> — GOLDEN RESET
- FULL CONTENT embedded:
  - Canon + Procedures + PD + DP + Course Outline + Mistakes/Fixes + Variants + Sources + VTA plan
- Links optional; nothing link-dependent.

B) Repo Pack ZIP (for updating GitHub)
- Modular files, ready to drop into repo:
  - any new/updated PAT/PD/DP under core_library/
  - topic pack updates under skills/<domain>/<topic>/
  - updated playlists/outlines/routing/exit criteria
  - sources + vta plan
  - README with integration steps

6) Applying a Repo Pack (GitHub Desktop safe path)
1. Unzip the Repo Pack to a temp folder.
2. Copy folders into repo root (merge/overwrite as directed):
   - core_library/...
   - skills/...
   - templates/... (if included)
3. Review changes in GitHub Desktop:
   - confirm moves/renames look right
4. Commit message format:
   - “Skill Forge: <domain>/<topic> closeout (canon+pd+dp+course+vta)”
5. Push.

7) Visual Teaching Artifacts (VTAs)
- DIAGRAM_TASKS.md is the queue.
- VTAs are optional during ingestion; they can be generated after DONE.
- Default VTA types:
  - 4-step cards (Gesture → Block → Rough → Final)
  - diagrams for tricky concepts (ellipses, VP spacing, value families, plane breaks)
- Keep a consistent style; file under:
  - skills/<domain>/<topic>/vta/

8) Naming Conventions (human readable)
- Patterns: PAT-<DOMAIN>-<TOPIC>-### (or PAT-CORE-### if truly universal)
- Practice Drills: PD-<DOMAIN/CORE>-<TOPIC>-### 
- Diagnostics: DP-<DOMAIN/CORE>-<TOPIC>-###
- Visual artifacts: VTA-<DOMAIN>-<TOPIC>-###

9) Transport Rules (hard-won)
- If PDFs truncate or are image-only and huge: prefer zip_images.
- Keep uploads ≤512MB; split into parts.
- If you care about verification: keep sha256 sidecar alongside the zip.

END
Door’s open.