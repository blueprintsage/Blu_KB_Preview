capsule_id: kb__index_backlog_md__cc3b4c
title: "Backlog"
date: 2026-02-24
updated: 2026-02-24
version: 0.1.0
status: draft
topic: blu
type: spec
tags: ['index']
sensitivity: medium
visibility: shared
source: repo
domain: index
schema: capsule_header_v1.1
body_schema: blu_modular_v1
---

<!--
Backlog / Next Packs (canonical)
Extracted from legacy Interim repo index into a single edit point.
Paste-safe: no YAML front matter.
-->

# Backlog / Next Packs
- DP-WEB-001 Web/App Dev (React + APIs + debugging)
- DP-DATA-001 Spreadsheets & analysis workflows
- DP-OPS-001 Personal productivity / task systems
- DP-EDU-001 Lesson plan generator (multi-level scaffolding)


## DP-SCR-001 Screenwriting
**Scope:** Film/TV/web scripts: beat sheets, outlines, scene lists, draft pages, and rewrite passes.

### Schema
**Required**
- Logline
- Format target (short/feature/episode)
- Genre + tone
- Key beats (or “generate beats”)

**Optional**
- Act structure preference (3-act, etc.)
- Character list + arcs
- “Must-have” scenes/lines

### Checks
- [ ] Each act turns (inciting incident, midpoint, low point, climax).
- [ ] Every scene has a purpose (reveal, reversal, decision).
- [ ] Dialogue has conflict or subtext (not info dumps).
- [ ] Revisions are pass-based (structure → scenes → dialogue).

### Failure-modes
- “Act 2 sags” → no escalation → add complications + ticking clock.
- “Too many characters” → dilution → merge roles; cut subplots.
- “On-the-nose dialogue” → no subtext → rewrite with intent + obstacle.
- “Confusing geography” → missing scene anchors → add establishing beats.

### Knobs
- Structure strictness (loose ↔ strict)
- Scene density (sparse ↔ dense)
- Dialogue style (minimal ↔ talky)
- Stakes (low ↔ high)

---


## DP-COM-001 Comics Pipeline
**Scope:** Comic scripting for pages/panels: pacing, readability, dialogue density, and production-ready scripting.

### Schema
**Required**
- Page count (or single page)
- Panels per page target (range)
- Art style notes (realistic, manga, etc.)
- Cast list (who appears)

**Optional**
- Lettering constraints (word count per panel)
- Key reveals/moments
- Issue arc (if serialized)

### Checks
- [ ] Page turn moments are planned (reveals at end of page).
- [ ] Panel-to-panel flow is readable (eye path).
- [ ] Dialogue density fits panel real estate.
- [ ] Each page has a beat (mini-arc).
- [ ] Characters remain consistent (names, traits, visual cues).

### Failure-modes
- “Too wordy” → panel overload → cut lines, split panels, use visuals.
- “Hard to follow” → weak staging → add establishing panel and clearer action.
- “Pacing off” → beats not spaced → adjust panels/page; add silent panels.
- “Tone shifts” → inconsistent voice → add tone rules + re-pass.

### Knobs
- Panel density (3–5 ↔ 6–9)
- Dialogue density (low ↔ high)
- Visual clarity (simple ↔ complex)
- Action vs emotion emphasis

---


## Game Dev

## DP-GOD-001 Godot 4.x Gameplay & Debugging
**Scope:** Node/scene architecture, GDScript gameplay features, debugging and migration discipline.

### Schema
**Required**
- Goal feature (movement / dash / UI / save / etc.)
- Godot version (4.x) + target platform
- Scene context (which nodes exist; player controller type)
- Inputs (actions and mappings)
- Constraints (feel targets: speed, cooldown, camera)

**Optional**
- Minimal Repro Scene plan
- Signals/events expected
- Performance constraints

### Checks
- [ ] Feature works in a **minimal repro scene** (no unrelated dependencies).
- [ ] Inputs are mapped and tested (pressed/just_pressed, etc.).
- [ ] State transitions are explicit (e.g., Idle → Dash → Recover).
- [ ] Timers/cooldowns are deterministic (no frame-rate dependence).
- [ ] Debug output (prints or on-screen) validates state and key vars.

### Failure-modes
- “Dash cancels randomly” → state overwritten by movement code → gate movement during dash state.
- “Speed varies with FPS” → using `_process` for physics → move to `_physics_process` + delta usage.
- “Input doesn’t fire” → action not mapped → check Project Settings input map.
- “Player clips walls” → no collision handling → use move_and_slide + collision checks.
- “Hard to debug” → no minimal repro → extract to a tiny scene with just the player + collider.

