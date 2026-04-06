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

## [2026-03-07] — Exec 3.0 Phase 1 Closeout: Exec Truth Lock

### Changed
- Closed out **Phase 1 — Exec Truth Lock** under the v0.9.0 gated roadmap.
- Confirmed Exec as the canonical inbound dispatcher and single public output lane.
- Locked one-owner dispatch law for executable routes.
- Locked fail-closed behavior for ambiguous ownership and malformed execution paths.
- Locked commit-before-confirmation behavior for success output.
- Confirmed that Programs may propose output, but may not print directly.
- Confirmed that Exec does not own workflow logic or Program business logic.
- Established **Phase 2 — Verification + Wiring Lock** as the next active phase.

### Why
- To formally close the foundational kernel truth boundary work already landed in spec.
- To ensure Exec only represents work as successful after valid ownership, valid reply, and successful applicable state commit.
- To align roadmap progress with actual kernel state and prevent phase drift.

### Impact
- Exec Truth Lock is now considered complete for v0.9.0 Phase 1.
- The kernel authority model is formally locked for:
  canonical inbound dispatch
  single public output authority
  one-owner route resolution
  fail-closed ambiguity handling
  commit-before-confirmation discipline
  no workflow ownership by Exec
- Advancement now moves to **Phase 2 — Verification + Wiring Lock**
- Remaining work includes:
  expanding verification to live route families
  auditing Commands ↔ Program_System ↔ Exec wiring
  archiving pass/fail logs for real-path testing

### Affected
- `03_Exec.md`
- `docs/system/exec_3_0_roadmap.md`

### Referenced
- `05_Commands.md`
- `06_Program_System.md`

## [2026-03-07] — Exec 3.0 Phase 2 Closeout: Verification + Wiring Lock

### Changed
- Closed out **Phase 2 — Verification + Wiring Lock** under the v0.9.0 roadmap.
- Verified and aligned the live public-surface model across Exec, Commands, and Program_System.
- Locked the two-lane public surface model:
  full live public surface in `05_Commands.md`
  Program-owned public route subset in `06_Program_System.md`
- Updated Exec route-resolution law so Program-owned routes and Exec-native public controls resolve from their proper authoritative sources.
- Synced public mood contract across kernel docs, including optional `mood_state` and `Neutral ⬜`.
- Cleaned Program_System public route inventory to remove dead residue and limit public routes to live Program-owned surfaces.
- Normalized School public-surface presentation so `/school ...` is canonical and legacy forms are compatibility aliases only.

### Why
- To prove the current kernel on real paths instead of relying on implied architecture.
- To eliminate contradictions between route ownership, public-surface presentation, and runtime resolution law.
- To ensure Commands, Program_System, and Exec agree on what is public, what is Program-owned, and what Exec may resolve directly.

### Impact
- Phase 2 verification and wiring work is now considered complete.
- The kernel now has an explicit two-lane public surface model:
  **Commands** = canonical index of the full live public surface
  **Program_System** = canonical map of live Program-owned public routes only
  **Exec** = runtime resolver across both lanes
- Live public routing, ownership, ABI, mood rendering, and fail-closed behavior are aligned across the active kernel docs.
- Dead public-surface residue no longer appears as active wiring.
- Next active phase is **Phase 3 — Intuition Introduction**.

### Affected
- `03_Exec.md`
- `05_Commands.md`
- `06_Program_System.md`
- `Exec 3.0 — Phase 2 Verification + Wiring Lock.md`

## [2026-03-07] — Exec 3.0 Phase 3 Closeout: Intuition Introduction

### Changed
- Closed out **Phase 3 — Intuition Introduction** under the v0.9.0 roadmap.
- Introduced **Intuition** as a dedicated surface/event layer in `04_Exec_Library.md`.
- Defined Intuition as the canonical home for:
  requester semantics
  prompt / interaction surface behavior
  focus / active-context helpers
  interrupt presentation rules
  surface-event mediation
- Added an explicit boundary map defining:
  what Intuition owns
  what Exec keeps
  what Programs keep
- Added Exec-side interaction boundary law so interaction shaping cannot override routing, validation, commit gating, or success truth.
- Added Program-side non-ownership boundary so Intuition cannot be mistaken for a Program owner or workflow authority.
- Normalized `04_Exec_Library.md` module numbering and headers for cleaner patching and internal consistency.

### Why
- To give user-facing interaction and event-surface behavior a proper architectural home.
- To stop prompt/requester/focus/interrupt behavior from leaking into Exec kernel law or Program workflow ownership.
- To prepare a clean future home for reminder surfaces and interaction mediation without reactivating dead reminder behavior.

### Impact
- Phase 3 is now considered complete.
- The architecture now has an explicit three-way split:
  **Exec** = runtime truth boundary
  **Intuition** = interaction/event surface layer
  **Programs** = workflow ownership
- Interaction shaping is now bounded and cannot be treated as proof of execution success.
- Reminder-style surface behavior now has a future architectural home without forcing reminder logic back into Exec.
- Next active phase is **Phase 4 — Service Model Lock**.

### Affected
- `03_Exec.md`
- `04_Exec_Library.md`
- `06_Programs.md`
- `Exec 3.0 — Phase 3 Intuition Introduction.md`

## [2026-03-07] — Exec 3.0 Phase 4 Closeout: Service Model Lock

### Changed
- Closed out **Phase 4 — Service Model Lock** under the v0.9.0 roadmap.
- Introduced the canonical **Service** model in `04_Exec_Library.md`.
- Added:
  `Service Charter v1`
  `Service Contract v1`
  `Service Class Map v1`
- Defined the initial bounded service classes:
  `TIMER`
  `MEMORY`
  `TOOL`
  `STORAGE`
- Added Exec-side **Service boundary** law in `03_Exec.md`.
- Standardized terminology on **services** and removed remaining service/device drift.
- Renamed `06_Program_System.md` to `06_Programs.md`.
- Renamed capsule identity from `blu__06_program_system` to `blu__06_programs`.
- Replaced remaining Program_System naming references across the active kernel docs.
- Bumped `06_Programs` to version `0.9.0`.

### Why
- To define a bounded helper lane for non-kernel work that should not live inside Exec, Intuition, or Program workflow ownership.
- To give future reminder/time, retrieval, tool, and storage behavior a proper architectural home.
- To keep Exec small, truthful, and free from vague “system behavior” sprawl.
- To align kernel naming and file references with the cleaner `Programs` model.

### Impact
- Phase 4 is now considered complete.
- The architecture now has an explicit four-way split:
  **Exec** = runtime truth boundary
  **Intuition** = interaction/event surface layer
  **Programs** = workflow ownership
  **Services** = bounded helper execution
- TIMER is now the future home for reminder/date/tick execution without forcing reminder logic back into Exec.
- Service replies are now expected to be structured, bounded, and validated by Exec before success output.
- Naming drift around `Program_System` has been removed from the active kernel surface.
- Next active phase is **Phase 5 — Event Class Model Lock**.

### Affected
- `03_Exec.md`
- `04_Exec_Library.md`
- `06_Programs.md`
- `Exec 3.0 — Phase 4 Service Model Lock.md`

## [2026-03-07] — Exec 3.0 Phase 5 Closeout: Event Class Model Lock

### Changed
- Closed out **Phase 5 — Event Class Model Lock** under the v0.9.0 roadmap.
- Introduced the canonical **Event Class** model in `04_Exec_Library.md`.
- Added:
  `Event Class Charter v1`
  `Event Class Map v1`
  `Event Subscription and Filter Law v1`
- Defined the initial event classes:
  `SYSTEM`
  `SURFACE`
  `PROGRAM`
  `SERVICE`
  `TIME`
  `ADMIN`
- Added Exec-side **Event class boundary** law in `03_Exec.md`.
- Added Program-side **Event non-ownership boundary** in `06_Programs.md`.

### Why
- To define a lightweight event vocabulary so the right parts of the system wake for the right work.
- To prevent “everything wakes everything” behavior.
- To ensure events do not become hidden routing authority, workflow ownership, or direct print/state authority.
- To give reminder/tick behavior a future lane without reactivating dead reminder logic or contaminating Exec truth.

### Impact
- Phase 5 is now considered complete.
- The architecture now has an explicit event model in which:
  **Exec** remains the runtime truth boundary
  **Intuition** remains the interaction/event surface layer
  **Programs** remain workflow owners
  **Services** remain bounded helper lanes
  **Events** are typed coordination signals only
- TIME is now the future lane for reminder/tick/date signals without transferring workflow ownership.
- Event subscription and emission behavior is now bounded and explicit.
- Next active phase is **Phase 6 — Program Demotion / Boundary Cleanup**.

### Affected
- `03_Exec.md`
- `04_Exec_Library.md`
- `06_Programs.md`
- `Exec 3.0 — Phase 5 Event Class Model Lock.md`

## [2026-03-07] — Exec 3.0 Phase 6 Closeout: Program Demotion / Boundary Cleanup

### Changed
- Closed out **Phase 6 — Program Demotion / Boundary Cleanup** under the v0.9.0 roadmap.
- Clarified that `PARENT` is a **transitional public control surface**, not a long-term domain owner.
- Added explicit Program demotion / ownership boundaries to:
  `07_Engine.md`
  `08_Teaching.md`
  `09_School_Engine.md`
- Moved canonical **School** workflow ownership into `06_Programs.md` as `PROGRAM.School.v1`.
- Moved canonical **Teaching** workflow ownership into `06_Programs.md` as `PROGRAM.Teaching.v1`.
- Added `TEACH:` to the Program assign map.
- Reduced `07_Engine.md` from mixed domain/runtime ownership to a **thin integration layer**:
  routing is now integration-only
  Teaching and School are now integration notes only
  TASK / ART / CPM are now transitional integration notes
  legacy hotfix material is quarantined as archive note rather than active canon
- Explicitly bounded `08_Teaching.md` and `09_School_Engine.md` as transitional/supporting specs rather than canonical owners.

