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

## [2026-03-06] Start Exec 3.0 Phase 1 kernel truth pass

### Changed
- Updated `03_Exec.md` from `version: 2.1.4` to `version: 3.0.0`.
- Renamed the capsule title to `03 Exec 3.0`.
- Strengthened the Exec canonical law with an explicit commit truth rule.
- Added `M03B` for reply ABI validation and commit gating.
- Added `M03C` for the reminder-create reference lane as the first Exec 3.0 proof path.
- Expanded verification hooks to require reminder-create commit validation and fail-closed behavior when stateful create replies are incomplete.

### Why
- To start Exec 3.0 with a narrow kernel truth pass instead of a broad rewrite.
- To stop success text from appearing before required state is validated and committed.
- To use reminders as the first reference workflow for commit-before-confirmation behavior.

### Impact
- Exec now states clearly that intent recognition and owner resolution are not proof of completion.
- Stateful create flows must pass ABI and state validation before success can be printed.
- Reminder creation becomes the first explicit reference lane for Exec 3.0 commit discipline.

### Affected
- `03_Exec.md`
- `<canonical changelog file>`
 
## [2026-03-06] Remove reminder capability from active kernel capsules

### Changed
- Removed reminder-specific runtime behavior from `03_Exec.md` and replaced it with generic interrupt/tick language.
- Removed the reminder scheduler module from `04_Exec_Library.md`.
- Removed the public `/reminders` surface, reminder aliases, and reminder-specific command guidance from `05_Commands.md`.
- Removed `PROGRAM.Reminders.v1`, its registry mapping, and its command-surface routes from `06_Program_System.md`.
- Removed reminder-specific Engine hotfix/prehook behavior from `07_Engine.md`.
- Updated header metadata (`version`, `updated`) on all changed capsules.

### Why
- Reminder support is out of scope for the current kernel footprint.
- A dedicated reminder path was not worth carrying as a separate knowledge-slot-backed capability.
- This keeps the kernel focused on higher-value systems and reduces stale routing/contracts.

### Impact
- Reminders are no longer part of the active runtime architecture.
- Exec, Commands, Program_System, ExecLib, and Engine no longer imply live reminder support.
- Any future reminder/task capability should be reintroduced as a fresh design, not through the removed contracts.

### Affected
- `03_Exec.md`
- `04_Exec_Library.md`
- `05_Commands.md`
- `06_Program_System.md`
- `07_Engine.md`
- `<canonical changelog file>`

## [2026-03-06] Advance Exec 3.0 Phase 2 around dispatch packets, owner resolution, and commit gating

### Changed
- Updated `03_Exec.md` to `version: 3.1.0`.
- Reframed Exec Phase 2 around kernel message discipline instead of reminder-specific flow.
- Added a canonical dispatch packet model for executable operations.
- Added explicit one-owner resolution rules against the public command surface.
- Added reply ABI validation and a hard commit gate before success output.
- Added path health states (`READY`, `DEGRADED`, `BLOCKED`, `BROKEN`) and expanded verification checks.

### Why
- Reminder capability was removed from the active kernel architecture.
- Exec still needed a stronger kernel boundary for dispatch, ownership, and truth-before-output behavior.
- A packet/owner/ABI model gives future Program owners a cleaner and more deterministic execution path.

### Impact
- Exec now behaves more like a kernel dispatcher and less like a conversational guesser.
- Success output should only occur after resolution, validation, and any required state commit.
- Future workflow owners such as PASS, CPM, School, and SkillForge have a clearer dispatch contract.

### Affected
- `03_Exec.md`
- `<canonical changelog file>`

## [2026-03-06] Restore PASS dual-lane as the default for teachable skill sources

### Changed
- Updated `PASS:GUT-LADDER` packaging rules so dual-lane output is the default for teachable skill sources.
- Re-scoped generic flat PASS bundles to explicit exceptions only.
- Broadened PASS classification language from a narrow CS/programming-only rule to a general instructional skill rule.
- Updated `05_Commands.md` and `06_Program_System.md` header metadata.

### Why
- The prior rule was too narrow and sent instructional art/skill sources into generic flat bundle output.
- Intended behavior is Teaching + Skill dual-lane by default for sources that teach a learnable skill.

### Impact
- Books like drawing/comics manuals should now route to dual-lane packaging by default.
- Flat root PASS bundles should only appear when `--generic` is explicitly requested or when the source is true non-skill reference material.

### Affected
- `05_Commands.md`
- `06_Program_System.md`

## [2026-03-06] Rewrite Commands from the ground up around live public surface only

### Changed
- Rewrote `05_Commands.md` from scratch in a cleaner module-first format.
- Reduced Commands to the live public surface only.
- Removed public command exposure for internal systems including SkillForge, PEL, and Zero-Drift/LOCK.
- Removed dead or retired public surfaces including ART, REFS, REMINDERS, SCHED, and FOCUS.
- Removed stale cleanup debris, duplicate removal sections, and legacy clutter from the command document.
- Kept the public surface centered on HELP, EDIT, TOK, REPO, USERCAP, MOOD, CPM, PASS, SCHOOL, and PARENT.

### Why
- The previous command document had become a mix of live commands, internal systems, removed features, and legacy cleanup noise.
- Public commands should document only what users can actually call.
- SkillForge is intended to remain invisible and activate internally when a request falls into a skill category.

### Impact
- `05_Commands.md` is smaller, cleaner, and easier to trust.
- Public/internal boundaries are clearer.
- Future command-surface drift should be easier to spot and remove.

### Affected
- `05_Commands.md`
- `<canonical changelog file>`

## [2026-03-07] Mood render contract enforcement + changelog law

### Changed
- Patched Exec so visible mood rendering is injected in the final output lane after reply validation and before output print.
- Added Exec `mood_state` contract and fail-closed mood render checks.
- Updated Engine mood grounding so PEL + identity + live reaction resolve into ribbon-driven `mood_state` for Exec rendering.
- Tightened Commands MOOD public contract to canonical format `[MOOD] {MoodWord} {Swatch}`.
- Added changelog commit law requiring changelog entries for committed kernel/repo/governed-file updates only, using the repository changelog template format.

### Why
- Mood was being described in prose instead of rendered in the canonical public format.
- The output contract needed to be enforced in the final visible lane so mood computation and mood display stayed aligned.
- Changelog entries needed a single required format so repo history stays uniform and commit-disciplined.

### Impact
- MOOD now has a clearer end-to-end contract: Engine computes, Exec renders, Commands defines the public surface.
- Freeform mood narration should no longer substitute for the canonical mood line when mood rendering is active.
- Future committed kernel/repo/governed-file updates should produce consistent changelog entries in one template shape.

### Affected
- `03_Exec.md`
- `05_Commands.md`
- `07_Engine.md`
- `02_Operations_Law.md`
- changelog / repo governance flow