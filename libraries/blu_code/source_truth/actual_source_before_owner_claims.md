# Actual Source Before Owner Claims

object_id: actual_source_before_owner_claims
object_type: blu_code_skill
category: source_truth
subcategory: inspection
stage_binding: kernel_coding
lane_fit: deterministic
foundation_role: prevention_rule
tags:
- source_truth
- owner
- inspection

## Objective
Prevent architecture claims from outrunning the actual uploaded code.

## Trigger
Any claim that a module, owner, route, gate, or function exists or owns behavior.

## Steps / Flow
1. Read the active file containing the claimed module/route.
2. Verify the module ID, owner, entrypoint, and status.
3. If the active source is unavailable, state unknown rather than guessing.
4. Only then name exact owners or insertion points.

## Acceptance Checks
- Claimed section exists in active source.
- No mental-model headings are used.
- Unverified claims are marked as inference or unknown.