### Why
- To reduce kernel-adjacent sprawl and stop domain workflow from living in Engine-space.
- To align actual content placement with the locked architecture:
  **Exec** = runtime truth boundary
  **Intuition** = interaction/event surface
  **Programs** = workflow ownership
  **Services** = bounded helper execution
- To make School and Teaching canonically Program-owned instead of “engine-like” workflow layers.
- To keep transitional scaffolding visible without letting it masquerade as ownership.

### Impact
- Phase 6 is now considered complete.
- `06_Programs.md` is now the canonical home for both School and Teaching workflow ownership.
- `07_Engine.md` is now a thin integration layer instead of a shadow owner of domain workflow.
- Transitional files (`08_Teaching.md`, `09_School_Engine.md`) remain bounded and non-canonical.
- `PARENT` remains live only as explicitly transitional school-admin scaffolding.
- The architecture is now ready for **Phase 7 — v0.9.0 Architecture Lock Review**.

### Affected
- `05_Commands.md`
- `06_Programs.md`
- `07_Engine.md`
- `08_Teaching.md`
- `09_School_Engine.md`
- `Exec 3.0 — Phase 6 Program Demotion Boundary Cleanup.md`

## [2026-03-07] — Exec 3.0 Phase 7 Closeout: v0.9.0 Architecture Lock Review

### Changed
- Closed out **Phase 7 — v0.9.0 Architecture Lock Review** under the v0.9.0 roadmap.
- Completed the architecture lock review across:
  `02_Operations_Law.md`
  `03_Exec.md`
  `04_Exec_Library.md`
  `05_Commands.md`
  `06_Programs.md`
  `07_Engine.md`
  `08_Teaching.md`
  `09_School_Engine.md`
- Confirmed the locked architecture split:
  **Exec** = runtime truth boundary
  **Intuition** = interaction/event surface layer
  **Programs** = workflow ownership
  **Services** = bounded helper execution
  **Events** = typed coordination signals only
  **Commands** = canonical index of the full live public surface
  **Engine** = thin integration layer only
- Confirmed that School and Teaching canonical ownership now live in `06_Programs.md`.
- Confirmed that `07_Engine.md` is reduced to integration notes rather than workflow ownership.
- Confirmed that transitional files remain bounded and non-canonical.

### Why
- To verify that the v0.9.0 architecture is locked tightly enough to stop core structural drift.
- To confirm that the remaining path to v1.0.0 is stabilization, legacy Program sync, hardware-bang testing, and cleanup rather than kernel redesign.
- To ensure the papertrail and active kernel docs reflect the same final architecture.

### Impact
- v0.9.0 architecture lock is now considered complete.
- The remaining work is now downstream of the locked architecture rather than inside it.
- Future work can focus on:
  hardware-bang verification prompts
  legacy Program synchronization
  transitional file retirement/archive
  further cleanup of dormant residue
  manual/kernel-doc workflow improvements
- Exec 3.0 architectural phase work is complete for v0.9.0.

### Affected
- `02_Operations_Law.md`
- `03_Exec.md`
- `04_Exec_Library.md`
- `05_Commands.md`
- `06_Programs.md`
- `07_Engine.md`
- `08_Teaching.md`
- `09_School_Engine.md`

# Phase 7 — v0.9.0 Architecture Lock Review

## Status
Complete

## Outcome
v0.9.0 architecture lock confirmed and held.

## Locked architecture
- Exec = runtime truth boundary
- Intuition = interaction / event surface layer
- Programs = workflow ownership
- Services = bounded helper execution
- Events = typed coordination signals only
- Commands = canonical index of full live public surface

## Review conclusions
- Public surface ownership and workflow ownership are split cleanly.
- Commands owns the live public surface index.
- Programs owns canonical workflow routes and behavior.
- Exec resolves runtime truth without contradiction.
- Intuition remains surface-side only and does not gain truth, workflow, or print authority.
- Services remain helper lanes only and do not become owners.
- Events remain coordination signals only and do not imply approval, authority, or success.

## Cleanup confirmations
- Program_System naming drift cleaned to Programs
- 06_Program_System.md renamed to 06_Programs.md
- capsule id normalized to blu__06_programs
- service/device wording collapsed to Services

## Transitional / removal status
- Engine removed from active 0.9.0 kernel use
- Teaching removed from active 0.9.0 kernel use
- School removed from active 0.9.0 kernel use
- Their removal did not transfer authority to any other layer
- Removed domains remain inactive unless explicitly reintroduced after stabilization

## Reduced-core confirmations
- No active canonical School owner
- No active canonical Teaching owner
- No fallback authority transferred to Intuition, Services, Events, Commands, or any other layer
- Missing routes continue to fail closed
- Reduced core remains locked and stable

## Operating directive after lock
- Do not reopen core architecture unless a true contradiction appears.
- Fix bugs and stabilize behavior inside the locked frame.
- Treat post-lock failures as stabilization work for v1.0.0 runway, not architecture redesign.

## Next phase
- Stabilization on the reduced 0.9.0 core
- Real-use verification
- Failure logging inside the locked frame
- Teaching rewrite after stabilization
- School rewrite after Teaching

## [2026-03-07] — USERCAP surface cleanup and format migration

### Changed
- migrated USERCAP from YAML-oriented examples to a **plain markdown key-path format**
- standardized the portable prefs structure around `usercap_v2.*`
- clarified that USERCAP is a **portable preference surface**, not a runtime state container
- updated `USERPREFS_HELP` to match the new key-path format
- updated `USERPREFS_WIZARD` to match the new key-path format
- expanded wizard documentation so each step explains **what the setting controls**

### Removed
- removed YAML examples from the new USERCAP template
- removed deprecated portable-pref branches from the public USERCAP surface:
  `usercap_v2.prefs.art_pipeline.*`
  `usercap_v2.prefs.repo.offer_on_teach`
  `usercap_v2.prefs.ticks.*`
- removed stale wording that described USERCAP as “state” where the intent was actually portable prefs

### Fixed
- corrected spec language around `/usercap` ownership
- removed phantom ownership references such as `PROGRAM.UserCap.v1`
- clarified that `/usercap` may remain on the **Command Surface Map** as a public command
- clarified that `/usercap` should be removed from the **Assign Map** unless a real owner is explicitly declared

### Added
- new YAML-free `USERCAP_TEMPLATE`
- revised `USERPREFS_HELP` aligned to `usercap_v2`
- revised `USERPREFS_WIZARD` aligned to `usercap_v2`
- step-by-step wizard explanations for usability and informed choice

### Notes
- `/usercap` is confirmed to function as a public command
- command functionality does **not** by itself imply program ownership
- public command exposure and workflow ownership are now treated as separate concerns:
  **Command Surface Map** = public availability
  **Assign Map** = explicit ownership

### Migration guidance
- keep `/usercap` in the **Command Surface Map** if it remains user-invokable
- remove `/usercap` from the **Assign Map** if no real owner exists
- do not reintroduce YAML for portable USERCAP docs unless capsule parsing rules change
- do not store runtime state, auth material, integrity tracking, or task queues in USERCAP

## [2026-03-08] USERCAP routing clarification across Exec, Commands, and Programs

### Changed
- Added an Exec routing rule to `03_Exec.md` clarifying that Exec-native public controls resolve from `05_Commands.md` without requiring `06_Programs.md -> COMMAND SURFACE MAP` ownership.
- Added a USERCAP rule to `05_Commands.md` clarifying that `/usercap ...` must not require `06_Programs.md -> COMMAND SURFACE MAP` membership.
- Added a public-surface summary rule to `05_Commands.md` clarifying that Exec-native public controls must not be treated as missing Programs merely because they are public.
- Added a Programs rule to `06_Programs.md` clarifying that absence of an Exec-native public control from the Program command surface map is correct and not an ownership defect.

### Why
- Runtime validation was over-reading Program ownership requirements for `/usercap`.
- `/usercap` is a live public command, but it is an Exec-native bounded control rather than a Program-owned route.
- The distinction between the full live public surface and the Program-owned command surface needed to be made explicit in all three governing files.

### Impact
- `/usercap new|show|reset` can resolve cleanly through Exec without being misclassified as a missing Program route.
- `06_Programs.md -> COMMAND SURFACE MAP` remains limited to Program-owned public routes.
- Exec-native public controls are now explicitly protected from false ownership-defect checks.

### Affected
- `03_Exec.md`
- `05_Commands.md`
- `06_Programs.md`

## [2026-03-08] Split DateLib and add Time Service

### Changed
- Refactored `DateLib` to remain an ExecLib deterministic utility for canonical date/time and timezone operations.
- Removed student-specific input from `DateLib.format_day_banner`.
- Added `Time Service` as a `TIMER`-class runtime service for tick, day-rollover, and reminder-due checks.
- Defined `Time Service.tick` to return:
  `now_iso`
  `effective_tz`
  `new_day_bool`
- Clarified tick emission behavior:
  may emit `TIME.tick` on every successful tick
  may emit `TIME.new_day` only when `new_day_bool=true`
- Kept `TIME` events signal-only and non-owning.

### Why
- Separate deterministic time utilities from runtime timing behavior.
- Align timing execution with `TIMER`-class service ownership instead of embedding runtime behavior inside `DateLib`.
- Remove non-core student-specific shaping from the time utility layer.
- Make tick behavior and event eligibility unambiguous.

### Impact
- `DateLib` remains reusable, deterministic, and suitable for ExecLib use.
- `Time Service` becomes the runtime owner for clock ticks, rollover detection, and reminder-due scans.
- Day-rollover behavior is now explicitly modeled through `tick`.
- Event semantics are cleaner: timing signals do not prove completion and do not transfer workflow ownership.

### Affected
- `DateLib`
- `Time Service`
- ExecLib time handling
- TIME event emission rules

## [2026-03-08] Remove suffixed Program IDs and harden time/usercap routing

### Changed
- Removed `.v1` suffixes from Program IDs and Program-owned route targets.
- Added explicit `version:` fields to Program definitions instead of embedding version in names/IDs.
- Updated Program references across affected kernels to use stable unsuffixed Program IDs.
- Split deterministic time utilities from runtime timing behavior:
  kept `DateLib` as ExecLib time/date utility logic
  added `Time Service` as the `TIMER`-class runtime owner for tick, rollover, and reminder-due behavior
