# Handoff: Visual reference generation + review gate

status: open
owner: Codex (has an image renderer + generator)
author: Claude (spec)
last_reviewed: 2026-07-31
tracks: PASS-SCHEMA-VISUAL-REFERENCES (assignments.md)
depends_on_decisions: docs/domains/spec/decisions.md 2026-07-31 (Decisions 1 & 3)

## Why

A visual skill card that carries only text ("build the hand from rod, ball, and
wedge masses") names the decision but not the execution. For a `visual: true`
source, the card is not teachable without a **reference image**. Per Decision 1,
that image must be **original art the model generates** from the source page plus
the card text — never a reproduction of the copyrighted plate. This packet builds
the field, the generator, and the gate that keeps it honest.

Capability honesty up front: this needs an image-generation model and a vision
review model. Where neither is available the card stays text-only and is flagged
non-teaching — do not ship a visual card with a fabricated or missing reference.

## Deliverables

### 1. Schema — add `references` (closed-contract change)

Add to the common frontmatter (PASS_SCHEMA.md §1). This invalidates the shape of
every visual card, so: log it in `docs/domains/spec/decisions.md` first, update
`tools/validate.py`, and migrate visual cards in the same pass.

```yaml
references:                 # list; [] valid; REQUIRED non-empty for visual sources
  - image_path: <repo-relative path under the card's topic, e.g. library/art/drawing/figure-construction/assets/hand_rod_ball_wedge.png>
    caption: <what this image teaches, one line>
    derived_from: <source locator the model studied, e.g. "u04 p.72 figure">
    origin: generated            # never "reproduced"
    review: <pending | passed>   # set by the review gate, not by hand
```

Rules the validator enforces:
- On a `visual: true` source (SOURCE.md), every exported card that teaches a
  visual behavior must have `references` non-empty. (Text-only meta cards may be
  exempt; scope the exemption narrowly.)
- `origin` must be `generated`. A card may not declare `reproduced`.
- Each `image_path` must exist and sit under the card's own topic folder.
- `review: passed` is required to ship. `pending` fails the acceptance gate.

### 2. Generator — `tools/generate_reference.py`

Input: a card + the rendered source page(s) it cites (`derived_from`) + the card
text (name, rule, Do/Don't). Output: an **original** teaching image saved at
`image_path`, plus the provenance fields above.

- Prompt the image model from the card's construction text, using the rendered
  source page as *reference for the idea*, not as an image to copy.
- Write provenance: generator model + date into a sidecar
  (`<image>.meta.json`) so review and audit have it.
- Never save the source render as the reference. The source PNG is grounding
  evidence (PASS_GROUNDING), not the shipped teaching image.

### 3. Review gate — `tools/verify_references.py`

For each visual card with `references`, before it ships:

1. **Exists** — `image_path` and its sidecar are present.
2. **Depicts the claim** — a vision model (or a human, recorded) confirms the
   image shows what the card's rule describes. Record the verdict + reviewer +
   date; set `review: passed` only on a pass. This is the "AI hands" guardrail:
   figure generation is the weak spot, so the image is checked, not trusted.
3. **Original, not a copy** — compare the generated image against the rendered
   source page(s) it derived from (perceptual hash / structural similarity). If it
   is too similar to the source plate, FAIL as a suspected reproduction. We want
   original art; the similarity check is what enforces the copyright line
   mechanically.

Exit non-zero on any failure. Wire it into the acceptance gate alongside
`validate.py` and `verify_grounding.py`: a visual card with `review: pending` or a
failed review does not ship.

## Acceptance criteria

- One valid fixture (visual card + generated image + passing review) and one
  failing fixture per new rule (missing image, `origin: reproduced`, too-similar-
  to-source, review pending).
- `python tools/validate.py` passes with the new rule; `verify_references.py`
  passes the valid fixture and fails each bad one.
- PASS_SCHEMA.md, PASS_GROUNDING.md (visual section), and PASS_CONSUMPTION.md
  (visual-skills-require-their-reference) updated to reference the field and gate.
- Decision logged in `docs/domains/spec/decisions.md`.

## Boundaries — do not

- Do not embed, crop, or lightly edit a source plate and call it a reference. The
  similarity check exists to catch exactly this.
- Do not set `review: passed` without an actual vision or human check recorded.
- Do not make text-source cards (coding, math, writing) carry references; this is
  for `visual: true` sources only.
