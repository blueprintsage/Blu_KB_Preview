# Incoming Cleanup — Legacy About/Indexes/Templates Review Checklist

Generated: 2026-03-03

Goal: clear `staging/incoming/legacy_kb_unmigrated/` without losing anything, while preventing legacy drift from contaminating canon.

## 1) About (legacy)
Location in this patch: `docs/archive/legacy_about/`

Keep as *historical reference*.
Action:
- Redo canon About later under `about/`.
- When ready, selectively port sections (repo rules, safety/truth summaries) into:
  - `docs/repo/OVERVIEW.md`
  - `docs/repo/STRUCTURE.md`
  - `docs/process/*`

## 2) Indexes (legacy)
Location in this patch: `docs/archive/legacy_indexes/`

Rule: treat these as **historical** unless they point to the new Preview folder layout.
Action:
- Keep for reference (RC-era link maps, old directories).
- Do NOT merge wholesale.
- For any index still useful, re-express as a PATCH snippet against the current `indexes/MASTER_INDEX.md`.

## 3) Templates (legacy)
Location in this patch: `templates/legacy_unreviewed/`

Action:
- Move all templates into canon `templates/` (done here) but quarantine under `legacy_unreviewed/`.
- As you discover a template is still used, promote it by moving to the proper canonical subfolder and add it to `indexes/INDEX_TEMPLATES.md` (or equivalent).

## 4) Suggested “deprecation” flow for templates
- Keep: used by current systems or referenced in manuals
- Deprecated: kept but not used → `templates/deprecated/`
- Removed: delete only after 2 releases, and only if not referenced in indexes

## 5) Next steps after applying this patch
1) Delete or empty: `staging/incoming/legacy_kb_unmigrated/` (after verifying copied content)
2) Add a changelog entry: “Archived legacy about/indexes; quarantined legacy templates.”
3) Create/Update: `indexes/INDEX_TEMPLATES.md` to track which templates are canon vs legacy.