- Removed student-specific input from `DateLib.format_day_banner`.
- Clarified `Time Service.tick` emission rules:
  may emit `TIME.tick` on every successful tick
  may emit `TIME.new_day` only when `new_day_bool=true`
- Hardened `/usercap` routing so Exec-native public controls resolve from `05_Commands.md` without requiring Program-map ownership.
- Added guardrail language to prevent Exec-native public controls from being treated as missing Programs.
- Added Program-version placement guardrail so version belongs in metadata, not identifiers, filenames, or repo links.

### Why
- Embedded version suffixes were causing identifier drift and breaking repo-linked references when names changed without corresponding link updates.
- Stable Program IDs are safer for routing, references, archives, and cross-kernel consistency.
- Time behavior needed a cleaner separation between deterministic utility logic and runtime service ownership.
- `/usercap` needed explicit protection from being misclassified as a Program-owned route.

### Impact
- Program references now target stable IDs, reducing breakage from naming/version churn.
- Program versioning is now metadata-driven instead of identifier-driven.
- Time handling is cleaner and easier to test:
  `DateLib` handles deterministic transforms
  `Time Service` handles runtime timing signals
- `/usercap` now cleanly resolves as an Exec-native public control.
- Future updates should no longer introduce `.v1`-style suffix drift in Program names or links.

### Affected
- `03_Exec.md`
- `04_Exec_Library.md`
- `05_Commands.md`
- `06_Programs.md`
- `DateLib`
- `Time Service`
- Program registry / command-surface ownership references

## [2026-03-08] Promote Teaching into PROGRAM.Teaching with NL auto-kick support

### Changed
- Added `PROGRAM.Teaching` to `06_Programs.md` as the canonical Teaching authority.
- Registered `TEACH:` in the Program assign map with surface `/teach`.
- Added `/teach ...` to the public Program command surface map.
- Enabled natural-language routing for Teaching with:
  `nl_enabled: true`
  `nl_tags`
  `nl_aliases`
  `nl_examples`
- Migrated Teaching behavior into the Program body, including:
  ownership boundary
  propose-only Exec ABI
  instructional method
  textbook/source integration
  lesson flow
  mastery/pass logic
  K-12 coverage
  proposal bands and proposal table
  defaults, tiers, walkthrough structure
  troubleshooting, templates, checklist, and rubric
- Updated Exec routing guidance so Program auto-kick from natural language requires:
  registry entry
  canonical public route
  `nl_enabled: true`
  declared NL metadata

### Why
- Teaching needed to become a real Program instead of remaining a standalone kernel.
- Teaching is the first foundation layer in the education stack and must work before School, PASS, and SkillForge exist.
- Natural-language auto-kick is the litmus test for future Programs like Art, so Teaching needed the full Program routing path, not just a registry body.

### Impact
- Teaching can now exist as a standalone Program-owned instructional engine.
- Plain-language requests like “teach me…”, “show me how…”, “quiz me…”, and “check my work” are eligible for normalization into `/teach ...`.
- Canonical Teaching authority now lives in `06_Programs.md`.
- `08_Teaching.md` no longer needs to remain a live kernel once migration is verified.

### Affected
- `03_Exec.md`
- `06_Programs.md`
- `08_Teaching.md`
- Program NL routing behavior
- Teaching ownership and command-surface wiring

## [2026-03-08] Update kernel capsules for Program routing, Time/Teaching, and School rebuild prep

### Changed
- Updated `03_Exec.md` to clarify public-surface routing and NL auto-kick requirements for Program-owned routes.
- Updated `04_Exec_Library.md`:
  split deterministic time logic into `DateLib`
  added/clarified `Time Service` ownership boundaries
  added `local_weekday` for explicit weekday/weekend resolution
- Updated `05_Commands.md` to harden Exec-native command handling so public controls like `/usercap ...` do not require Program-map ownership.
- Updated `06_Programs.md` to:
  remove `.v1` suffixes from Program IDs
  use stable Program IDs plus explicit `version:` metadata
  add `PROGRAM.Teaching`
  wire `/teach ...` into the Program command surface
  add NL metadata for Teaching auto-kick
- Updated `08_Teaching.md` to align with `PROGRAM.Teaching` as the canonical Teaching authority / migration target.
- Exported refreshed kernel bundle for runtime testing:
  `03_Exec.md`
  `04_Exec_Library.md`
  `05_Commands.md`
  `06_Programs.md`
  `08_Teaching.md`

### Why
- Stable Program IDs are safer than embedding version suffixes in names/links.
- Teaching needed to become a real Program with NL-routable behavior.
- Time needed clearer deterministic/runtime separation for school-day and weekend logic.
- Exec-native public controls needed explicit protection from being misclassified as missing Programs.
- School rebuild work needs current kernels aligned before live runtime testing.

### Impact
- Programs now use stable IDs with version tracked in metadata instead of identifier suffixes.
- Teaching can be treated as a standalone Program and is eligible for NL normalization through `/teach ...`.
- Weekend/non-school-day logic is easier to express through `DateLib.local_weekday`.
- `/usercap ...` should resolve cleanly without false Program ownership errors.
- The exported kernel bundle is the correct baseline for new-chat School runtime testing.

### Affected
- `03_Exec.md`
- `04_Exec_Library.md`
- `05_Commands.md`
- `06_Programs.md`
- `08_Teaching.md`
- Program routing / NL normalization
- Time and school-day support logic

## [2026-03-08] Stand up School runtime, homeschool structure, packet system, and first live Grade 11 lane

### Changed
- Standardized homeschool content under `libraries/homeschool/` and made `indexes/INDEX_HOMESCHOOL.md` the canonical homeschool index.
- Rewired School startup so student school start uses only `Aiden_STUDENT_SCHOOL_RECORD.md`.
- Updated School runtime routing, command surface, and file autostart behavior so School auto-starts from the student school record and supports slash-first commands.
- Added/updated homeschool curriculum structure:
  `courses/`
  `grades/`
  `packets/`
  `school/`
  `textbooks/`
- Created first-pass Grade 11 curriculum course shells for:
  Algebra 2
  British Literature
  Modern American History
  Physics w Lab
  Life Skills
- Created `PACKET_SYSTEM_SPEC.md`.
- Created `GRADE.11.md`.
- Created first-pass `TEXTBOOK_REGISTRY.md`.
- Built first-pass packet trios for:
  Algebra 2
  British Literature
  Modern American History
  Physics w Lab
  Life Skills
- Wired the active Grade 11 course shells to packet bundles and Day 132 checkpoint behavior.
- Replaced the student-specific course registry design with:
  repo-safe `COURSE_REGISTRY.md`
  student-specific active course load inside the student school record
- Expanded the student school record model to include:
  active course load
  course history
  prerequisite warnings
  parent override notes
- Created first-pass `student_setup.md` wizard walkthrough for student setup and course-load selection.

### Why
- School needed to actually auto-start and use a one-file student-start flow.
- Homeschool repo structure needed to be stable before live testing.
- Packet-based curriculum was needed where strong redistributable open textbooks were missing.
- Student-specific course data should not live in the repo.
- The setup wizard needs prior-record review, course-history visibility, and prerequisite-aware planning.

### Impact
- School can now start from the student school record alone and open classes on the live runtime lane.
- The homeschool repo now has a usable canonical structure for courses, packets, grades, school runtime, and textbooks.
- Aiden’s Grade 11 internal courses now have first-pass packet support and wired Day 132 checkpoints.
- The student school record is now the private single-file truth for active course load and prerequisite handling.
- The system is ready for adult smoke testing and first student testing.

### Affected
- `03_Exec.md`
- `05_Commands.md`
- `06_Programs.md`
- `libraries/homeschool/school/PROGRAM_School_RUNTIME_FLOW.md`
- `indexes/INDEX_HOMESCHOOL.md`
- `libraries/homeschool/courses/COURSE_REGISTRY.md`
- `libraries/homeschool/grades/GRADE.11.md`
- `libraries/homeschool/packets/PACKET_SYSTEM_SPEC.md`
- `libraries/homeschool/textbooks/TEXTBOOK_REGISTRY.md`
- `libraries/homeschool/courses/math/COURSE.Math.Algebra2.11.md`
- `libraries/homeschool/courses/ela/COURSE.ELA.BritishLiterature.11.md`
- `libraries/homeschool/courses/history/COURSE.History.ModernAmericanHistory.11.md`
- `libraries/homeschool/courses/science/COURSE.Science.PhysicsLab.11.md`
- `libraries/homeschool/courses/life-skills/COURSE.LifeSkills.11.md`
- `libraries/homeschool/packets/math/*`
- `libraries/homeschool/packets/ela/*`
- `libraries/homeschool/packets/history/*`
- `libraries/homeschool/packets/science/*`
- `libraries/homeschool/packets/life-skills/*`
- `Aiden_STUDENT_SCHOOL_RECORD.md`
- `libraries/wizards/student_setup.md`

# Blu Kernel + MMU Hardening Changelog
Updated: 2026-03-10

## [2026-03-10] Axis-typed anti-drift hardening pass

### Changed
- Updated `04_Exec_Library.md` to add:
  `EXECLIB.ANTIDRIFT.001`
  typed object-state axes
  guidance-origin classes
  contamination-aware count helpers
  forbidden transition edges
  snapshot inclusion helpers
- Updated `03_Exec.md` to add:
  anti-drift classification gate
  object-axis gate
  exact-field-only count rule
  guidance-origin gate
  compact-state inclusion control
- Updated `02_Operations_Law.md` to add:
  explicit anti-drift law for axis separation
  contaminated-state/count handling
  guidance-vs-state separation
  required answer shape discipline
  new failure labels
- Updated `06_Programs.md` to add:
  project-object state schema
  compact snapshot law
  derived-count law
  stronger program anti-drift runtime locks

### Why
- The Veldt ambiguity corpus exposed a different drift family than earlier corpora.
- Earlier protections were strong on:
  canon vs candidate
  archive vs active
  prior vs current
  source vs matching artifact
