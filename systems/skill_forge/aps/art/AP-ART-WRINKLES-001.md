# AP-ART-WRINKLES-001

**Scope:** Wrinkles/drapery system for clothed figure rendering governed by force+anchors.

- status: ACTIVE
- domain: art
- subject: wrinkles_drapery
- role: child
- parent_ap: AP-ART-FIGURE-DRAWING-001
- notes: Freeze v1.0 child system.

---

module_set: AP
status: ACTIVE
domain: art
subject: wrinkles_drapery
role: child
parent_ap: AP-ART-FIGURE-DRAWING-001

modules:
- module: AP.BASE
    purpose: Render cloth folds governed by force + anchors + material response.
    step_bindings:
      step_0:
        decide:
          - material weight/tightness
          - motion vs static
          - anchor points
      step_1:
        do:
          - anchor map + tension/compression zones
      step_2:
        do:
          - choose fold system module; place primary folds
      step_3:
        do:
          - secondary folds per material response; avoid noise
      step_4:
        do:
          - simplify + clarify + preserve motion hierarchy
    core_checks:
      - No decorative randomness
      - Folds follow force direction
      - Anchors explain wrinkle origins

  - module: AP.MOD.DIRECT_THRUST
    when: A thrust/impact creates radiating tension.
    notes:
      - Radial response; keep hierarchy primary > secondary.

  - module: AP.MOD.BEND
    when: Joint bend creates compression on concave side.
    notes:
      - Accordion compression concave; stretch convex.

  - module: AP.MOD.SWAG_HANG
    when: Draped cloth under gravity dominates.
    notes:
      - Vertical gravity flow; anchor breakpoints.

  - module: AP.MOD.FLYING
    when: Fast motion creates trailing cloth.
    notes:
      - Directional elongation; reduced compression behind.
