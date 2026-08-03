# Handoff PASS-TOOL-1: Schema validator + index generator

status: open
audience: Codex (or any coding assistant)
prerequisites:
- Read `docs/PASS/PASS_SCHEMA.md` in full — it is the specification for this tool.
- Read `docs/PASS/PASS_LEDGER.md` for the ledger formats being checked.
- Read `AGENTS.md` and `docs/dev/assistant_coding_behavior.md`.
- Python 3 available. No third-party dependencies beyond a YAML parser
  (`pyyaml`); if that is unavailable, STOP and report rather than hand-rolling a
  YAML parser.
base branch: master.

## Goal

Two scripts that make PASS rules mechanical instead of remembered:

```
tools/validate.py     checks every object in library/ against PASS_SCHEMA.md
tools/build_index.py  regenerates library/INDEX.md and per-package indexes
```

After this lands, "verified" stops meaning "a model said so" and starts meaning
`tools/validate.py` exits 0. That is the acceptance gate PASS currently lacks.

## Scope honesty

Nothing here is hard, but the value is entirely in the rules being *complete and
correct*. A validator that checks frontmatter presence and nothing else is worse
than no validator, because it grants false confidence.

The corpus now holds **63 real objects** across 5 packages (`software_development`,
`writing`, `mathematics`, `art`, `metaskills`) from 10 sources. Build fixtures for
per-rule proof, but **also run against the real library** — it currently passes a
hand-rolled version of rules 1-20, so a correct implementation should report zero
failures on it. If yours reports failures, suspect the validator before the cards.

Two traps found while hand-checking, both worth stealing:

- `library_path` is written in YAML **block-list** form. A regex expecting inline
  `[a, b]` silently matches nothing and reports zero violations — a false pass.
  Handle both forms.
- Matching frontmatter keys with `^([a-z_]+):` at column 0 misses every nested
  `reference:` sub-key and reports them all missing. That produced 70 phantom
  failures on the first attempt.

## Deliverables — validate.py

Exit 0 when everything passes; non-zero with a per-file report otherwise. Each
failure names the file, the rule, and what was found.

**Structural checks**

1. File begins at byte 0 with `---`. Exactly one frontmatter block.
2. Required keys present for the object's type; **no extra keys**; no renamed keys
   (`id`, `type`, root-level `source_id`, anything containing `guard`).
3. `reference` contains exactly its seven keys.
4. Every enum value is legal (see PASS_SCHEMA §1).
5. `routing_class: general` ⇒ `specialization_axis: none`; `specialized` ⇒ not
   `none`.
5b. `library_path` is a list of **2+ non-empty lowercase segments**, and joining
   them under `library/` **exactly equals the object's directory**. `category` and
   `subcategory` are invalid keys and must be rejected if present. The first
   segment is the installable package.
6. Body headings present, in order, no extras, no substitutes. Any heading
   containing "Guard" fails.
7. H1 matches `name` exactly.
8. No unreplaced `<...>` tokens. `Unknown` allowed only for `reference.author` /
   `reference.publish_date`. `provisional` never allowed.
9. Filename has the correct `PAT_` / `DRILL_` / `AP_` prefix and is not ID-only.
10. `name` is not numeric or ID-like; at least two alphabetic words unless
    whitelisted.

**Referential checks**

11. Every `cross_links[].target_object_id` resolves to an existing object.
12. `object_id` is unique across the library.
13. **Fail-closed:** `reference.locator` names a unit that
    `ledger/<source_id>/UNITS.md` marks `processed`. Unresolvable locator or a
    unit marked `queued`/`blocked`/`empty` is a failure.
14. If `variants` is non-empty, each `variant_id` is mentioned in `## Notes`.

**Cross-object body checks** (the ones that matter most)

15. Normalize each `Do` / `Don't` / `Checklist` / `Notes` sentence by stripping the
    object `name`, the IF clause, and the THEN clause, then lowercasing and
    collapsing whitespace. If a normalized sentence appears in **more than 3**
    objects, every object containing it fails, and the report lists them together.
16. Same threshold for IF clauses across patterns, and for ELSE clauses.
17. First `Do` item is not a restatement of the THEN clause; `Notes` does not open
    with one. Use a similarity threshold, and report the pair so a human can judge
    borderline cases.
18. No duplicate items within one object, ignoring case.
19. The full `name` string does not appear in body text outside the H1.
20. Source-independence: flag `see page`, `as shown above`, `as shown in the
    diagram`, `study the figure`, `repeat the exercise from the source`, `use the
    pictured …`, `refer to the illustration`.

Rules 15–17 are the reason this tool exists. They replace four generations of
banned-template catalogues, and unlike prose rules they cannot be forgotten or
worked around by inventing a new wrapper.

Make the thresholds constants at the top of the file, not scattered literals.

## Deliverables — build_index.py

- Walk `library/`, read frontmatter, emit `library/INDEX.md` plus one index per
  **package** (the first `library_path` segment), grouped by the remaining path
  segments.
- **The index is the retrieval layer, not decoration.** It is what makes merge
  (`PASS_RUN.md` §6) and any future genericization tractable without reading every
  file, so each row carries: `object_id`, `name`, `object_type`, `library_path`,
  `foundation_role`, `tags`, and the file path. Answering "does a related skill
  already exist for this candidate?" must cost one index read plus a few targeted
  opens.
- Deterministic ordering, so regenerating with no changes produces a zero-diff.
- Every generated file carries a header line saying it is generated and must not
  be hand-edited.
- **Do not move files.** Placement comes from frontmatter; if an object's
  `library_path` does not match its directory, report it and exit non-zero.
  Relocation is a separate decision.

## Explicitly NOT in this slice

- No extraction, no retrieval, no card authoring, no LLM calls.
- No auto-fixing. The validator reports; a human or a later slice fixes.
- No moving or renaming existing files.
- No CI configuration.
- No corpus migration from DungeonForge `docs/coding/`.

## Danger zone

There is no code in this repo yet, so nothing can be broken — but a validator that
passes a bad object is the failure mode here. Ship fixtures that prove each rule
fires: for every numbered rule, one object that passes and one that fails on that
rule alone.

## Verification

- `python tools/validate.py` exits 0 on the passing fixtures.
- For each numbered rule, the matching failing fixture is rejected **by that rule**
  — not incidentally by another. State the count of rules covered.
- `python tools/build_index.py` twice in a row produces no diff on the second run.
- Report which rules you implemented and which, if any, you deferred and why.

## On completion

Update `docs/domains/tooling/worklog.md`, set PASS-TOOL-1 to `review` in
`docs/worklogs/assignments.md` noting rule coverage, replace the "no validator
exists" guardrail in that file with the real command, and push.

Collision domain: `tools/*`, fixtures under `tests/`, tooling worklog.
