# BC-SKILL-004 — Single Renderer Ownership

## Trigger
Use when multiple components can shape or print the same public line.

## Failure Pattern
Upstream components generate display text and bypass the official renderer.

## Do
1. Identify the one component that owns public rendering.
2. Make upstream components return structured data only.
3. Block direct display strings from support libraries/source documents.
4. Validate final output after the renderer builds it.
5. Remove competing render paths.

## Do Not
- Do not let source/persona/support libraries print user-visible lines.
- Do not allow both a library and Exec to render the same surface.
- Do not patch every layer; choose the owner and enforce it.

## Validation
- Only the renderer produces public output.
- Upstream payloads contain no display-ready strings.
- Final output format is stable across routes.

## Example
Bad:
Persona outputs `steady — warm, present`.

Good:
Persona provides `{ mood_word: "Steady", swatches: ["Blue"] }`; Exec renders `[MOOD] Steady 💙`.