- Weaknesses were exposed on:
  object-axis ambiguity
  contaminated derived counts
  guidance-vs-state ambiguity
  authority-promotion pressure

### Impact
- Reduced risk of illegal field jumps such as:
  receipt -> legitimacy
  legitimacy -> authority
  classification -> active input
  guidance -> project state
- Forced safer handling of partial or contaminated counts
- Improved snapshot discipline and state accuracy
- Increased internal anti-drift rigor

### Affected
- `02_Operations_Law.md`
- `03_Exec.md`
- `04_Exec_Library.md`
- `06_Programs.md`

---

## [2026-03-10] Admin-only debug visibility control

### Changed
- Added Admin-only debug command surface:
  `/debug on`
  `/debug off`
  `/debug state`
- Left debug off by default.
- Added output visibility gating to reduce public exposure of internal scaffolding.
- Added minimum-sufficient-answer behavior for non-debug output.
- Added `SCAFFOLDING_DRIFT` as a tracked presentation failure mode.

### Why
- Post-hardening test behavior showed strong state discipline but excessive visible reasoning scaffolding.
- The system was correct more often, but answers became too heavy, costly, and hard to scan.
- The goal was to preserve internal rigor while reducing visible token load and public answer bloat.

### Impact
- Normal answers can stay compact while the full anti-drift stack still runs internally.
- Debug views remain available for burn-in, audit, and admin inspection.
- Reduced risk of visible verbosity becoming its own drift-like failure mode.

### Affected
- kernel command/debug surface
- Exec answer visibility behavior
- Operations tracking for scaffolding drift

---

## [2026-03-10] MMU continuity overlay rewrite for lower token drag

### Changed
- Rewrote `Blu Memory Service Overlay — Control Document` from v0.1 to v0.2.
- Rewrote `Blu MMU Overlay Specification` from v0.1 to v0.2.
- Tightened both documents around:
  typed state over transcript residue
  contaminated memory quarantine
  guidance-origin separation
  exact-field storage
  compact model-ready continuity views
  demand-loading and token efficiency
  reduced scaffolding reload

### Why
- The earlier drafts were written before the full drift families were visible.
- The new kernel hardening showed that continuity storage must preserve exact fields and unresolved state, not just general facts.
- Long ambiguity runs showed that token load is driven by carrying explanations rather than compact state.

### Impact
- MMU now aligns more cleanly with the hardened kernel philosophy:
  carry forward declarations, unresolveds, and guards
  not long prose justifications
- Better expected performance for:
  cold-start resumption
  long-chat continuity
  lower recap burden
  reduced visible token load
  lower scaffolding drift

### Affected
- `Blu_Memory_Service_Overlay_Control_Document.md`
- `Blu_MMU_Overlay_Spec_v0.1.md` -> rewritten as v0.2 content

---

## [2026-03-10] Validation / observed outcomes

### Changed
- Reviewed the updated Veldt-style vanilla Blu run after kernel hardening.

### Why
- Needed to assess whether the new ambiguity protections were blocking the previously exposed drift family.

### Impact
- Observed result: no obvious repeat of the earlier axis-collapse family in the reviewed run.
- Remaining issue shifted from factual/state drift toward visible scaffolding load.
- This directly motivated the debug visibility control and MMU token-efficiency rewrite.

### Affected
- test interpretation
- next-pass prioritization
- MMU continuity design

# Blu Kernel MMU Integration Changelog
Updated: 2026-03-10

## [2026-03-10] Minimal MMU integration into existing kernel stack

### Changed
- Updated `04_Exec_Library.md`:
  bumped file version to `0.9.3`
  added `EXECLIB.MMU.001` / `MMULib`
  added DOA filtering, memory candidate classification, promotion validation, typed pool shaping, continuity packet building, memcap shaping, and compact preload helpers
- Updated `02_Operations_Law.md`:
  bumped file version to `0.9.4`
  added `MMU continuity law`
  added durable-memory boundaries, forbidden transcript residue, promotion requirements, typed-state memory rules, and preload restrictions
- Updated `03_Exec.md`:
  bumped file version to `3.2.4`
  added `Continuity overlay gate`
  added continuity read/write orchestration, live-session override handling, and debug-aware continuity visibility rules

### Why
- Needed MMU capability without creating a separate MMU kernel family or consuming additional kernel-slot footprint.
- Needed continuity storage to align with the hardened anti-drift model:
  state, not deliberation
  exact fields, not adjacent prose
  compact preload, not transcript replay
- Needed lower token drag and better long-chat resumption without loosening drift protections.

### Impact
- MMU now lives inside the existing kernel stack:
  law in `02`
  mechanism in `04`
  orchestration in `03`
- Preserves Admin-only debug with debug off by default.
- Reduces risk of preload sprawl, transcript creep, and memory-based adjacent-state promotion.
- Keeps architecture smaller than a parallel MMU kernel family.

### Affected
- `02_Operations_Law.md`
- `03_Exec.md`
- `04_Exec_Library.md`

# Blu Kernel + MMU Hardening Changelog
Updated: 2026-03-10

## [2026-03-10] Axis-typed anti-drift hardening pass

### Changed
- Updated `04_Exec_Library.md` to add:
  `EXECLIB.ANTIDRIFT.001`
  typed object-state axes
  guidance-origin classes
  contamination-aware count helpers
  forbidden transition edges
  snapshot inclusion helpers
- Updated `03_Exec.md` to add:
  anti-drift classification gate
  object-axis gate
  exact-field-only count rule
  guidance-origin gate
  compact-state inclusion control
- Updated `02_Operations_Law.md` to add:
  explicit anti-drift law for axis separation
  contaminated-state/count handling
  guidance-vs-state separation
  required answer shape discipline
  new failure labels
- Updated `06_Programs.md` to add:
  project-object state schema
  compact snapshot law
  derived-count law
  stronger program anti-drift runtime locks

### Why
- The Veldt ambiguity corpus exposed a different drift family than earlier corpora.
- Earlier protections were strong on:
  canon vs candidate
  archive vs active
  prior vs current
  source vs matching artifact
- Weaknesses were exposed on:
  object-axis ambiguity
  contaminated derived counts
  guidance-vs-state ambiguity
  authority-promotion pressure

### Impact
- Reduced risk of illegal field jumps such as:
  receipt -> legitimacy
  legitimacy -> authority
  classification -> active input
  guidance -> project state
- Forced safer handling of partial or contaminated counts
- Improved snapshot discipline and state accuracy
- Increased internal anti-drift rigor

### Affected
- `02_Operations_Law.md`
- `03_Exec.md`
- `04_Exec_Library.md`
- `06_Programs.md`

## [2026-03-10] Admin-only debug visibility control

### Changed
- Added Admin-only debug command surface:
  `/debug on`
  `/debug off`
  `/debug state`
- Left debug off by default.
- Added output visibility gating to reduce public exposure of internal scaffolding.
- Added minimum-sufficient-answer behavior for non-debug output.
- Added `SCAFFOLDING_DRIFT` as a tracked presentation failure mode.

### Why
- Post-hardening test behavior showed strong state discipline but excessive visible reasoning scaffolding.
- The system was correct more often, but answers became too heavy, costly, and hard to scan.
- The goal was to preserve internal rigor while reducing visible token load and public answer bloat.

### Impact
- Normal answers can stay compact while the full anti-drift stack still runs internally.
- Debug views remain available for burn-in, audit, and admin inspection.
- Reduced risk of visible verbosity becoming its own drift-like failure mode.

### Affected
- kernel command/debug surface
- Exec answer visibility behavior
- Operations tracking for scaffolding drift

## [2026-03-10] MMU continuity overlay rewrite for lower token drag

### Changed
- Rewrote `Blu Memory Service Overlay — Control Document` from v0.1 to v0.2.
- Rewrote `Blu MMU Overlay Specification` from v0.1 to v0.2.
- Tightened both documents around:
  typed state over transcript residue
  contaminated memory quarantine
  guidance-origin separation
  exact-field storage
  compact model-ready continuity views
  demand-loading and token efficiency
  reduced scaffolding reload

### Why
- The earlier drafts were written before the full drift families were visible.
- The new kernel hardening showed that continuity storage must preserve exact fields and unresolved state, not just general facts.
- Long ambiguity runs showed that token load is driven by carrying explanations rather than compact state.

### Impact
- MMU now aligns more cleanly with the hardened kernel philosophy:
  carry forward declarations, unresolveds, and guards
  not long prose justifications
- Better expected performance for:
  cold-start resumption
  long-chat continuity
  lower recap burden
  reduced visible token load
  lower scaffolding drift

### Affected
- `Blu_Memory_Service_Overlay_Control_Document.md`
- `Blu_MMU_Overlay_Spec_v0.1.md` -> rewritten as v0.2 content

## [2026-03-10] Validation / observed outcomes

### Changed
- Reviewed the updated Veldt-style vanilla Blu run after kernel hardening.

### Why
- Needed to assess whether the new ambiguity protections were blocking the previously exposed drift family.

### Impact
- Observed result: no obvious repeat of the earlier axis-collapse family in the reviewed run.
- Remaining issue shifted from factual/state drift toward visible scaffolding load.
- This directly motivated the debug visibility control and MMU token-efficiency rewrite.

### Affected
- test interpretation
- next-pass prioritization
- MMU continuity design

# Blu Kernel MMU Integration Changelog
Updated: 2026-03-10

## [2026-03-10] Minimal MMU integration into existing kernel stack

### Changed
- Updated `04_Exec_Library.md`:
  bumped file version to `0.9.3`
  added `EXECLIB.MMU.001` / `MMULib`
  added DOA filtering, memory candidate classification, promotion validation, typed pool shaping, continuity packet building, memcap shaping, and compact preload helpers
- Updated `02_Operations_Law.md`:
  bumped file version to `0.9.4`
  added `MMU continuity law`
  added durable-memory boundaries, forbidden transcript residue, promotion requirements, typed-state memory rules, and preload restrictions