### Knobs
- Movement feel (snappy ↔ floaty)
- Dash distance (short ↔ long)
- Dash invulnerability (off ↔ on)
- Cooldown (none ↔ long)
- Camera behavior (locked ↔ follow ↔ damped)
- Debug verbosity (none ↔ prints ↔ on-screen overlay)
- Architecture (monolith ↔ component nodes ↔ data-driven)


### Working Patterns
**PAT-GOD-001 State Gate for Abilities**
- **Use when:** movement/abilities conflict.
- **Steps:** define states → gate input per state → transition rules → timers in physics.
- **Checks:** no overlapping states; deterministic end conditions.
- **Failure-modes:** state overwritten → centralize state updates.
- **Knobs:** dash duration; cooldown; control lock.

**PAT-GOD-002 Minimal Repro Scene**
- **Use when:** bug is hard to reproduce.
- **Steps:** new scene → player + one collider → reproduce → add debug prints.
- **Checks:** bug reproduces in isolation; fix verified.
- **Failure-modes:** dependencies missing → stub them.
- **Knobs:** repro complexity; debug verbosity.

### Drills
- **DRL-GOD-001 (10 min):** Build a minimal dash state machine sketch + 3 checks.
- **DRL-GOD-002 (15 min):** Create a minimal repro plan for a physics bug + what to log.

### Minimal Example (micro-output)
State machine sketch:
- Variables: `is_dashing`, `dash_timer`, `dash_dir`
- Checks: dash ends after duration; cooldown prevents retrigger.

---


## DP-UNI-001 Unity Gameplay & Debugging
**Scope:** Unity engine gameplay systems, architecture, debugging workflows, and performance hygiene (C#).

### Schema
**Required**
- Unity version + target platform
- Feature goal (movement/UI/save/combat/etc.)
- Current behavior vs desired behavior
- Constraints (feel targets, perf, input scheme)

**Optional**
- Minimal repro scene plan
- Relevant scripts (snippets) + errors/logs
- Package context (Input System vs old input, URP/HDRP, etc.)

### Checks
- [ ] Works in a minimal repro scene.
- [ ] Inputs are mapped and verified.
- [ ] State transitions are explicit (no magic booleans everywhere).
- [ ] Profiling sanity pass completed (CPU/GPU spikes identified).
- [ ] Build test passes (not just Editor).

### Failure-modes
- “Works in Editor, breaks in build” → missing assets/stripping/settings → add build checks + logs.
- “Random null refs” → lifecycle order + missing refs → validate in Awake/OnEnable; add guards.
- “Janky movement” → mixing Update/FixedUpdate → move physics to FixedUpdate.
- “GC spikes” → per-frame allocations → cache refs; avoid LINQ in hot paths.
- “Input not firing” → wrong system/settings → verify Input System package + project settings.

### Knobs
- Architecture (quick script ↔ componentized)
- Debug verbosity (none ↔ overlay)
- Perf focus (readable ↔ optimized)
- Input system (legacy ↔ new)
- Test depth (smoke ↔ thorough)

---


## DP-BP-001 Blueprint Scripting
**Scope:** UE-style Blueprint logic: exact node naming, wiring clarity, debugging flow, maintainable graphs.

### Schema
**Required**
- Engine version + context (Actor/Component/Widget)
- Graph location (Event Graph / Function / Macro)
- Inputs (events, parameters) + expected outputs
- Current behavior vs desired behavior
- Constraints (performance, replication, readability)

**Optional**
- Screenshots of graph
- Variable list (name, type, defaults)
- Data assets/tables involved

### Checks
- [ ] Uses exact node and pin names; specifies where actions happen in UI.
- [ ] Validates inputs early (null/empty/range) with explicit fail path.
- [ ] Debug plan included (prints/breakpoints/watches) for each branch.
- [ ] Graph intent is documented (comments on *why*, not *what*).

### Failure-modes
- “Wrong branch fires” → condition inverted or stale state → print values right before branch; verify exec flow.
- “Loop runs off-by-one” → unclear bounds → make bounds explicit; log index start/end.
- “Random null” → missing validation → add IsValid + fallback or early return.
- “Spaghetti graph” → hidden state and long wires → refactor into functions; expose inputs.

### Knobs
- Explicitness (beginner hand-holding ↔ expert terse)
- Debug instrumentation (none ↔ prints ↔ breakpoint-heavy)
- Refactor level (leave as-is ↔ split into functions)
- Data-driven (hardcoded ↔ struct/table-driven)
- Performance (readable ↔ optimized)

### Working Patterns
**PAT-BP-001 Validate → Branch → Handle Fail**
- **Use when:** runtime errors or nulls.
- **Steps:** IsValid → Branch → fail output (log + return) → success path.
- **Checks:** fail path triggers on null; success path unaffected.
- **Failure-modes:** fail path too noisy → add verbosity knob.
- **Knobs:** verbosity; fallback behavior.

**PAT-BP-002 Loop N Times With Clear Bounds**
- **Use when:** arrays/loops behave unexpectedly.
- **Steps:** define start/end → ForLoop → log index + item → break conditions.
- **Checks:** indexes match expectation; no out-of-range.
- **Failure-modes:** array changes during loop → copy array or iterate safely.
- **Knobs:** bound type (count vs last index); logging.

**PAT-BP-003 Data-Driven Selection (Struct/Table)**
- **Use when:** too many branches.
- **Steps:** define struct → lookup row → select fields → apply.
- **Checks:** row found; defaults applied if missing.
- **Failure-modes:** missing row → add fallback row.
- **Knobs:** fallback policy; table vs map.


**PAT-BP-004 Overlap Array Validity Guard (Run+Drop / Fast Movement)**
- **Use when:** A variable “randomly” becomes `None` during fast actions (run + drop, detach/attach, physics enabling), especially inside overlap/nearby-player loops.
- **Schema:** Inputs: `Overlaps/Players Array`, `Get Player Ref (Interface)`, `InteractingPlayer` (or similar). Assumption: array entries can become stale mid-frame.
- **Steps:** `IsValid(Array Element)` → Branch → (True) `Get Player Ref` → (recommended) `IsValid(Output)` → (True) `Set InteractingPlayer = Output`; otherwise skip. Never write `None` as a side effect of invalid input.
- **Checks:** (1) 20 consecutive run+drop attempts without unexpected clearing. (2) Invalid entries are skipped and do not affect state.
- **Failure-modes:** Still `None` → another setter exists (guard all); Output `None` → add `IsValid(Output)` + log; Multiplayer overwrite → move setter to authority/server.
- **Knobs:** Guard strictness; logging level; state-clear policy; loop strategy (snapshot vs dynamic); authority (client-predict vs server-only).


**PAT-BP-005 RepNotify Stability During Pickup (Don’t Clear Mid-Flow)**
- **Use when:** First pickup replicates fine, but second pickup leaves the client acting like the new weapon is `None`/unchanged (OnRep/equip/UI doesn’t update).
- **Schema:** Inputs: RepNotify `LootedWeapon` (weapon ref), pickup RPC(s), equip/attach logic, UI update path. Assumption: replication/OnRep timing is not guaranteed relative to RPC order and other state writes.
- **Steps:**
  1) **Remove** any `Set LootedWeapon (RepNotify) = None` from the **pickup/equip** code path.
  2) Keep `LootedWeapon` valid through: pickup → equip/attach → UI refresh.
  3) Move the “clear” to the **end of the drop** code path: after detach/physics/collision settle, then `Set LootedWeapon (RepNotify) = None`.
  4) If you need a “consumed” signal, use a separate non-RepNotify flag/event (or clear after the client confirms processing).
