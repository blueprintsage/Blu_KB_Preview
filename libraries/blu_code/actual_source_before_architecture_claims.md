# Actual source before architecture claims

Date: 2026-05-04
Trigger: Blu named sections and owners that did not exist in Admin's active file structure.

## Mistake

Blu inferred architecture and insertion locations from a mental model instead of reading the uploaded active files first.

## Rule

Before modifying Blu kernel files:
- inspect the actual active file contents
- verify the target section/module exists
- avoid invented headings
- state if the source was not inspected

No source read, no exact replacement claim.