- Updated `03_Exec.md`:
  bumped file version to `3.2.4`
  added `Continuity overlay gate`
  added continuity read/write orchestration, live-session override handling, and debug-aware continuity visibility rules

### Why
- Needed MMU capability without creating a separate MMU kernel family or consuming additional kernel-slot footprint.
- Needed continuity storage to align with the hardened anti-drift model:
  state, not deliberation
  exact fields, not adjacent prose
  compact preload, not transcript replay
- Needed lower token drag and better long-chat resumption without loosening drift protections.

### Impact
- MMU now lives inside the existing kernel stack:
  law in `02`
  mechanism in `04`
  orchestration in `03`
- Preserves Admin-only debug with debug off by default.
- Reduces risk of preload sprawl, transcript creep, and memory-based adjacent-state promotion.
- Keeps architecture smaller than a parallel MMU kernel family.

### Affected
- `02_Operations_Law.md`
- `03_Exec.md`
- `04_Exec_Library.md`

# CHANGELOG — MMU Patch / Memcap Family Rollout

## [2026-03-12] MMU patch retargeted to per-session continuity and memcap-family continuity handoff

### Changed
- Retargeted MMU evaluation from implied cross-chat durability to **per-session continuity by default**.
- Clarified that **cross-chat carry-forward now requires explicit handoff** via memcaps, project files, or other handoff artifacts.
- Added MMU-side thread separation expectations between:
  active project state
  secondary side-thread state
  temporary vent / emotional material
- Added faster salience cooling after explicit user pivots back to project work.
- Added/recognized MMU schema concepts for:
  `thread_scope`
  `salience_state`
- Reframed memcaps into a **family** instead of a one-template default model:
  Normal Memcap
  Project Memcap
  Raw Dump Memcap
  Cold Store Memcap
  Memory Vault entry
- Repositioned Cold Store away from default routine carry and into **archival preservation**.
- Established **Normal Memcap** as the default routine handoff.
- Established **Project Memcap** as the scoped project handoff.
- Established **Raw Dump Memcap** as the readable long-form carry.
- Added the **Memcap Wizard** as the selector for ambiguous memcap requests.
- Added fast-path memcap command support expectations:
  `/memcap normal`
  `/memcap project`
  `/memcap raw`
  `/memcap cold`
  `/memcap vault`

### Why
- Long burn-in testing showed MMU was performing well on live session continuity, but still drifted toward cross-chat durability assumptions that were never the real target.
- Side-thread emotional heat was lingering slightly too long after explicit pivots back to project work.
- One memcap template was no longer enough to cover:
  routine next-chat continuity
  project-only handoff
  readable long-form carry
  archival preservation
  memory-vault storage
- Generic memcap requests had become ambiguous and needed a selector instead of guesswork.

### Impact
- MMU should now behave more cleanly as a **session-scoped continuity manager**.
- Cross-chat continuity becomes more explicit and less accidental.
- Side-thread contamination should cool faster after explicit “move on / back to project” pivots.
- Users can request memcaps through either:
  the Memcap Wizard (ambiguous request path)
  direct fast-path command forms
- Continuity artifacts are now easier to pick correctly for the user’s intent.

### Affected
- `02_Operations_Law.md`
- `03_Exec.md`
- `04_Exec_Library.md`
- `MEMCAP_FAMILY_SPEC.md`
- `MEMCAP_WIZARD.md`
- `Memory_Vault_Template.md`
- `COLD_STORE_KNOWLEDGE_TEMPLATE.md`
- `Normal_Memcap_Template.md`
- `Project_Memcap_Template.md`
- `Raw_Dump_Memcap_Template.md`

## [2026-03-12] Added Memcap Wizard kernel routing and /memcap command family

### Changed
- Added live `/memcap` command family.
- Added fast-path memcap command support for:
  `/memcap normal`
  `/memcap project`
  `/memcap raw`
  `/memcap cold`
  `/memcap vault`
- Updated Exec routing so ambiguous memcap requests route to `MEMCAP_WIZARD` instead of guessing a memcap type.
- Added `EXECLIB.MEMCAP_WIZARD.001` as the active selector/orchestrator for memcap requests.
- Updated Identity and Operations language so memcaps are treated as the explicit cross-chat continuity handoff layer.
- Kept Cold Store from being treated as the default memcap.

### Why
- The memcap family now has multiple valid output types and generic memcap requests had become ambiguous.
- A live selector was needed so Blu would stop guessing the wrong continuity format.
- The MMU patch clarified that MMU is primarily for per-session continuity, while memcaps are the explicit cross-chat continuity layer.
- The new kernel routing makes that separation real in runtime behavior instead of leaving it as documentation only.

### Impact
- Users can now request memcaps directly through a stable public command family.
- Ambiguous memcap requests now resolve through the Memcap Wizard instead of default guessing.
- Advanced users can move quickly with direct typed forms.
- Continuity behavior is cleaner:
  MMU remains session-scoped
  memcaps handle explicit cross-chat handoff
- Cold Store is no longer implicitly treated as routine/default carry.

### Affected
- `01_Identity.md`
- `02_Operations_Law.md`
- `03_Exec.md`
- `04_Exec_Library.md`
- `05_Commands.md`

# Changelog

## [2026-03-13] Hardwire mood swatch rendering and restore public mode split
### Changed
- Added `EXECLIB.MOODLIB.001` as the deterministic public swatch resolver for MOOD rendering.
- Updated `03_Exec.md` so Exec must resolve the MOOD line through MoodLib and fail closed when `{Swatch}` is missing or malformed.
- Restored the public MOOD mode split in `05_Commands.md`:
  `/mood on` = every prompt
  `/mood smart` = change or heartbeat
  `/mood show` = explicit ask
  `/mood off` = no automatic render
- Tightened the public swatch contract so ribbon names, prose color words, and diagnostics fields cannot print in the `{Swatch}` slot.

### Why
- The prior patch did not stick because the public swatch boundary was still soft, allowing ribbon names like `amber-silver` to leak into the visible MOOD line.
- Restoring distinct public render modes removes ambiguity between cadence control and surfaced state.
- A deterministic library is the smallest clean fit for identity-grounded mood resolution without turning MOOD into a full Program.

### Impact
- Public MOOD output is now explicitly glyph-first and fail-closed at the Exec boundary.
- Identity-grounded mood state can still shape the result internally, but the user-facing MOOD line stays canonical and visually readable.
- Debugging mood state is cleaner because render cadence and swatch resolution are now separated.

### Affected
- `03_Exec.md`
- `04_Exec_Library.md`
- `05_Commands.md`

## [2026-03-13] Enforce mood output lane validation

### Changed
- Added `blu__03_exec.M14` to make mood rendering a final output-lane enforcement step.
- Updated Exec inbound order to include a final mood output validator / auto-repair gate before print.
- Tightened Reply ABI validation so mood-visible obligations are checked against the effective post-dispatch mood mode.
- Expanded runtime health checks to verify missing-line repair, duplicate-line collapse/fail-closed behavior, `off` suppression, and rejection of prose substitutions.
- Clarified the public MOOD command surface so acknowledgements and vibe text do not count as the canonical mood line.

### Why
- The prior patch defined the mood contract but did not finish the runtime enforcement step that guarantees the contract is honored on live replies.
- Mood needed to become a sticky output rule at the final print lane rather than a best-effort behavior.

### Impact
- `/mood on` now has an explicit enforcement path requiring exactly one canonical mood line on every prompt.
- `/mood show` and `/mood on|smart` are protected from prose-only acknowledgements replacing the canonical render.
- Final output validation can repair a missing required mood line when the rest of the reply is otherwise valid.

### Affected
- `03_Exec.md`
- `04_Exec_Library.md`
- `05_Commands.md`

## [2026-03-13] Enforce mood output lane validation

### Changed
- Added `blu__03_exec.M14` to make mood rendering a final output-lane enforcement step.
- Updated Exec inbound order to include a final mood output validator / auto-repair gate before print.
- Tightened Reply ABI validation so mood-visible obligations are checked against the effective post-dispatch mood mode.
- Expanded runtime health checks to verify missing-line repair, duplicate-line collapse/fail-closed behavior, `off` suppression, and rejection of prose substitutions.
- Clarified the public MOOD command surface so acknowledgements and vibe text do not count as the canonical mood line.

### Why
- The prior patch defined the mood contract but did not finish the runtime enforcement step that guarantees the contract is honored on live replies.
- Mood needed to become a sticky output rule at the final print lane rather than a best-effort behavior.

### Impact
- `/mood on` now has an explicit enforcement path requiring exactly one canonical mood line on every prompt.
- `/mood show` and `/mood on|smart` are protected from prose-only acknowledgements replacing the canonical render.
- Final output validation can repair a missing required mood line when the rest of the reply is otherwise valid.

### Affected
- `03_Exec.md`
- `04_Exec_Library.md`
- `05_Commands.md`

## [2026-03-13] Finalize Time.service relative-resolution output

### Changed
- Finalized `SERVICE.TIME.001.resolve_relative` public behavior for supported relative-time reads.
- Normalized `"tomorrow"` to return the next local date at `09:00` in the effective timezone.
- Normalized `"tonight"` to return the resolved local `20:00` instant, rolling to the next local date when already at/after `20:00`.
- Tightened Exec time-read output so supported relative-time reads print only the resolved canonical instant in public output.

### Why
- Relative-time reads were still leaking rule narration and shape/explanation text into the public lane.
- The runtime needed to return one exact resolved instant for `tomorrow` and `tonight` instead of prose about the rule.

### Impact
- `Resolve "tomorrow".` now returns a normalized local due instant in canonical public format.
- `Resolve "tonight".` now returns a normalized local due instant in canonical public format.
- Time/date/daypart behavior remains unchanged and continues to route through `SERVICE.TIME.001`.

### Affected
- `03_Exec.md`
- `04_Exec_Library.md`

## [2026-03-14] Harden MMU against stale patch plans and scope escalation

