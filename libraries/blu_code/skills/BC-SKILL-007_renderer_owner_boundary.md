# BC-SKILL-007 — Renderer Owner Boundary

## Trigger

Use when a route produces public text, status lines, command confirmations, mood lines, help output, or exports.

## Failure Pattern

Multiple layers shape the same public line, or a legacy renderer leaks output after the route owner changed.

## Do

1. Identify the one component that owns the public render packet for the route.
2. Make upstream components return structured fields, not display-ready text, unless they are the renderer.
3. Add forbidden-output checks for known legacy formats.
4. Let Egress authorize print; do not let the renderer print directly.
5. Remove or denylist competing renderers.

## Do Not

- Do not allow both Exec and a service to render the same feature output.
- Do not patch help text as proof that execution rendering changed.
- Do not accept legacy wording as close enough.
- Do not let Persona/source/support output resemble command output.

## Validation

- Only the selected owner packet supplies printable_output.
- Forbidden legacy prefixes fail validation.
- Help/inventory output and execution output are separately tested.
- Final output shape is stable across state changes.

## Example

Bad: `/mood on` prints `Mood display enabled.` from a legacy handler.

Good: Mood owner returns `Mood display set to always for this chat.` and Egress prints it.
