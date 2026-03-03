# Art Folder Cleanup Patch Pack v1
Goal: remove mess, preserve nuclear canon, and relocate AP glue contracts into system space.

## What this patch pack PROVIDES (to merge into Preview repo)
1) Canonical AP glue contracts:
   - systems/skill_forge/aps/art/AP-ART-FIGURE-DRAWING-001.md
   - systems/skill_forge/aps/art/AP-ART-HANDS-001.md
   - systems/skill_forge/aps/art/AP-ART-HEADS-001.md
   - systems/skill_forge/aps/art/AP-ART-WRINKLES-001.md

2) Hogarth Lane B runtime core:
   - skills/art/hogarth/_hogarth_core/

3) Legacy archive bucket (pre-nuclear mixed-era):
   - archive/legacy/art_pre_nuclear/patterns/
   - archive/legacy/art_pre_nuclear/drills/

## Intent
- Lane B runtime stays modular under skills/...
- APs live under systems/... (glue contracts, not art content)
- Old mixed-era patterns/drills are archived to avoid drift.