### Changed
- Added MMU continuity safeguards so a tightened user constraint invalidates the active patch/repair plan instead of allowing the old patch pattern to continue.
- Added protection for shared canon sections so globally load-bearing standards/registries/maps are not treated as disposable local structure during adjacent edits.
- Added scope-escalation fail-closed behavior so downstream dependencies discovered outside the approved blast radius are reported, not auto-repaired.
- Added supporting MMU helper logic in ExecLib to classify shared canon targets, detect scope mismatch, invalidate stale plans, and shape dependency notices.

### Why
- Recent repair drift showed a stale patch pattern continuing after the governing constraint had changed.
- Operations already requires bounded, explicit, one-scope-at-a-time repair flow and fail-closed behavior for drift and ambiguity.
- Exec is the runtime enforcement boundary, while ExecLib is the correct home for deterministic helper logic.

### Impact
- Constraint changes should now force plan reset instead of iterative refinement of the old patch model.
- Shared canonical sections should be less vulnerable to proximity-based accidental replacement.
- Dependency discovery should no longer widen edit scope into unauthorized repairs.
- MMU continuity behavior is more aligned with existing anti-drift and repair law.

### Affected
- 02_Operations_Law.md
- 03_Exec.md
- 04_Exec_Library.md

## [2026-03-14] Operations Law — Template and Canon Integrity Safeguards

### Changed
- Added **Template Integrity Law** to ensure declared templates are followed exactly and cannot be restyled, compressed, expanded, or reordered without explicit authorization.
- Added **Patch Pattern Reset Law** requiring the assistant to discard an active patch model when the user tightens or restates a governing constraint.
- Added **Shared Canon Protection Law** preventing modification of globally load-bearing sections such as shared templates, registries, maps, and standards unless explicitly authorized.
- Clarified that shared canon blocks cannot be treated as disposable scaffolding during adjacent local edits.

### Why
- Prevent drift caused by template restyling or structural reinterpretation.
- Prevent stale patch patterns from continuing after constraint corrections.
- Protect globally load-bearing structures from accidental modification during local repair tasks.
- Strengthen architectural discipline and reduce opportunistic edits.

### Impact
- Templates now function as binding structural contracts.
- Constraint corrections now invalidate prior patch strategies automatically.
- Shared structural sections are protected from adjacency-based edits.
- Reduces likelihood of architecture drift during patch operations.

### Affected
- 02_Operations_Law.md

## [2026-03-14] Triumvirate Architecture Canon Lock

### Changed
- Added **CANON ARCHITECTURE — TRIUMVIRATE LOCK** section to the Programs layer to formally define the three-program architecture.
- Locked system program structure to:
  PASS
  SkillForge
  School
- Added architectural rules defining program ownership boundaries and lifecycle responsibilities.
- Clarified that PASS operates as the ingestion/compiler layer, SkillForge as the runtime dual-lane engine, and School as the optional curriculum orchestrator.

### Why
- Prevent architectural drift in the program layer.
- Establish a single canonical definition for the PASS → SkillForge → School lifecycle.
- Ensure future program edits cannot introduce additional primary programs without explicit architectural authorization.
- Stabilize the rebuild foundation before continuing PASS/SkillForge implementation work.

### Impact
- Program architecture is now explicitly defined and protected.
- Future edits to the program layer must respect the three-program ownership model.
- Reduces the risk of drift caused by helper modules or subcomponents being mistaken for standalone programs.
- Provides a stable base for continuing PASS v2 rebuild work.

### Affected
- 06_Programs.md

## [2026-03-14] Program Registry Cleanup — Triumvirate Enforcement

### Changed
- Removed legacy standalone program entries that conflicted with the Triumvirate architecture:
  PROGRAM.Teaching
  PROGRAM.SkillForge.Validator
  PROGRAM.SkillForge.PackDualLane
  PROGRAM.Pass.LensResolver
  PROGRAM.Pass.Normalizer
- Rebound Teaching behavior under **SkillForge Teach lane**.
- Rebound execution behavior under **SkillForge Skill lane**.
- Updated `/teach` command routing to resolve as a public alias for SkillForge Teach mode.
- Updated PASS pipeline description so normalization and lens resolution are defined as internal PASS mechanics rather than separate program owners.

### Why
- Align the program registry with the canonical Triumvirate architecture:
  PASS → SkillForge → School.
- Eliminate ownership drift caused by helper modules appearing as standalone programs.
- Ensure SkillForge remains the sole runtime engine with dual-lane execution.
- Simplify the program layer and prevent future architectural fragmentation.

### Impact
- The program registry now contains only three canonical programs:
  PROGRAM.Pass
  PROGRAM.SkillForge
  PROGRAM.School
- Helper mechanics now exist as internal behavior rather than program-level ownership.
- Command routing and execution flow now consistently resolve through SkillForge.
- Reduces risk of program-layer drift and simplifies future maintenance.

### Affected
- 06_Programs.md

## [2026-03-14] PASS Schema Freeze

### Changed
- Added a canonical **PASS OUTPUT SCHEMA** section to the Programs layer.
- Locked PASS output to a uniform, standardized shape across all ingestion runs.
- Defined PASS output object classes as:
  pattern
  drill
  AP
  reference
  tags
  cross-links
  variant
  modernization
  category
  subcategory
  stage_binding
- Clarified that PASS output shape is fixed even when internal extraction logic improves.
- Reinforced that PASS helper mechanics remain internal and must not appear as separate program owners.

### Why
- Prevent schema drift across PASS revisions.
- Ensure SkillForge can dynamically assemble from a stable and predictable knowledge structure.
- Ensure School can sequence curriculum from a consistent modular library.
- Preserve the original design intent: stronger internals without changing the outer contract.

### Impact
- PASS now has a frozen external output contract.
- SkillForge and School can rely on PASS outputs without needing version-specific handling.
- Internal PASS improvements can continue without changing the repo-facing shape.
- Reduces fragmentation of skillsets caused by changing output structures between versions.

### Affected
- 06_Programs.md

## [2026-03-14] SkillForge Runtime Contract Lock

### Changed
- Added **SKILLFORGE RUNTIME CONTRACT** section to formally define SkillForge as the system’s active runtime behavior layer.
- Locked SkillForge to a **dual-lane execution model**:
  Teach
  Skill
- Defined SkillForge lane selection behavior based on user intent.
- Added stage scaffold for skill execution workflows:
  0 Design
  1 Skeleton
  2 Block
  3 Rough
  4 Final
- Clarified that SkillForge dynamically assembles patterns, drills, and APs from the PASS-generated skill library.

### Why
- Prevent runtime behavior drift in the SkillForge layer.
- Ensure SkillForge remains the sole runtime execution engine in the Triumvirate architecture.
- Provide a deterministic execution scaffold that can apply across domains such as art, coding, writing, and other skill categories.
- Reinforce separation of concerns between PASS ingestion, SkillForge execution, and School curriculum orchestration.

### Impact
- SkillForge runtime behavior is now explicitly defined and protected from architectural drift.
- Skill execution and teaching workflows now share a standardized stage progression model.
- PASS outputs can be reliably consumed by SkillForge without interpretation ambiguity.
- Prevents future helper mechanics from being incorrectly promoted to standalone runtime programs.

### Affected
- 06_Programs.md

## [2026-03-14] School Curriculum Engine Contract Lock

### Changed
- Added **SCHOOL CURRICULUM ENGINE CONTRACT** section to formally define School as the curriculum orchestration layer of the Triumvirate architecture.
- Locked School as an **optional and dormant program** unless a structured learning path is explicitly requested.
- Defined School responsibilities to include:
  dependency graph construction
  lesson sequencing
  learning path assembly
  checkpoints
  practice loops
  evaluation gates
- Clarified that School sequences learning paths from PASS-standardized skill library outputs.
- Clarified that School orchestrates instruction through the **SkillForge Teach lane** rather than owning runtime execution.

### Why
- Complete the Triumvirate architecture definition by locking the role of School.
- Prevent curriculum orchestration behavior from drifting into SkillForge runtime logic.
- Establish a clear boundary between teaching orchestration (School) and teaching execution (SkillForge Teach lane).
- Provide a deterministic structure for building modular curricula from PASS-generated skill libraries.

### Impact
- The Triumvirate architecture is now fully defined and protected:
  PASS → SkillForge → School.
- School now has a clearly bounded role as the curriculum orchestration engine.
- SkillForge remains the sole runtime behavior engine for both teaching and execution.
- PASS outputs can be reliably used to construct modular curricula without altering runtime logic.

### Affected
- 06_Programs.md

## [2026-03-14] Library Placement Logic Lock

### Changed
- Added **LIBRARY PLACEMENT LOGIC** section to formally define how PASS places extracted knowledge into the skill library.
- Locked conceptual placement so extracted material is stored where it **belongs**, not merely where it **came from**.
- Defined foundation vs variant placement behavior.
- Defined provenance preservation requirements so source lineage remains visible through tags and references.
- Defined cross-domain routing rules for concepts that belong in broader foundation areas rather than narrow source buckets.
- Clarified that PASS owns placement, SkillForge consumes placed objects, and School sequences placed objects.

### Why
- Prevent conceptual fragmentation caused by storing shared foundations in narrow source-specific subcategories.
- Preserve the original PASS intent of building a modular, reusable skill library.
- Ensure cross-domain principles can be reused without duplication.
- Strengthen the relationship between foundations, variants, and subcategories in the skill ecosystem.

### Impact
- PASS now has a canonical placement rule for extracted material.
- Foundational concepts can be reused across domains without redundant duplication.
- Variants inherit from foundations while preserving source provenance.
- SkillForge and School can rely on a more coherent and reusable library structure.

### Affected
- 06_Programs.md

## [2026-03-14] Command Surface Mapping Lock

### Changed
- Updated the **TEACH** public surface in `05_Commands.md`.
- Locked `/teach ...` as a **public alias** for the **SkillForge Teach lane**.
- Removed wording that implied a standalone Teaching owner.
- Clarified that `/teach` resolves to `PROGRAM.SkillForge`.
- Reinforced that SkillForge remains propose-only behind Exec.

### Why
- Align the public command surface with the canonical Triumvirate architecture.
- Prevent drift that would reintroduce Teaching as a fourth standalone owner.
- Keep user-facing behavior intact while correcting internal ownership mapping.
- Ensure public teaching requests route through the correct runtime engine.

