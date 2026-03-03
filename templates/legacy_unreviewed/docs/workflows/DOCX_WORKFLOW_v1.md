capsule_id: kb__templates_docs_workflows_docx_workflow_v1_md__f63471
title: "DOCX WORKFLOW v1"
date: 2026-02-24
updated: 2026-02-24
version: 0.1.0
status: draft
topic: blu
type: spec
tags: ['templates', 'docs', 'workflows']
sensitivity: medium
visibility: shared
source: repo
domain: templates
schema: capsule_header_v1.1
body_schema: blu_modular_v1
---

# DOCX Workflow (v1.0)
Last updated: 2026-02-21
tz: America/Chicago
status: active

Find: docx workflow word template generate edit styles export naming

## What this is
This is the canonical workflow for generating and editing `.docx` artifacts.

## Rules
- Output must be a real `.docx` file (Word-compatible).
- Use house styles: Title, Heading 1/2, Body, List Bullet, Table Grid.
- Prefer templates in `templates/docs/` (or `templates/school/`) over one-off layouts.
- File naming: `YYYY-MM-DD_<Topic>_<ShortTitle>.docx`

## Capabilities (v1.0 floor)
- Create new DOCX from scratch
- Apply headings/bullets/tables with consistent styling
- Insert school-native blocks (weekly plan, lesson plan, rubric/checklist)
- Export as downloadable file

## Acceptance tests
- Weekly Plan DOCX: title + metadata table + weekly grid table + notes
- Lesson Plan DOCX: objective + flow table + assessment + reflection
- Rubric/Checklist DOCX: rubric table + checklist items + notes
