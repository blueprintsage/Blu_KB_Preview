# COLD STORE — PASS:GUT-LADDER Default Lens Stacks
Version: v1.0
Date: 2026-03-03
tz: America/Chicago
Enforcement: ON

Scope: PASS defaults only.

---

## 1) PASS:GUT-LADDER Default Behavior
When the user types:
- PASS:GUT-LADDER

PASS MUST:
1) Detect subject (or use explicit subject=... if provided)
2) Run the full lens stack for that subject, in order (multi-pass)
3) Canon-merge all extracted gates/tests/drills into one canonical set
4) Output BOTH lanes, in this order:
   - Lane B (runtime canonical) first
   - Lane A (teaching pack) second
5) Emit a single merged “Freeze Pack” zip at the end:
   - includes Lane A + Lane B + ledgers + index patch snippets

No interactive “do drills now?” prompts mid-run.
Drills are generated only after canon-merge (end of full run).

---

## 2) Subject → Default Lens Stack Map

### ART: Figure Drawing / Anatomy / Construction
lens_stack = [
  mechanics,          # structure, masses, planes, rotation, force
  depth,              # foreshortening, stacking, perspective agreement
  clarity,            # silhouette, tangents, negative space
  cloth,              # anchors/tension/compression (if applicable)
  stylization_safety, # what may simplify vs must not break
  production          # workflow, common failure modes, checklists
]

### ART: Comics / Sequential Art
lens_stack = [
  mechanics,          # figure truth still required
  clarity,            # silhouette/read at thumbnail size
  emphasis,           # focal hierarchy/value grouping
  staging_camera,     # shot distance, angle, composition control
  narrative_pacing,   # beats, page rhythm, setup/payoff
  production          # pipeline, timeboxing, common mistakes
]

### ART: Ref Sheets / Turnarounds / Character Bibles
lens_stack = [
  mechanics,
  consistency,        # proportion locks, landmarks, turn consistency
  clarity,
  stylization_safety,
  production
]

### CODE: Programming Languages (C/C++/Java/Python/etc.)
lens_stack = [
  fundamentals,       # syntax, types, core concepts
  patterns,           # idioms, best practices, design patterns
  correctness,        # invariants, edge cases, testing strategy
  performance,        # complexity, profiling, memory
  security,           # input handling, common vulns
  production          # build, tooling, packaging, debugging
]

### CODE: APIs / System Design
lens_stack = [
  requirements,       # contracts, constraints, success criteria
  reliability,        # retries, timeouts, idempotency
  security,
  observability,      # logs/metrics/traces
  scalability,        # caching, queues, capacity
  production          # docs, versioning, rollout
]

### WRITING: Fiction / Comics Script
lens_stack = [
  story_structure,    # beats, arcs, pacing
  character,          # voice, motivation, consistency
  clarity,            # readability, scene goals
  dialogue,           # subtext, rhythm, economy
  production          # outlines, revision passes, checklists
]

---

## 3) Overrides (Optional)
User may override subject detection:
- PASS:GUT-LADDER subject=comics

User may override lens stack:
- PASS:GUT-LADDER lenses=mechanics,clarity,emphasis,narrative_pacing

Default if no subject can be inferred:
- mechanics, clarity, production

---

## 4) Mandatory Canon Merge Output
After all passes:
- Merge duplicates
- Resolve conflicts:
  - keep general rule as canonical
  - keep narrow cases as variants (tagged)
- Emit one merged gate list + merged tests + merged drills
- Generate Lane A from Lane B references
- Package into one zip.