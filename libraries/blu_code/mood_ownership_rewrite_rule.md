---
name: Mood ownership rewrite rule
description: Persona/Ribbon/MoodLib may support mood, but Exec owns final public render.
type: architecture
---

## Ownership

```text
PersonaLib -> structured state/signals only
RibbonLib  -> normalized color tokens only
MoodLib    -> mood payload / should_render only
Exec       -> command routing, glyph mapping, final `[MOOD]` print
```

## Public render

Only Exec may print:

```text
[MOOD] <MoodWord> <Swatches>
```

## Forbidden public mood output

- `mood: ...`
- `Mood: ...`
- `steady — warm, present`
- comma-separated trait lists
- raw color words in the swatch slot
- Persona prose fused with mood display