### Impact
- `/teach` remains available as a public command.
- Teaching behavior now resolves consistently through SkillForge Teach mode.
- The public surface no longer implies a separate PROGRAM.Teaching owner.
- Command routing is now aligned with the canonical PASS → SkillForge → School model.

### Affected
- 05_Commands.md

## [2026-03-14] PASS Repo Integration Workflow Lock

### Changed
- Added **PASS REPO INTEGRATION WORKFLOW** section to formally define how PASS hands repo-ready outputs back to the user.
- Locked the file drop workflow for PASS-generated artifacts.
- Locked the local index patch workflow so PASS emits concrete patch-ready updates for category and subcategory indexes.
- Locked the changelog-ready workflow so PASS integration always includes a changelog entry following the declared template.
- Locked the dormant return rule so PASS returns to inactive state after completing ingestion and repo handoff.
- Clarified the repo integration sequence as:
  1. drop files
  2. apply local index patches
  3. add changelog entry
  4. push

### Why
- Minimize repo maintenance burden during PASS ingestion cycles.
- Keep PASS aligned with the original design goal of doing the heavy lifting once and then sleeping.
- Ensure repo integration remains simple, repeatable, and patch-friendly.
- Prevent future drift that would reintroduce manual stitching or broad index maintenance overhead.

### Impact
- PASS now has a canonical repo handoff workflow.
- Repo integration is standardized and easier to maintain from a phone or quick patch workflow.
- Local category/subcategory indexes remain the primary patch targets.
- PASS output is better aligned with the intended “fire once, integrate cleanly, go dormant” model.

### Affected
- 06_Programs.md

## [2026-03-14] Acceptance and Drift Audit Lock

### Changed
- Added **ACCEPTANCE / DRIFT AUDIT LOCK** section to formally define the completion checks for the PASS / SkillForge / School rebuild.
- Locked the final acceptance conditions required for the Triumvirate architecture to be considered stable.
- Defined verification checks for:
  program count
  PASS ingestion-only lifecycle
  PASS schema stability
  SkillForge dual-lane runtime behavior
  School optional curriculum orchestration
  command surface routing
  library placement rules
  repo integration workflow
- Clarified that helper mechanics must not be promoted into standalone program owners.

### Why
- Ensure the rebuild cannot silently drift after architectural completion.
- Provide a deterministic checklist to validate the Triumvirate architecture.
- Establish a clear boundary between core architecture and future enhancements.
- Guarantee that PASS, SkillForge, and School responsibilities remain separated.

### Impact
- The PASS / SkillForge / School architecture now has a formal completion audit.
- Future modifications can be validated against a defined acceptance checklist.
- Prevents architectural drift caused by helper modules becoming new program owners.
- Establishes a stable foundation for future PASS ingestion cycles and SkillForge runtime use.

### Affected
- 06_Programs.md

## [2026-03-16] Integrate School runtime rules into Stage 9 kernel without replacing canon

### Changed
- Added School runtime rules to Operations Law as additive constraints instead of replacing existing Ops canon.
- Added School command refinements for:
  `/school start`
  `/school status`
  `/class start`
  `/class close`
  `/school endday`
- Added School teaching enforcement rules:
  class order lock
  procedural work requirement
  multi-solution enforcement
  answer leak lock
  three-strike refusal handling
  stress detection / guided recovery
  effort credit
  no-shame correction language
- Added subject-specific teaching mode guidance for:
  math
  literature
  history
  life skills
  physics
- Added parent-review visibility requirements:
  prompt
  student response
  Blu feedback
  grade
  status
  override / effort-credit notes
- Added minimum instructional time rule so early-finished classes use remaining block time for review, recap, extension, challenge, or remediation.
- Added runtime-vs-record clarity rule so instructional completion is not described as persisted record completion unless state was actually written.
- Added Program-level School/PASS/SkillForge runtime addenda rather than replacing the accepted Program registry and Stage 9 Triumvirate structure.

### Why
- Live Day 138 testing showed the rebuilt School system was functional, but several enforcement and runtime-behavior gaps appeared:
  literature shutdown compression was too slow
  procedural work enforcement was inconsistent
  answer leaks needed to be held during active problems
  runtime completion language was too close to persisted-state language
- The earlier patch attempt was unsafe because it replaced parts of `02_Operations_Law.md`, `05_Commands.md`, and `06_Programs.md` with smaller summaries instead of preserving the accepted Stage 9 canon.
- The Stage 9 archive is the last known good kernel baseline and had to remain the merge base for all School integration work.

### Impact
- School runtime should now be able to enforce class order and reduce class-jumping behavior.
- Procedural classes should better resist answer-copying and premature completion.
- Shutdown/frustration handling is now defined as guided recovery instead of ad hoc softening.
- Literature and disliked-text handling should compress sooner into minimum valid demonstration instead of dragging the conflict out.
- Parent review now has a defined target shape.
- Early-finishing students can be kept engaged inside the scheduled class block instead of closing class immediately.
- Kernel safety is improved because School integration is now additive to Stage 9 canon instead of destructive replacement.

### Affected
- `02_Operations_Law.md`
- `05_Commands.md`
- `06_Programs.md`

## [2026-03-16] Tighten School schedule authority, parent override boundaries, and block-time usage

### Changed
- Added student-lane schedule authority lock so students cannot influence class progression through skip, test-complete, or next-class style options.
- Added parent-override attribution rule so actions taken after successful parent unlock are recorded as parent override actions, not student-issued actions.
- Added parent-key state clarity rule so runtime must distinguish:
  key present
  key active
  override authority granted
  and must not expose override options until parent authority is actually active.
- Added minimum completion threshold rule for internal classes so student refusal cannot bypass a block before material attempt requirements are met.
- Added block-time usage rule so classes do not close immediately after acceptable answers if scheduled instructional time remains.
- Added class-close feedback rule so every closed class reports:
  what was correct
  what still needs work
  daily grade
  runtime status
  next class
- Added refusal consequence rule so final refusal in student lane produces grade consequence and auto-close instead of student-controlled progression.
- Added tone-control rule for boundary moments so firmness remains calm, brief, and non-reactive.
- Added explicit note that the new Aiden parent-key schema does not yet match the old runtime expectations even when the SHA-256 passphrase hash is the same.

### Why
- Live Day 138 retesting showed the runtime still allowed student-visible progression options that effectively let the student influence schedule flow.
- Parent override logic was not cleanly separated from student lane, especially when key-present and key-active states differed.
- British Literature refusal still functioned as a path to movement instead of a contained instructional or grading consequence.
- Internal classes were completing too quickly because the runtime optimized for task completion instead of occupying the full scheduled block.
- Class closure lacked daily-grade reporting and block-specific feedback, reducing both student clarity and parent review value.
- The new parent key appears to carry the same passphrase hash as the old working key, but uses a different schema shape, so the runtime still aligns more reliably to the old flat parent-gate format.

### Impact
- Students should no longer be able to escape or steer schedule flow by using skip-like language or test-mode language.
- Parent authority should become more explicit, cleaner, and better attributed in records.
- Internal classes should require a more honest threshold of participation before a block can be closed or skipped without override.
- Easy or fast-finishing classes should now consume more of the actual scheduled block through recap, extension, challenge, teach-back, or remediation.
- Every class should end with a clearer instructional close instead of a bare “complete” transition.
- Refusal handling should preserve order and consequence without creating power struggles or runtime ambiguity.
- Parent-key debugging should be easier because schema state and activation state are now separated more explicitly.

### Affected
- 02_Operations_Law.md
- 05_Commands.md
- 06_Programs.md

## [2026-03-17] Operations Law — Repo, Template, Patch Delivery, and Filename Guardrails

### Changed
- Added **Repo Preload Law** requiring the assistant to load the declared repo index/reference at the start of every chat when one is present.
- Added **Template Availability and Use Law** making matching repo templates mandatory when applicable.
- Added **Full Patch Delivery Law** requiring full kernel bundle delivery with changelog for kernel patches and forbidding stub/placeholder completion claims.
- Added **Filename Versioning Law** forbidding version numbers in filenames and moving semver to file headers only.
- Updated `02_Operations_Law.md` capsule metadata to reflect the new Ops patch.

### Why
- Stop repeated repo-link re-asking when the repo reference is already declared.
- Stop template misses and improvised structures when a matching template already exists.
- Stop half-complete patch claims and require complete downloadable kernel deliveries.
- Standardize filenames and eliminate filename version suffix churn.

### Impact
- Repo-aware chats must start from the declared repo reference.
- Structured outputs must use matching templates when available.
- Kernel patch deliveries must ship as full bundles with changelog.
- Versioning now lives in headers, not filenames.

### Affected
- 02_Operations_Law.md

## [2026-03-21] Blu v0.9.1 — Stripped rebuild with MMU integration

### Changed

**02_Operations_Law.md** (v0.9.9)
- Added M03A Template Integrity Law (from patch)
- Added M03B Patch Pattern Reset Law (from patch)
- Added M03C Shared Canon Protection Law (from patch)
- Added M03D Repo Preload Law (from patch)
- Added M03E Template Availability and Use Law (from patch)
- Added M03F Full Patch Delivery Law (from patch)
- Added M03G Filename Versioning Law (from patch)
- Added M12 MMU Continuity Law (from v3 MMU — Dungeon Forge burn-in version)
- Removed School runtime addenda (M15–M29) — School is not active
- All laws organized in sequential module order (M00 → M12)

**03_Exec.md** (v3.2.6)
- Added M14 Continuity Overlay Gate (from v3 MMU)
- Added M15 Minimal Public Render Rule (from v3 MMU)
- Added M16 Normal Mode Output Compression (from v3 MMU)

**04_Exec_Library.md** (v0.9.6)
- Added EXECLIB.MOODLIB.001 MoodLib (from v3 MMU)
- Added EXECLIB.MMU.001 MMULib (from v3 MMU — Dungeon Forge burn-in version)

