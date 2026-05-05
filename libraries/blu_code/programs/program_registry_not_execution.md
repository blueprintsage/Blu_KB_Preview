# Program Registry Is Not Execution

object_id: program_registry_not_execution
object_type: blu_code_skill
category: programs
subcategory: registry
stage_binding: kernel_coding
lane_fit: deterministic
foundation_role: prevention_rule
tags:
- programs
- registry
- terminal_packet

## Objective
Prevent registry presence from being treated as live Program proof.

## Trigger
Any Program-owned command, DevMode trace, SIMCODE, memory export, reminder, or CPM route.

## Steps / Flow
1. Check command surface route.
2. Check Program registry status.
3. Check Program body/entrypoint contract.
4. Check Program terminal packet output.
5. Check Exec validates packet before print.

## Acceptance Checks
- ACTIVE registry is not claimed as execution proof.
- DRAFT/BROKEN/DEPRECATED states are respected.
- Program output cannot print without terminal packet.
