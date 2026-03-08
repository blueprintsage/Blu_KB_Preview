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

## 2026-03-07 — Exec 3.0 Phase 1 Closeout: Exec Truth Lock

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

## 2026-03-07 — Exec 3.0 Phase 2 Closeout: Verification + Wiring Lock

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

## 2026-03-07 — Exec 3.0 Phase 3 Closeout: Intuition Introduction

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

## 2026-03-07 — Exec 3.0 Phase 4 Closeout: Service Model Lock

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

## 2026-03-07 — Exec 3.0 Phase 5 Closeout: Event Class Model Lock

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

## 2026-03-07 — Exec 3.0 Phase 6 Closeout: Program Demotion / Boundary Cleanup

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

## 2026-03-07 — Exec 3.0 Phase 7 Closeout: v0.9.0 Architecture Lock Review

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