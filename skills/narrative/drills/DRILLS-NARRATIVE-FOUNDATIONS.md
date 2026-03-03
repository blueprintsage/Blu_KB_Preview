# DRILLS-NARRATIVE-FOUNDATIONS

**Scope:** Human teaching drills for the Narrative Step Ladder (0–4). Patterns are checkpoints.

- status: ACTIVE
- domain: narrative
- storage_mode: hybrid
- split_rule: drills>7 or lines>1200

---

module_set: DRILLS
status: ACTIVE
domain: narrative

modules:
  - module: DRL-NAR-FOUND-001
    name: "Beat List From Premise"
    tags: [domain:narrative, phase:core, level:L0]
    lesson_goal: "Convert a premise into a beat list with changes."
    ladder:
      step_0:
        do: ["Write objective + emotion target"]
        checkpoints: [PAT-NAR-GLOBAL-INTENT]
      step_1:
        do: ["Write 6–12 beats: setup → action → consequence"]
        checkpoints: [PAT-NAR-GLOBAL-BEATS]
      step_2:
        do: ["Assign 1–3 shots/panels per beat"]
        checkpoints: [PAT-NAR-GLOBAL-CLARITY]
      step_3:
        do: ["Check continuity (screen direction, geography)"]
        checkpoints: [PAT-NAR-GLOBAL-SHOT_CONTINUITY]
      step_4:
        do: ["Identify 2 keyframes for emphasis"]
        checkpoints: [PAT-NAR-GLOBAL-EMPHASIS]
    pass:
      - "Each beat changes the situation"
    fail:
      - "Beats are descriptions without change"

  - module: DRL-NAR-FOUND-002
    name: "Clarity Pass"
    tags: [domain:narrative, phase:remediation, level:L0]
    lesson_goal: "Fix confusion by re-establishing geography and change."
    ladder:
      step_1:
        do: ["Write who/where for each beat"]
        checkpoints: []
      step_2:
        do: ["For each shot: label who/where/what changed"]
        checkpoints: [PAT-NAR-GLOBAL-CLARITY]
      step_3:
        do: ["Mark screen direction arrows; fix reversals"]
        checkpoints: [PAT-NAR-GLOBAL-SHOT_CONTINUITY]
    pass:
      - "Viewer never asks 'what happened?'"
    fail:
      - "Orientation breaks persist"

  - module: DRL-NAR-FOUND-003
    name: "Pacing Allocation"
    tags: [domain:narrative, phase:integration, level:L1]
    lesson_goal: "Allocate space/time to match intent."
    ladder:
      step_0:
        do: ["Pick one beat to emphasize and one to speed through"]
        checkpoints: []
      step_3:
        do: ["Increase shots/panels/time for emphasis; reduce for speed"]
        checkpoints: [PAT-NAR-GLOBAL-PACING]
      step_4:
        do: ["Verify emphasis moments land"]
        checkpoints: [PAT-NAR-GLOBAL-EMPHASIS]
