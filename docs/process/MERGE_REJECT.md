# Process — Merge / Reject

## Merge order
1) Patterns: dedupe and select the best law expression.
2) Drills: dedupe and consolidate; keep drills short and ladder-bound.
3) AP modules: only when the behavior is reusable and deterministic.

## Canonical rule
- Canonical files are:
  - skills/<domain>/patterns/PATTERNS-<DOMAIN>.md (or PATTERNS-CODE.md etc.)
  - skills/<domain>/drills/DRILLS-<DOMAIN>-<TOPIC>.md
  - skills/<domain>/AP-*.md
- Patch files are temporary and should be pruned after merge.

## Reject rule
- If a source adds no new durable laws or drills, mark REJECTED and do not create patches.
