# Interim Canon — Subject Layout (Teaching + Skills)
updated: 2026-03-03

For every subject:

skills/<domain>/<subject>/
  <SUBJECT>_INDEX.md

  Skills/
    <SUBJECT>_B.md   # machine-facing: patterns, tests, drills, APs, ledger (modules)

  Teaching/
    <SUBJECT>_A.md   # human-facing: explanation, drills, patterns, AP usage (modules)

  overlays/ (only if needed)
    <overlay_id>/
      Skills/<SUBJECT>_B_<OVERLAY>.md
      Teaching/<SUBJECT>_A_<OVERLAY>.md

Rules:
- Always output both lanes (A + B).
- No dump/inbox folders.
- Patterns are explicit IF/THEN laws.
- Drills must have pass/fail or scoring+stop.
- Master index remains TOC-only; view indexes point to entrypoints.