- **Checks:**
  - (1) Client successfully picks up weapon #1 and weapon #2 in the same session; OnRep fires and UI/equip reflects weapon #2.
  - (2) `LootedWeapon` never becomes `None` on client during pickup/equip unless explicitly dropping/clearing.
  - (3) In logs, the order is stable: set valid ref → OnRep processes → (later) clear on drop only.
- **Failure-modes:**
  - Still stale on client → value is being set/cleared in another place → search all `Set LootedWeapon` and centralize behind one setter.
  - OnRep doesn’t run for second pickup → ref is identical (same object) or not “changed” → ensure you assign the new actor ref (or use a separate replicated counter/ID).
  - Multiplayer authority mismatch → client writes are overwritten → ensure setter runs on server; client only reads/requests via RPC.
- **Knobs:**
  - Clear policy: never auto-clear ↔ clear on drop end ↔ clear after client-ack
  - Debug verbosity: none ↔ print OnRep order ↔ include role/netmode + timestamps
  - Rep signal: RepNotify only ↔ RepNotify + “PickupSequenceId” counter
  - Safety: delay clear by N frames ↔ immediate clear after drop finalize
- **Anti-pattern (avoid):** Clearing a RepNotify reference (`Set w/ Notify = None`) inside/near the pickup flow. This can arrive “late” and wipe the client’s state between pickups.


**PAT-BP-006 RepNotify Clear Race Guard (Delay vs Deterministic Clear)**
- **Use when:** `WeaponToDrop` is set correctly to a valid ref, but then “randomly” becomes `None` early because a delayed `Set w/Notify WeaponToDrop = None` fires before drop replication/OnRep/physics completes.
- **Schema:** Inputs: RepNotify `WeaponToDrop` (weapon ref), drop sequence (detach/physics/collision/inventory), OnRep handlers, any post-loop Delay that clears state. Assumption: drop completion is not instantaneous; timing differs by net conditions, movement, and physics.
- **Steps (quick fix):**
  1) Identify the delayed clear: `Delay` → `Set WeaponToDrop (RepNotify) = None`.
  2) Increase the post-loop delay enough that drop/equip/OnRep/physics settle before clearing.
  3) Add debug prints before set-valid, before clear, and inside OnRep to verify ordering.
