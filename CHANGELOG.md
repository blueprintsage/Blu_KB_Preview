# CHANGELOG (Preview Repo)

All notable changes to this repository will be documented in this file.

Format: Keep entries additive. Prefer “Added / Changed / Fixed / Removed”.  
Dates are local: America/Chicago.  

## [2026-03-06] - Standardize kernel capsule module formatting

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

## [2026-03-06] - Clean up Program_System and convert capsule to module format

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

## [2026-03-06] - Start Exec 3.0 Phase 1 kernel truth pass

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
 
## [2026-03-06] - Remove reminder capability from active kernel capsules

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

## [2026-03-06] - Advance Exec 3.0 Phase 2 around dispatch packets, owner resolution, and commit gating

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

## [2026-03-06] - Restore PASS dual-lane as the default for teachable skill sources

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

## [2026-03-06] - Rewrite Commands from the ground up around live public surface only

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

## [2026-03-07] - Mood render contract enforcement + changelog law

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
  - canonical inbound dispatch
  - single public output authority
  - one-owner route resolution
  - fail-closed ambiguity handling
  - commit-before-confirmation discipline
  - no workflow ownership by Exec
- Advancement now moves to **Phase 2 — Verification + Wiring Lock**
- Remaining work includes:
  - expanding verification to live route families
  - auditing Commands ↔ Program_System ↔ Exec wiring
  - archiving pass/fail logs for real-path testing

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
  - full live public surface in `05_Commands.md`
  - Program-owned public route subset in `06_Program_System.md`
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
  - **Commands** = canonical index of the full live public surface
  - **Program_System** = canonical map of live Program-owned public routes only
  - **Exec** = runtime resolver across both lanes
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
  - requester semantics
  - prompt / interaction surface behavior
  - focus / active-context helpers
  - interrupt presentation rules
  - surface-event mediation
- Added an explicit boundary map defining:
  - what Intuition owns
  - what Exec keeps
  - what Programs keep
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
  - **Exec** = runtime truth boundary
  - **Intuition** = interaction/event surface layer
  - **Programs** = workflow ownership
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
  - `Service Charter v1`
  - `Service Contract v1`
  - `Service Class Map v1`
- Defined the initial bounded service classes:
  - `TIMER`
  - `MEMORY`
  - `TOOL`
  - `STORAGE`
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
  - **Exec** = runtime truth boundary
  - **Intuition** = interaction/event surface layer
  - **Programs** = workflow ownership
  - **Services** = bounded helper execution
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
  - `Event Class Charter v1`
  - `Event Class Map v1`
  - `Event Subscription and Filter Law v1`
- Defined the initial event classes:
  - `SYSTEM`
  - `SURFACE`
  - `PROGRAM`
  - `SERVICE`
  - `TIME`
  - `ADMIN`
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
  - **Exec** remains the runtime truth boundary
  - **Intuition** remains the interaction/event surface layer
  - **Programs** remain workflow owners
  - **Services** remain bounded helper lanes
  - **Events** are typed coordination signals only
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
  - `07_Engine.md`
  - `08_Teaching.md`
  - `09_School_Engine.md`
- Moved canonical **School** workflow ownership into `06_Programs.md` as `PROGRAM.School.v1`.
- Moved canonical **Teaching** workflow ownership into `06_Programs.md` as `PROGRAM.Teaching.v1`.
- Added `TEACH:` to the Program assign map.
- Reduced `07_Engine.md` from mixed domain/runtime ownership to a **thin integration layer**:
  - routing is now integration-only
  - Teaching and School are now integration notes only
  - TASK / ART / CPM are now transitional integration notes
  - legacy hotfix material is quarantined as archive note rather than active canon
- Explicitly bounded `08_Teaching.md` and `09_School_Engine.md` as transitional/supporting specs rather than canonical owners.

### Why
- To reduce kernel-adjacent sprawl and stop domain workflow from living in Engine-space.
- To align actual content placement with the locked architecture:
  - **Exec** = runtime truth boundary
  - **Intuition** = interaction/event surface
  - **Programs** = workflow ownership
  - **Services** = bounded helper execution
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
- `Exec 3.0 — Phase 6 Program Demotion - Boundary Cleanup.md`

## [2026-03-07] — Exec 3.0 Phase 7 Closeout: v0.9.0 Architecture Lock Review

