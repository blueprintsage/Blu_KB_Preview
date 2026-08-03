# Handoff PASS-TOOL-RETRIEVAL: a greppable object manifest for §6 placement

status: open
audience: any coding assistant
prerequisites:
- `tools/build_index.py` exists and calls `validate_library()` from
  `tools/validate.py`, returning `ObjectRecord` values with `.data`
  (parsed frontmatter), `.sections` (body sections keyed by `##` heading), and
  `.relative_path`. Verify before starting; if the signature has changed, STOP
  and report.
- `tests/test_tools.py` exists and runs under
  `python -m unittest discover -s tests`.
- Read `AGENTS.md`, `docs/dev/assistant_coding_behavior.md`,
  `docs/worklogs/assignments.md`, `docs/PASS/PASS_RUN.md` §6, and
  `docs/PASS/PASS_SCHEMA.md` §1 and §6.
base branch: `master` at `86dadfc`.
Verify with `git merge-base --is-ancestor 86dadfc HEAD`.

## Goal

After this lands, an assistant running PASS §6 can find the ~5 objects a
candidate might collide with by grepping one generated file, instead of walking
the library tree and opening whole cards to discover they are irrelevant.

§6 is the dominant context cost of a PASS run and it scales with **library size,
not unit size** (`docs/domains/corpus/decisions.md`, 2026-08-01). Measured on the
library at `86dadfc`: 214 objects, ~152k tokens total, ~712 tokens per card. A
20-page chapter yields ~11 candidates; at ~5 neighbours each that is 25-30 unique
card reads — roughly 20k tokens *after* the neighbours have been located, and the
locating is the larger, unmeasured half. This is what put Codex at ~89% context on
a two-chapter run.

A manifest row is ~150 tokens. The whole-library manifest is ~30k tokens, but it
is a file you **grep**, never read end to end.

## Scope honesty

The manifest does not exist in any form today. Generated `INDEX.md` files carry
name, type, and stage only — no tags, no IF clause, no foundation/variant
relationships. There is currently no artifact between a filename and a full
712-token card. That gap *is* the O(library) cost.

Two things this cannot fix, so do not let the scope drift toward them:

1. **This is a cost fix, not a quality fix.** It helps place candidates that were
   already extracted. It does nothing for under-extraction in §5, which is where
   the misses in the `programmers_brain` u01-u02 review actually came from.
2. **Tag-based retrieval is currently unreliable and this slice does not repair
   it.** At `86dadfc` there are 256 distinct tags over 214 objects, **120 of them
   singletons (47%)**, while `cpp` alone covers 80 objects. Half the tags can
   never surface a neighbour; the broadest one returns a whole lane. Emit tags
   into the manifest as they are. Do not rewrite tags. See
   `PASS-CORPUS-TAG-AUDIT`.

If effort balloons past the deliverables below, ship what works and STOP +
report rather than starting on ranking.

## Deliverables

1. **Extend `tools/build_index.py` to emit `library/MANIFEST.jsonl`.**
   Extend it — do not fork a new tool. `build_index.py` already performs the
   validated walk, already owns the determinism contract, and already has test
   coverage; a second walker would duplicate all three and drift from them.

2. **One JSON object per line, plus a leading header record.** JSONL because the
   point is `grep`-ability: one object per line means a tag or path match returns
   a complete, self-describing record. The first line is a header record
   (`{"_generated_by": "tools/build_index.py", "_object_count": N}`) standing in
   for the `<!-- GENERATED -->` comment that JSON cannot carry.

3. **Fields per object** — exactly what §6 needs to choose a disposition, and
   nothing else:

   | field | why §6 needs it |
   |---|---|
   | `object_id`, `relative_path` | open the card once it is worth opening |
   | `name`, `object_type`, `stage_binding` | identify it |
   | `library_path` (list) and `library_path_str` (posix, e.g. `software-engineering/foundations/readability`) | prefix retrieval by grep |
   | `tags` | cross-cutting retrieval keys |
   | `if_clause`, `then_clause` | **the learner decision** — the thing §6 step 3 actually tests |
   | `target_skill` (drills) | the drill's equivalent of the learner decision |
   | `foundation_role`, `foundation_object_id`, `specialization_axis`, `routing_class` | foundation vs specialization route |
   | `variants` — list of `{variant_id, variant_name, variant_basis, source_id}` | stops a run re-absorbing a variant that is already there |
   | `cross_links` | neighbours the object itself declares |

   Use `null` for a field an object type does not carry (`if_clause` on a drill,
   `target_skill` on a pattern). Do not omit keys — a stable key set keeps rows
   greppable by field name.

