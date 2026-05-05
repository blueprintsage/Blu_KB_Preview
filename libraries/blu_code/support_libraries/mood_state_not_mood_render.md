# Mood State Is Not Mood Render

object_id: mood_state_not_mood_render
object_type: blu_code_skill
category: support_libraries
subcategory: mood
stage_binding: kernel_coding
lane_fit: deterministic
foundation_role: prevention_rule
tags:
- mood
- ownership
- exec_renderer

## Objective
Preserve clean ownership for mood-like systems.

## Trigger
Building or repairing Mood, Ribbon, Persona, or another reflective subsystem.

## Steps / Flow
1. Persona produces current-turn state only.
2. Ribbon/color support normalizes tokens only.
3. Mood decision support resolves word/colors/signature only.
4. Exec owns command route, state commit, swatch mapping, and public render.
5. Do not let any support library emit `mood:` prose or public mood lines.

## Acceptance Checks
- Only Exec prints `[MOOD] <Word> <Swatches>`.
- Support outputs are structured and non-renderable.
- Route proof exists before mood payload/render changes.
