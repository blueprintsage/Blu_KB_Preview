# Tooling Next Steps

status: active
owner: docs/domains/tooling
last_reviewed: 2026-08-03

The next safe step, not a wishlist. Anything speculative belongs in
`assignments.md` as `spec-needed` or in a design doc PARKED section.

## Next

1. **`PASS-TOOL-RETRIEVAL` phase 1 is packeted and runnable** — extend `tools/build_index.py` to emit `library/MANIFEST.jsonl`. Packet: `docs/assistants/handoffs/PASS-TOOL-RETRIEVAL.md`, base `master` at `86dadfc`. This is the highest-leverage tooling item: §6 scales with library size, not unit size, so every assistant hits the same wall eventually. Ranking is deliberately out of scope and blocked on `PASS-CORPUS-TAG-AUDIT`.
2. Admit the OCR-updated *Dynamic Figure Drawing* PDF after this tooling branch
   merges. Preflight passes with 177 PDF pages aligned to all 177 archived images;
   inspect its reported weak physical pages during the relevant units. Current
   master has no Hogarth registry row, so this is a fresh admission.
3. Migrate a legacy unit ledger to v2 when that unit is next revised; do not rewrite the unresolved TCPL Chapter 19 count without recovering its missing candidate.
4. Rerun the SkillForge portability test in a valid execution environment. First verify that SkillForge is actually active through repository discovery, installed knowledge, or an explicitly logged resolver/card pass. Then evaluate staged image continuity separately, using the accepted prior image as the edit target and rejecting landmark drift before a result is called an overlay.

## Blocked

-

## Parked (with resume trigger)

-