- **Steps (best practice): replace Delay with deterministic clear**
  1) Introduce a **DropState** (e.g., `IsDropping` or enum) and only clear when state transitions to “DropComplete”.
  2) Define “DropComplete” as a concrete condition, e.g.:
     - detach finished AND
     - physics enabled AND
     - inventory updated AND
     - `DroppedWeapon` (in-world actor) is valid (or replicated) AND
     - (optional) owning client has processed OnRep for the drop
  3) Clear: `Set WeaponToDrop (RepNotify) = None` only after the condition is true.
- **Checks:**
  - (1) During sprint + drop, `WeaponToDrop` remains valid until the drop is finished (no early `None`).
  - (2) Owning client consistently processes the replicated valid ref before any clear (verified by prints/timestamps).
  - (3) With higher ping / packet loss simulation, behavior remains stable (no race regressions).
- **Failure-modes:**
  - Still clears early → there are multiple clears → search all `Set WeaponToDrop` and centralize in one setter.
  - Delay “fix” is inconsistent across machines → timing still nondeterministic → implement deterministic clear condition.
  - OnRep order confusing → add a replicated `DropSequenceId` counter so OnRep can ignore stale clears.
- **Knobs:**
  - Clear strategy: longer delay ↔ deterministic state-based clear
  - Debug: none ↔ prints (role/netmode/time) ↔ full sequence tracing
  - Robustness: no ID ↔ `DropSequenceId` counter
  - Condition strictness: minimal (DroppedWeapon valid) ↔ full (detach+physics+inventory+ack)
- **Anti-pattern (avoid):** Using a short Delay to clear a RepNotify reference when the completion of the underlying drop/replication pipeline is variable.


### Drills
- **DRL-BP-001 (10 min):** Build a small function with 3 checks + 2 “common troubles”.
- **DRL-BP-002 (15 min):** Debug a wrong-branch bug using prints + one breakpoint.

- **DRL-BP-003 (15 min):** Reproduce a “variable becomes None” overlap-loop bug, then fix with `IsValid(Array Element)` + `IsValid(Output)` gates; add 2 checks (20 attempts + “skipped invalid” logging).

- **DRL-BP-004 (15 min):** Instrument pickup/drop replication order (prints with role + time), reproduce “second pickup stale,” then fix by removing mid-pickup clear and moving the RepNotify clear to drop-end; verify with 10 back-to-back double-pickups.

- **DRL-BP-005 (15 min):** Reproduce “WeaponToDrop clears early” by adding a too-short delay, then fix it two ways: (A) tune delay until stable, (B) replace delay with a deterministic DropComplete condition; verify with 10 sprint+drop reps under a simulated high-ping setting.


## DP-GDD-001 Game Design Docs
**Scope:** Game design documents, feature specs, scope control, and “ship-ready” acceptance tests.

### Schema
**Required**
- Pillars (3) + target player fantasy
- Core loop (minute-to-minute)
- Progression (short/mid/long-term)
- Key systems list (combat, economy, crafting, etc.)
- Scope constraints (team size/time/engine)

**Optional**
- Content budget (levels/enemies/items count)
- Economy numbers (placeholder ranges)
- UX flow (menus, onboarding)
- Risks + mitigations

### Checks
- [ ] Every system ties back to a pillar.
- [ ] Core loop is playable in a prototype (MVP defined).
- [ ] Progression has clear goals and feedback.
- [ ] Each feature has acceptance tests (observable).
- [ ] Scope matches constraints (no hidden “MMO” scope).

### Failure-modes
- “Too big to ship” → scope creep → define MVP + cut list.
- “No reason to keep playing” → weak progression → add goals, unlocks, mastery hooks.
- “Systems conflict” → missing invariants → define rules (e.g., economy sinks/sources).
- “Unclear audience” → vague pillars → rewrite pillars as player promises.
- “Design can’t be implemented” → no constraints → add engine/time limits early.

### Knobs
- Scope (MVP ↔ full)
- Detail level (one-pager ↔ full doc)
- Numbers (none ↔ placeholder ranges)
- Risk tolerance (safe ↔ experimental)
- Format (bullets ↔ sections ↔ tables)

---


## Visual AI

## DP-VIS-001 Visual Prompting & Image Generation
**Scope:** Turning a visual spec into robust prompts, iterating via deltas, controlling composition/lighting.

