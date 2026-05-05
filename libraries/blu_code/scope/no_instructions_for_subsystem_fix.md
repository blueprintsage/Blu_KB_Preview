# No Instructions For Subsystem Fix

object_id: no_instructions_for_subsystem_fix
object_type: blu_code_skill
category: scope
subcategory: kernel_layers
stage_binding: kernel_coding
lane_fit: deterministic
foundation_role: prevention_rule
tags:
- instructions
- scope
- layers

## Objective
Keep `00_Instructions.md` emergency-only for open runtime, not subsystem patching.

## Trigger
A fix is proposed for Mood, Commands, Programs, ExecLib, memory, CPM, etc.

## Steps / Flow
1. First determine whether Exec/Programs/ExecLib can own the behavior.
2. Do not edit `00_Instructions.md` unless the open runtime floor itself changes.
3. If a subsystem only works through Instructions, treat that as proof the subsystem owner is broken.
4. Repair the lower owner instead.

## Acceptance Checks
- No `00_Instructions.md` change for subsystem bugs.
- Fix lands in 01-06 or repo library as appropriate.
- README confirms excluded files when relevant.
