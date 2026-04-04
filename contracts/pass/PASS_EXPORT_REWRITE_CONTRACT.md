# PASS Export Rewrite Contract
updated: 2026-04-03
tz: America/Chicago
status: canon
version: 1.0

## Purpose
Define the required outputs for Stage 8 export and the full-rewrite rule for repo artifacts.

## Global laws
- Objects are emitted as full rewritten files, not partial object patches.
- Parent files are fully rewritten when `variants[]` changes.
- Index files are fully rewritten when changed.
- PASS may not claim full success without emitted artifacts.
- If export cannot produce required rewrite targets, PASS must stop and label the run as partial-stage.

## Compare outcomes
- ADD -> new full object file
- UPDATE -> full rewritten replacement object file
- VARIANT -> full rewritten parent object file
- REJECT -> reject log only

## Required emitted artifacts for full success
- repo_drop tree
- normalized object files
- rewritten category/subcategory indexes
- retrieval profile tree
- source record
- run summary
- reject log
- zip bundle

## Repo-drop layout
`repo_drop/` mirrors the destination repo structure exactly.

Human-canonical object paths:
- `skills/<Category>/<Subcategory>/patterns/<slug>.md`
- `skills/<Category>/<Subcategory>/drills/<slug>.md`
- `skills/<Category>/<Subcategory>/aps/<slug>.md`

Machine-canonical retrieval paths:
- `indexes/retrieval/skills/<Category>/<Subcategory>/manifest.json`
- `indexes/retrieval/skills/<Category>/<Subcategory>/patterns/<slug>.json`
- `indexes/retrieval/skills/<Category>/<Subcategory>/drills/<slug>.json`
- `indexes/retrieval/skills/<Category>/<Subcategory>/aps/<slug>.json`

## Truth rule
Anything that stops before required export artifacts exist must be labeled partial-stage.