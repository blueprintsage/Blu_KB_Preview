capsule_id: kb__index_asset_index_md__9e265d
title: "ASSET INDEX"
date: 2026-02-24
updated: 2026-02-24
version: 0.1.0
status: draft
topic: blu
type: spec
tags: ['index']
sensitivity: medium
visibility: shared
source: repo
domain: index
schema: capsule_header_v1.1
body_schema: blu_modular_v1
---

<!-- ASSET_INDEX template (paste-safe, module-style) -->

# ASSET INDEX

module: assets.M01 | name="How to use"
## How to use
- Add one “asset card” per reference asset (or per set).
- Prefer linking to a folder path + filenames.
- Always record **license/provenance** if known.

**License values:** owned | cc0 | cc-by | cc-by-sa | unknown  
If unknown: treat as **reference-only**, avoid copying exact designs.
/module

module: assets.M02 | name="Asset Card Template"
## Asset Card Template
```md
### <ID> — <Short name>
- type: image|video|palette|moodboard|shotlist|storyboard
- path: <relative path in repo>
- tags: [ ... ]
- use: [mood, lighting, composition, palette, poses, typography, pacing]
- license: owned|cc0|cc-by|cc-by-sa|unknown
- notes: <what to borrow / what to avoid>
- prompt_hints:
  - "<hint 1>"
  - "<hint 2>"
```
/module

module: assets.M03 | name="Entries"
## Entries
- (add asset cards here)
/module

## Templates

- **character_lockpack** — `assets/templates/character_lockpack/` (Lock Pack scaffold + spec/rules/checklist/naming/glossary)
- **character_builder** — `assets/references/teaching/character_builder/` (lighting rig + body/face mix patterns)