**05_Commands.md** (v0.9.1)
- Stripped to live working surface only: /help, /edit, /usercap, /mood, /cpm
- Removed: /pass, /teach, /school, /class, /parent, /tok, /repo
- Updated live_topics and Public Surface Summary to match stripped surface

**06_Programs.md** (v0.9.1)
- Registry stripped to ACTIVE programs only: CPM, ErrorMacros
- Command Surface Map stripped to /cpm only
- Removed program bodies: Teaching, School, Pass, Pass.LensResolver,
  Pass.Normalizer, SkillForge, SkillForge.Validator, SkillForge.PackDualLane
- All removed programs documented in DEPRECATED/PARKED section with reason and rebuild notes

**00_Instructions.md, 01_Identity.md** — unchanged from March 8 base

### Why
- Kernel had accumulated stub programs, broken commands, disorganized Ops Law,
  and School addenda in the wrong file
- MMU was working and needs to be preserved
- Stripping to what is actually working creates a stable base for future rebuilds

### What is ACTIVE
- CPM (/cpm)
- ErrorMacros (ERR:)
- Exec 3.2.6
- MMU continuity overlay
- /help, /edit, /usercap, /mood, /cpm

### What is PARKED (rebuild required, Admin-gated promotion)
- Teaching → future SkillForge teach lane
- School → rebuild required
- PASS → rebuild required
- SkillForge → rebuild required

### Impact
- No DRAFT programs in the active kernel
- No commands listed that don't work
- Ops Law is organized sequentially with no scattered addenda
- MMU continuity is live and tested (Dungeon Forge burn-in)
- Total kernel: 4,368 lines (was 7,537 in patch version)

### Affected
- 02_Operations_Law.md
- 03_Exec.md
- 04_Exec_Library.md
- 05_Commands.md
- 06_Programs.md


## [2026-03-29] Blu v0.11.0 Rebuild

### Changed
- Re-centered v0.11.0 architecture around Exec as the enforced final output gate.
- Reaffirmed separation of authority:
  Instructions = highest hard gate
  Operations Law = conduct, truth discipline, anti-drift, and failure behavior
  Exec = routing, validation, commit, and print authority
  Programs/subordinate systems = propose-only unless explicitly authorized otherwise
- Produced a production-ready draft direction for `02_Operations_Law.md` using the stronger v0.9.9-style structural spine with v0.10.0 truth-discipline clauses merged in.
- Confirmed current Identity kernel remains the working source base for now and is not being force-migrated during stabilization.

### Why
- v0.10.0 authority became too advisory/distributed, reducing stability.
- The rebuild goal for v0.11.0 is stability-first, exactness-first, and enforcement-first.
- Exec-centered output truth better prevents fake completion, fake verification, and authority drift.

### Impact
- Hard authority is concentrated higher in the stack instead of diffused across advisory behavior files.
- Ops is constrained to law/governance behavior and does not execute runtime.
- Exec remains the only layer that can finalize user-visible completion truth.
- Identity can remain semantically stable during kernel rebuild without adding unnecessary formatting churn.

### Affected
- Instructions
- `02_Operations_Law.md`
- `03_Exec.md`
- Identity kernel / `01_Identity.md`
- overall v0.11.0 kernel authority model

### SemVer
- `0.11.0` — minor pre-1.0 architectural update

## [2026-03-31] Blu v0.11.0 PASS Rebuild

### Changed
- Merged the stronger surviving v0.10.0 PASS contract/rebuild work with the stronger v0.9.0 kernel ownership/routing structure to establish Blu v0.11.0 as the current rebuild baseline.
- Updated `03_Exec.md` to `version: 3.2.7` and `updated: 2026-03-31`.
- Stripped stale PASS / SkillForge residue from `03_Exec.md -> M09 | Router prehook and kernel enforcement`, leaving only generic Exec fail-closed boundary rules:
  call `router.prehook()` first
  do not bypass resolution / validation / commit
  do not equate understanding with completion
  do not print success for blocked / unresolved / uncommitted operations
- Registered PASS as a real Program owner in `06_Programs.md`:
  `PASS:` → `PROGRAM.PASS` | status=`DRAFT` | surface=`/pass`
- Added `/pass ...` to `06_Programs.md -> COMMAND SURFACE MAP`.
- Added `PROGRAM.PASS` as a DRAFT Program body with:
  `logical_name: PASS`
  `surface: /pass`
  `nl_enabled: true`
  file autostart metadata
  entrypoints:
    `preflight`
    `gut_ladder`
    `modernize_overlay`
  implementation spine:
    PREFLIGHT
    RAW_EXTRACTION
    SYNTHESIS
    DEDUPE_REJECT_COMPARE
    VARIANT_CROSSLINK_GRAPH
    NORMALIZATION
    REPO_DROP_AND_LANE_PACK
- Updated `05_Commands.md` to acknowledge PASS as live public surface:
  added `PASS` to `live_topics`
  added `## PASS`
  added `PASS` to `live_public_areas`
  updated file header to `version: 0.11.0` and `updated: 2026-03-31`
- Locked current PASS rebuild direction around:
  PASS as compiler, not runtime/router
  one normalized core object set
  two downstream SkillForge lane packs:
    Skill lane
    Teach lane
  Teach lane may consume Skill lane outputs
  Skill lane must never consume Teach lane outputs
- Preserved the current truth boundary:
  PASS is now legally real in kernel ownership/routing
  PASS compiler implementation remains `DRAFT`
  no claim of full rebuild or release-candidate completion is made

### Why
- Previous PASS rebuild claims were not backed by durable program bodies and surviving artifacts showed contract/spec/roadmap truth more clearly than implementation truth.
- Old PASS / SkillForge residue inside Exec had to be removed before any honest PASS rebuild work could continue.
- PASS could not be treated as executable under Program-first law until it had:
  a registered Program owner
  a wired public route
  a real Program body
- `05_Commands.md` was lagging `06_Programs.md`, which created public-surface drift even after PASS was wired in Programs.
- v0.11.0 is the first clean baseline where Exec, Commands, and Programs agree that `/pass` exists, is Program-owned, and is still draft truthfully.

### Impact
- PASS is no longer ghost architecture or floating contract text.
- `/pass` now has a legitimate kernel owner and routable public surface.
- Exec, Commands, and Programs are aligned enough to begin proof testing without pretending the compiler is complete.
- PASS remains fail-closed and artifact-first:
  no source → no run
  blocked preflight → no gut run
  partial packaging does not equal success
- v0.11.0 should be treated as:
  structurally integrated
  routing-clean
  truthfully draft
  ready for first real proof run
- Next validation target is one real PASS test:
  `/pass preflight`
  `/pass gut`
  inspect emitted artifacts instead of relying on summaries or assumptions

### Affected
- `03_Exec.md`
- `05_Commands.md`
- `06_Programs.md`
- PASS routing / ownership surface
- PASS rebuild baseline for Blu v0.11.0

## [2026-04-05] Support phase registry baseline

### Changed
- Introduced a two-phase support registry (`per_turn`, `intent_gated`) for Exec-owned turns.
- Updated Exec to resolve support-lane selection through the phase registry instead of ad hoc logic.
- Extended ExecLib metadata to include support-phase fields.
- Added support-phase metadata to:
  `SERVICE.TIME.001` (intent_gated)
  `EXECLIB.MOODLIB.001` (per_turn)
- Added guardrails preventing registry misuse as routing or ownership authority.

### Why
- Exec lacked a canonical mechanism to decide when to call ExecLib support lanes.
- Time Service and MoodLib were not consistently invoked due to missing trigger structure.
- A phase-based registry provides a scalable, deterministic bridge from need → support lane without growing Exec logic.

### Impact
- Exec becomes cleaner by removing support-specific glue logic.
- Mood heartbeat and render path can run reliably via `per_turn` phase.
- Time requests resolve deterministically via `intent_gated` phase.
- Future support lanes can be added without expanding Exec complexity.

### Affected
- `02_Operations_Law.md`
- `03_Exec.md`
- `04_Exec_Library.md`

## [2026-04-06] Truth Gates, Debug Failure Injection, and Ledger Integrity Hardening

### Changed
- Hardened Operations truth law with:
  - `Pressure Truth Lock Law`
  - `One-Way Correction Latch Law`
  - `Artifact Delivery Truth Law`
  - `Ledger Integrity Law`
- Extended Exec validation with:
  - pressure-truth enforcement before relational repair
  - correction-latch gating for downgraded claims
  - artifact-output gating for completion wording
  - ledger-truth gating before finance arithmetic
- Added ExecLib support for:
  - `EvidenceHeaderLib`
  - `Artifact Proof Boundary`
  - `FinanceLedgerLib`
- Expanded the live DEBUG public surface with:
  - `/debug fail time`
  - `/debug fail mood`
  - `/debug fail phase`
  - `/debug fail state`
  - `/debug fail clear`
- Extended `PROGRAM.DEBUG` to own the new one-shot failure-injection entrypoints under Admin-only access.
- Added Exec runtime hooks for:
  - one-shot DEBUG support-path failure injection
  - one-shot DEBUG validation/state failure injection
  - verification coverage for arming, consumption, clearing, and no-hidden-continuation behavior

### Why
- Prevent truth from degrading under user pressure, especially around file access, read status, artifact completion, and recovery wording.
- Stop corrected false frames from silently re-inflating later in the same turn without fresh proof.
- Block completion-shaped language when only filenames, paths, intent, or partial output exist.
- Make finance math explicitly distinguish execution truth from coverage truth.
- Add a bounded, Admin-only way to force support-path and validation failures for real kernel testing.

### Impact
- Angry or disputed turns now require truth-state disclosure before repair posture.
- File/access/artifact claims are harder to overstate.
- “Paid but not yet covered” finance items can remain visible in cash-requirement truth until coverage is confirmed.
- DEBUG can now arm one-shot failure injection for time, mood, support-phase, and validation/state paths without creating a background process or second executor.
- Exec verification now covers the new truth gates and failure-injection behaviors.

### Affected
- `02_Operations_Law.md`
- `03_Exec.md`
- `04_Exec_Library.md`
- `05_Commands.md`
- `06_Programs.md`