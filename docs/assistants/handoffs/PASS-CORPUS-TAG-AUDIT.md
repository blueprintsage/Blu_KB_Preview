# Handoff PASS-CORPUS-TAG-AUDIT: make tags a retrieval key that retrieves

status: open
audience: any coding assistant
prerequisites:
- `tools/validate.py` exposes `validate_library(library_root, ledger_root)`
  returning `ObjectRecord` values whose `.data["tags"]` and
  `.data["library_path"]` are YAML-parsed. Use this loader, not regex over the
  frontmatter — list indentation is inconsistent across the corpus (`- x` and
  `  - x` both occur) and a regex sweep silently miscounts. Verify first.
- `PASS_SCHEMA.md` §1 currently specifies tags as nothing more than
  `list of strings`. `PASS_DOCTRINE.md` ("One relationship model across every
  skill family") carries the only statement of intent. Read both.
- Read `AGENTS.md`, `docs/dev/assistant_coding_behavior.md`,
  `docs/worklogs/assignments.md`, and `docs/PASS/PASS_RUN.md` §6.
base branch: `master` at `e3dfe64`.
Verify with `git merge-base --is-ancestor e3dfe64 HEAD`.

## Goal

After this lands, a tag can be used to find an object that `library_path` would
not already have found — which is the one job doctrine assigns tags. That
unblocks `PASS-TOOL-RETRIEVAL` phase 2 (ranked ~5-nearest retrieval), which
cannot be built on the current vocabulary without encoding its defects.

## Scope honesty

Nothing here is a tooling gap. The vocabulary itself is broken, and it broke
quietly because **nothing has ever depended on it** — §6 retrieval is manual
grep today, so no run has ever been punished for a bad tag.

Measured at `e3dfe64` over all 214 objects:

| measure | value |
|---|---|
| objects carrying **exactly four** tags | **214 / 214** |
| distinct tags | 259 |
| singletons (reach exactly 1 object) | 122 (47%) |
| confined to a single `library_path` | 185 (71%) |
| restate a `library_path` segment verbatim | 34 distinct, 305 applications |
| **true cross-cutters** (≥2 objects across ≥2 paths) | **74 (29%)** |
| objects with no cross-cutting tag at all | 11 |

Read the first row first: **every object has exactly four tags.** Nobody decided
that 214 unrelated skills each have precisely four relevant contexts. That is a
quota being filled, and it is the same template-stamping pressure
`PASS_DOCTRINE.md` describes under "Why the process is per-unit" — when a slot
must be filled, filling it is cheaper than judging whether it should be.

The quota is also the **cause** of the rot, not a separate problem. When an
object genuinely has two context keys, slots three and four get invented, and an
invented tag is by construction a one-off. That is where 122 singletons came
from. Fix the quota or the singletons grow back on the next run.

The 71% confined to a single `library_path` is the same failure seen from the
retrieval side: a tag that never leaves one directory returns a subset of what
prefix retrieval already returns. It cannot cross-cut, because there is nothing
to cross.

## The rule to establish

Doctrine already states the intent — tags "name contexts such as `python`,
`manga`, `life_drawing`, `robot_design`, `tank`, `resume_writing`, and
`technical_writing`. Tags connect related routes even when navigation paths
differ." Every one of those examples is a **context**, not a topic. Write that
down as an enforceable rule:

1. **A tag names a context; `library_path` names the topic.** Context means the
   language, tool, framework, medium, style, genre, tradition, domain, or
   audience a skill applies to. Note this is nearly the `specialization_axis`
   enum the schema already defines — the corpus has a context vocabulary, tags
   just stopped drawing from it.
2. **A tag equal to a `library_path` segment is invalid** (normalizing `-`/`_`).
   It duplicates a retrieval route that already exists. 34 tags currently
   violate this.
3. **Reach floor: a tag must reach ≥2 objects across ≥2 distinct
   `library_path`s.** Below that it retrieves nothing prefix retrieval did not
   already give.
4. **No quota. Any count, including zero.** An object with no cross-cutting
   context legitimately carries no tags. Four is not a target.

`cpp` (80 objects across 24 paths) **satisfies this rule and must not be split.**
It is precisely doctrine's `python` example. Breadth is not rot: a broad key is
narrowed by *combining* it with another (`cpp` + `refactoring`), which is what
§6's "tighten if it returns 40" already asks for. Do not subdivide a correct
tag to make a count look better.

## Deliverables

1. **Write the policy** into `PASS_SCHEMA.md` §1 where `tags` is currently
   specified as `list of strings`, stated as the four rules above. Record the
   rationale and the measured evidence as a dated entry in
   `docs/domains/corpus/decisions.md` — the reason is what tells a future reader
   whether the decision still holds.

2. **`tools/audit_tags.py`** — a report, not a gate. For the current library
   print: distinct count, reach histogram, singletons, path-segment collisions,
   per-tag path span, and objects with no cross-cutting tag. This is how the
   migration is steered and how the result is checked. Reuse `validate_library()`.

3. **Migrate the 214 objects.** Sequence it so the diff is reviewable:
   - **3a — mechanical removals.** Drop the 34 path-segment duplicates and every
     singleton that names a topic rather than a context. Pure deletion, checkable
     against the audit report.
   - **3b — considered additions.** Give the 11 dead-zone objects real context
     keys. Prioritise these: 6 of them are the new
     `foundations/code-comprehension` lane, which is exactly where *Code Complete*
     and *The Pragmatic Programmer* are expected to attach variants
     (`docs/domains/corpus/next_steps.md`). The newest lane is currently the
     least retrievable one.
   - Keep 3a and 3b as separate commits. A single 214-file retag is not
     reviewable in one pass.

4. **Enforce, last.** Add validator rules for #2 (path-segment collision) and #4
   (no quota — reject a library where every object has an identical tag count).
   **Do not add the reach floor (#3) as a hard validator rule**: it is a property
   of the vocabulary as a whole, not of one file, and a card legitimately drops
   below the floor the moment it is the first of its kind. Leave #3 to
   `audit_tags.py`. Enforcement lands after migration — added first, it fails all
   214 objects and blocks every other run.

## Explicitly NOT in this slice

- **Ranked retrieval.** `PASS-TOOL-RETRIEVAL` phase 2 owns it, and it is the
  consumer of this work, not part of it.
- **`library/MANIFEST.jsonl`.** `PASS-TOOL-RETRIEVAL` phase 1. If that has
  already landed, regenerate it after migrating and confirm it still round-trips;
  do not change its shape here.
- **Any change to `library_path`.** Retagging must not become re-shelving. If an
  object looks mis-shelved, note it and move on — placement is PASS's, per
  `PASS_DOCTRINE.md` "Ownership boundary."
- **Adding or removing frontmatter keys.** `PASS_SCHEMA.md` §1 is closed.
- **Splitting `cpp`.** See above.

## Danger zone

- **This touches every object in the library.** Nothing else may ride along.
  `git diff --stat` after 3a should show tag lines only.
- **`INDEX.md` must stay byte-identical.** Generated indexes carry name, type,
  and stage — not tags — so a correct retag changes zero index bytes. Regenerate
  and assert `git diff --stat -- 'library/**/INDEX.md'` is empty. If an index
  moves, something other than tags was edited.
- **`tags` is not referenced by `cross_links`, `foundation_object_id`, or any
  ledger field**, so retagging cannot break resolution — but confirm with
  `validate.py` rather than assuming, since dangling-link detection is the check
  that would catch a mistake.
- **Do not regex the frontmatter.** Inconsistent list indentation across the
  corpus makes regex sweeps undercount silently; that is how the first pass at
  these numbers was wrong. Use the YAML-parsed loader.
- **Resist re-hitting four.** The instinct when removing a tag is to backfill.
  Do not. An object dropping to one or zero tags is a valid outcome and is the
  signal the quota is actually gone.

## Verification

- `python tools/validate.py` exit 0 (214 objects at the base commit).
- `python tools/build_index.py` — second run `0 changed`;
  `git diff --stat -- 'library/**/INDEX.md'` empty.
- `python -m unittest discover -s tests` exit 0.
- `python tools/audit_tags.py` against the migrated library, meeting:
  - tags equal to a `library_path` segment: **0**
  - singletons: **≤5%** of distinct tags (from 47%)
  - distinct tags spanning ≥2 paths: **≥90%** (from 29%)
  - objects with no cross-cutting tag: **0**, or each remaining one listed with a
    stated reason
  - tags-per-object is **no longer a constant**
- Manual smoke: pick two objects in *different* `library_path`s that a
  practitioner would want returned together, and confirm a single tag now
  retrieves both.
- Report exactly what shipped vs. deferred.

## On completion

Update `docs/domains/corpus/worklog.md`, set `PASS-CORPUS-TAG-AUDIT` to `review`
in `docs/worklogs/assignments.md` with what was tested, and push. If the reach
floor turns out to need a different threshold than ≥2/≥2, say so with the numbers
rather than quietly adopting another one.

Collision domain: `tags` frontmatter across all of `library/`,
`tools/audit_tags.py`, `tools/validate.py`, `docs/PASS/PASS_SCHEMA.md` §1,
`docs/domains/corpus/decisions.md`.
