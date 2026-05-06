# BC-SKILL-013 — Renderer Contract Boundary

## Trigger

Use when a renderer emits an invalid public line, accepts malformed upstream state, or a patch proposes changing renderer behavior to compensate for bad proposal data.

## Failure Pattern

A renderer that should be dumb, literal, and strict gets loosened to handle expressive or malformed upstream state. The visible output may appear more flexible, but the route becomes unstable because the terminal contract is no longer the final invariant.

Common symptoms:
- renderer accepts compound descriptors where a single token is required
- renderer accepts unsupported emoji, glyphs, labels, aliases, or fallback text
- renderer emits optional adornments when upstream justification is missing
- renderer tries to infer, repair, beautify, summarize, or emotionally reinterpret proposal data
- renderer changes because the actual bug is in the proposal, normalization, or validation layer

## Do

1. Identify the canonical renderer and freeze its public output contract before patching.
2. Treat the renderer as the terminal formatting boundary only.
3. Patch the upstream proposal, normalization, weighting, or validator layer so renderer input is already contract-valid.
4. Keep support libraries and Persona source lanes structured-state only.
5. Validate payload shape before render.
6. Reject, drop, or clamp invalid optional fields before render according to the existing contract.
7. Fail closed when required fields cannot be made valid without changing the render contract.
8. Add negative tests for the exact malformed payloads that escaped.

## Do Not

- Do not loosen the renderer contract to hide upstream contamination.
- Do not add new public shapes, emoji, glyphs, aliases, or text fallbacks unless the contract itself is explicitly being changed.
- Do not let the renderer infer emotional meaning from invalid fields.
- Do not move weighting, selection, semantic repair, or source interpretation into the renderer.
- Do not call a patch successful because the renderer can “handle” bad input.
- Do not mutate deterministic output after render.

## Validation

A renderer-bound patch passes only if:

- the renderer’s accepted public shape is unchanged
- malformed upstream payloads are blocked before render or fail closed
- optional adornments are omitted unless upstream justification passes threshold
- unsupported symbols never reach public output
- final output remains deterministic and exact across routes
- live route matrix proves the affected route still terminates through the renderer

Minimum negative tests:
- compound descriptor input is rejected or collapsed upstream before render
- unsupported emoji/glyph input is rejected upstream before render
- optional swatch/ribbon input below threshold is omitted
- prose or display-ready strings from support libraries are rejected
- renderer does not invent fallback phrasing for invalid payloads

## Example

Bad:

```yaml
patch:
  renderer:
    accept_descriptors:
      - single_word
      - hyphenated_phrase
    accept_swatches:
      - approved_palette
      - expressive_emoji
```

Good:

```yaml
patch:
  upstream_normalizer:
    descriptor:
      input: "Fed-up-solidarity"
      output: "Frustrated"
    swatches:
      input: ["🔥", "💙"]
      output: ["💙"]
      invalid_dropped: ["🔥"]
  renderer:
    contract_unchanged: true
    output: "[MOOD] Frustrated 💙"
```

Better when ribbon threshold is not met:

```yaml
patch:
  upstream_validator:
    descriptor: "Frustrated"
    swatches: []
    ribbon_threshold_met: false
  renderer:
    contract_unchanged: true
    output: "[MOOD] Frustrated"
```
