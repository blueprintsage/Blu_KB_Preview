---
name: Mood command fallthrough bug
description: `/mood ...` commands printed Persona prose because command interception failed.
type: bug
---

## Symptom

Observed outputs:
- `/mood on` -> `mood: on`
- `/mood show` -> `mood: steady, warm, present`
- ordinary turn after `/mood on` -> no `[MOOD]` line

## Cause

The `/mood` input was treated as ordinary conversation or Persona-style reflection, not a deterministic Exec-native command.

## Fix principle

Before touching MoodLib/RibbonLib, force `/mood ...` through Exec command routing:
- slash command intercept
- deterministic lane
- exact output table for state commands
- exact `[MOOD] <Word> <Swatches>` render for `/mood show`
- fail closed with `ERR: MOOD_ROUTE_NOT_EXECUTED` if not executed

## Test

Run:
```text
/mood on
/mood show
/mood circles
/mood show
```

Expected:
```text
Mood display set to always for this chat.
[MOOD] Calm 💙
Mood swatch mode set to circles.
[MOOD] Calm 🔵
```