4. **Lift the IF/THEN extraction into a named helper in `validate.py`.** The
   regex `(?m)^\*\*(IF|THEN)\*\*\s*(.+)$` against
   `record.sections["Pattern Rule"]` already exists, inlined inside
   `normalize_sentence()`. Extract it to a shared function and call it from both
   sites. Do not copy the regex into `build_index.py` — two copies will diverge
   and the validator's THEN-recycling rule depends on this parse.

5. **Inherit fail-closed behaviour.** `build_index.py` today refuses to generate
   indexes when the library is invalid ("Refusing to generate indexes for an
   invalid library"). The manifest is subject to the same rule: an invalid
   library produces **no** manifest write, not a partial one. A stale manifest is
   recoverable; a manifest that silently disagrees with the library is the same
   class of failure as an ungrounded card.

6. **Determinism**, matching the existing contract: a second consecutive run
   changes zero bytes. Sort rows by the existing `object_sort_key`. Serialize
   with sorted keys and `ensure_ascii=False`.

7. **Tests in `tests/test_tools.py`**: header record present and counts match;
   one row per object; a pattern row carries `if_clause`/`then_clause` and a null
   `target_skill`; a drill row the inverse; a card with absorbed variants emits
   all of them; second generation is byte-identical; an invalid library writes no
   manifest.

8. **Update `PASS_RUN.md` §6 step 1** to name the manifest as the retrieval
   surface, keeping the existing "aim for ~5, tighten if it returns 40" rule.
   One or two sentences. Do not restructure §6.

## Explicitly NOT in this slice

- **Ranked "~5 nearest" retrieval.** That is the hard half, and it is blocked on
  the tag audit — ranking over a vocabulary that is 47% singletons would encode
  the rot. A greppable manifest is most of the value at a fraction of the risk.
  Follow-on slice owns it.
- **The tag vocabulary audit.** `PASS-CORPUS-TAG-AUDIT` owns it. Corpus domain,
  not tooling.
- **Embedding or semantic similarity.** Not until lexical retrieval over a clean
  vocabulary has been shown to be insufficient.
- **Any change to the object schema.** `PASS_SCHEMA.md` §1 is a closed contract:
  extra keys are invalid. The manifest is *derived* from objects. Do not add a
  field to cards to make the manifest easier to build.
- **Changing any existing `INDEX.md`.** See Danger zone.

## Danger zone

- **The 45 existing `INDEX.md` files must stay byte-identical.** Assert it:
  regenerate, then `git diff --stat -- 'library/**/INDEX.md'` must be empty. It
  is easy to refactor the shared walk and perturb ordering.
- **`library/MANIFEST.jsonl` placement.** It sits at the library root and is
  generated. Confirm it does not get treated as an installable package artifact
  by the root index renderer — `render_root()` enumerates packages from
  `library_path[0]`, so a stray file at that level must not appear as a package.
- **Frontmatter values containing colons, quotes, or non-ASCII.** Card prose
  contains em-dashes, backticks, and curly quotes. Round-trip a card whose IF
  clause contains a colon and confirm the row re-parses.
- **`extract_sections()` keys on the literal `##` heading text.** A pattern whose
  Pattern Rule section is missing or renamed yields no IF clause. Emit `null` and
  let `validate.py` remain the thing that complains; do not add a second
  validation path.

## Verification

- `python tools/validate.py` exit 0 (214 objects at the base commit).
- `python tools/build_index.py` twice: second run reports `0 changed` and
  `MANIFEST.jsonl` is byte-identical.
- `python -m unittest discover -s tests` exit 0 (32 tests at the base commit,
  plus the new ones).
- `git diff --stat -- 'library/**/INDEX.md'` empty after regeneration.
- Manual smoke, the case this exists for: take the candidate *"avoid short
  identifiers that are easy to confuse visually"* and, **using only greps against
  `MANIFEST.jsonl`**, reach `PAT_use_descriptive_names` and confirm from the row
  that it already carries `v_cognition_visually_distinct_identifiers`. Correct
  means answering "variant, already absorbed" without opening a single card.
- Report exactly what shipped vs. deferred.

## On completion

Update `docs/domains/tooling/worklog.md`, set `PASS-TOOL-RETRIEVAL` to `review`
in `docs/worklogs/assignments.md` with what was tested, and push.

Collision domain: `tools/build_index.py`, `tools/validate.py`,
`tests/test_tools.py`, `library/MANIFEST.jsonl`, `docs/PASS/PASS_RUN.md` §6.