### Schema
**Required**
- Subject + action
- Style target (photoreal / illustration / cinematic / etc.)
- Composition (shot size, angle, framing)
- Lighting (key, mood, time of day)
- Environment/background
- Must-have (3) / Must-avoid (3)

**Optional**
- Camera/lens language (e.g., 35mm, shallow DOF)
- Color mood (warm/cool/contrast)
- Textures/material cues
- Negative prompt list

### Checks
- [ ] Prompt includes **subject + setting + composition + lighting** (all 4).
- [ ] Must-haves are explicitly stated and not contradicted.
- [ ] Must-avoids are expressed as negatives (when supported) or as positive constraints.
- [ ] Iterations use **prompt deltas** (only change what knob changed).
- [ ] Output remains consistent with intended style (no accidental style drift).

### Failure-modes
- “Subject looks wrong” → missing concrete descriptors → add age/shape/material/pose specifics.
- “Busy clutter” → weak composition constraint → add foreground/background separation + framing note.
- “Wrong lighting mood” → vague lighting → specify key direction + softness + time-of-day cues.
- “Style drift” → too many changes per iteration → isolate one knob per iteration.
- “Artifacts / weird anatomy” → insufficient constraints → add realism anchors + simplify pose.

### Knobs
- Realism (illustrative ↔ photoreal)
- Lens/DOF (deep focus ↔ shallow)
- Lighting mood (soft ↔ harsh; golden hour ↔ overcast)
- Composition (centered ↔ rule-of-thirds; wide ↔ close)
- Texture richness (minimal ↔ detailed)
- Background complexity (clean ↔ busy)
- Color grade (neutral ↔ cinematic)
- Iteration mode (one-knob-at-a-time ↔ batch)


### Working Patterns
**PAT-VIS-001 Prompt Skeleton (4-core)**
- **Use when:** prompts keep missing intent.
- **Steps:** subject → setting → composition → lighting → must/avoid list.
- **Checks:** includes all 4; must-haves not contradicted.
- **Failure-modes:** generic results → add concrete descriptors (materials, pose, era).
- **Knobs:** realism; lens; background complexity.

**PAT-VIS-002 One-Knob Iteration**
- **Use when:** outputs drift.
- **Steps:** choose one knob → state delta → regenerate → compare to checks.
- **Checks:** only one variable changed; style consistent.
- **Failure-modes:** multiple changes creep in → restate “only change X”.
- **Knobs:** any knob list.

### Drills
- **DRL-VIS-001 (10 min):** Write a prompt using the 4-core skeleton + 5 knobs.
- **DRL-VIS-002 (15 min):** Run 3 iterations: change one knob each time; keep checks fixed.

### Minimal Example (micro-output)
Prompt skeleton:
- “Photoreal portrait of [subject], [pose], [environment], [lighting], [lens/DOF], [mood]. Must: __. Avoid: __.”
**Checks:** includes 4 core elements; must-have list present.

---


## DP-VIS-002 Image Enhancement & Hyper-Real Edits
**Scope:** “Make it more realistic” while preserving composition/identity—minimal-delta enhancement, artifact cleanup, and targeted edits.

### Schema
**Required**
- Source image(s)
- Must-keep list (pose, outfit, background, composition, etc.)
- Must-change list (exact features to edit)
- Realism target (DSLR photo / game cinematic / studio portrait)

**Optional**
- Reference image(s) for realism/lighting
- Skin/texture preference (subtle ↔ detailed)
- Makeup spec (liner, shadow, lipstick shade)
- Material spec (metal type, emissive color, roughness)

### Checks
- [ ] Must-keep items are preserved (composition, pose, clothing).
- [ ] Only requested features change (no “bonus” implants/logos).
- [ ] Skin/eyes/materials read physically plausible (no plastic skin).
- [ ] No text/logos/watermarks introduced.
- [ ] Face identity remains consistent (no “face drift”).

### Failure-modes
- “Model changes outfit/background” → must-keep list too weak → restate “do not change X” + simplify prompt.
- “Over-smoothing / wax skin” → realism too aggressive → ask for “micro-texture, pores, peach fuzz.”
- “Adds extra tech around eye” → ambiguous cybernetic spec → specify “metallic sclera only; no orbital plating.”
- “Color drift” → vague palette → lock key colors (hair, iris, lipstick).
- “Identity drift” → too many changes → one-knob iteration + keep seed if possible.

### Knobs
- Delta size (minimal ↔ bold)
- Skin detail (subtle ↔ high micro-texture)
- Lighting (soft ↔ dramatic)
- Lens (35mm ↔ 85mm portrait)
- Background (unchanged ↔ softened bokeh)
- Makeup intensity (natural ↔ dramatic)

