capsule_id: kb__templates_meta_naming_rules_md__a93b75
title: "naming rules"
date: 2026-02-24
updated: 2026-02-24
version: 0.1.0
status: draft
topic: blu
type: spec
tags: ['templates', '-meta']
sensitivity: medium
visibility: shared
source: repo
domain: templates
schema: capsule_header_v1.1
body_schema: blu_modular_v1
---

module: blu__templates.03 | name="Template Naming Rules"

# Naming Rules

## Goal
Names should sort well, be readable, and encode size + variant + version.

## Pattern
<domain>_<type>_<size>_<variant>_v<version>.<ext>

Examples:
- comic_board_11x17_blueline_clean_v1.pdf
- comic_board_11x17_blueline_reference_v1_300dpi.png
- capsule_header_template_v1.md

## Notes
- Use `_300dpi` suffix for raster exports.
- Prefer `v1`, `v2` bumps over ambiguous “final/final2”.

/module
