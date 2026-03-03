capsule_id: kb__index_healthcheck_md__7d6dec
title: "HEALTHCHECK"
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

# Repo Health Check
Last updated: 2026-02-20
Find: healthcheck ping raw open

Use this page to verify the repo is reachable end-to-end (UI + raw). If any raw link fails, the repo may be partially broken or GitHub may be lagging.

module: INDEX.HEALTHCHECK.M01 | name="Healthcheck links"
| alias | purpose | open | raw |
|---|---|---|---|
| HC_MASTER_INDEX | Deterministic entrypoint | https://github.com/blueprintsage/Blu_KB/blob/main/index/MASTER_INDEX.md | https://raw.githubusercontent.com/blueprintsage/Blu_KB/refs/heads/main/index/MASTER_INDEX.md |
| HC_TEMPLATES_INDEX | Templates index (Core + Skills) | https://github.com/blueprintsage/Blu_KB/blob/main/index/TEMPLATES_INDEX.md | https://raw.githubusercontent.com/blueprintsage/Blu_KB/refs/heads/main/index/TEMPLATES_INDEX.md |
| HC_SKILLS_INDEX | Skills index | https://github.com/blueprintsage/Blu_KB/blob/main/index/SKILLS_INDEX.md | https://raw.githubusercontent.com/blueprintsage/Blu_KB/refs/heads/main/index/SKILLS_INDEX.md |
| HC_PROTOCOLS_INDEX | Protocols index | https://github.com/blueprintsage/Blu_KB/blob/main/index/PROTOCOLS_INDEX.md | https://raw.githubusercontent.com/blueprintsage/Blu_KB/refs/heads/main/index/PROTOCOLS_INDEX.md |
| HC_REPO_FETCH_RULES | Repo fetch / parsing rules | https://github.com/blueprintsage/Blu_KB/blob/main/templates/_meta/repo_fetch_rules.md | https://raw.githubusercontent.com/blueprintsage/Blu_KB/refs/heads/main/templates/_meta/repo_fetch_rules.md |
| HC_SKILL_MODULAR_COVER_LETTERS | New skill: modular cover letters | https://github.com/blueprintsage/Blu_KB/blob/main/libraries/Domain_Libraries/Skills/writing/cover_letters/modular_cover_letters.md | https://raw.githubusercontent.com/blueprintsage/Blu_KB/refs/heads/main/libraries/Domain_Libraries/Skills/writing/cover_letters/modular_cover_letters.md |
| HC_TEMPLATE_DP | DP template | https://github.com/blueprintsage/Blu_KB/blob/main/templates/skills/dp/DP_TEMPLATE.md | https://raw.githubusercontent.com/blueprintsage/Blu_KB/refs/heads/main/templates/skills/dp/DP_TEMPLATE.md |
| HC_TEMPLATE_PD | PD template | https://github.com/blueprintsage/Blu_KB/blob/main/templates/skills/pd/PD_TEMPLATE.md | https://raw.githubusercontent.com/blueprintsage/Blu_KB/refs/heads/main/templates/skills/pd/PD_TEMPLATE.md |
| HC_TEMPLATE_FUNDAMENTALS | Fundamentals template | https://github.com/blueprintsage/Blu_KB/blob/main/templates/skills/fundamentals/FUNDAMENTALS_TEMPLATE.md | https://raw.githubusercontent.com/blueprintsage/Blu_KB/refs/heads/main/templates/skills/fundamentals/FUNDAMENTALS_TEMPLATE.md |
| HC_COMIC_BOARD_PNG | Comic board (PNG, preferred) | https://github.com/blueprintsage/Blu_KB/blob/main/templates/art/comics/boards/comic_board_11x17_blueline_clean_300dpi.png | https://raw.githubusercontent.com/blueprintsage/Blu_KB/refs/heads/main/templates/art/comics/boards/comic_board_11x17_blueline_clean_300dpi.png |
/module

Notes:
- If GitHub/raw seems stale, append a cache-buster query: `?v=1` (change the number).
- PNG boards are the supported default; PDFs are optional.
