# AP-ART-HANDS-001 — Hands (Application Pack)

- id: AP-ART-HANDS-001
- name: Hands
- domain: art
- subject: hands
- status: active
- tags: [domain:art, topic:hands, context:general, level:L1]
- links:
  - parent_ap: AP-ART-FIGURE-DRAWING (TBD)

## Governing Patterns (LAW)
- governing_patterns:
  - PAT-ART-SI-001
  - PAT-ART-SI-002
  - PAT-ART-SI-003
  - PAT-ART-HAND-001
  - PAT-ART-HAND-003
  - PAT-ART-HAND-004
  - PAT-ART-HAND-005
  - PAT-ART-READ-001
  - PAT-ART-REC-001
- pattern_clusters:
  - GLOBAL_SPATIAL_INTEGRITY
  - GLOBAL_READABILITY
  - GLOBAL_RECOVERY
  - HANDS

## Function Contract
- purpose: Draw believable, readable hands for comics, ref sheets, character bibles, and concept work.
- inputs: pose intent, camera angle, style target (optional), object interaction (optional)
- outputs: hand drawing consistent in 3D and clear in silhouette
- done_means: passes all HARD pattern checks; silhouette communicates intent; no structural contradictions

---

## Step Ladder Binding

### Step 0 — Intent Lock
- decide:
  - function: gesture / grip / support / impact
  - camera: neutral vs foreshortened
  - style: simplified vs rendered
- outputs:
  - 3–6 thumbnails exploring intent + angle

### Step 1 — Skeleton
- procedure:
  - one gesture line for whole hand
  - finger clusters before individual fingers
  - thumb opposition line placed separately
- checks:
  - PAT-ART-SI-002
  - PAT-ART-HAND-002

### Step 2 — Block
- procedure:
  - palm mass first (tilt + plane)
  - fingers as segmented volumes
  - overlaps designed if foreshortened
- checks:
  - PAT-ART-SI-001
  - PAT-ART-SI-003
  - PAT-ART-HAND-001
  - PAT-ART-HAND-004
  - PAT-ART-HAND-005

### Step 3 — Rough
- procedure:
  - enforce joint logic; add only helpful landmarks
  - stress-test solidity; rebuild if HARD checks fail
- checks:
  - PAT-ART-HAND-003
  - PAT-ART-REC-001 (when triggered)

### Step 4 — Final
- procedure:
  - clean line economy; preserve silhouette
  - apply style dampers: detail only where it reinforces form/intent
- checks:
  - PAT-ART-READ-001
  - PAT-ART-HAND-006 (if gesture-focused)

---

## Failure Modes (routing anchors)
- flat symbol → repeat Step 2 + DRL-ART-HANDS-001
- rubbery fingers → repeat Step 3 + DRL-ART-HANDS-003
- bad thumb/pinch → repeat Step 2 + DRL-ART-HANDS-004
- broken foreshortening → repeat Step 2 + DRL-ART-HANDS-005

---

## Modules (VARIANTS + ADD-ONS)

### AP.MOD.GESTURE_COMICS
- when_to_use: comics acting; hands communicating
- step_deltas:
  - step_4_add:
      - simplify interior detail until silhouette reads instantly
- extra_checks: [PAT-ART-READ-001, PAT-ART-HAND-006]

### AP.MOD.REFSHEET_TURNAROUND
- when_to_use: ref sheets / bibles
- step_deltas:
  - step_0_add:
      - lock proportion language for consistency across views
  - step_4_add:
      - add minimal landmark callouts only if they aid reuse

### AP.MOD.OBJECT_INTERACTION
- when_to_use: holding props
- step_deltas:
  - step_0_add:
      - define contact points + pressure points
  - step_3_add:
      - verify wrap + opposition supports the object

---

## Source Pointer (no quotes)
- source_ptr:
  - development study synthesis (Hands) for Skill Forge 2.0 proof pack