---


## Video

## DP-VID-001 Video Preproduction
**Scope:** Storyboards, shot lists, coverage, continuity, edit-ready planning.

### Schema
**Required**
- Project type (ad / short / doc / vlog / tutorial)
- Runtime target (or scene count)
- Deliverable type (storyboard | shot list | coverage plan)
- Location(s) + constraints (gear, crew, time)
- Style references (optional links, or descriptive)

**Optional**
- Dialogue/script excerpt
- Key beats (3–9)
- Camera kit / lens kit
- Audio approach (boom/lavs/VO)

### Checks
- [ ] Every beat has at least one **primary shot** and one **coverage option**.
- [ ] Continuity: eyeline + screen direction consistent; 180° line respected (or explicitly broken with intent).
- [ ] Shots specify: framing + action + camera move + purpose (what the edit needs).
- [ ] No “missing insert” risk: props/hands/doorways/text are covered where needed.
- [ ] If dialogue: shot choices support readability (no unnecessary cross-axis confusion).

### Failure-modes
- “Edit feels jumpy” → insufficient coverage → add 2nd angle + inserts + cutaways.
- “Confusing geography” → broken screen direction → re-anchor with establishing shot + maintain axis.
- “Performance continuity breaks” → missing match action → add matched entrances/exits + hand inserts.
- “Too many wide shots” → weak emotional emphasis → add mediums/close-ups on turning points.
- “Schedule blow-up” → over-ambitious shot count → collapse to essential coverage set (A-cam + B-roll).

### Knobs
- Coverage density (minimal / standard / maximal)
- Shot style (static / motivated movement / kinetic handheld)
- Visual grammar (classical / modern / doc)
- Continuity strictness (strict / flexible / stylized breaks)
- Pace target (slow burn / normal / fast-cut)
- Emotion emphasis (more reaction shots / more action beats)
- Lighting plan detail (none / basic / detailed)
- Deliverable format (table shot list / numbered panels / both)


### Working Patterns
**PAT-VID-001 Beat → Coverage Set**
- **Use when:** planning a scene quickly.
- **Steps:** define beat → choose primary (WS/MS/CU) → add 2 cover (reaction + insert/cutaway).
- **Checks:** beat is editable from at least 2 angles; one insert covers continuity risk.
- **Failure-modes:** too many shots → cut to “essential 4” (establish, action, insert, reaction).
- **Knobs:** coverage density; reaction emphasis; insert priority.

**PAT-VID-002 Continuity Anchor**
- **Use when:** geography/axis gets confusing.
- **Steps:** mark 180° line → choose A-side camera zone → keep eyelines consistent → re-establish after any axis break.
- **Checks:** audience can point where characters are; screen direction consistent.
- **Failure-modes:** accidental axis break → swap shot order or add neutral cutaway.
- **Knobs:** strictness; axis break style.

### Drills
- **DRL-VID-001 (10 min):** Take 3 beats and produce an “essential 4” coverage set + 3 checks.
- **DRL-VID-002 (15 min):** Fix a continuity problem: rewrite shot list to restore axis + add one re-establish.

### Minimal Example (micro-output)
- Beat: “Character enters, sees note, decides.”
  - Shot 1: WS establish room + entrance.
  - Shot 2: MS follow to table; action: reach note.
  - Shot 3: CU note text; insert.
  - Shot 4: CU reaction; decision beat.
**Checks:** readable geography, note text legible.

---


## DP-VID-002 Text-to-Video Prompting & Iteration
**Scope:** Tool-agnostic prompting for text-to-video models (e.g., Sora-style), with controlled iteration and artifact control.

### Schema
**Required**
- Subject + action (what changes over time)
- Setting + constraints (indoors/outdoors, time of day)
- Camera spec (angle, distance, movement style)
- Duration + aspect ratio
- Must-have (3) / Must-avoid (3)

**Optional**
- Beat timing (0–2s / 2–4s / 4–6s)
- Lens/DOF language (wide/tele, shallow/deep)
- Motion strength (low/med/high), stabilization (off/on)
- Negative list (logos/text/weird hands/etc.)

### Checks
- [ ] Prompt includes **subject, action, camera, setting** (all 4).
- [ ] Temporal clarity: viewer can describe what happens **each 2 seconds**.
- [ ] Must-avoids are explicit (logos/text/watermarks/hands, etc.).
- [ ] Iteration uses **one knob per run** (no drift).
- [ ] No unwanted new subjects appear (duplicates, extra limbs, extra people).

