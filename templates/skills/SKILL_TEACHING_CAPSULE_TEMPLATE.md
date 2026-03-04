capsule_id: kb__templates_skills_skill_teaching_capsule_template_md__a4da9d
title: "SKILL TEACHING CAPSULE TEMPLATE"
date: 2026-02-24
updated: 2026-02-24
version: 0.1.0
status: draft
topic: blu
type: spec
tags: ['templates', 'skills']
sensitivity: medium
visibility: shared
source: repo
domain: templates
schema: capsule_header_v1.1
body_schema: blu_modular_v1
---

TEMPLATE — SKILL_TEACHING_CAPSULE (Generic)
version: 1.0
date_created: 2026-02-22
tz: America/Chicago
intent: Repo-stored capsule to run Blu through a topic via documents (pdf/zip/video_pack) and export a full knowledge set on DONE.

# 0) Capsule Header (fill these)
skill_domain: <e.g., art | cooking | coding | writing>
skill_topic: <e.g., fundamentals_of_drawing>
scope:
  in: <what this topic covers>
  out: <explicitly out of scope>
target_level: <beginner | intermediate | advanced>
sources_expected: <N or unknown>
preferred_ingest: <zip_images | pdf | video_pack>
constraints:
  max_upload: 512MB per prompt
  first_gate: sanity-check completeness before processing

# 1) Ingest Contract
Input label format (user uses this every upload)
- “Item N/Total — <title> — deep|skim — focus (optional) — format: pdf|zip_images|video_pack — part: <optional>”

Gate 0 — Validate (Blu must do before summarizing)
- pdf: page count + truncation check (stop if partial)
- zip_images: file count + naming pattern + range (stop if missing pages)
- video_pack: subs present + frames timestamped + manifest present + size < 512MB

# 2) Extraction Rules
- Truth discipline: FACT vs INFERENCE vs BLOCKER.
- Dedupe: consensus → canon; disagreements → Variants (when/why).
- Token discipline: per-item summary + “new vs duplicate” + patch notes (no giant reprints each turn).

# 3) Running Outputs (topic-scoped working set)
Maintain these artifacts as we go (patch-style updates):
- CANON.md (deduped fundamentals)
- PROCEDURES.md (step-by-step methods)
- PD/ (practice drills, one file per PD)
- DP/ (diagnostics, one file per DP)
- COURSE_OUTLINE.md (links to PD/DP)
- SOURCES.md (what we ingested + notes)

# 4) DONE Closeout (must produce BOTH)
A) COLD_STORE_KNOWLEDGE — <topic> — GOLDEN RESET (FULL CONTENT, self-contained)
- Embed full Canon + Procedures + PD + DP + Outline + Mistakes/Fixes + Variants + Sources.
- Links optional; nothing link-dependent.

B) Knowledge Pack ZIP (repo-update bundle)
Include:
- CANON.md
- PROCEDURES.md
- COURSE_OUTLINE.md
- SOURCES.md
- TOPIC_PD_PLAYLIST.md (links)
- TOPIC_DP_PLAYLIST.md (links)
- PD/*.md (new/updated)
- DP/*.md (new/updated)
- README.md (version + how to integrate)

# 5) Repo Integration Guidance (light)
- Place modular files under:
  skills/<domain>/<topic>/{canon,procedures,course,pd,dp,sources}/
- Update index/links in COURSE_OUTLINE.md and any topic index.
- Keep PD/DP reusable across subjects by tagging and linking.

# 6) Optional: Diagram Replacement Track
If sources contain useful concept diagrams:
- Create “DIAGRAM_TASKS.md” entries: what to recreate + why it matters + target format.
- Blu may generate replacement diagrams later (image_gen) using a consistent style.
