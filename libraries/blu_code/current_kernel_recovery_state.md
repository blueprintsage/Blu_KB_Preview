---
name: Current Blu kernel recovery state
description: Active truth after the 2026-05-04 mood regression and recovery attempt.
type: context
---

## Current truth

- Mood regression was reproduced with outputs such as:
  - `mood: on`
  - `mood: steady, warm, present`
  - `steady — warm, present, anchored 💙`
- Those outputs prove `/mood ...` commands were falling through to ordinary Persona-style prose instead of deterministic Exec command routing.
- Emoji mapping was not the root issue. The render path was not being reached.
- The immediate recovery target is `/mood` command routing before ordinary conversation.
- The implemented recovery uses a hosted slash command fast path in `00_Instructions.md` and `03_Exec.md`.

## Do not repeat

Do not keep rewriting MoodLib or RibbonLib when `/mood` is not reaching Exec. Fix command interception first.
