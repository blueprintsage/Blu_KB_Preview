# CHANGELOG (Preview Repo)

All notable changes to this repository will be documented in this file.

Format: Keep entries additive. Prefer “Added / Changed / Fixed / Removed”.  
Dates are local: America/Chicago.  

## [2026-03-06] Standardize kernel capsule module formatting

### Changed
- Standardized capsule layout toward a consistent module-first shape.
- Added human-readable `##` headers above module blocks for easier scanning.
- Converted standalone hotfix/addendum-style sections into normal modules.
- Wrapped non-module intro prose into `Capsule Canon` modules where needed.
- Added a repo template for future kernel capsule/module drafting.

### Why
- To make kernel capsules easier for humans to scan and maintain.
- To reduce one-off “hotfix/addendum” drift.
- To keep future capsule edits aligned with one visible format.

### Impact
- Core/runtime capsule files now follow a more uniform presentation pattern.
- Future updates can start from the module template instead of ad hoc formatting.
- Headers and versions were refreshed on changed files.

### Affected
- `01_Identity.md`
- `02_Operations_Law.md`
- `03_Exec.md`
- `04_Exec_Library.md`
- `05_Commands.md`
- `06_Program_System.md`
- `07_Engine.md`
- `08_Teaching.md`
- `09_School_Engine.md`
- `10_USERCAP.md`
- `template/systems/KERNEL_CAPSULE_MODULE_TEMPLATE.md`

## [2026-03-06] Clean up Program_System and convert capsule to module format

### Changed
- Converted `06_Program_System.md` to human-header plus module format throughout.
- Removed `PROGRAM.ArtPipeline.v1` from the registry and command surface.
- Removed `PROGRAM.ReferenceResolver.v1` from the registry and command surface.
- Removed the legacy `Programs — Art Stack` section.
- Removed the `Verification Programs (RC/Release Gate)` section.
- Added a `PROGRAM_SYSTEM_MODULE_TEMPLATE.md` repo template for future module-standard edits.
- Bumped `06_Program_System.md` header metadata to `version: 0.8.8` and refreshed `updated`.

### Why
- To reduce Program_System to actual current workflow owners.
- To remove old drawing and RC scaffolding ahead of Exec 3.0 work.
- To bring the capsule closer to a consistent module-first repo format.

### Impact
- Program_System is cleaner and easier to reason about.
- Old Art/ReferenceResolver/RC wiring is no longer presented as live Program ownership.
- Future Program_System edits now have a template path for consistent formatting.

### Affected
- `06_Program_System.md`
- `template/systems/PROGRAM_SYSTEM_MODULE_TEMPLATE.md`
- `<canonical changelog file>`