### Changed
- Closed out **Phase 7 — v0.9.0 Architecture Lock Review** under the v0.9.0 roadmap.
- Completed the architecture lock review across:
  - `02_Operations_Law.md`
  - `03_Exec.md`
  - `04_Exec_Library.md`
  - `05_Commands.md`
  - `06_Programs.md`
  - `07_Engine.md`
  - `08_Teaching.md`
  - `09_School_Engine.md`
- Confirmed the locked architecture split:
  - **Exec** = runtime truth boundary
  - **Intuition** = interaction/event surface layer
  - **Programs** = workflow ownership
  - **Services** = bounded helper execution
  - **Events** = typed coordination signals only
  - **Commands** = canonical index of the full live public surface
  - **Engine** = thin integration layer only
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
  - hardware-bang verification prompts
  - legacy Program synchronization
  - transitional file retirement/archive
  - further cleanup of dormant residue
  - manual/kernel-doc workflow improvements
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
  - `usercap_v2.prefs.art_pipeline.*`
  - `usercap_v2.prefs.repo.offer_on_teach`
  - `usercap_v2.prefs.ticks.*`
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
  - **Command Surface Map** = public availability
  - **Assign Map** = explicit ownership

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
  - `now_iso`
  - `effective_tz`
  - `new_day_bool`
- Clarified tick emission behavior:
  - may emit `TIME.tick` on every successful tick
  - may emit `TIME.new_day` only when `new_day_bool=true`
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
  - kept `DateLib` as ExecLib time/date utility logic
  - added `Time Service` as the `TIMER`-class runtime owner for tick, rollover, and reminder-due behavior
- Removed student-specific input from `DateLib.format_day_banner`.
- Clarified `Time Service.tick` emission rules:
  - may emit `TIME.tick` on every successful tick
  - may emit `TIME.new_day` only when `new_day_bool=true`
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
  - `DateLib` handles deterministic transforms
  - `Time Service` handles runtime timing signals
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
  - `nl_enabled: true`
  - `nl_tags`
  - `nl_aliases`
  - `nl_examples`
- Migrated Teaching behavior into the Program body, including:
  - ownership boundary
  - propose-only Exec ABI
  - instructional method
  - textbook/source integration
  - lesson flow
  - mastery/pass logic
  - K-12 coverage
  - proposal bands and proposal table
  - defaults, tiers, walkthrough structure
  - troubleshooting, templates, checklist, and rubric
- Updated Exec routing guidance so Program auto-kick from natural language requires:
  - registry entry
  - canonical public route
  - `nl_enabled: true`
  - declared NL metadata

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
  - split deterministic time logic into `DateLib`
  - added/clarified `Time Service` ownership boundaries
  - added `local_weekday` for explicit weekday/weekend resolution
- Updated `05_Commands.md` to harden Exec-native command handling so public controls like `/usercap ...` do not require Program-map ownership.
- Updated `06_Programs.md` to:
  - remove `.v1` suffixes from Program IDs
  - use stable Program IDs plus explicit `version:` metadata
  - add `PROGRAM.Teaching`
  - wire `/teach ...` into the Program command surface
  - add NL metadata for Teaching auto-kick
- Updated `08_Teaching.md` to align with `PROGRAM.Teaching` as the canonical Teaching authority / migration target.
- Exported refreshed kernel bundle for runtime testing:
  - `03_Exec.md`
  - `04_Exec_Library.md`
  - `05_Commands.md`
  - `06_Programs.md`
  - `08_Teaching.md`

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
  - `courses/`
  - `grades/`
  - `packets/`
  - `school/`
  - `textbooks/`
- Created first-pass Grade 11 curriculum course shells for:
  - Algebra 2
  - British Literature
  - Modern American History
  - Physics w Lab
  - Life Skills
- Created `PACKET_SYSTEM_SPEC.md`.
- Created `GRADE.11.md`.
- Created first-pass `TEXTBOOK_REGISTRY.md`.
- Built first-pass packet trios for:
  - Algebra 2
  - British Literature
  - Modern American History
  - Physics w Lab
  - Life Skills
- Wired the active Grade 11 course shells to packet bundles and Day 132 checkpoint behavior.
- Replaced the student-specific course registry design with:
  - repo-safe `COURSE_REGISTRY.md`
  - student-specific active course load inside the student school record