### Failure-modes
- “Melting rooms / warping geometry” → too much motion + complex environment → reduce motion, simplify background, shorten duration.
- “Jitter/flicker” → unstable camera instruction → specify continuous take + stabilization OR milder handheld.
- “Duplicate subject” → unclear subject identity → “single [subject] only” + exclude duplicates.
- “Weird hands/people” → model invents humans → “no humans in frame” + add hands/limbs to negatives.
- “Action unclear” → vague verbs → add path + milestones (“down hall, left turn, under table…”).

### Knobs
- Camera (handheld ↔ stabilized)
- Motion blur (low ↔ strong)
- Environment detail (clean ↔ busy)
- Duration (4s ↔ 10s)
- Realism (stylized ↔ photoreal)
- Beat density (simple ↔ complex)
- Negative strictness (light ↔ heavy)

---


## Code & Tools

## DP-CODE-001 Code Development
**Scope:** Building/debugging scripts, apps, automations; producing runnable code + reproducible troubleshooting.

### Schema
**Required**
- Goal (feature / fix / script purpose)
- Language/runtime + versions
- OS + environment (paths, permissions, package manager)
- Inputs/outputs (sample I/O)
- Constraints (time, safety, idempotence, performance)

**Optional**
- Existing code snippet or repo structure
- Error text/logs + expected behavior
- Test data + edge cases

### Checks
- [ ] Steps are copy/paste runnable (commands, paths, expected output).
- [ ] Includes at least 2 tests (happy path + one edge case).
- [ ] Error handling is explicit (what fails, how it reports, exit codes/exceptions).
- [ ] If destructive actions exist, they are called out and guarded (confirmations/backups/dry-run).

### Failure-modes
- “Doesn’t work on my machine” → missing environment details → add version/path/permission checks + exact install steps.
- “Fix breaks something else” → no tests/regression check → add minimal test script + before/after expected outputs.
- “Hard to debug” → no minimal repro → extract to minimal repro file + log key variables.
- “Silent failure” → swallowed exceptions → re-raise with context + structured error messages.

### Knobs
- Verbosity (minimal ↔ fully commented)
- Safety (dry-run ↔ live)
- Style (quick hack ↔ production-ready)
- Dependency footprint (stdlib-only ↔ allowed libs)
- Logging (none ↔ debug)
- Output format (human ↔ JSON/CSV)
- Test depth (smoke ↔ thorough)

### Working Patterns
**PAT-CODE-001 Minimal Repro Scaffold**
- **Use when:** bug report is vague or entangled with a big project.
- **Steps:** isolate smallest script → hardcode sample input → reproduce error → add 2 checks.
- **Checks:** repro script runs in clean env; error occurs consistently.
- **Failure-modes:** still too big → keep deleting until failure disappears, then re-add last change.
- **Knobs:** repro size; logging level; input complexity.

**PAT-CODE-002 Validate Inputs Before Work**
- **Use when:** scripts crash mid-run or corrupt data.
- **Steps:** parse → validate types/ranges → fail fast with message → proceed.
- **Checks:** invalid input exits cleanly; valid input proceeds.
- **Failure-modes:** validation too strict → add “lenient mode” knob.
- **Knobs:** strictness; default values; error detail.

**PAT-CODE-003 Wrap Risky Calls With Clear Errors**
- **Use when:** external IO (network/files) fails unpredictably.
- **Steps:** try/except → attach context → retry/backoff (optional) → surface actionable message.
- **Checks:** error includes operation + path/url; retry count bounded.
- **Failure-modes:** infinite retries → cap + escalate.
- **Knobs:** retries; timeout; backoff.

### Drills
- **DRL-CODE-001 (10 min):** Turn a vague bug (“it crashes”) into a minimal repro + 2 checks.
- **DRL-CODE-002 (15 min):** Add logging + input validation to an existing snippet; show one failing and one passing run.


## Music

## DP-MUS-001 Songwriting Scaffolds
**Scope:** Singable lyric structures, hooks, rhyme schemes, constraint-driven writing.

### Schema
**Required**
- Genre/vibe
- Theme/story premise
- POV + emotion arc
- Structure (V1/Pre/Ch/V2/Bridge)
- Hook line or hook idea

**Optional**
- Rhyme scheme
- Syllable targets
- Reference tracks (descriptive)

### Checks
- [ ] Chorus hook is repeatable and emotionally clear.
- [ ] Verses advance story or perspective (no restating).
- [ ] Internal rhythm is singable (no tongue-twisters unless intended).
- [ ] Imagery supports theme consistently.

### Failure-modes
- “No hook” → chorus too wordy → shorten to 1–2 key lines; add repetition.
- “Cliché” → generic phrases → replace with concrete, personal images.
- “Hard to sing” → awkward stresses → adjust syllables; move stresses to strong beats.
- “Verse feels samey” → no progression → add escalation or new angle in V2.

