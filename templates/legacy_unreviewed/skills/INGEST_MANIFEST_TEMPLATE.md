capsule_id: kb__templates_skills_ingest_manifest_template_md__f2fa55
title: "INGEST MANIFEST TEMPLATE"
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

TEMPLATE — INGEST_MANIFEST (per batch)
batch_id: <YYYY-MM-DD_HHMM_CST or other>
topic: <skill_topic>
format: <pdf|zip_images|video_pack>
items:
  - order: 1
    title: <string>
    filename: <string>
    depth: <deep|skim>
    parts: <optional: Part 1/3 etc>
    notes: <optional: what to focus on>
done_definition:
  - <what counts as DONE for this topic?>
