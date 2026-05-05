# BC-SKILL-006 — Structured Support Payloads

## Trigger
Use when Exec depends on PersonaLib, MoodLib, RibbonLib, or any support library.

## Failure Pattern
Support libraries return prose, partially rendered strings, or mixed data that Exec cannot validate deterministically.

## Do
1. Define strict input/output fields.
2. Return structured data only.
3. Keep rendering out of support libraries unless the library is explicitly the renderer.
4. Validate payload shape before Exec consumes it.
5. Fail closed on malformed support payloads.

## Do Not
- Do not return mixed prose and state.
- Do not include final display strings in support output unless contracted.
- Do not let invalid payloads degrade into conversational fallback.

## Validation
- Support output has required fields.
- No unauthorized display-ready text exists.
- Exec can build final output from fields alone.

## Example
Bad:
MoodLib returns `Mood: steady, warm`.

Good:
MoodLib returns `{ mood_word: "Steady", swatch_colors: ["Blue"] }`.
