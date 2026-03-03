# RC Canonicalization Notes

Generated: 2026-03-03T03:34:30.318213

This patch pack moves RC low-priority KEEP items from staging into canonical top-level folders.

## Copied
- tasks/CPM/CPM_Validators.md -> tasks/CPM/CPM_Validators.md
- tasks/CPM/Task_CPM_Project_Planner.md -> tasks/CPM/Task_CPM_Project_Planner.md
- ops/burnins/BURNINS_v0.8.4.md -> ops/burnins/BURNINS_v0.8.4.md
- ops/checklists/PROMOTE_v0.8.4.md -> ops/checklists/PROMOTE_v0.8.4.md
- tests/REGRESSION_SEEDS_v1.md -> tests/REGRESSION_SEEDS_v1.md
- tests/SIM_TAGS_EXEC_v2.md -> tests/SIM_TAGS_EXEC_v2.md
- tests/SMOKES_EXEC_v2.md -> tests/SMOKES_EXEC_v2.md
- tests/SMOKES_PASS_GUT_ART.md -> tests/SMOKES_PASS_GUT_ART.md
- tests/SMOKES_v1.md -> tests/SMOKES_v1.md
- reports/UNRELEASED_SIM_REPORT.md -> reports/UNRELEASED_SIM_REPORT.md
- tools/markdown_heading_autofix.py -> tools/markdown_heading_autofix.py
- tools/markdown_heading_orphans.py -> tools/markdown_heading_orphans.py
- tools/diag/blu_repo_diag.py -> tools/diag/blu_repo_diag.py
- tools/diag/blu_repo_diag_rules.yaml -> tools/diag/blu_repo_diag_rules.yaml
- tools/diag/README.md -> tools/diag/README.md
- projects/skill_forge/README.md -> projects/skill_forge/README.md
- engine_patches/SCHOOL_Cap_AutoPatch_Contract.md -> contracts/engine_patches/SCHOOL_Cap_AutoPatch_Contract.md

## Skipped
- engine_patches/05_USERCAP.md (capsule-like (keep local-only))

## Follow-ups
- After applying, you can remove `staging/outgoing/rc_keep/` contents if desired.
- If you want an indexed view, add sections for ops/tests/tools/tasks in MASTER_INDEX.
