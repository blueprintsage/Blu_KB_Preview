# Terminal Packet Before Print

object_id: terminal_packet_before_print
object_type: blu_code_skill
category: deterministic_lanes
subcategory: validation
stage_binding: kernel_coding
lane_fit: deterministic
foundation_role: prevention_rule
tags:
- terminal_packet
- validation
- commands

## Objective
Ensure deterministic lanes cannot print plausible prose.

## Trigger
Commands, Programs, libraries, services, schemas, exports, artifacts, and static renders.

## Steps / Flow
1. Classify lane before dispatch.
2. Require packet fields: lane_class, owner, source_or_contract, executed_action, validation_result, terminal_state, printable_output/artifact_output.
3. Reject fallback prose when packet is missing.
4. Apply lane-specific exact shape validation before print.

## Acceptance Checks
- Deterministic output has packet proof.
- Fallback prose is blocked.
- Final line matches the owner contract exactly.

## Notes
Matches PASS acceptance-test discipline: make the completion shape testable before implementation.

## Reference Inputs
- 03_Exec.md terminal packet validator
- PASS acceptance testing pattern
