# AP-ART-FIGURE-DRAWING-001

**Scope:** Structural spine for figure drawing. Governs child APs and enforces the Step Ladder.

- status: ACTIVE
- domain: art
- subject: figure_drawing
- role: spine
- notes: Freeze v1.0; changes require version bump.

---

module_set: AP
status: ACTIVE
domain: art
subject: figure_drawing
role: spine

modules:
- module: AP.BASE
    purpose: Structural spine for human figure drawing using the Step Ladder.
    ladder_order:
      - step: 0
        name: Intent Lock (thumbs)
        checks:
          - Force path defined
          - Primary weight-bearing support identified
      - step: 1
        name: Skeleton Framework
        checks:
          - Balance axis plausible
          - Joint limits plausible
      - step: 2
        name: Mass Blocking
        checks:
          - Volumes consistent in space
          - Foreshortening coherent
      - step: 3
        name: Structural Refinement
        checks:
          - Landmarks align to skeleton
          - Mass grouping readable
      - step: 4
        name: Final Rendering
        checks:
          - Readable at thumbnail size
          - Motion preserved (no detail-kill)
    non_negotiables:
      - No detail before mass.
      - No mass before skeleton.
      - No skeleton before intent.
      - If it breaks: return to the earliest failing step and rebuild.

  - module: AP.MOD.ARCHETYPE_SCALING
    when: Archetype exaggeration is required (hero/brute/giant).
    overrides:
      - proportion ratios (head-count tier)
      - mass dominance (torso/limb emphasis)
    notes:
      - Preserve balance axis and Step 1 skeleton integrity.

  - module: AP.MOD.NATURALISTIC
    when: Target style is observational/naturalistic.
    overrides:
      - dampen exaggeration
      - reduce surface segmentation
    notes:
      - Structure-first discipline unchanged.