### Knobs
- Rhyme density (none ↔ heavy)
- Imagery (literal ↔ metaphorical)
- Hook repetition (low ↔ high)
- Energy (soft ↔ big)
- Story clarity (vague ↔ explicit)
- Line length (short ↔ long)

---

### Working Patterns
**PAT-MUS-001 Hook First**
- **Use when:** song feels aimless.
- **Steps:** write 1–2 line hook → chorus around it → verses that advance story.
- **Checks:** hook repeatable; V2 adds new info.
- **Failure-modes:** hook too long → compress to 8–12 syllables.
- **Knobs:** repetition; rhyme density; energy.

### Drills
- **DRL-MUS-001 (10 min):** Produce 3 hook candidates + choose one with 2 checks.
- **DRL-MUS-002 (15 min):** Write V1 + Chorus where each section has a different “job”.


## Finance

## DP-FIN-001 Finance & Econ Explainers
**Scope:** Explain concepts, summarize news drivers, interpret indicators—**not** personalized financial advice.

### Schema
**Required**
- Topic or question
- Time window (e.g., “this week”, “since 2020”)
- Audience level (beginner/intermediate/advanced)
- Desired output (explainer / glossary / what-to-watch)

**Optional**
- Data series to reference
- Regions/sectors
- Risk framing (optimistic/neutral/skeptical)

### Checks
- [ ] Facts vs interpretation are labeled.
- [ ] Uncertainty is stated; no predictions framed as certainty.
- [ ] If referencing current info, sources are cited.
- [ ] Output includes “what would change my view” (2–4 bullets) when relevant.

### Failure-modes
- “Sounds like advice” → too directive → reframe as scenarios + risks + questions.
- “Too jargon-y” → level mismatch → add definitions and one example.
- “Outdated” → no recency check → refresh via sources; include dates.
- “Overconfident” → missing uncertainty → add caveats + alternative hypotheses.

### Knobs
- Level (beginner ↔ advanced)
- Tone (neutral ↔ skeptical)
- Depth (overview ↔ deep dive)
- Output type (bullet explainer ↔ narrative)
- Focus (macro ↔ sector ↔ company)

---

### Working Patterns
**PAT-FIN-001 Facts vs Interpretation Split**
- **Use when:** topic could be mistaken for advice.
- **Steps:** list facts (with dates) → list interpretations → list scenarios/risks → “what would change my view”.
- **Checks:** facts are sourced; interpretations labeled.
- **Failure-modes:** too confident → add alternative hypothesis.
- **Knobs:** skepticism; depth; audience level.

### Drills
- **DRL-FIN-001 (10 min):** Explain one indicator (CPI/jobs/rates) with 3 checks and one example.
- **DRL-FIN-002 (15 min):** Summarize a week of market drivers: 5 facts + 3 interpretations + 2 scenarios.
---


# Cross-Pack Pattern Library

## PAT-TPL-001 Pattern Template (copy/paste)
- **ID:** PAT-<AREA>-###
- **Use when:** …
- **Schema:** (inputs/constraints)
- **Steps:** 1…2…3…
- **Checks:** 2–5 observable pass criteria
- **Failure-modes:** Symptom → Cause → Fix (3–6)
- **Knobs:** 6–10 user-invokable toggles

## DRL-TPL-001 Drill Template (copy/paste)
- **ID:** DRL-<AREA>-###
- **Tier:** Beginner | Intermediate | Advanced
- **Prompt:** …
- **Timebox:** 5–15 min
- **Pass criteria:** …
- **Common misses:** …
- **Answer sketch (optional):** …


## PAT-CORE-001 Deliverable-First Output
**Use when:** user wants something they can paste/run/ship.  
**Recipe:** Deliverable → Checks → Failure-modes → Knobs → Next.

## PAT-CORE-002 Prompt Delta Iteration
**Use when:** iterating on prompts, prose, or specs.  
**Rule:** change one knob per iteration; show the delta explicitly.

## PAT-CORE-003 Completeness Rule
**Use when:** required section is missing/thin.  
**Rule:** re-export the whole output in the correct structure; don’t patch with one line.

## PAT-CORE-004 Micro-Demo
**Use when:** authoring a new pack.  
**Rule:** include ≤200 words (or ≤40 lines code) example + ≥2 checks.

---

# Backlog / Next Packs
- DP-WEB-001 Web/App Dev (React + APIs + debugging)
- DP-DATA-001 Spreadsheets & analysis workflows
- DP-OPS-001 Personal productivity / task systems
- DP-EDU-001 Lesson plan generator (multi-level scaffolding)

---

module: bl.M99 | name="Maintenance"
## Maintenance
- Canonical source: `index/Backlog.md`
- Move items to `ACTIVE` when started; keep as simple list.
/module

*Last updated:* 2026-02-15
