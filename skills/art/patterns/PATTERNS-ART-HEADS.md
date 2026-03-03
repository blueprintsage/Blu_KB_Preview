# PATTERNS — ART — HEADS (v1)
Version: v1.0
Date: 2026-03-03

---
module_set:
  id: PAT-ART-HEADS-001
  domain: art
  subject: heads
  type: patterns
  status: active
  binds_to:
    aps:
      - AP-ART-HEADS-001
  ladder_binding: [0,1,2,3,4]
---

## PAT-ART-HEADS-001 — Head Starts as a Solid, Not an Outline
IF drawing a head  
THEN block it as a 3D volume (cranium + jaw mass) before features.  
PASS: face planes turn correctly in 3/4 view.  
FAIL: features “stickered” onto a flat oval.

## PAT-ART-HEADS-002 — Features Hang on Landmarks
IF placing eyes/nose/mouth  
THEN anchor to brow ridge, cheekbone, nose plane, jaw hinge, chin.  
PASS: expression changes without shifting skull structure.  
FAIL: features float or slide when rotated.

## PAT-ART-HEADS-003 — Neck Is a Support Column
IF finishing Step 2 masses  
THEN connect head to torso with neck cylinder + trapezius/SCM masses, not a thin line.  
PASS: head feels supported and posed.  
FAIL: “lollipop head.”

## PAT-ART-HEADS-004 — Plane Breaks Drive Likeness
IF refining (Step 3)  
THEN prioritize plane changes (forehead, cheek, muzzle, jaw) over eyelashes/lines.  
PASS: likeness improves with planes alone.  
FAIL: detail added but structure still wrong.
