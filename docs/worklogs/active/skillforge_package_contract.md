status: active
owner: docs/worklogs/active/skillforge_package_contract.md
last_reviewed: 2026-07-30
superseded_by:
notes: Resolved by docs/PASS/PASS_LIBRARY.md on 2026-07-30.

# SkillForge Package Contract - Discovery Record

## What changed

Defined the required design slice in `docs/PASS/PASS_LIBRARY.md`: top-down
generated indexes, independently installable packages, and a mandatory bootstrap
metaskill.

## What was tested or reviewed

Reviewed the library placement rule, the closed object schema, and the existing PASS-TOOL-1 handoff. The handoff already owns generated root and per-category indexes, but no contract currently defines installable packages or bootstrap loading.

## What worked

Variable-depth `library_path` derives package membership without separate package
metadata in objects. The universal metaskill has a stable object id:
`AP_plan_and_build_work_from_thumbnail_to_final`.

## What failed

No package manifest was added by hand. `tools/build_index.py` now derives root,
package, and topic indexes from validated `library_path` values instead.

## Known risks

An index can declare the mandatory metaskill, but only a SkillForge consumer can enforce that it is loaded before optional packages. Cross-links that span optional packages also need an explicit dependency or degradation rule.

## Next safe step

Use the generated indexes as the navigation surface and run the validator plus
generator after each processed source unit.

## Files changed

`docs/PASS/PASS_LIBRARY.md`, `docs/dev/docs_index.md`,
`docs/worklogs/assignments.md`, and `docs/worklogs/active/skillforge_package_contract.md`.
