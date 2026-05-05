# Static Command Surface Exactness

object_id: static_surface_exactness
object_type: blu_code_skill
category: commands
subcategory: surface
stage_binding: kernel_coding
lane_fit: deterministic
foundation_role: prevention_rule
tags:
- commands
- surface
- auth

## Objective
Keep public command discovery deterministic and auth-aware.

## Trigger
Updating `/commands`, `/help`, command inventory, or command surface maps.

## Steps / Flow
1. Use canonical render blocks only.
2. Filter by auth tier without synthesizing extra commands.
3. Ensure command surface maps route to actual Exec/Program owners.
4. Add tests for removed/stale command forms.

## Acceptance Checks
- No hidden/Admin commands leak.
- No stale command appears.
- Discovery does not imply execution bypass.
