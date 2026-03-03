# Blu_KB — Repo Canon (Templates • Skills • PEL • Homeschool Index)

module: repo.M00 | name="Scope Lock"
## Scope Lock (hard boundary)

This repo contains **canon, reusable knowledge** and **templates** for Blu (repo-first).

✅ Includes:
- **Indexes** (navigation + entrypoints for skills/templates)
- **Skills** (course assets, drills, procedures, routing maps)
- **Core Library** (shared PD/DP drills and reusable procedures)
- **Templates** (docs, skills scaffolds, memory/project formats, cold_store templates)
- **PEL** (Public Experience Library) + PEL ops modules
- **Homeschooling support** (planning/log formats + index pointers)
- **Tools/scripts** (repo hygiene utilities; optional)

🚫 Excludes (do not commit):
- Personal info, family memories, student logs, report cards
- Parent secrets (passphrases, hashes, HMAC keys)
- Anything “private runtime state” for a household

**Privacy rule:** Repo stays safe to share publicly. Household data lives local-only.
/module


module: repo.M01 | name="Quick Start"
## Quick Start

- Browse repo to find:
  - Templates: `/templates/`
  - Skills: `/skills/`
  - Homeschool index: `/homeschool/`
  - PEL: `/pel/`
  - Tasks (e.g., CPM dormant): `/tasks/`

Notes:
- Homeschool content here is an **index + planning layer** (links). Curriculum remains on the source sites.
- If using SCHOOL Mode with a family, keep logs/keys in a local `family_private/` folder (gitignored).
/module


module: repo.M02 | name="Directory Layout (canon)"
## Directory Layout (canon)

```
/index/
  MASTER_INDEX.md
  ASSET_INDEX.md

/templates/
  docs/
  art/
  assets/
  indexes/
  kb/
  school/

/skills/
  art/
  writing/
  gamedev/
  ...

/pel/
  library/
  ops/

/tasks/
  CPM/

/homeschool/
  index.md
  docs/
  ep_levels/
  high_school/
  subjects/

/tools/
  (optional scripts)

/00_Instructions.md
/01_Identity.md
/02_Operations_Law.md
/03_Commands.md
/04_Engine.md
/05_USERCAP.md
/06_Tasks.md
/07_Teaching.md
```

/module


module: repo.M03 | name="Naming Conventions"
## Naming Conventions

### Capsule IDs (preferred)
- `capsule_id` matches the file header number (e.g., `blu__04` for Engine)
- Module IDs: `blu__04.M01`, `blu__03.M18`, etc.

### Skills content (DP/PD)
- DPs: `DP-<SKILL>-<SUB>-###.md`
- PDs: `PD-<SKILL>-<SUB>-###.md`
- Rule: PDs live under the subfolder they train.

### Assets
- Images: `IMG-<THEME>-####.(png|jpg|webp)`
- Video refs: `VID-<THEME>-####.(mp4|mov|gif)`
- Optional metadata sidecar: same name + `.yml` (template provided)

/module


module: repo.M04 | name="Homeschool Index Rules (no curriculum copying)"
## Homeschool Index Rules (no curriculum copying)

- `/homeschool/` is a **link index + planning layer**.
- Do **not** copy/paste full curriculum content into this repo.
- Always include:
  - Source credit
  - Homeschool law note (requirements vary by state/region)
  - Donate/support link when available

Recommended: Put parent-facing setup docs under `/homeschool/docs/`.
/module


module: repo.M05 | name="Git Hygiene / Private Data"
## Git Hygiene / Private Data

Do not commit household runtime files. Suggested local-only folder:
- `family_private/`
  - `<Student>_Log_Current.md`
  - parent private caps (secrets/keys)
  - report exports

Add patterns to `.gitignore` (example):
- `family_private/`
- `*_Log_Current.md`
- `*_Parent_Private*.md`

/module


module: repo.M06 | name="GitHub Raw Cache Note"
## GitHub Raw Cache Note

Sometimes `raw.githubusercontent.com` can appear stale.
If a raw file looks wrong:
- open the GitHub UI version to confirm, and/or
- add a cache-bust query (e.g., `?v=<commit>`).

/module


module: repo.M09 | name="Bootstrap Checklist"
## Bootstrap Checklist

- [ ] Keep canon knowledge in repo; keep private family state local-only
- [ ] Use module blocks consistently (`module: ...` / `/module`)
- [ ] Keep `homeschool/` as an index (links + notes), not copied curriculum
- [ ] Ensure every DP/PD is discoverable from a local index
- [ ] Prefer deprecate over delete: `INTAKE → DRAFT → ACTIVE → DEPRECATED`

/module

*Last updated:* 2026-02-19


---

## Repo stability
This repo follows **REPO_LAYOUT_CONTRACT.md**. If something feels like it keeps moving, start there.


## Release
See `protocols/RELEASE_PROTOCOL_v1.md` for RC/Release gates (tags + smokes + sims + changelog).
