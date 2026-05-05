# Single printer ownership lesson
Date: 2026-05-04
Example area: PersonaLib, RibbonLib, MoodLib, Exec mood output

## Lesson
Public output needs one printer. For Mood:
- PersonaLib: current-turn state/payload only
- RibbonLib: normalized color tokens only
- MoodLib: mood decision/payload only
- Exec: command route, state commit, swatch mapping, public render

## Rule
Any public-shaped prose outside the assigned printer is a leak. Route proof comes first; if the command is falling through, ownership rewrites will not be reached.
