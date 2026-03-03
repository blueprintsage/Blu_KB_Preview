# AP-ART-HEADS-001

**Scope:** Head construction system (cranial + facial masses) for integration into Figure Drawing.

- status: ACTIVE
- domain: art
- subject: heads
- role: child
- parent_ap: AP-ART-FIGURE-DRAWING-001
- notes: Freeze v1.0 child system.

---

module_set: AP
status: ACTIVE
domain: art
subject: heads
role: child
parent_ap: AP-ART-FIGURE-DRAWING-001

modules:
- module: AP.BASE
    purpose: Construct head via cranial + facial mass system; maintain rotation consistency.
    step_bindings:
      step_0:
        decide:
          - head type (broad/medium/long) if needed
          - camera angle
      step_1:
        do:
          - cranial mass + facial wedge placement
      step_2:
        do:
          - major planes/volumes; jaw/cheek structure
      step_3:
        do:
          - landmarks; feature placement checks
      step_4:
        do:
          - cleanup + readability + style compliance
    core_checks:
      - Landmark placement consistency
      - Rotation consistency across features
      - Proportional alignment (front/side agreement)

  - module: AP.MOD.AGING
    when: Aging variant required.
    overrides:
      - proportion + sag/compression cues
    notes:
      - Keep cranial/facial mass relationship coherent.
