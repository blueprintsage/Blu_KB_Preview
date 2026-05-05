# Propose-Only Library Boundary

object_id: propose_only_library_boundary
object_type: blu_code_skill
category: support_libraries
subcategory: execlib
stage_binding: kernel_coding
lane_fit: deterministic
foundation_role: prevention_rule
tags:
- execlib
- library_boundary
- print

## Objective
Keep ExecLib libraries from becoming hidden routers or printers.

## Trigger
Any ExecLib library/service supports a command, ordinary turn, or Program.

## Steps / Flow
1. Define exactly what the library owns and does not own.
2. Library returns structured data, not public print, unless its contract explicitly says Exec consumes a render payload.
3. Exec validates and prints; library never applies state directly.
4. If a library output leaks user-visible prose into a deterministic path, mark invalid.

## Acceptance Checks
- Library has required metadata.
- No direct print authority.
- State changes are returned as proposals only.
