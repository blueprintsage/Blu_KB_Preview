# Owner Before Renderer

object_id: owner_before_renderer
object_type: blu_code_skill
category: routing
subcategory: ownership
stage_binding: kernel_coding
lane_fit: deterministic
foundation_role: prevention_rule
tags:
- owner
- renderer
- support

## Objective
Prevent render rewrites when the real bug is wrong owner path.

## Trigger
Any feature output is malformed or missing.

## Steps / Flow
1. Identify the active owner that should produce the output.
2. Verify the request actually enters that owner.
3. Verify support dependencies are called only after owner lock.
4. Do not alter renderer or payload schema if owner proof is missing.

## Acceptance Checks
- Owner proof exists before render changes.
- One owner per job is preserved.
- Competing fallback/prose path is blocked.