- Expanded the student school record model to include:
  - active course load
  - course history
  - prerequisite warnings
  - parent override notes
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
  - `EXECLIB.ANTIDRIFT.001`
  - typed object-state axes
  - guidance-origin classes
  - contamination-aware count helpers
  - forbidden transition edges
  - snapshot inclusion helpers
- Updated `03_Exec.md` to add:
  - anti-drift classification gate
  - object-axis gate
  - exact-field-only count rule
  - guidance-origin gate
  - compact-state inclusion control
- Updated `02_Operations_Law.md` to add:
  - explicit anti-drift law for axis separation
  - contaminated-state/count handling
  - guidance-vs-state separation
  - required answer shape discipline
  - new failure labels
- Updated `06_Programs.md` to add:
  - project-object state schema
  - compact snapshot law
  - derived-count law
  - stronger program anti-drift runtime locks

### Why
- The Veldt ambiguity corpus exposed a different drift family than earlier corpora.
- Earlier protections were strong on:
  - canon vs candidate
  - archive vs active
  - prior vs current
  - source vs matching artifact
- Weaknesses were exposed on:
  - object-axis ambiguity
  - contaminated derived counts
  - guidance-vs-state ambiguity
  - authority-promotion pressure

### Impact
- Reduced risk of illegal field jumps such as:
  - receipt -> legitimacy
  - legitimacy -> authority
  - classification -> active input
  - guidance -> project state
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
  - `/debug on`
  - `/debug off`
  - `/debug state`
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
  - typed state over transcript residue
  - contaminated memory quarantine
  - guidance-origin separation
  - exact-field storage
  - compact model-ready continuity views
  - demand-loading and token efficiency
  - reduced scaffolding reload

### Why
- The earlier drafts were written before the full drift families were visible.
- The new kernel hardening showed that continuity storage must preserve exact fields and unresolved state, not just general facts.
- Long ambiguity runs showed that token load is driven by carrying explanations rather than compact state.

### Impact
- MMU now aligns more cleanly with the hardened kernel philosophy:
  - carry forward declarations, unresolveds, and guards
  - not long prose justifications
- Better expected performance for:
  - cold-start resumption
  - long-chat continuity
  - lower recap burden
  - reduced visible token load
  - lower scaffolding drift

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
  - bumped file version to `0.9.3`
  - added `EXECLIB.MMU.001` / `MMULib`
  - added DOA filtering, memory candidate classification, promotion validation, typed pool shaping, continuity packet building, memcap shaping, and compact preload helpers
- Updated `02_Operations_Law.md`:
  - bumped file version to `0.9.4`
  - added `MMU continuity law`
  - added durable-memory boundaries, forbidden transcript residue, promotion requirements, typed-state memory rules, and preload restrictions
- Updated `03_Exec.md`:
  - bumped file version to `3.2.4`
  - added `Continuity overlay gate`
  - added continuity read/write orchestration, live-session override handling, and debug-aware continuity visibility rules

### Why
- Needed MMU capability without creating a separate MMU kernel family or consuming additional kernel-slot footprint.
- Needed continuity storage to align with the hardened anti-drift model:
  - state, not deliberation
  - exact fields, not adjacent prose
  - compact preload, not transcript replay
- Needed lower token drag and better long-chat resumption without loosening drift protections.

### Impact
- MMU now lives inside the existing kernel stack:
  - law in `02`
  - mechanism in `04`
  - orchestration in `03`
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
  - `EXECLIB.ANTIDRIFT.001`
  - typed object-state axes
  - guidance-origin classes
  - contamination-aware count helpers
  - forbidden transition edges
  - snapshot inclusion helpers
- Updated `03_Exec.md` to add:
  - anti-drift classification gate
  - object-axis gate
  - exact-field-only count rule
  - guidance-origin gate
  - compact-state inclusion control
- Updated `02_Operations_Law.md` to add:
  - explicit anti-drift law for axis separation
  - contaminated-state/count handling
  - guidance-vs-state separation
  - required answer shape discipline
  - new failure labels
- Updated `06_Programs.md` to add:
  - project-object state schema
  - compact snapshot law
  - derived-count law
  - stronger program anti-drift runtime locks

### Why
- The Veldt ambiguity corpus exposed a different drift family than earlier corpora.
- Earlier protections were strong on:
  - canon vs candidate
  - archive vs active
  - prior vs current
  - source vs matching artifact
- Weaknesses were exposed on:
  - object-axis ambiguity
  - contaminated derived counts
  - guidance-vs-state ambiguity
  - authority-promotion pressure

