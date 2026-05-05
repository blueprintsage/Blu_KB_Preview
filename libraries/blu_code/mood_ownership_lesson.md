# Mood ownership lesson

Date: 2026-05-04
Affected area: PersonaLib, RibbonLib, MoodLib, Exec mood output

## Lesson

Public mood output needs one printer.

Recommended ownership:
- PersonaLib: current-turn state/payload only
- RibbonLib: normalized color tokens only
- MoodLib: mood decision/payload only
- Exec: command route, state commit, swatch mapping, public render

## Rule

Any mood-shaped prose outside the Exec-rendered public line is a leak.

Valid public line shape:
`[MOOD] <MoodWord> <Swatches>`

But route proof comes first. If `/mood` is falling through, ownership rewrites will not be reached.
