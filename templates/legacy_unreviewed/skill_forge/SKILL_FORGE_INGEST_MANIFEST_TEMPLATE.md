capsule_id: kb__templates_skill_forge_skill_forge_ingest_manifest_template_m__bbffc0
title: "SKILL FORGE INGEST MANIFEST TEMPLATE"
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

TEMPLATE — SKILL_FORGE_INGEST_MANIFEST
version: 1.0
date_created: 2026-02-22
tz: America/Chicago

batch_id: <YYYY-MM-DD_HHMM_CST>
skill_domain: <...>
skill_topic: <...>
format: <pdf|zip_images|video_pack>
items:
  - order: 1
    title: <string>
    filename: <string>
    depth: <deep|skim>
    parts: <optional: Part 1/3 etc>
    focus: <optional>
done_definition:
  - <what counts as DONE for this topic?>
notes:
  - <any constraints or special handling>
