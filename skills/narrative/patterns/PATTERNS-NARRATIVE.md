# PATTERNS-NARRATIVE (GLOBAL LAW)

**Scope:** Cross-medium narrative constraints (patterns-as-law) bound to the Step Ladder (0–4).

- status: ACTIVE
- domain: narrative
- role: global_law

---

module_set: PATTERNS
status: ACTIVE
domain: narrative

modules:
  - module: PAT-NAR-GLOBAL-INTENT
    severity: HARD
    bind_stage: 0
    law:
      IF: "Building a sequence"
      THEN: "Define: objective, audience emotion target, and the minimum beats required"
    evidence:
      PASS: "Step 0 sequence brief exists (objective + emotion + beats)"
      FAIL: "Sequence proceeds without objective/emotion/beat plan"
    failure_signatures:
      - "scene feels aimless"
      - "beats don't land"

  - module: PAT-NAR-GLOBAL-CLARITY
    severity: HARD
    bind_stage: 2
    law:
      IF: "A beat is shown"
      THEN: "Ensure the viewer can answer: who, where, what changed"
    evidence:
      PASS: "Readable staging; change is unambiguous"
      FAIL: "Confusing geography or unclear action change"
    failure_signatures:
      - "I don't know what happened"
      - "where are they now?"

  - module: PAT-NAR-GLOBAL-BEATS
    severity: HARD
    bind_stage: 1
    law:
      IF: "Designing a sequence skeleton"
      THEN: "Express the sequence as beats: setup → action → consequence (repeat as needed)"
    evidence:
      PASS: "Beat list exists and each beat has a change"
      FAIL: "Shots exist but no beat-level change"
    failure_signatures:
      - "pretty panels, no momentum"
      - "no consequences"

  - module: PAT-NAR-GLOBAL-SHOT_CONTINUITY
    severity: HARD
    bind_stage: 3
    law:
      IF: "Cutting between shots"
      THEN: "Maintain continuity: screen direction, spatial anchors, and temporal order"
    evidence:
      PASS: "Viewer orientation preserved across cuts"
      FAIL: "Unmotivated reversals / teleporting"
    failure_signatures:
      - "characters swap sides"
      - "space resets randomly"

  - module: PAT-NAR-GLOBAL-PACING
    severity: SOFT
    bind_stage: 3
    law:
      IF: "A beat requires emphasis or speed"
      THEN: "Allocate time/space accordingly (more space/time = emphasis; less = speed)"
    evidence:
      PASS: "Pacing matches intent"
      FAIL: "Rushed emotional beat or overlong trivial beat"
    failure_signatures:
      - "too fast to feel"
      - "drags without purpose"

  - module: PAT-NAR-GLOBAL-EMPHASIS
    severity: HARD
    bind_stage: 4
    law:
      IF: "Choosing what to show"
      THEN: "Show the moment of maximum narrative value (peak intent, reveal, consequence)"
    evidence:
      PASS: "Keyframe selection supports the beat"
      FAIL: "Shown moment is neutral or unclear"
    failure_signatures:
      - "impact missing"
      - "reveal doesn't read"

  - module: PAT-NAR-GLOBAL-RECOVERY
    severity: HARD
    bind_stage: 3
    law:
      IF: "Sequence becomes confusing or flat"
      THEN: "Return to beats + geography, rebuild from skeleton, then re-cut"
    evidence:
      PASS: "Beat list + spatial anchors re-established"
      FAIL: "Patching individual shots without re-baseline"
    failure_signatures:
      - "band-aid edits"
      - "continuity breaks persist"
