# PASS Lens Registry
Version: v1.0
Date: 2026-03-03
tz: America/Chicago

Purpose:
A single canonical registry that PASS reads to:
- infer/accept `subject`
- select a default `lens_stack`
- run PASS:GUT-LADDER as multi-pass saturation
- canon-merge outputs
- emit Lane B → Lane A → merged zip

---

## 1) Definitions

### Lens
A named extraction focus. Lenses are stable identifiers once published.

### Lens Stack
An ordered list of lenses used for a given subject.
Order matters (early lenses define primitives; later lenses harden soft wisdom).

### Subject
A coarse domain topic (e.g., `art_comics`, `code_language_c`, `writing_comics_script`).

---

## 2) PASS:GUT-LADDER Default Execution (Registry-Driven)

When the user types:
- `PASS:GUT-LADDER`

PASS MUST:
1) Determine `subject`:
   - If user provides `subject=...`, use it.
   - Else infer from title/metadata/context.
2) Select `lens_stack` from this registry:
   - If no match, fall back to the registry default stack.
3) Run multi-pass extraction in lens order:
   - Each pass produces: gates (patterns) + tests + notes for merge.
   - No “run drills now?” prompts mid-run.
4) Canon-merge (mandatory):
   - merge duplicates
   - resolve conflicts (general rule canonical, narrow cases as tagged variants)
5) Emit outputs:
   - Lane B first (canonical runtime)
   - Lane A second (teaching pack compiled from Lane B references)
6) Emit a single merged “Freeze Pack” zip at the end.

---

## 3) Registry Defaults

### 3.1 Global Defaults
- reject_test: ON
- soft_to_hard: ON (convert soft guidance into enforceable gates where possible)
- output: both
- lane_order: B_then_A
- drill_generation: AFTER canon-merge only

### 3.2 Fallback Stack (if subject unknown)
lens_stack_default = [
  "mechanics",
  "clarity",
  "production"
]

---

## 4) Lens Catalog (v1.0)

### Core Art Lenses
- mechanics: structure, construction, anatomy, planes, rotation, force chain
- depth: foreshortening, stacking, perspective agreement, scale shift, overlap truth
- clarity: silhouette, negative space, tangent elimination, read-at-thumbnail
- emphasis: focal hierarchy, value grouping, contrast dominance, shape language
- staging_camera: shot distance, angle control, composition, eye-line management
- narrative_pacing: beats, page rhythm, setup/payoff, escalation, reveal timing
- cloth: anchors, tension vs compression, fold budgets, seam logic
- consistency: turnarounds, proportion locks, landmark invariants, model stability
- stylization_safety: what may simplify vs must not break (anti-drift)
- production: workflow, checklists, timeboxing, common failure modes

### Core Code Lenses
- fundamentals: syntax, types, core primitives
- patterns: idioms, standard patterns, architecture primitives
- correctness: invariants, edge cases, tests, proofs of behavior
- performance: complexity, memory, profiling, optimization constraints
- security: threat surface, input handling, common vulnerabilities
- observability: logs/metrics/traces, debugging hooks
- reliability: retries/timeouts/idempotency/backoff
- scalability: caching/queues/capacity/limits
- production: builds, packaging, deployment, docs, versioning

### Core Writing Lenses
- story_structure: beats, arcs, pacing, scene goals
- character: motivations, voice, consistency, change
- clarity: readability, specificity, continuity, scene mechanics
- dialogue: subtext, rhythm, economy, intent
- production: outlines, revision passes, checklists

---

## 5) Subject → Lens Stack Map (v1.0)

### ART

#### art_figure_drawing (anatomy / construction)
lens_stack = ["mechanics","depth","clarity","stylization_safety","production"]

#### art_anatomy (deep anatomy)
lens_stack = ["mechanics","depth","clarity","stylization_safety","production"]

#### art_hands
lens_stack = ["mechanics","depth","clarity","stylization_safety","production"]

#### art_head_neck
lens_stack = ["mechanics","depth","clarity","stylization_safety","production"]

#### art_wrinkles_drapery
lens_stack = ["mechanics","cloth","clarity","stylization_safety","production"]

#### art_ref_sheets (turnarounds / bibles)
lens_stack = ["mechanics","consistency","clarity","stylization_safety","production"]

#### art_comics (sequential art)
lens_stack = ["mechanics","clarity","emphasis","staging_camera","narrative_pacing","production"]

#### art_storyboards
lens_stack = ["clarity","staging_camera","narrative_pacing","emphasis","production"]

### CODE

#### code_language_generic
lens_stack = ["fundamentals","patterns","correctness","performance","security","production"]

#### code_api_design
lens_stack = ["requirements","reliability","security","observability","scalability","production"]

### WRITING

#### writing_comics_script
lens_stack = ["story_structure","character","clarity","dialogue","production"]

#### writing_fiction_generic
lens_stack = ["story_structure","character","clarity","dialogue","production"]

---

## 6) Extending the Registry (How to Add New Subjects)
To add a subject:
1) Create a new subject key (snake_case).
2) Assign an ordered lens stack using existing lenses.
3) If a new lens is required:
   - add it to the Lens Catalog
   - keep the name stable forever after publish

Guiding rule:
Prefer adding new subjects/stacks over inventing new lenses.

---

## 7) Invocation Examples

### Default (auto subject)
PASS:GUT-LADDER

### Explicit subject
PASS:GUT-LADDER subject=art_comics

### Manual override (rare)
PASS:GUT-LADDER lenses=mechanics,clarity,emphasis
