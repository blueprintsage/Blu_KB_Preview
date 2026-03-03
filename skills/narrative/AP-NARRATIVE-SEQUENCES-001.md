# AP-NARRATIVE-SEQUENCES-001

**Scope:** Cross-medium spine for designing sequences (comics, storyboards, animation beats, visual novels) using the Step Ladder (0–4).

- status: ACTIVE
- domain: narrative
- subject: sequences
- role: spine
- notes: Medium-specific rules live in modules (COMICS / STORYBOARD / ANIMATION / VN).

---

module_set: AP
status: ACTIVE
domain: narrative
subject: sequences
role: spine

modules:
  - module: AP.BASE
    purpose: "Build a readable, beat-driven sequence from intent to final deliverable."
    governing_patterns:
      - PAT-NAR-GLOBAL-INTENT
      - PAT-NAR-GLOBAL-BEATS
      - PAT-NAR-GLOBAL-CLARITY
      - PAT-NAR-GLOBAL-SHOT_CONTINUITY
      - PAT-NAR-GLOBAL-PACING
      - PAT-NAR-GLOBAL-EMPHASIS
      - PAT-NAR-GLOBAL-RECOVERY

    ladder_order:
      - step: 0
        name: Intent Lock
        outputs:
          - "Sequence objective"
          - "Emotion target"
          - "Constraints (length, medium, audience)"
          - "Beat count target"
        checks:
          - "Objective explicit"
          - "Emotion explicit"

      - step: 1
        name: Skeleton (Beats)
        outputs:
          - "Beat list (setup → action → consequence)"
          - "Cast + location list"
          - "Spatial anchors (where is left/right/near/far)"
        checks:
          - "Each beat has a change"
          - "Geography is establishable"

      - step: 2
        name: Block (Shots / Panels / Moments)
        outputs:
          - "Shot/panel plan per beat"
          - "Establishing shot + re-establish points"
          - "Keyframe selection notes"
        checks:
          - "Viewer can answer who/where/what changed"
          - "Show the moment of maximum value"

      - step: 3
        name: Rough (Timing + Continuity)
        outputs:
          - "Rough storyboard/page layout/beatboard"
          - "Continuity checks (screen direction, time order)"
          - "Pacing allocation (space/time per beat)"
        checks:
          - "Orientation preserved"
          - "Pacing matches intent"

      - step: 4
        name: Final (Deliverable)
        outputs:
          - "Final pages/boards/beat sheet/VN script chunk"
          - "Revision notes + alt beats if needed"
        checks:
          - "Clarity at speed"
          - "Impact moments land"

    failure_modes:
      - signature: "Confusing action"
        prescribe:
          - step: 1
          - apply: PAT-NAR-GLOBAL-BEATS
          - apply2: PAT-NAR-GLOBAL-CLARITY
      - signature: "Continuity flips"
        prescribe:
          - step: 3
          - apply: PAT-NAR-GLOBAL-SHOT_CONTINUITY
      - signature: "Flat pacing"
        prescribe:
          - step: 3
          - apply: PAT-NAR-GLOBAL-PACING

  - module: AP.MOD.COMICS
    when: "Deliverable is comics pages/panels"
    step_deltas:
      step_2_add:
        - "Panel count targets per beat"
      step_4_add:
        - "Balloon placement / reading flow pass"
    notes:
      - "Clarity includes reading order and balloon hierarchy."

  - module: AP.MOD.STORYBOARD
    when: "Deliverable is storyboard frames"
    step_deltas:
      step_3_add:
        - "Camera notes (lens/angle/move)"
        - "Action lines / staging arrows"
    notes:
      - "Continuity includes screen direction and match cuts."

  - module: AP.MOD.ANIMATION_BEATS
    when: "Deliverable is beatboard / animatic beats"
    step_deltas:
      step_3_add:
        - "Timing notes (frames/seconds)"
      step_4_add:
        - "Animatic checklist (tempo + clarity)"
    notes:
      - "Emphasis is often timing-first, not detail-first."

  - module: AP.MOD.VISUAL_NOVEL
    when: "Deliverable is VN script + shots"
    step_deltas:
      step_2_add:
        - "Sprite/pose/CG callouts"
      step_4_add:
        - "Branch notes + state flags"
    notes:
      - "Clarity includes choice consequences and state continuity."