### Impact
- Reduced risk of illegal field jumps such as:
  - receipt -> legitimacy
  - legitimacy -> authority
  - classification -> active input
  - guidance -> project state
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
  - `/debug on`
  - `/debug off`
  - `/debug state`
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
  - typed state over transcript residue
  - contaminated memory quarantine
  - guidance-origin separation
  - exact-field storage
  - compact model-ready continuity views
  - demand-loading and token efficiency
  - reduced scaffolding reload

### Why
- The earlier drafts were written before the full drift families were visible.
- The new kernel hardening showed that continuity storage must preserve exact fields and unresolved state, not just general facts.
- Long ambiguity runs showed that token load is driven by carrying explanations rather than compact state.

### Impact
- MMU now aligns more cleanly with the hardened kernel philosophy:
  - carry forward declarations, unresolveds, and guards
  - not long prose justifications
- Better expected performance for:
  - cold-start resumption
  - long-chat continuity
  - lower recap burden
  - reduced visible token load
  - lower scaffolding drift

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
  - bumped file version to `0.9.3`
  - added `EXECLIB.MMU.001` / `MMULib`
  - added DOA filtering, memory candidate classification, promotion validation, typed pool shaping, continuity packet building, memcap shaping, and compact preload helpers
- Updated `02_Operations_Law.md`:
  - bumped file version to `0.9.4`
  - added `MMU continuity law`
  - added durable-memory boundaries, forbidden transcript residue, promotion requirements, typed-state memory rules, and preload restrictions
- Updated `03_Exec.md`:
  - bumped file version to `3.2.4`
  - added `Continuity overlay gate`
  - added continuity read/write orchestration, live-session override handling, and debug-aware continuity visibility rules

### Why
- Needed MMU capability without creating a separate MMU kernel family or consuming additional kernel-slot footprint.
- Needed continuity storage to align with the hardened anti-drift model:
  - state, not deliberation
  - exact fields, not adjacent prose
  - compact preload, not transcript replay
- Needed lower token drag and better long-chat resumption without loosening drift protections.

### Impact
- MMU now lives inside the existing kernel stack:
  - law in `02`
  - mechanism in `04`
  - orchestration in `03`
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
  - active project state
  - secondary side-thread state
  - temporary vent / emotional material
- Added faster salience cooling after explicit user pivots back to project work.
- Added/recognized MMU schema concepts for:
  - `thread_scope`
  - `salience_state`
- Reframed memcaps into a **family** instead of a one-template default model:
  - Normal Memcap
  - Project Memcap
  - Raw Dump Memcap
  - Cold Store Memcap
  - Memory Vault entry
- Repositioned Cold Store away from default routine carry and into **archival preservation**.
- Established **Normal Memcap** as the default routine handoff.
- Established **Project Memcap** as the scoped project handoff.
- Established **Raw Dump Memcap** as the readable long-form carry.
- Added the **Memcap Wizard** as the selector for ambiguous memcap requests.
- Added fast-path memcap command support expectations:
  - `/memcap normal`
  - `/memcap project`
  - `/memcap raw`
  - `/memcap cold`
  - `/memcap vault`

### Why
- Long burn-in testing showed MMU was performing well on live session continuity, but still drifted toward cross-chat durability assumptions that were never the real target.
- Side-thread emotional heat was lingering slightly too long after explicit pivots back to project work.
- One memcap template was no longer enough to cover:
  - routine next-chat continuity
  - project-only handoff
  - readable long-form carry
  - archival preservation
  - memory-vault storage
- Generic memcap requests had become ambiguous and needed a selector instead of guesswork.

### Impact
- MMU should now behave more cleanly as a **session-scoped continuity manager**.
- Cross-chat continuity becomes more explicit and less accidental.
- Side-thread contamination should cool faster after explicit “move on / back to project” pivots.
- Users can request memcaps through either:
  - the Memcap Wizard (ambiguous request path)
  - direct fast-path command forms
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
  - `/memcap normal`
  - `/memcap project`
  - `/memcap raw`
  - `/memcap cold`
  - `/memcap vault`
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
  - MMU remains session-scoped
  - memcaps handle explicit cross-chat handoff
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
  - `/mood on` = every prompt
  - `/mood smart` = change or heartbeat
  - `/mood show` = explicit ask
  - `/mood off` = no automatic render
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
