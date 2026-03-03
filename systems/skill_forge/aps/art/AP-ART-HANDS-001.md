# AP-ART-HANDS-001

**Scope:** Hands construction system for integration into Figure Drawing.

- status: ACTIVE
- domain: art
- subject: hands
- role: child
- parent_ap: AP-ART-FIGURE-DRAWING-001
- notes: Freeze v1.0 child system.

---

module_set: AP
status: ACTIVE
domain: art
subject: hands
role: child
parent_ap: AP-ART-FIGURE-DRAWING-001

modules:
- module: AP.BASE
    purpose: Construct believable hands via mass + joint logic + foreshortening discipline.
    step_bindings:
      step_0:
        decide:
          - intent (gesture/grip/point/relaxed)
          - contact points (if holding object)
      step_1:
        do:
          - gesture line + finger grouping + thumb opposition direction
      step_2:
        do:
          - palm mass + finger segment volumes; perspective
      step_3:
        do:
          - landmark/stress cues + joint-limit checks + proportion checks
      step_4:
        do:
          - readability + style dampers + cleanup
    core_checks:
      - Joint limits plausible
      - Finger proportion consistency
      - Force clarity (intent reads)

  - module: AP.MOD.OBJECT_INTERACTION
    when: Hand is holding/pressing/pulling something.
    overrides:
      - add contact/pressure cues
      - add deformation/occlusion checks
