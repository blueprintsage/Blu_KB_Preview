# Documentation Index

status: active
owner: docs/dev
last_reviewed: 2026-07-30

## Purpose

The routing map. An assistant reads `AGENTS.md`, then this, then the one domain
index it actually needs. Nobody reads the whole tree.

## Read first

```text
AGENTS.md
docs/dev/assistant_coding_behavior.md
docs/worklogs/assignments.md
```

## Project-wide guides

```text
docs/dev/assistant_coding_behavior.md   assistant-neutral coding behavior
docs/dev/doc_status_header_standard.md  doc metadata + safe deprecation
```

## Canonical PASS documents

Read in this order:

```text
docs/PASS/PASS_DOCTRINE.md   what PASS is, the three object types, the contract
docs/PASS/PASS_SCHEMA.md     closed object contracts + the mechanical rules
docs/PASS/PASS_RUN.md        the per-unit run procedure
docs/PASS/PASS_LEDGER.md     source / unit / candidate ledger formats
docs/PASS/PASS_LIBRARY.md    generated library tree, packages, and bootstrap contract
docs/PASS/PASS_GROUNDING.md  the anti-skim gate: reading receipts + verify_grounding.py
docs/PASS/PASS_CONSUMPTION.md the use-time contract: golden-truth, foundations-first, task-scoped
```

Supporting:

```text
docs/templates/{AP,DRILL,PATTERN}_OBJECT_TEMPLATE.md   fill-in shapes
```

`PASS_SCHEMA.md` is the source of truth for card shape. A card that disagrees
with it is the card's bug — never widen the schema to accommodate one card.

## Repo layout

```text
sources/    the books — GITIGNORED, never committed (see sources/README.md)
ledger/     per-source run record: SOURCE.md, UNITS.md, units/*  (tracked)
library/    extracted objects, path derived from frontmatter      (tracked)
tools/      validator + index generator (PASS-TOOL-1, not built yet)
docs/       specs and the agent system
```

## Domains

Each domain owns a folder with a routing `index.md` and the continuity quartet
(`worklog.md`, `decisions.md`, `failures.md`, `next_steps.md`).

| Domain | Path | Notes |
|---|---|---|
| spec | `docs/domains/spec/` | The PASS method and object schemas. Owns `PASS_v20.6_ABSOLUTE_SPEC_FLAT.md` and `docs/templates/`. Schema changes ripple into every card, so they get logged here first. |
| corpus | `docs/domains/corpus/` | Produced cards — APs, patterns, drills — and the per-source extraction ledger. |
| tooling | `docs/domains/tooling/` | Schema validation, index generation, and any scripts that check the corpus mechanically. |

Copy `docs/domains/_TEMPLATE/` to start a new domain.

## Historical material

```text
docs/archive/pass_chat_era/PASS_v20.6_ABSOLUTE_SPEC_FLAT.md  superseded spec
docs/archive/pass_chat_era/notes/                            ladder, lenses, memcaps, roadmaps
docs/archive/pass_chat_era/exports/                          prior run exports (zips)
```

All chat-era material. Kept for history, **not for execution** — do not run PASS
from anything under `docs/archive/`. Two files there are still worth reading:
`notes/memcaps/Incident report.md` (the 2026-03-04 fail-open root cause that the
fail-closed rule exists to prevent) and the superseded spec's Generation 1-4
failure catalogues, which are what the validator rules are derived from.

## Assistant packets

```text
docs/assistants/index.md
```

## Worklogs

```text
docs/worklogs/assignments.md    the assignment ledger
docs/worklogs/active/           cross-cutting work notes
```
