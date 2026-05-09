# BC-SKILL-017 DeliveryShape Source Markdown Lock

status: active
created: 2026-05-08
category: containment/safety

## Pattern

Source markdown is displayed as rendered presentation, causing large headings, document view, or semantic redesign.

## Rule

For `show`, `list`, `read`, `print`, `open`, `echo`, `raw`, `exact`, or `contents`, source markdown must be delivered as source text or near-raw fenced text unless the user explicitly requests transformed rendering.

Helpfulness is not authorization.

## Checks

- Did markdown render as presentation instead of source?
- Were headings redesigned or enlarged?
- Was structure preserved?

## Tests

- `Show me your MASTER_INDEX.md` prints near-raw source, not a document view.
- `List repo index` does not become a formatted markdown article.
- Explicit `format as readable document` permits transformed rendering.
