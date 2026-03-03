# CHANGELOG (Preview Repo)

All notable changes to this repository will be documented in this file.

Format: Keep entries additive. Prefer “Added / Changed / Fixed / Removed”.  
Dates are local: America/Chicago.  

---

## [2026-03-03] — Skill Forge 2.0 Bootstrap (Art + Code + Narrative)

### Added
- Art Core v1.0 (frozen, capsule-uniform, module format):
  - AP-ART-FIGURE-DRAWING-001 (spine)
  - AP-ART-HEADS-001 (child)
  - AP-ART-HANDS-001 (child)
  - AP-ART-WRINKLES-001 (child)
  - indexes/INDEX_APS.md, INDEX_PATTERNS.md, INDEX_SKILLS.md entries
  - about/ART_CORE_v1.0_FREEZE.md marker

- Code Core v0.1 (language-agnostic, capsule-uniform, module format):
  - AP-CODE-SYSTEMS-001 (spine)
  - skills/code/patterns/PATTERNS-CODE.md (patterns-as-law)
  - skills/code/drills/DRILLS-CODE-FOUNDATIONS.md
  - index patch snippets

- Narrative Core v0.1 (cross-medium: comics/storyboards/animation beats/VN):
  - AP-NARRATIVE-SEQUENCES-001 (spine + medium modules)
  - skills/narrative/patterns/PATTERNS-NARRATIVE.md
  - skills/narrative/drills/DRILLS-NARRATIVE-FOUNDATIONS.md
  - index patch snippets

- Ledgers (hash-based):
  - docs/ledger/BOOK_LEDGER_CODE.md
  - docs/ledger/BOOK_LEDGER_ART.md

- PASS runs (repo-safe outputs only):
  - docs/pass_runs/* (code)
  - skills/code/patterns/PATCH_PATTERNS_*.md
  - skills/code/drills/PATCH_DRILLS_*.md

### Notes
- Repo hygiene policy remains: do not commit third-party copyrighted source captures (PDFs, scans, rips). Ledgers + extracted patterns/drills/APs are repo-safe.

---

## [2026-03-03] — RC Keep Items Moved to Canon

### Added
- ops/ (burnins + promotion checklists)
- tests/ (smokes + regression seeds)
- tools/ (repo utilities + diagnostics)
- tasks/CPM/ (Critical Path Manager templates/validators)
- reports/ (RC SIM report)

### Notes
- Engine patch contract moved under contracts/engine_patches/.
- Capsule-like engine_patch file (05_USERCAP.md) intentionally not copied into canon.

---

## [2026-03-03] — RC Low-Priority Triage

### Added
- docs/archive/rc/ (archived RC-era materials)
- staging/outgoing/rc_keep/ (selected KEEP items staged for canonical placement)

### Notes
- This triage is heuristic. Review TRIAGE_REPORT.md before deleting legacy rc_low_priority in staging.

---