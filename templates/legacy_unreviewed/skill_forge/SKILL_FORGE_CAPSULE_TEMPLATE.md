capsule_id: kb__templates_skill_forge_skill_forge_capsule_template_md__00c08d
title: "SKILL FORGE CAPSULE TEMPLATE"
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

TEMPLATE — SKILL_FORGE_CAPSULE
version: 1.1
date_created: 2026-02-22
tz: America/Chicago
intent: Repo-stored capsule that runs Skill Forge for a topic and defines exports on DONE.

# 0) Capsule Header (fill these)
skill_domain: <art|cooking|coding|writing|...>
skill_topic: <topic_slug>
scope:
  in: <what this topic covers>
  out: <explicitly out of scope>
target_level: <beginner|intermediate|advanced>
sources_expected: <N or unknown>
preferred_ingest: <zip_images|pdf|video_pack>
constraints:
  max_upload: 512MB per prompt
  gate0: validate completeness before processing

# 1) Core Libraries Policy (single source of truth)
single_source_of_truth:
  patterns: core_library/patterns/ (PAT-*)
  drills_pd: core_library/drills/pd/ (PD-*)
  drills_dp: core_library/drills/dp/ (DP-*)
topic_pack_rule:
  - Topic packs SHOULD link to Core Libraries via playlists and outline links.
  - Topic packs SHOULD NOT duplicate drill/pattern content in normal repo docs.
  - COLD_STORE_KNOWLEDGE MUST embed full content (backup is link-independent).

# 2) Ingest Contract
input_label_format: “Item N/Total — <title> — deep|skim — focus(optional) — format: pdf|zip_images|video_pack — part(optional)”
gate0_validate:
  pdf:
    - check page count and truncation; STOP if partial
  zip_images:
    - check file count and naming/range; STOP if missing pages
  video_pack:
    - check subs present + frames timestamped + manifest present + size < 512MB; STOP if missing

# 3) Extraction Rules
truth_discipline: FACT vs INFERENCE vs BLOCKER
dedupe_rule:
  - consensus → canon
  - disagreements → VARIANTS (when/why)
token_discipline:
  - per-item summary + new-vs-duplicate + patch notes
  - avoid reprinting full masters each turn

# 4) Routing + Exit Criteria
routing_map_file: course/ROUTING_MAP.md
exit_criteria_file: course/EXIT_CRITERIA.md
rule:
  - DP results route to PD/PROC (don’t say “practice more” without mapping)

# 5) Running Outputs (topic-scoped working set)
- canon/CANON.md
- procedures/PROCEDURES.md
- course/COURSE_OUTLINE.md (links to PD/DP/VTA)
- course/TOPIC_PD_PLAYLIST.md (links)
- course/TOPIC_DP_PLAYLIST.md (links)
- sources/SOURCES.md
- vta/DIAGRAM_TASKS.md (VTA plan)
