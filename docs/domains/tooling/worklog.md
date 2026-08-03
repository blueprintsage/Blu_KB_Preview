# Tooling Worklog

status: active
owner: docs/domains/tooling
last_reviewed: 2026-08-01

Newest entry first.

## 2026-08-01 - SkillForge resolver (consumption side) MVP

### What changed

Added `tools/resolve.py`, the first consumption-side tool: given a natural-language
task it parses card frontmatter (reusing validate.py's frontmatter contract), scores
candidates by weighted overlap against tags, `library_path`, name, and `IF` clause,
expands foundations upward (declared `foundation_object_id` plus a reverse index over
`foundation_of`/`prerequisite_for` links), orders the bundle metaskill -> foundations
-> patterns -> APs -> drills, and emits either paths (`--format paths`) or the
consumption contract + metaskill + every selected card inlined (`--format full`) for
one-read loading. Added `.claude/skills/skillforge/SKILL.md`, a Claude Code adapter
whose description triggers on covered-domain work and whose body runs the resolver and
consumes the bundle per `docs/PASS/PASS_CONSUMPTION.md`. No change to the library,
schema, or existing tools.

### What was tested or reviewed

Ran against the live 231-object library. C++ queries pull the real `languages/cpp`
package (const-correctness, casting, resource-management/RAII, copy-control,
memory-management) with correct upward foundation expansion; an out-of-domain query
("sourdough starter") correctly returns `coverage: none`; the term-level coverage line
honestly reports words the library is not filed under (e.g. "silent on: ownership,
lifetime" even while RAII cards load). `--format full` produces a well-formed 1058-line
bundle (contract + metaskill + foundation + 12 cpp cards), foundations first, exit 0.
`python -m unittest discover -s tests` = 35 passed; `git status` clean except the two
new files.

### What worked

Testing against the real library caught four design bugs the paper design missed:
foundation links point foundation->dependent, so upward expansion needs the reverse
index; skill-lane drill exclusion must precede the cap or drills starve the actual
skills; a min-score floor is needed to reject lone weak name hits; and stdout must be
forced to UTF-8 for card/contract unicode on a cp1252 console.

### What failed / still open

Matching is lexical (tag/path/name/IF overlap with a small alias map), so it has no
synonymy beyond the alias list -- "ownership" does not retrieve RAII by meaning, only
the shared `cpp` topic does. The resolver enforces what loads, not what the model
applies; that ceiling is documented in the SKILL.md and PASS_CONSUMPTION.md and is not
closed by this tool. No unit tests for resolve.py yet. No generated runtime cache (231
files parse fast enough that direct parsing is simpler); revisit if the library grows.

### Known risks

Lexical recall can miss a relevant card whose vocabulary differs from the query, and
the min-score floor can drop a genuinely relevant single-term match. Both fail toward
under-retrieval plus an honest coverage line rather than silent bad application.

### Next safe step

Add resolve.py unit tests (scoring, reverse foundation expansion, lane/floor filters,
coverage classification) against a small fixture library. Consider a `--json` output
for programmatic callers and an optional receipt of applied vs. loaded objects.

### Files changed

`tools/resolve.py` (new), `.claude/skills/skillforge/SKILL.md` (new), this worklog.

## 2026-08-01 - Hogarth OCR retest passes with one instructional miss

### What changed

Extended PDF preflight output with `weak_physical_pages` so a visual run knows
which pages require direct inspection even when the source-level text layer
passes. Corrected continuity: current master has no Hogarth registry row, so the
OCR payload will be admitted fresh rather than replacing an admitted hash.

### What was tested or reviewed

The OCR-updated 177-page PDF reports 167 meaningful-text pages, 164 fully usable
pages, and 150,827 alphanumeric characters. Renderer and 177-image archive both
pass. Visually inspected all 13 weak pages; twelve are covers, title pages, or
drawing plates. Physical PDF page 117 / printed page 116 is the only
instructional prose page missed by OCR.

### What worked

Preflight now passes the OCR payload while exposing the exact exception that a
unit reader must handle through the page image.

### What failed / still open

Acrobat did not recognize the two short instructional paragraphs on physical
page 117. They remain visually legible and therefore do not block the source.

### Known risks

Weak-page reporting locates low text volume; it cannot decide whether the page
contains prose. Visual review remains required.

### Next safe step

Merge the tooling branch, admit SHA-256 `588f72509b5a...`, and use `image:`
grounding when the unit containing printed page 116 is processed.

### Files changed

`tools/preflight_pdf.py`, `tests/test_tools.py`, PASS run guidance, assignment
status, and corpus/tooling continuity docs.

## 2026-08-01 - Art-book PDF preflight and page-image grounding

### What changed

Added a fail-closed PDF preflight that reports text-layer usability before
source admission and, for visual sources, proves the run has both vision
capability and a working renderer or verified page-image set. Added direct and
ZIP-member `image:` receipt evidence. PDF rendering now uses the visible CropBox
by default, with an explicit MediaBox override.

### What was tested or reviewed

Added tests for empty/mixed text layers, contiguous and decodable ZIP page sets,
direct and ZIP page-image grounding with spaces, and CropBox command generation.
Ran the preflight against the real 177-page *Dynamic Figure Drawing* PDF and its
177-image archive: the renderer and archive passed while the empty text layer
correctly returned `NOT READY / NEEDS_OCR`.

### What worked

The preflight distinguishes source readability from visual availability. It
probes an actual renderer output instead of trusting executable discovery, and
the source archive can remain zipped while supplying exact receipt evidence.
CropBox rendering removes the large blank scanner margins observed in Hogarth.

### What failed / still open

The current Hogarth PDF has zero extractable characters and cannot pass until an
OCR copy is supplied. Preflight can verify numbering and decoding but cannot
prove page identity; the first, middle, and last mappings still require visual
confirmation. Existing four-digit and fresh-prefix renderer issues remain out of
scope.

### Known risks

Text-layer classification is a readiness heuristic. A `mixed` art source still
requires per-unit reading and grounding, and successful image decoding does not
prove the art was understood. OCR replacement changes the hash of an already
admitted payload and therefore needs explicit identity review.

### Next safe step

Re-run the same preflight after Acrobat OCR, confirm 177 aligned pages, and only
then decide how to update the already-admitted Hogarth source identity.

### Files changed

`tools/{preflight_pdf.py,render_pdf.py,verify_grounding.py}`,
`tests/test_tools.py`, PASS run/grounding/ledger docs, tooling and corpus
continuity docs, and `docs/worklogs/assignments.md`.

## 2026-08-01 - PASS-TOOL-RETRIEVAL packeted; tag rot found and split out

### What changed

Wrote `docs/assistants/handoffs/PASS-TOOL-RETRIEVAL.md` and moved the assignment
from `spec-needed` to `open`. Scoped it **down**: the row asked for a ranked
"~5 nearest neighbours" retriever; the packet ships only phase 1, extending
`build_index.py` to emit `library/MANIFEST.jsonl` — one greppable row per object
carrying tags, `library_path`, the IF/THEN learner decision, foundation route,
and already-absorbed variant ids. Filed `PASS-CORPUS-TAG-AUDIT` as a new
`spec-needed` row.

### What was tested or reviewed

Measured the library at `86dadfc` rather than estimating: 214 objects,
~152k tokens, ~712 tokens/card, 159/214 carrying a parseable `**IF**` line.
Confirmed generated `INDEX.md` carries name/type/stage only — no tags, no IF, no
foundation/variant links — so nothing exists today between a filename and a full
card. Confirmed `ObjectRecord.sections` already exposes `Pattern Rule`, and that
the IF/THEN regex is already inlined in `validate.normalize_sentence()`, so the
packet requires lifting it to a shared helper rather than duplicating it.

### What worked

Splitting cost from ranking. The manifest is mostly serialization of a walk
`build_index.py` already performs, and it is unblocked; ranking is neither.

### What failed / still open

**The tag vocabulary is too weak to rank on.** Authoritative figures (YAML
loader, not the regex sweep first used): 259 distinct tags over 214 objects,
122 singletons (47%), 185 (71%) confined to one `library_path`, only 74 (29%)
genuinely cross-cutting. A singleton never surfaces a neighbour; a
single-path tag returns a subset of what prefix retrieval already gives. This is
invisible today only because §6 retrieval is manual; it becomes load-bearing the
moment anything ranks on tags. Hence the split — building ranking first would
have encoded the rot. Packeted as `PASS-CORPUS-TAG-AUDIT`, which carries the
root cause: every object has exactly four tags, so slots three and four get
invented, which is where the singletons come from.

### Known risks

The manifest is a **cost** fix, not a **quality** fix, and the packet says so
twice. It helps place candidates that were already extracted; it does nothing for
§5 under-extraction, which is where the misses in the `programmers_brain` u01-u02
review actually came from. Do not let it be reported as a fix for extraction
yield.

### Next safe step

Implement phase 1 per the packet. Do not start ranking until
`PASS-CORPUS-TAG-AUDIT` has a packet and has run.

### Files changed

`docs/assistants/handoffs/PASS-TOOL-RETRIEVAL.md` (new), `docs/worklogs/assignments.md`,
`docs/domains/tooling/next_steps.md`, and this worklog.

## 2026-07-31 - Generated Visual References and Release Review Gate

### What changed

Added `tools/generate_reference.py` to persist original image-model output and
provenance, `tools/verify_references.py` to require review evidence and reject
source-like output, and validator rule 23 for the closed reference shape.

### What was tested or reviewed

The 31-test tooling suite covers a valid visual fixture plus missing image,
forbidden `origin: reproduced`, pending review, and copied-source failures.
Ran `validate.py`, `verify_grounding.py --source gen1_art_fundamentals_4step`,
`verify_references.py`, and deterministic index generation.

### What worked

The review gate failed the first near-copy candidate and passed the distinct
generated fixture only after a recorded visual review.

### What failed / still open

The first image's similarity failure was expected gate behavior; it was replaced,
not accepted and not used to relax the detector.

### Known risks

Perceptual similarity is a conservative release signal, not copyright analysis;
the mandatory review record remains part of the control.

### Next safe step

Add a vision-model adapter only when the repository has an approved, auditable
model endpoint; human review records are supported now.

### Files changed

`tools/{validate.py,generate_reference.py,verify_references.py}`,
`tests/test_tools.py`, generated indexes, and the visual fixture assets.

## 2026-07-31 - First-Party Source Provenance Path

### What changed

Added a fail-closed `first_party_source` origin: it bypasses only the
near-copy comparison and only when the referenced source declares
`rights: first_party`. Claim review and provenance remain mandatory.

### What was tested or reviewed

Added the no-rights failure fixture and ran the complete 32-test suite plus all
three release gates.

### What worked

The authorized Gen 1 source image passes without weakening protections for
generated art or unmarked sources.

### What failed / still open

No new failure.

### Known risks

Rights metadata is a declaration, so its truth remains the rights holder's
responsibility; the code only ensures it cannot be silently omitted.

### Next safe step

Require the same explicit declaration before adding any future direct-source
reference.

### Files changed

`tools/{validate.py,generate_reference.py,verify_references.py}` and
`tests/test_tools.py`.

## 2026-07-30 - PDF Renderer and Corpus Integrity Checks

### What changed

Added `tools/render_pdf.py`, a fail-closed Poppler wrapper that accepts a source, inclusive page range, and output prefix. It verifies every expected PNG and falls back from the broken runtime wrapper to its sibling direct executable. Added ledger v2 validation: `candidate_count` must equal disposition rows, and variant rows need foundation, learner decision, basis, method or policy, and tradeoff. Generated indexes now list absorbed variant names and bases below their foundation objects. Upgraded the Gaddis and Marvel unit ledgers to v2 and documented the format.

### What was tested or reviewed

Ran `python -m unittest discover -s tests -v` (26 tests pass), `python tools/validate.py` (54 objects pass), and `python tools/build_index.py` twice (first run changed three indexes; second changed zero). Ran the renderer against the Marvel PDF for pp. 44-51: the fallback selected the direct Poppler executable and produced all eight expected PNGs. Ran `git diff --check` before commit.

### What worked

The renderer no longer treats a zero exit status as evidence of a render: all requested files must exist, and a reused output prefix is rejected. Ledger v2 catches both count mismatches and a variant rationale hidden in generic prose. Variant alternatives are visible from generated navigation without creating duplicate object files.

### What failed / still open

The environment's `pdftoppm.cmd` wrapper reports a path error; the new helper detects its missing output and succeeds through the direct Poppler fallback. Legacy v1 ledgers remain readable but are not retroactively forced into v2, because TCPL Chapter 19 has a documented unresolved 11-versus-10 accounting discrepancy that must not be papered over.

### Known risks

The fallback path is a known layout of the available runtime; a different Poppler installation should use `PATH`, `PASS_PDFTOPPM`, or `--renderer`. A partial renderer failure retains its files and stops rather than mixing them with a fallback attempt. Ledger v2 migration is incremental until older units are revised.

### Next safe step

Use `tools/render_pdf.py` for the next visual source review. Migrate each legacy ledger when its unit is revised, and recover the missing TCPL Chapter 19 candidate before promoting that ledger to v2.

### Files changed

`tools/{render_pdf.py,validate.py,build_index.py}`, `tests/test_tools.py`, `docs/PASS/{PASS_RUN.md,PASS_LEDGER.md,PASS_LIBRARY.md}`, two unit ledgers, generated library indexes, tooling and corpus continuity docs, and `docs/worklogs/assignments.md`.

## 2026-07-30 - PASS Validator and Recursive SkillForge Indexes

### What changed

Added `tools/validate.py`, `tools/build_index.py`, and an explicit PyYAML
dependency. Replaced fixed two-level object placement with variable-depth
`library_path`, migrated all 17 current objects, and generated eight root-to-leaf
indexes. The root index declares the universal construction AP as the mandatory
load-first object and `metaskills` as the first package.

### What was tested or reviewed

Ran `python -m unittest tests/test_tools.py -v` (22 passing tests: a valid
fixture, one failing fixture for each numbered validator rule 1-20, and a
deterministic index-generation test). Ran `python tools/validate.py` against the
current library (17 objects, pass). Ran `python tools/build_index.py` twice; the
second run changed zero files. Ran `git diff --check`.

### What worked

Indexes derive all hierarchy from `library_path`; package membership is the first
path segment. The current library resolves to independent `metaskills`, `art`,
and `software_development` packages, without duplicate export trees.

### What failed / still open

The first validator run exposed an internal unhashable-record bug in its
cross-object deduplication. It was corrected before corpus validation. SkillForge
runtime enforcement of the bootstrap load order is outside this repository.

### Known risks

The bootstrap object id is intentionally explicit in the generator. Adding more
mandatory bootstrap objects requires a future contract change rather than a
silent automatic promotion.

### Next safe step

Run `python tools/validate.py` and `python tools/build_index.py` after every
processed source unit, then review any reported cross-package dependency before
shipping a selected package set.

### Files changed

`tools/validate.py`, `tools/build_index.py`, `tests/test_tools.py`,
`requirements.txt`, generated `library/**/INDEX.md`, schema and library contract
docs, migrated library objects, assignment log, and tooling worklog/decisions.

## 2026-07-29 - <short title>

### What changed

### What was tested or reviewed

### What worked

### What failed / still open

### Known risks

### Next safe step

### Files changed
