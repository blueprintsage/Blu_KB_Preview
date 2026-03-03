# v0.8.4 Promote Checklist (Phase 5) --- module: kb__ops_checklists_promote_v0_8_4.M01 | name="Promote checklist"
[CAPSULE_HEADER_BEGIN]
mem_id: 2026_02_28__blu__promote-v0-8-4
title: v0.8.4 Promote Checklist (Phase 5)
date: 2026-02-28
status: draft
topic: blu
type: checklist
tags: promote, release, changelog, versioning
sensitivity: medium
visibility: private
source: roadmap
domain: ops
authority: canon
[CAPSULE_HEADER_END]

## Scope lock
- This promote includes Phase 1–5 changes only.
- Any additional work goes to Parking Lot + next patch pack.

## Files must be updated
- `VERSION.md` (if version bumps for this promote)
- `CHANGELOG.md` (entry for this promote)
- Any modified protocol/spec docs referenced by these changes

## Required checks
- Burn-ins: run `ops/burnins/BURNINS_v0.8.4.md` and record results.
- SOFTKICK contract verified manually in a plain-text paste target.
- Parent Gate TTL tests pass.

## Verification (canonical for v0.8.4 Preview)
- Fixed regression seeds (run first): `tests/REGRESSION_SEEDS_v1.md`
- Baseline smoke tests: `tests/SMOKES_v1.md`
- Exec 2.0 smoke add-on (required when Exec touched): `tests/SMOKES_EXEC_v2.md`
- Exec 2.0 SIM TAGS (required when Exec touched): `tests/SIM_TAGS_EXEC_v2.md`

## Promote output
- Tag name: `v0.8.4` (or repo standard)
- Attach burn-in record (or link)
- Ensure docs reference canonical sources (no duplicates)

[/module]
