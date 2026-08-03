# Corpus Worklog

status: active
owner: docs/domains/corpus
last_reviewed: 2026-08-01

Newest entry first.

## 2026-08-01 - Dynamic Figure Drawing run scrapped

### What changed

Closed the Chapter 1 and Chapter 2 Hogarth assignments as failed. Removed the
source registry entry and ledger, every Hogarth-derived card and generated
reference from both runs, the Chapter 1 Body-Form Chain addition to
`PAT_build_gesture_into_clear_masses`, and the older Chapter 2 notation variant
from the iterative-construction AP. Restored the gesture-to-mass pattern to its
pre-Chapter-1 single-reference, no-variant state.

### What was tested or reviewed

Reviewed the cleanup against the exact file lists in commits `7554220`,
`03725a5`, and `b2f007c`, plus the untracked Chapter 2 draft set. The user
reviewed the curriculum and generated images and found the selection severely
limited, most images anatomically incorrect, and only four generated references
usable.

### What worked

Git history made the source-specific footprint separable from unrelated library
and workspace changes. The original first-party teaching reference on
`PAT_build_gesture_into_clear_masses` remains intact.

### What failed

The extraction rejected established artistic standards based on generic
technical judgments, underrepresented the source, and spent too much of the
user's weekly token budget generating references before curriculum quality and
anatomy had been proven. Visual provenance and similarity checks passed or were
being optimized while the more important instructional and anatomical quality
bar was not met.

### Known risks

Historical worklog entries describe the discarded attempts and are retained as
history; they are superseded by this entry and the corpus failure record. They
must not be used as evidence that any Hogarth object remains validated.

### Next safe step

Do not run another visual art source until
`PASS-PROC-VISUAL-ART-SOURCE-QUALITY` has a packet covering source conventions,
anatomy review, and an early token/cost checkpoint.

### Files changed

Removed the Hogarth source ledger, Chapter 1/2 cards and images, and both
absorbed variants; restored the original gesture foundation; regenerated
indexes; closed assignment state; updated corpus failure and continuity docs.

## 2026-08-01 - Dynamic Figure Drawing, Chapter 1

### What changed

Admitted Burne Hogarth's *Dynamic Figure Drawing* as
`burne_hogarth_dynamic_figure_drawing` after its full SHA-256 matched the expected
OCR payload, then processed u01, "The Definitive Body Forms" (printed pp. 9-44 /
physical PDF pp. 10-45). Added two patterns and one drill, and absorbed the
Body-Form Chain as a method-sequence variant of
`PAT_build_gesture_into_clear_masses`. Recorded three rejects rather than silently
dropping them: an unsupported limb-copying drill, the fixed breast-placement
formula, and the categorical sex-specific torso-ratio formula.

### What was tested or reviewed

Read the complete chapter twice by pairing per-page OCR with all 36 archived page
images. Inspected every page at overview resolution and candidate-bearing figures
at full resolution. Physical pages 20, 25, and 44 were read visually because
their weak text layers cover image plates. Generated and visually reviewed four
original teaching references; rejected one ambiguous limb draft, one hand/foot
draft with an opposed-looking toe, and one torso draft whose rear view read too
much like the front. `python tools/validate.py` passes 217 objects;
`python tools/verify_grounding.py --source burne_hogarth_dynamic_figure_drawing`
passes 1/1 processed units; `python tools/verify_references.py` passes every
reference; `python tools/build_index.py` generated 45 indexes with 4 changed.

### What worked

The decision-versus-method check kept the overall mannequin construction as a
variant of the live gesture-to-mass foundation while allowing genuinely missing
limb, extremity, and torso-turn decisions to become new objects. The visual gate
also did real work: all three rejected image drafts were corrected before their
claims were marked reviewed. The chapter's two narrow anatomical formulas remain
visible in the ledger with exact methods and technical durability tests.

### What failed / still open

No final schema, grounding, reference, index, or whitespace gate failed. The PDF
render helper emitted its already-known stale wrapper warning after the direct
CropBox renderer wrote the requested pages; the complete archive set was used for
the receipt. Chapters 2-6 remain queued and were not processed. The source was not
reconciled and its payload was not retired.

### Known risks

The S/B limb rhythms are simplifying construction controls, not literal contour
templates; the card preserves that caveat. The body-form variant favors rounded
attachment over explicit planar faces. The breast and torso-ratio formulas may be
useful as stylized design choices, but would become misleading if retrieved as
universal anatomy, which is why they remain rejects rather than cards.

### Next safe step

Stop for review. If the user resumes the source, process u02, "Figure Notation in
Deep Space" (printed pp. 45-64 / physical PDF pp. 46-65), as its own run and
retrieve first against the existing deep-space-notation variant and the four u01
construction contributions.

### Files changed

Hogarth source ledger, u01 ledger and persistent visual-comparison evidence;
three new figure-construction objects; one revised foundation; four generated
references with provenance; generated indexes; corpus continuity docs; and the
assignment log.

## 2026-08-01 - Dynamic Figure Drawing OCR readiness check

### What changed

Rechecked the user-supplied OCR payload under the new paired text-and-image
procedure. No source was admitted and no unit or library object changed.

### What was tested or reviewed

Preflight passed: 177 PDF pages, 167 meaningful-text pages, 164 fully usable
pages, 150,827 alphanumeric characters, working CropBox rendering, and 177
aligned archive images. Visually reviewed all 13 weak physical pages.

### What worked

Twelve weak pages are non-prose covers, titles, or full-page plates. The only
instructional OCR miss is physical page 117 / printed page 116, whose two short
paragraphs are legible in the page image.

### What failed / still open

Printed page 116 must be read from the image and grounded with `image:` evidence
when its unit runs. Current master contains no Hogarth registry row despite an
older worklog describing an unmerged attempt.

### Known risks

The OCR is a reading aid, not visual evidence; the art remains primary. Numeric
archive alignment still does not replace unit-level visual judgment.

### Next safe step

After the tooling branch merges, hash-check and admit the OCR PDF as a fresh
source, then process one chapter-sized unit per run.

### Files changed

Corpus worklog/next steps only; no source ledger or library object changed.

## 2026-08-01 - Art-book run readiness made explicit

### What changed

Changed the run procedure so PDFs are preflighted before admission and art books
are read from paired per-page OCR text and images. Added hard gates for a usable
text layer, a vision-capable model, and renderer or page-image access. Documented
overview inspection of every bounded page plus full-resolution review of pages
that ground candidates.

### What was tested or reviewed

Reviewed the policy against the real *Dynamic Figure Drawing* PDF and image
archive. The PDF has 177 image-only pages; the archive has 177 aligned,
contiguously numbered, decodable images. The new preflight blocks only on OCR.

### What worked

The workflow avoids paying vision tokens to transcribe prose while preserving
the art as primary evidence. The image archive can supply cleaner page evidence
than repeated PDF renders without weakening receipt coverage.

### What failed / still open

The current PDF is not OCR-readable. The OCR-updated payload has not yet been
supplied or identity-reviewed, so no Hogarth unit was processed in this change.

### Known risks

First/middle/last archive mapping must still be visually confirmed; numeric
alignment alone cannot detect a consistently shifted or incorrectly assembled
archive. A decoded image is availability evidence, not comprehension evidence.

### Next safe step

Run preflight on the OCR copy, compare its page count and sample mappings with
the archive, then resume one Hogarth unit under the paired reading procedure.

### Files changed

PASS run/grounding/ledger docs, corpus decisions/worklog, tooling continuity,
and `docs/worklogs/assignments.md`; no library object or source ledger changed.

## 2026-08-01 - The Programmer's Brain, Ch.1-2: review, repair, and merge

### What changed

Reviewed Codex's `codex/programmers-brain-ch1-2` run and merged it to master.
Four repairs. Added `v_cognition_visually_distinct_identifiers` to
`PAT_use_descriptive_names` (u02 p. 17) — Hermans deliberately obfuscates a Java
routine with `b` and `l` iterators and notes `l` reads as `1`, a perceptual naming
constraint the gcbc foundation covers nowhere; it was the run's one genuine
extraction gap. Added the p. 25 recall-order step to
`DRILL_reproduce_code_to_diagnose_knowledge`, whose locator already claimed that
page while the body ignored it. Recorded two deliberate `reject` rows in u02
(comment-as-scaffold, name-your-reading-goal) that were previously unaccounted
for. Fixed a missing blank line in `PAT_comment_why_not_what` and
`PAT_make_code_readable` that merged variant prose into the foundation paragraph,
and reordered both so the foundation's own rationale precedes its variants.
u02 `candidate_count` 11 → 14.

### What was tested or reviewed

Re-ran both gates independently rather than trusting the run report:
`validate.py` 214 objects, `verify_grounding.py --source programmers_brain` 2/2,
32 tooling tests, `build_index.py` deterministic (second pass changes zero files).
Verified **all seven** reading-receipt quotes verbatim against the PDF via pypdf,
not a spot sample; `pdf_page_offset: 26` independently confirmed at both chapter
openings. Read both chapters in full to test yield rather than accept it.

### What worked

The disposition audit is the result worth keeping: all ten of Codex's dispositions
were upheld. No under-linking, no over-forcing — the failure mode this lane was
supposed to expose did not appear. Codex split the beacons material into a
writer-side variant *and* a reader-side new pattern rather than forcing it one way,
which is the `decisions.md` 2026-07-30 recovery model applied unprompted. Variant
attachment rate is the adaptability signal: 23% here (3 of 13) against 2.4% for
Effective C++ (2 of 82), exactly as `next_steps.md` predicted craft-core material
would behave against gcbc foundations.

### What failed / still open

The branch was based at `31f1c88` while master had moved to `f9c9413`, so
`git diff master..branch` displayed master's two newer commits as deletions —
including the rule protecting `tmp/worktrees/`. Codex authored none of them; no
branch commit touches those files. Merged rather than rebased, which preserved
both sides. **This is a recurring hazard when assistants run concurrently and is
not a defect in the run itself** — inspect `git merge-base` before reading a
cross-branch diff as authored intent.

### Known risks

Context-wall degradation in u02 is real but subtle: the cards are full-strength
(comparable length, receipt reaching p. 31), yet every under-extraction miss and
both formatting defects landed in u02, clustered in the late writer-side stretch.
It shows up as misses and sloppy finishing, not thin cards. Supports the existing
one-unit-per-chat decision.

### Next safe step

Resume at u03, one unit per chat. Source stays active at 2/13; not reconciled,
payload not retired.

### Files changed

`library/software-engineering/foundations/readability/` (three cards + INDEX),
`library/software-engineering/foundations/code-comprehension/DRILL_reproduce_code_to_diagnose_knowledge.md`,
`ledger/programmers_brain/units/u02.md`, `docs/worklogs/assignments.md`,
`docs/domains/corpus/next_steps.md`, and this worklog.

## 2026-08-01 - The Programmer's Brain, Chapter 2 (review tranche complete)

### What changed

Processed u02, "Speed reading for code" (printed pp. 13-32 / PDF pp. 39-58).
Added three patterns and three drills to the code-comprehension foundation topic:
semantic chunking, reader-knowledge scope calibration, beacon-based hypothesis
testing, a code-at-a-glance drill, a beacon inventory, and timed code reproduction
for knowledge-gap diagnosis. Absorbed three grounded variants into gcbc foundations:
`v_cognition_design_patterns_as_chunks` and `v_cognition_semantic_beacons` in
`PAT_make_code_readable`, plus `v_cognition_high_level_comments_as_chunks` in
`PAT_comment_why_not_what`. Rejected the non-code symbol demonstration and raw
memory-capacity facts as context already carried by the usable objects. The requested
tranche is now 2/13 units and stops here without reconciliation or retirement.

### What was tested or reviewed

Read the full chapter twice. Rendered all twenty pages with
`python tools/render_pdf.py ... --pages 39-58 --output-prefix
tmp/pdfs/programmers_brain/u02/page`; the resolved renderer was
`C:\Users\Methuselas\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdftoppm.exe`.
Inspected every page, including the recall overlays, chess and program-memory
experiments, graphs, letter and keyword layouts, tree traversal, and exercises.
Retrieved about five neighbours per candidate from gcbc readability, abstraction,
modularity, contracts, and code-quality foundations, plus u01's new topic. All gates
pass: `python tools/validate.py` (214 objects), `python
tools/verify_grounding.py --source programmers_brain --pdftotext "C:\Program
Files\Git\mingw64\bin\pdftotext.exe"` (2/2 processed units), and `python
tools/build_index.py` (45 indexes, 5 changed; second run 0 changed). `git diff
--check` passes.

### What worked

The decision-versus-method check prevented three duplicate cards. Known design
patterns and semantic beacons change how the existing readability decision is
implemented, while high-level functional comments add a precise chunking emphasis
to the existing comment policy. The reader-side actions remain new because they
change how someone investigates code rather than how an author presents it.

### What failed / still open

No object, grounding, or index gate failed. The renderer repeated the known
fallback-wrapper warning after the direct renderer wrote all twenty expected PNGs;
the complete output set was enumerated and inspected. The first scratch-removal
attempt lacked filesystem permission; an approved retry against the exact resolved
run directory removed all u01-u02 PNGs. u03-u13 are intentionally unprocessed and
remain queued.

### Known risks

Design patterns aid chunking only when they fit and the reader recognizes them;
the absorbed variant explicitly preserves that constraint. Beacons can also anchor
a wrong hypothesis, so the reader pattern requires later evidence to confirm or
refute the first interpretation. Chapter 13 may deepen the onboarding-scope pattern
and should reconcile against it instead of duplicating it.

### Next safe step

Stop for review. If the source is resumed after review, process u03, "How to learn
programming syntax quickly" (printed pp. 33-45), as its own unit and retrieve against
the u01-u02 code-comprehension foundations first.

### Files changed

`ledger/REGISTRY.md`, `ledger/programmers_brain/{UNITS.md,units/u02.md}`, six new
code-comprehension objects, two revised gcbc readability foundations, generated
indexes, `docs/worklogs/assignments.md`, this worklog, and
`docs/domains/corpus/next_steps.md`.

## 2026-08-01 - The Programmer's Brain, Chapter 1

### What changed

Admitted Felienne Hermans's *The Programmer's Brain* as `programmers_brain` after
its SHA-256 was absent from the registry, scaffolded its 13 chapter-native units,
and processed u01, "Decoding your confusion while coding" (printed pp. 3-12 /
PDF pp. 29-38). Added three patterns and one drill under
`software-engineering/foundations/code-comprehension`: diagnose whether confusion
comes from missing knowledge, missing information, or processing overload;
externalize intermediate trace state; verify familiar-looking tokens; and audit
the cognitive processes used while reading code. One explanatory-model candidate
was rejected as context rather than a separate craft action.

### What was tested or reviewed

Read the full chapter twice. Rendered all ten pages with
`python tools/render_pdf.py ... --pages 29-38 --output-prefix
tmp/pdfs/programmers_brain/u01/page`; the resolved renderer was
`C:\Users\Methuselas\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdftoppm.exe`.
Inspected every page, including both figures, the exercise table, and the code
listings. Compared each candidate with nearby gcbc readability, abstraction,
contracts, and avoiding-surprises foundations. `python tools/validate.py` passes
208 objects. `python tools/verify_grounding.py --source programmers_brain
--pdftotext "C:\Program Files\Git\mingw64\bin\pdftotext.exe"` passes the
processed unit. `python tools/build_index.py` generated 45 indexes (4 changed),
and a second run changed 0. `git diff --check` passes.

### What worked

Holding the behavior constant across APL, Java, and BASIC made the three sources
of confusion separable without turning the cognitive model into a summary card.
Neighbour retrieval also kept the placement honest: these are reader-side
decisions, while the closest gcbc cards change how an author writes code, so none
was absorbed as a superficial variant.

### What failed / still open

The grounding gate initially could not launch `pdftotext` because it is not on
this runtime's PATH; the existing Git installation supplies a working executable,
and the gate passed with that explicit path. The first index-generation attempt
was denied write access inside the isolated worktree; rerunning the same command
with the required workspace approval succeeded. The renderer repeated the known
fallback-wrapper warning after the direct renderer had written all ten expected
PNGs; every expected file was enumerated and inspected.

### Known risks

Chapter 1 introduces remedies that later chapters develop in more depth. The
cards retain only actions this chapter actually demonstrates: navigate for hidden
information, externalize a trace, verify expected tokens, and audit the source of
confusion. Later units may add grounded variants or replace thin parts rather than
duplicating them.

### Next safe step

Process u02, "Speed reading for code" (printed pp. 13-32 / PDF pp. 39-58), as
the second and final review unit. Retrieve its chunking, comments, design-pattern,
and beacon candidates against the gcbc readability and abstraction foundations.

### Files changed

`ledger/REGISTRY.md`, `ledger/programmers_brain/{SOURCE.md,UNITS.md,units/u01.md}`,
four new objects under `library/software-engineering/foundations/code-comprehension/`,
generated indexes, `docs/worklogs/assignments.md`, this worklog, and
`docs/domains/corpus/next_steps.md`.

## 2026-08-01 - Effective C++, 3rd ed., Chapter 9 + source reconciliation (SOURCE COMPLETE)

### What changed

Processed the final unit u09, Chapter 9 "Miscellany" (Items 53-55, printed pp. 262-272 / PDF pp. 283-293) and reconciled the source. As anticipated, this was a low-yield unit: 0 new objects, 2 variants absorbed into gcbc foundations, 2 rejects. Item 53 (heed compiler warnings) became variant `v_cpp_warnings_implementation_dependent` in `PAT_treat_compiler_warnings_as_potential_bugs`; the kernel of Item 54 (know the standard library/TR1) became variant `v_cpp_know_standard_library_and_tr1` in `PAT_reuse_before_reinventing`. Item 54's component inventory and all of Item 55 (Boost) were rejected as reference/awareness material. The source is now complete: 9/9 units, 80 objects (64 patterns, 16 drills), 2 absorbed variants.

### What was tested or reviewed

Read the full chapter, including re-reading the cut-off tail of Item 55 to find the true book-body end (printed p. 272; Appendix A follows) — corrected u09 to pp. 262-272. §6 retrieval read both target gcbc foundations before choosing the variant disposition. All gates pass: `python tools/validate.py` (204 objects), `python tools/verify_grounding.py --source effective_cpp_3e` (all nine units grounded), `python tools/build_index.py`. Grounding first failed on one u09 quote attributed to the wrong page (the tr1::function line is on p. 266, not 265); replaced with a p. 265 quote and re-verified.

### What worked

Chapter 9 is the clearest demonstration yet of PASS's cross-book merge: rather than manufacture thin C++ cards for advice gcbc already covers, the two real skills attached as C++ variants to the language-agnostic gcbc foundations, and the two reference-only Items were honestly rejected with grounding. Low yield is a real, correct result, not a failure.

### What failed / still open

Nothing outstanding. One quote-page correction (as above). Payload retirement deliberately deferred (see below).

### Known risks

Payload retirement was NOT performed: the book lives in the user's curated `sources/Programming/C++/` shelf (the subject of the reading-order deliverable), so moving it to `trash/` would undermine that shelf. The sha256 in REGISTRY remains the duplicate guard, so the source will not be reprocessed regardless of location. Retire only on user request. Several Effective C++ 3rd cards use pre-C++11 idioms (auto_ptr, tr1::*, private-undefined copy suppression, manual RVO reasoning); these are correct for the source and are the intended targets for `replace`/variant absorption when *Effective Modern C++* is run.

### Next safe step

Source complete. Select the next source. The natural follow-on is *Effective Modern C++*, which will exercise the `replace` disposition against this lane for the first time (move semantics, `= delete`, `std::unique_ptr`/`std::shared_ptr`, `std::function`/`std::bind`).

### Files changed

`ledger/REGISTRY.md` (row to complete), `ledger/effective_cpp_3e/{SOURCE.md (summary + status),UNITS.md,units/u09.md}`, two revised gcbc foundations (`PAT_treat_compiler_warnings_as_potential_bugs`, `PAT_reuse_before_reinventing`) with absorbed variants, generated indexes, this worklog, and `docs/domains/corpus/next_steps.md`.

## 2026-08-01 - Effective C++, 3rd ed., Chapter 8

### What changed

Processed unit u08, Chapter 8 "Customizing new and delete" (Items 49-52). Added 8 objects — 6 patterns + 2 drills — all under the existing `memory-management` topic in the `software-engineering/languages/cpp` lane, alongside the Ch.3 new/delete-form patterns. Items 49 and 52 each split into two patterns. Library 196 to 204; source now 8/9 units, 80 objects.

### What was tested or reviewed

Read the chapter from `pdftotext`. Boundary correction: the initial UNITS.md placeholder said pp. 239-259, but Item 52 actually runs to printed p. 261 (Chapter 9 begins printed p. 262 / PDF p. 283). The first extraction (PDF 260-280) cut off Item 52's tail, so it was extracted separately (PDF 280-282) and read in full before extraction — fail-closed on a partial unit. Corrected u08 to pp. 239-261 and u09 to pp. 262-269. All gates pass first try: `python tools/validate.py` (204 objects), `python tools/verify_grounding.py --source effective_cpp_3e` (all eight units grounded; u08 receipt is 7 verbatim mid-page quotes spanning printed pp. 241-261), `python tools/build_index.py` (44 indexes, 5 changed).

### What worked

The chapter's four items yielded a clean split: new-handler behavior plus the CRTP class-specific-handler technique (Item 49); when to replace new/delete (Item 50); the writing conventions (Item 51); and the placement-new/placement-delete pairing plus the standard-form-hiding fix (Item 52). Cross-links tie back to Ch.3 new/delete forms, Ch.2 virtual destructors (size correctness), Ch.5 exception safety (placement-new leak), and Ch.6 name hiding (standard-form hiding). All landed in the existing memory-management topic, so Ch.3 and Ch.8 memory material now sits together.

### What failed / still open

Nothing failed. The only wrinkle was the unit-boundary correction, caught by re-reading the cut-off tail rather than extracting from the partial page — the fail-closed reading discipline working as intended.

### Known risks

Item 49's class-specific handler uses the CRTP with tr1-era idioms; the technique is timeless. Chapter 9 (u09) is the last unit and is expected to be low-yield: Item 53 (heed compiler warnings) is a real skill, but Items 54 (standard library / TR1) and 55 (Boost) are largely awareness/reference and may be recorded partly as empty context. Source reconciliation (PASS_RUN §8) is due after u09.

### Next safe step

Run Chapter 9 "Miscellany" (Items 53-55, printed pp. 262-269 / PDF pp. 283-290), the final unit, then reconcile the source: fix any cross_links, write the SOURCE.md summary, set the REGISTRY row to complete, and retire the payload to trash/.

### Files changed

`ledger/REGISTRY.md`, `ledger/effective_cpp_3e/{UNITS.md,units/u08.md}`, 8 new objects under `library/software-engineering/languages/cpp/memory-management/`, generated indexes, this worklog, and `docs/domains/corpus/next_steps.md`.

## 2026-08-01 - Effective C++, 3rd ed., Chapter 7

### What changed

Processed unit u07, Chapter 7 "Templates and Generic Programming" (Items 41-48, printed pp. 199-238 / PDF pp. 220-259). Added 10 objects — 8 patterns + 2 drills — across three topics in the `software-engineering/languages/cpp` lane: `templates` (Items 41-46 + the base-class-name drill), `traits` (Item 47 + the dispatch drill), and `metaprogramming` (Item 48). Library 186 to 196; source now 7/9 units, 72 objects.

### What was tested or reviewed

Read the full chapter (87 KB) from `pdftotext` of PDF pp. 220-259, across two Read passes. Second read against the candidate list. All gates pass first try: `python tools/validate.py` (196 objects), `python tools/verify_grounding.py --source effective_cpp_3e` (all seven units grounded; u07 receipt is 8 verbatim mid-page quotes spanning printed pp. 201-237), `python tools/build_index.py` (44 indexes, 7 changed).

### What worked

This is the most template-syntax-dense chapter, so body prose was written deliberately without any angle-bracket template syntax (the validator's rule-8 placeholder check reads `<...>` as an unreplaced token). Referring to instantiations in words ("a SmartPtr instantiated on U", "Factorial of n-1", "iterator_traits") kept every card clean and passed validation on the first attempt. Cross-links tie back across the book: Item 43 to Ch.6 name-hiding, Item 44 to Ch.6 private inheritance and Ch.5 inlining, Item 45 to Ch.2 compiler-generated members, Item 46 to Ch.4 non-member operators, Item 48 to Ch.1 enum hack; traits and metaprogramming cross-link to each other.

### What failed / still open

Nothing failed. The angle-bracket discipline (a lesson first learned in Ch.1) mattered most here and held throughout.

### Known risks

Items 45-47 use tr1::shared_ptr / tr1::function and TR1 traits names; the timeless techniques (member templates, friend template operators, traits dispatch, TMP) are extracted, with std-namespace and modern-trait naming deferred to *Effective Modern C++*. Chapters 8-9 page ranges in UNITS.md remain approximate until claimed.

### Next safe step

Run Chapter 8 "Customizing new and delete" (Items 49-52, printed pp. 239-259 / PDF pp. 260-280) — the new-handler, replacing global and class new/delete, and the placement-new/placement-delete pairing convention.

### Files changed

`ledger/REGISTRY.md`, `ledger/effective_cpp_3e/{UNITS.md,units/u07.md}`, 10 new objects under `library/software-engineering/languages/cpp/{templates,traits,metaprogramming}/`, generated indexes, this worklog, and `docs/domains/corpus/next_steps.md`.

## 2026-08-01 - Effective C++, 3rd ed., Chapter 6

### What changed

Processed unit u06, Chapter 6 "Inheritance and Object-Oriented Design" (Items 32-40, printed pp. 149-198 / PDF pp. 170-219) — the largest chapter at nine items. Added 12 objects — 10 patterns + 2 drills — across two topics in the `software-engineering/languages/cpp` lane: `inheritance` (Items 32, 33, 38, 39, 40 + the broken-is-a drill) and `virtual-functions` (Items 34, 35, 36, 37 + the NVI drill). Item 35 split into two patterns (NVI idiom; Strategy). Library 174 to 186; source now 6/9 units, 62 objects.

### What was tested or reviewed

Read the full chapter (103 KB) from `pdftotext` of PDF pp. 170-219, across two Read passes. Second read against the candidate list. All gates pass first try: `python tools/validate.py` (186 objects), `python tools/verify_grounding.py --source effective_cpp_3e` (all six units grounded; u06 receipt is 9 verbatim quotes spanning printed pp. 151-197, all deliberately mid-page after the Ch.5 straddle lesson), `python tools/build_index.py` (41 indexes, 6 changed).

### What worked

Strong cross-book and cross-chapter linking: Item 32 (public inheritance is is-a) and Item 38 (composition) both link to gcbc's `PAT_prefer_composition_over_inheritance`; Item 36 links to the Ch.2 virtual-destructor pattern; Item 40 links to the Ch.5 compilation-dependencies pattern (Interface class). Item 35 legitimately produced two patterns (NVI and Strategy), and Item 37's fix reuses the NVI pattern from Item 35 via cross-link. The is-a / has-a / is-implemented-in-terms-of trio (Items 32/38/39) now sits together in the inheritance topic.

### What failed / still open

Nothing failed this run. Mid-page quote selection (the Ch.5 lesson) held — grounding passed on the first attempt.

### Known risks

Item 35 uses tr1::function and tr1::bind; the timeless Strategy/NVI design is extracted, with the modern std::function/std::bind naming deferred to *Effective Modern C++*. Chapters 7-9 page ranges in UNITS.md remain approximate until claimed; Chapter 7 is the Template C++ sublanguage and may surface more genuinely specialist material.

### Next safe step

Run Chapter 7 "Templates and Generic Programming" (Items 41-48, printed pp. 199-238 / PDF pp. 220-259) — implicit interfaces and compile-time polymorphism, typename, dependent names, factoring template code, member function templates, traits classes, and template metaprogramming.

### Files changed

`ledger/REGISTRY.md`, `ledger/effective_cpp_3e/{UNITS.md,units/u06.md}`, 12 new objects under `library/software-engineering/languages/cpp/{inheritance,virtual-functions}/`, generated indexes, this worklog, and `docs/domains/corpus/next_steps.md`.

## 2026-07-31 - Effective C++, 3rd ed., Chapter 5

### What changed

Processed unit u05, Chapter 5 "Implementations" (Items 26-31, printed pp. 113-148 / PDF pp. 134-169). Added 10 objects — 8 patterns + 2 drills — across five new topics in the `software-engineering/languages/cpp` lane (`variable-definitions`, `casting`, `exception-safety`, `inlining`, `compilation-dependencies`) plus the existing `encapsulation` topic (Item 28, returning handles). Two items yielded two patterns each: Item 27 (minimize/prefer C++ casts; avoid dynamic_cast) and Item 29 (offer a guarantee; copy-and-swap for the strong guarantee). Library 164 to 174; source now 5/9 units, 50 objects.

### What was tested or reviewed

Read the full chapter from `pdftotext` of PDF pp. 134-169. Second read against the candidate list. `python tools/validate.py` passes (174 objects) and `python tools/build_index.py` regenerates (39 indexes, 10 changed). Grounding initially FAILED on one u05 receipt quote and was fixed (see below); `python tools/verify_grounding.py --source effective_cpp_3e` now passes all five units.

### What worked

Item 28 slotted into the existing `encapsulation` topic alongside the Ch.4 private-data and non-member patterns — the returning-handles rule is the same encapsulation concern at implementation time. Item 29 cross-links to the Ch.3 RAII foundation and the Ch.4 swap pattern (copy-and-swap depends on a non-throwing swap), and Item 31 cross-links to gcbc's `PAT_expose_clean_api_hide_implementation`. Splitting Items 27 and 29 into two patterns each kept one decision per card.

### What failed / still open

The grounding gate rejected one receipt quote: "when multiple inheritance is in use, it happens virtually all the time" — the words "when multiple" sit on printed p.118, so the quote straddled the page break and was not found on p.119. Replaced it with a quote wholly on p.119 ("casting object addresses to char* pointers ... yields undefined behavior") and grounding passed. This is the gate working as intended; lesson: pick receipt quotes from the middle of a page, not adjacent to the running-header boundary.

### Known risks

Item 29's examples use tr1::shared_ptr and the pre-C++11 pimpl copy-and-swap; the timeless exception-safety guarantees are extracted, with move-based refinements deferred to *Effective Modern C++*. Chapters 6-9 page ranges in UNITS.md remain approximate until claimed.

### Next safe step

Run Chapter 6 "Inheritance and Object-Oriented Design" (Items 32-40, printed pp. 149-198 / PDF pp. 170-219) — the largest remaining chapter, nine items on is-a, name hiding, interface/implementation inheritance, alternatives to virtual functions, and private/multiple inheritance.

### Files changed

`ledger/REGISTRY.md`, `ledger/effective_cpp_3e/{UNITS.md,units/u05.md}`, 10 new objects under `library/software-engineering/languages/cpp/{variable-definitions,casting,encapsulation,exception-safety,inlining,compilation-dependencies}/`, generated indexes, this worklog, and `docs/domains/corpus/next_steps.md`.

## 2026-07-31 - Effective C++, 3rd ed., Chapter 4

### What changed

Processed unit u04, Chapter 4 "Designs and Declarations" (Items 18-25, printed pp. 78-112 / PDF pp. 99-133; range refined by locating Chapter 5 at PDF p. 134). Added 10 objects — 8 patterns + 2 drills — across five new topics in the `software-engineering/languages/cpp` lane: `interface-design` (Items 18, 19 + the redesign drill), `parameter-passing` (Items 20, 21), `encapsulation` (Items 22, 23), `operators` (Item 24), and `swap` (Item 25 + the swap drill). Library 154 to 164; source now 4/9 units, 40 objects.

### What was tested or reviewed

Read the full chapter from `pdftotext` of PDF pp. 99-133. Second read against the candidate list. All gates pass first try: `python tools/validate.py` (164 objects), `python tools/verify_grounding.py --source effective_cpp_3e` (all four units grounded; u04 receipt is 8 verbatim quotes spanning printed pp. 79-111), `python tools/build_index.py` (34 indexes, 9 changed).

### What worked

Item 18 "make interfaces hard to misuse" is the cleanest cross-book link yet: it is a direct C++ specialization of gcbc's `PAT_make_code_hard_to_misuse`, so its `foundation_object_id` points there. The other items are one decision each: class-as-type design (19), pass-by-reference-to-const (20), return-by-value for new objects (21), private data members (22), non-member non-friend functions (23), non-member operators for all-argument conversion (24), and the full non-throwing swap recipe (25). Item 21 cross-links to the Ch.1 return-by-const-value and Ch.1 local-statics patterns; Item 25 cross-links to Ch.2 self-assignment (swap is a self-assignment tool).

### What failed / still open

Nothing failed this run.

### Known risks

Items 20/21 and 24/25 lean on pre-C++11 idioms in spots (e.g., manual RVO reasoning, tr1::shared_ptr in Item 18's factory example). The cards extract the timeless design rules; move-semantics refinements (move constructors changing the return-by-value calculus, std::move) belong to *Effective Modern C++* and should be absorbed there. Chapters 5-9 page ranges in UNITS.md remain approximate until claimed.

### Next safe step

Run Chapter 5 "Implementations" (Items 26-31, printed pp. 113-148 / PDF pp. 134-169). It covers postponing variable definitions, minimizing casting, exception-safe code, inlining, and minimizing compilation dependencies.

### Files changed

`ledger/REGISTRY.md`, `ledger/effective_cpp_3e/{UNITS.md,units/u04.md}`, 10 new objects under `library/software-engineering/languages/cpp/{interface-design,parameter-passing,encapsulation,operators,swap}/`, generated indexes, this worklog, and `docs/domains/corpus/next_steps.md`.

## 2026-07-31 - Effective C++, 3rd ed., Chapter 3

### What changed

Processed unit u03, Chapter 3 "Resource Management" (Items 13-17, printed pp. 61-77 / PDF pp. 82-98; range refined from the approximate UNITS.md placeholder by locating Chapter 4 at PDF p. 99). Added 7 objects — 5 patterns + 2 drills — under two new topics in the `software-engineering/languages/cpp` lane: `resource-management` (Items 13, 14, 15 + both drills) and `memory-management` (Items 16, 17). Library 147 to 154; source now 3/9 units, 30 objects.

### What was tested or reviewed

Read the full chapter from `pdftotext` of PDF pp. 82-98 (clean text and code). Second read against the candidate list. All gates pass first try: `python tools/validate.py` (154 objects), `python tools/verify_grounding.py --source effective_cpp_3e` (all three units grounded; u03 receipt is 6 verbatim quotes spanning printed pp. 63-77), `python tools/build_index.py` (29 indexes, 6 changed).

### What worked

The five Items are one decision each: RAII as the core resource discipline (Item 13); deliberate copy semantics for hand-written RAII classes (Item 14); providing raw-resource access, explicit vs implicit (Item 15); matching new/delete forms (Item 16); and storing newed objects in a smart pointer in a standalone statement to avoid an evaluation-order leak (Item 17). Item 13 is the RAII foundation the copy-behavior and raw-access Items build on. Item 14 cross-links to Ch.2's `PAT_suppress_copying_with_private_undefined_or_uncopyable` (the prohibit-copying option), a clean intra-lane link.

### What failed / still open

Nothing failed this run (the Ch.2 drill frontmatter lesson held — both drills carried `foundation_object_id: none`).

### Known risks

Items 13-15 use the pre-C++11 auto_ptr and tr1::shared_ptr. The cards extract the timeless RAII/copy/raw-access skills and name auto_ptr/shared_ptr only as the source's examples; the modern std::unique_ptr/std::shared_ptr successors belong to *Effective Modern C++* and should be absorbed as variants/replacements there, not invented now (same policy as the Ch.2 `= delete` note). Chapters 4-9 page ranges in UNITS.md remain approximate until claimed.

### Next safe step

Run Chapter 4 "Designs and Declarations" (Items 18-25). Item 18 begins printed p. 78 / PDF p. 99; refine the endpoint at claim by locating Chapter 5 "Implementations". It is the closest merge test against the gcbc abstraction and contracts foundations.

### Files changed

`ledger/REGISTRY.md`, `ledger/effective_cpp_3e/{UNITS.md,units/u03.md}`, 7 new objects under `library/software-engineering/languages/cpp/{resource-management,memory-management}/`, generated indexes, this worklog, and `docs/domains/corpus/next_steps.md`.

## 2026-07-31 - Effective C++, 3rd ed., Chapter 2

### What changed

Processed unit u02, Chapter 2 "Constructors, Destructors, and Assignment Operators" (Items 5-12, printed pp. 34-60 / PDF pp. 55-81). Added 11 objects — 9 patterns + 2 drills — under three new topics in the `software-engineering/languages/cpp` lane: `copy-control` (Items 5, 6, 10, 11, 12, plus both drills), `destructors` (Items 7, 8), and `construction` (Item 9). Library goes from 136 to 147 objects; the source is now 2/9 units, 23 objects.

### What was tested or reviewed

Read the full chapter from `pdftotext` of PDF pp. 55-81 (clean text and code, no figures). Second read against the candidate list. All gates pass: `python tools/validate.py` (147 objects), `python tools/verify_grounding.py --source effective_cpp_3e` (both u01 and u02 grounded; u02 receipt is 7 verbatim quotes spanning printed pp. 35-59, verified against the payload), `python tools/build_index.py` (27 indexes, 7 changed).

### What worked

The eight Items split cleanly into distinct decisions: know the generated special members and when they are refused (Item 5); suppress copying via private-undefined or an Uncopyable base (Item 6); virtual destructors for polymorphic bases only (Item 7); never let exceptions escape a destructor (Item 8); no virtual calls in ctor/dtor (Item 9); return *this from assignment (Item 10); self-assignment safety (Item 11); and copy-all-parts plus don't-implement-one-copying-function-via-the-other (Item 12, two patterns). Item 12 legitimately produced two patterns from one Item. Cross-links reach gcbc foundations where they fit: Item 6 to `PAT_make_code_hard_to_misuse`, Item 8 to `PAT_dont_hide_errors`.

### What failed / still open

Two drills initially failed validation for a missing `foundation_object_id` key (I included `specialization_axis` but omitted `foundation_object_id: none`). Fixed. Note for future drills: drills carry the full common frontmatter plus `target_skill`; `foundation_object_id` is required even when `none`.

### Known risks

Item 6 documents the pre-C++11 private-undefined/Uncopyable idiom; its modern successor `= delete` belongs to *Effective Modern C++* and should be absorbed as a variant/replacement when that source is run, not invented now. Chapter 3+ page ranges in UNITS.md remain approximate until claimed.

### Next safe step

Run Chapter 3 "Resource Management" (Items 13-17, printed pp. 61-85 approx). It introduces RAII and smart pointers — the closest merge test against the new copy-control and destructors topics and the gcbc resource/immutability foundations.

### Files changed

`ledger/REGISTRY.md`, `ledger/effective_cpp_3e/{UNITS.md,units/u02.md}`, 11 new objects under `library/software-engineering/languages/cpp/{copy-control,destructors,construction}/`, generated indexes, this worklog, and `docs/domains/corpus/next_steps.md`.

## 2026-07-31 - software-engineering package: add foundations/ lane

### What changed

Structural placement fix. Adding the `languages/cpp` lane (Effective C++ Ch.1) left the package asymmetric: the 122 gcbc pillar objects sat at the package root (`software-engineering/<pillar>/`) while the C++ cards were nested under `languages/`. Moved all 122 gcbc objects into a `foundations/` lane — `software-engineering/foundations/<pillar>/` — mirroring the reference structure in `PASS_LIBRARY.md` ("Universal foundation structure": `software_development/foundations/error_handling/` alongside `software_development/languages/python/...`). The package now has two parallel lanes, `foundations/` and `languages/cpp/`.

### What was tested or reviewed

`library_path` for the 122 pillar objects was edited programmatically (insert `foundations` as the second segment; scoped to the ten pillar folders, never `languages/`), then files moved with `git mv` to match. `object_id`s were untouched, so every `cross_link` and `foundation_object_id` — including the new cpp→gcbc foundation links — still resolves. All gates pass: `python tools/validate.py` (136 objects), `python tools/build_index.py` (24 indexes, 12 changed), `python tools/verify_grounding.py --source effective_cpp_3e` (still grounded; locators unchanged).

### What worked

Because placement is `library_path` frontmatter and links are keyed on `object_id`, the move was mechanical and non-breaking — the same property that made the cpp relocation clean. Root index still lists three packages (Metaskills, Art, Software Engineering 134); the foundation links are now intra-package.

### What failed / still open

Nothing. Note for future runs: language-specific skills go under `software-engineering/languages/<lang>/`; portable skills under `software-engineering/foundations/<topic>/`; a domain-specific source would introduce a `domains/<domain>/` lane.

### Known risks

None material. gcbc's `SOURCE.md` "Library placement" note was updated to record the `foundations/` lane so it does not read as stale.

### Files changed

122 gcbc objects moved under `library/software-engineering/foundations/`, generated indexes regenerated, `ledger/gcbc_think_like_swe/SOURCE.md`, and this worklog.

## 2026-07-31 - Effective C++, 3rd ed., Chapter 1

### What changed

First unit of a new source, `effective_cpp_3e` (Scott Meyers, *Effective C++*, 3rd ed.). Admitted the source through `ledger/REGISTRY.md` (sha256 begins `4f983195c37c`, not previously present), created its `SOURCE.md` (pdf_page_offset 21) and `UNITS.md` (9 chapters, chapter-per-unit). Processed Chapter 1 "Accustoming Yourself to C++" (Items 1-4, printed pp. 11-33 / PDF pp. 32-54). Added 12 objects — 10 patterns + 2 drills — into the existing `software-engineering` package under a new `languages/cpp` lane (topics `foundations`, `preprocessor`, `const-correctness`, `initialization`). Two patterns link back to gcbc foundations: const-correctness specializes `PAT_prefer_immutable_objects`, and the preprocessor pair specialize `PAT_adopt_language_features_when_best_tool`. Library goes from 124 to 136 objects.

Placement correction (same session, follow-up commit): the cards were first placed in a separate top-level `cpp` package. That split one skill family across two installable packages and turned the foundation links into cross-package dependencies. Per `PASS_LIBRARY.md` ("Universal foundation structure", which shows `software_development/languages/python/...`), language-specific skills are a `languages/<lang>` lane inside the software package, not a package of their own. Moved all 12 to `software-engineering/languages/cpp/`; object_ids were unchanged, so every cross_link and foundation_object_id still resolves, and the links are now intra-package.

### What was tested or reviewed

Read the full chapter from `pdftotext` extraction of PDF pp. 32-54; text and code extracted cleanly (no scans, no figures needing render — captions/`Figure` references absent from the extracted text). Second read against the candidate list. All three gates run and pass: `python tools/validate.py` (136 objects), `python tools/verify_grounding.py --source effective_cpp_3e` (1 processed unit grounded; 6 verbatim quotes spanning printed pp. 11-33 verified against the payload), and `python tools/build_index.py` (22 indexes, 6 changed). Initial validate surfaced 4 shape issues, all fixed (see below).

### What worked

Chapter 1's four Items map cleanly to distinct skills: the federation-of-sublanguages mental model (Item 1); prefer-const/enum and prefer-inline over the preprocessor (Item 2, two patterns); four const-correctness patterns (Item 3: apply const, return-by-const-value, logical constness with mutable, non-const-calls-const delegation); and three initialization patterns (Item 4: manual built-in init, initializer lists, local-statics vs the static-init-order fiasco). Twelve objects matches the gcbc chapter cadence (~11/unit), so chapter-per-unit is the right size here.

### What failed / still open

Two mechanical schema traps, both fixed before commit: (1) an unquoted `#` in a YAML `name:` value silently truncated the name as a comment, failing the H1-match rule — fixed by quoting; (2) literal C++ template/cast syntax (`<int>`, `<char&>`, `<typename T>`) in body prose tripped the unreplaced-angle-bracket rule — fixed by rephrasing the code references without angle brackets. Note for future C++ runs: keep angle-bracket template syntax out of body text, and quote any frontmatter value containing `#`.

### Known risks

The enum-hack method was folded into the Notes/Do of `PAT_prefer_const_and_enum_to_define` rather than emitted as a separate variant; if a later C++ source treats the enum hack as its own decision, revisit whether it should become a variant. UNITS.md page ranges for the unprocessed chapters (u03-u09 except u06) are approximate and must be refined at claim time.

### Next safe step

Review the Chapter 1 objects, then run Chapter 2 "Constructors, Destructors, and Assignment Operators" (Items 5-12, printed pp. 34-60). It is the closest merge test against Chapter 1's const/initialization and the gcbc contracts/immutability foundations.

### Files changed

`ledger/REGISTRY.md`, `ledger/effective_cpp_3e/{SOURCE.md,UNITS.md,units/u01.md}`, 12 new objects under `library/software-engineering/languages/cpp/`, generated indexes (`library/INDEX.md` + the new `software-engineering/languages/cpp` indexes), `docs/worklogs/assignments.md`, this worklog, and `docs/domains/corpus/next_steps.md`.

## 2026-07-30 - Dynamic Figure Drawing, Chapter 3

### What changed

Processed Chapter 3, "Figure Unity in Deep Space: Interconnection of Forms." Added patterns for connecting blocked figure masses through directional interconnection lines and for using a dominant outer contour to coordinate a complex figure. Added a three-study drill that tests those connections without visible arrows. Absorbed foreground-background overlap staging into the draw-through foundation and connected tonal unification into the shading foundation. Corrected the chapter boundary from PDF pp. 66-106 to PDF pp. 66-105 after visual confirmation that Chapter 4 begins on PDF p. 106. The source now has 3/6 processed units, ten objects, and four absorbed variants.

### What was tested or reviewed

Used the PDF skill's render-and-inspect workflow. Rendered PDF pp. 66-106 with `python tools/render_pdf.py` at `tmp/pdfs/dynamic_figure_drawing/ch03/page`; the native Poppler renderer wrote all 41 requested PNGs. Visually inspected the full bounded sequence and performed a second read of the overlap, interconnection, contour, tonal, and Chapter 4 boundary pages. The helper then emitted its known false missing-output warning from the broken override wrapper after the verified files existed. Reviewed the two revised foundations against their full card templates and checked the three new cards plus the v2 unit ledger manually against `PASS_SCHEMA.md`. `python tools/validate.py` accepts every Dynamic Figure Drawing object and reports only two unrelated software-testing cards whose source unit is unprocessed. `python tools/build_index.py` correctly refuses to generate indexes while those same unrelated errors remain. `git diff --check` passed.

### What worked

The chapter's cohesion instruction yields three distinct learner decisions: clarify front-to-back ordering after construction, carry a connecting path through major mass transitions, and coordinate the final figure with an outer contour or integrated tone. The first and fourth decisions genuinely vary existing foundations; the connecting path and dominant contour are distinct reusable figure-construction patterns.

### What failed / still open

The renderer's override-wrapper still emits a false failure after writing verified output files. Repository-wide validation and generated indexes remain blocked by two unrelated software-testing cards that cite an unprocessed source unit; neither issue is a defect in this Chapter 3 run.

### Known risks

Interconnection lines must follow the actual mass attachment and pose; they should not become decorative, formulaic curves. A dominant contour and connected tone are late-stage cohesion tools, not replacements for solving construction, overlap order, or balance.

### Next safe step

Run Chapter 4, "Figure Invention: Controlling Size in Foreshortened Forms," beginning at printed p. 105 / PDF p. 106. Locate the Chapter 5 title page visually before finalizing Chapter 4's endpoint.

### Files changed

`ledger/REGISTRY.md`, `ledger/burne_hogarth_dynamic_figure_drawing/{SOURCE.md,UNITS.md,units/ch03.md}`, two revised construction foundations, three new objects under `library/art/drawing/figure-construction/`, `docs/worklogs/assignments.md`, this worklog, and `docs/domains/corpus/next_steps.md`.

## 2026-07-30 - Dynamic Figure Drawing, Chapter 2

### What changed

Processed Chapter 2, “Figure Notation in Deep Space.” Added patterns for coordinating paired torso masses through their middle insertion and for building a leg back from its supporting foot. Added drills for a torso-first action sequence and for growing a notation across scales. Absorbed the source's torso–legs–arms–head construction sequence into the universal construction AP. Corrected the ledger boundary after visual review: Chapter 2 ends at PDF p. 65; the Chapter 3 title page is PDF p. 66. The source now has 2/6 processed units, seven objects, and two absorbed variants.

### What was tested or reviewed

Used the PDF skill's render-and-inspect workflow. Rendered PDF pp. 47-66 with `python tools/render_pdf.py` at the fresh prefix `tmp/pdfs/dynamic_figure_drawing/ch02/page`; all 20 requested PNGs were written by `C:\Users\Methuselas\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdftoppm.exe`. Inspected the full bounded chapter visually, then reread the candidate-bearing pages and the Chapter 3 title page. The helper then emitted its known false missing-output warning from the broken override wrapper, after verified outputs existed. Reconciled against the staged construction AP and five related figure-construction cards. `git diff --check` passed. The full validator included every new and revised Dynamic Figure Drawing object without a source-specific error, then reported five unrelated software-engineering cards whose locators name an unprocessed unit.

### What worked

The chapter provides two distinct action checks beyond general figure blocking: the middle insertion makes independent torso movements readable, while a supporting foot anchors the pelvis-to-leg force chain. Its sequential notation exercises differ from the existing key-pose drill by rehearsing a fixed torso-first construction order, and its small-to-large studies provide a concrete scale-retention drill.

### What failed / still open

The renderer's override-wrapper still reports a false failure after creating and verifying the requested files. The full-repository validation gate and index generation are blocked by five unrelated software-engineering cards that cite an unprocessed source unit; no validation failure in this source should be conflated with that library-wide condition.

### Known risks

Hogarth's stated torso–legs–arms–head order is retained as an action-figure method variant, not a rigid hierarchy for all drawing tasks. The support-foot pattern establishes readable force direction; it is not a substitute for observational balance analysis or perspective-ground construction.

### Next safe step

Run Chapter 3, “Figure Unity in Deep Space: Interconnection of Forms,” bounded by printed pp. 65-104 / PDF pp. 66-106, with special attention to whether overlapping-form instruction is genuinely distinct from the existing draw-through and foreshortening patterns.

### Files changed

`ledger/REGISTRY.md`, `ledger/burne_hogarth_dynamic_figure_drawing/{SOURCE.md,UNITS.md,units/ch02.md}`, the updated construction AP, four new objects under `library/art/drawing/figure-construction/`, `docs/worklogs/assignments.md`, this worklog, and `docs/domains/corpus/next_steps.md`.

## 2026-07-30 - How to Draw Comics the Marvel Way, Chapter 6

### What changed

Processed Chapter 6, “The Name of the Game Is Action!”, after the earlier out-of-order Chapter 7 run. Added a superhero-comics gesture-amplification pattern and an action-through-key-poses drill. Absorbed the center-line-first action search into the existing stick-figure foundation and the action-centerline five-step figure build into the universal construction AP. Updated the Marvel registry summary to 7/12 processed units and 24 objects.

### What was tested or reviewed

Visually identified the Chapter 6 title page at PDF p. 52 and Chapter 7 at PDF p. 66, without deriving PDF positions from printed pagination. Rendered and inspected PDF pp. 52-65 twice at 150 DPI. `python tools/render_pdf.py` resolved `C:\Users\Methuselas\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdftoppm.exe`, wrote all 28 fresh-prefix PNGs, then reported the already-known broken override-wrapper error. Scoped validation of the two new cards, the two updated foundations, and `ch06.md` passed; `git diff --check` passed.

### What worked

The chapter distinguishes a forceful superhero-comics action from a merely readable pose through an exaggerated, coherent center-line sweep and deliberately opposed limbs. Its instructional sequence also produces two non-duplicate routes: mapping continuous motion to find the impactful key pose, and preserving the action curve through an exploratory five-step construction-to-tone pass.

### What failed / still open

Whole-repository validation and index generation were not run because six unrelated uncommitted programming cards have an in-progress source unit. The known renderer override-wrapper failure recurred only after every requested PNG had been written and inspected; it is already recorded in `failures.md`.

### Known risks

The new gesture pattern is explicitly specialized to heightened superhero-comics action. It is not a universal instruction to exaggerate every pose. The center-line variant helps action discovery but gives less immediate precision for a measured contact, balance, or reach constraint than the joint-first foundation.

### Next safe step

Review the Chapter 6 cards and variants. The next queued Marvel unit is Chapter 8, “Drawing the Human Head!”; locate the Chapter 8 and 9 title pages visually before bounding it, then retrieve only genuine head-construction and expression overlaps.

### Files changed

`ledger/REGISTRY.md`, `ledger/marvel_how_to_draw_comics/{UNITS.md,units/ch06.md}`, two new cards in `library/art/drawing/{comics,construction}/`, two updated foundations in `library/{art/drawing/construction,metaskills/iterative-construction}/`, `docs/worklogs/assignments.md`, and `docs/domains/corpus/{worklog.md,next_steps.md}`.

## 2026-07-30 - How to Draw Comics the Marvel Way, Chapter 7

### What changed

Processed the explicitly user-selected out-of-order Chapter 7, “Foreshortening! The Knack of Drawing the Figure in Perspective!”, while leaving Chapter 6 queued. Added a connected-solid method for foreshortening a figure mass and a block-figure comparison drill. Updated the Marvel source summary in the registry to 6/12 processed units and 22 objects.

### What was tested or reviewed

Visually identified the Chapter 7 title page at PDF p. 66 and Chapter 8 at PDF p. 73, without deriving PDF positions from printed pagination. Rendered and inspected exactly the bounded Chapter 7 PDF pp. 66-72 twice at 150 DPI. Used `python tools/render_pdf.py` with two fresh prefixes; it resolved `C:\Users\Methuselas\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdftoppm.exe`, wrote all fourteen PNGs, then reported the known override-wrapper error. Scoped validation of the two new Marvel cards and `ch07.md` passed, and `git diff --check` passed.

### What worked

The source supplies the missing reusable method that Chapter 5 did not: build the whole figure from connected solids, then shorten individual masses as their axes recede. The apparent shortening of a thigh or limb is therefore grounded in the direction of its construction volume rather than treated as a proportion mistake. Retrieval was limited to the three genuine overlap decisions: simple-solid construction, figure mass blocking, and scene-perspective anchoring; none teaches this foreshortening choice.

### What failed / still open

Whole-repository validation and index generation were not run because six unrelated uncommitted programming cards have an in-progress source unit. The known renderer override-wrapper failure recurred after all requested fresh images were written; it is already recorded in `failures.md` and no new rendering approach was attempted.

### Known risks

The method is tied to a figure mass turning toward or away from the viewer. It does not authorize arbitrary limb-length changes; the underlying solid must make the changed apparent length legible. The chapter uses superhero-comics figures, but the card retains the transferable construction decision rather than a genre-specific anatomy prescription.

### Next safe step

Review the two Chapter 7 cards. The next queued Marvel unit is still Chapter 6, “The Name of the Game Is Action!”; locate the Chapter 7 title page visually when eventually bounding it, then retrieve against the Chapter 5 action-pose cards and this Chapter 7 method.

### Files changed

`ledger/REGISTRY.md`, `ledger/marvel_how_to_draw_comics/{UNITS.md,units/ch07.md}`, two new cards in `library/art/drawing/construction/`, `docs/worklogs/assignments.md`, and `docs/domains/corpus/{worklog.md,next_steps.md}`.

## 2026-07-30 - Calibration tranche: 8 runs, 10 sources, 63 objects - DISCARDED

### What changed

Eight PASS runs across four domains with deliberate pairwise overlap: two
programming (Stroustrup TCPL 4e, Gaddis Starting Out 8e, plus Automate the Boring
Stuff), two figure drawing (Hogarth, Marvel), two mathematics (Wallace, OpenStax),
two creative writing (Hamand, Starkey). 63 objects across 5 packages.

**All discarded except the metaskills AP.** These were calibration runs for tuning
settings, not library content. The cards are gone; the findings below are the
actual product and are why the tranche was worth running.

Kept: `metaskills/iterative-construction/AP_plan_and_build_work_from_thumbnail_to_final`.
Its absorbed Marvel variant was stripped along with the rest - that source's ledger
is gone, so the provenance would dangle. Recoverable from git if wanted.

### What was tested or reviewed

Full audit of all 63 objects before discard.

### What worked

**The per-unit design holds at scale.** At 63 objects, 5 packages, 10 sources - the
first point where the template-reuse rules could realistically fire - the library
showed:

- 0 sentences repeated in more than 3 objects
- 0 sentences repeated in even 2-3 objects
- 0 shared IF clauses at any count; 0 shared ELSE clauses at any count
- 0 name-in-body violations
- 0 `library_path` / directory mismatches
- 0 `routing_class` / `specialization_axis` violations
- 6/6 objects with populated `variants` named those variant_ids in Notes

Ten objects was too small to prove anything about template-stamping. Sixty-three
across five unrelated domains is a real result.

**Merge and variant absorption work.** All four overlap pairs absorbed correctly
onto the first source's foundation card, with grounded `difference_from_foundation`
and `when_to_use` / `when_not_to_use` naming real conditions - including the exact
Gaddis-vs-Stroustrup checked-subscript contrast the doctrine cites. Note the shape:
variants land on the FOUNDATION card, so a second source correctly shows zero
variants of its own. That is the design working, not a failure.

**Yield per unit:** 1-11 objects, mean ~6.3. Consistent with a healthy unit size.

### What failed / still open

1. **Over-specialization recurs, and it is the main open defect.** ch19 came back
   6/10 specializations; art came back 8/9. In art the `specialization_axis`
   correlated exactly with which book the object came from - Hogarth to `method`,
   Marvel to `medium` - not with any real constraint. Bodies like "IF drawing a head
   from a changing angle" are universal construction, not medium-bound.
2. **Intended distinctions never reached the cards.** The art specializations were
   meant to separate comic / cartoon / manga / life drawing. No card carried a style
   in its tags, axis, or IF clause; every one was tagged `figure-drawing` plus body
   parts. The library could not answer "show me manga figure construction." If style
   is to be differentiated, it has to be named in the IF, carried in `tags`, and use
   `specialization_axis: style` or `tradition`.
3. **The registry goes stale.** The Gaddis row read 0/28 units and 0 objects while
   the library held 7. Ledger is ground truth; the registry is a summary and drifted
   within a day. A reconcile check belongs in tooling.
4. **Supporting docs drift faster than cards.** After the `library_path` migration
   the cards were all correct, but PASS-TOOL-1's packet still specified the
   validator against `category`/`subcategory` - it would have rejected the entire
   library. The cards were never the stale thing.

### Known risks

Two parser traps found while hand-checking, both recorded in the PASS-TOOL-1
packet: `library_path` is block-list YAML, so an inline-`[a,b]` regex silently
matches nothing and reports a false clean pass; and matching frontmatter keys at
column 0 misses every nested `reference:` sub-key, which produced 70 phantom
failures on a first attempt. A validator with either bug looks like it is working.

### Next safe step

Re-run with tuned settings. The 9 discarded sources were removed from
`ledger/REGISTRY.md` so the hash guard will re-admit them; leaving the rows would
have blocked every re-run with "already processed."

Watch specifically whether the over-specialization default holds after tuning: a
non-operator-overloading, non-art unit should come back mostly `foundation`.

### Files changed

- Deleted `library/{art,mathematics,software_development,writing}/**` (62 objects)
- Deleted `ledger/` folders for the 9 discarded sources
- `ledger/REGISTRY.md` reduced to the retained source
- Metaskills AP: `variants: []`, variant paragraph removed from Notes

## 2026-07-30 - Creative Writing: Four Genres in Brief, Chapter 2 “Writing dialogue”

### What changed

Admitted David Starkey's *Creative Writing: Four Genres in Brief*, 3rd ed. as `starkey_creative_writing_four_genres_3e_2017` by SHA-256 and queued its 40 source-native instructional sections and anthologies. Processed the user-selected Chapter 2 “Writing dialogue” section, adding five patterns and two drills for contextual dialogue register, direct versus reported speech, speaker-paragraph formatting, attribution density, neutral `said` tags, observed-speech shaping, and table-reading for false formality. Absorbed a transcript-sifting method into fractured turns and a revise-with-breathers method into the existing dialogue-scene AP. One placement candidate was rejected as already covered by direct-versus-reported speech and the existing scene-ending pattern.

### What was tested or reviewed

Read printed pp. 130-136 / PDF pp. 233-239 twice. Visually inspected all seven pages at 150 DPI, including the two-speaker formatting example, tag and punctuation guidance, and the revision checklist. Ran `python tools/validate.py` (63 objects pass), `python tools/build_index.py` twice (first run changed three indexes; second changed zero), `python -m unittest discover -s tests -v` (26 tests pass), and `git diff --check` (no issues).

### What worked

The close same-domain source tested merge discipline rather than repeating the prior chapter. Its observed-speech method and revision-first breathing method are genuine alternatives to existing foundations, while the source's choices about narrative distance, social register, visual turn-taking, and attribution are separate learner decisions. The section's examples and checklist rendered clearly enough to ground both the formatting pattern and the audible-revision drill.

### What failed / still open

The first `tools/render_pdf.py` invocation returned exit 3 while the direct renderer wrote all seven requested PNGs beneath the fresh nested prefix. A retry correctly refused the existing files, so the helper could not provide a clean success exit for the run. The exact files were enumerated and visually inspected; the behavior is recorded as `PASS-TOOL-RENDER-FRESH-PREFIX` rather than changed during this corpus assignment.

### Known risks

The source's punctuation examples use a particular prose convention; the exported formatting pattern keeps only the durable one-speaker-per-paragraph rule. Observing public speech can produce privacy-sensitive material, so the drill trains writers to capture rhythms rather than names, particulars, or verbatim exchanges. Direct and reported speech remain complementary choices, not a rule that direct dialogue is automatically better.

### Next safe step

Review the seven objects and two variants against the existing fiction-dialogue package. If another Starkey unit is selected, Chapter 2 “Setting the scene” is the closest prose-dialogue extension; Chapter 4 “Writing convincing dialogue” is the closest contrasting medium test.

### Files changed

`ledger/REGISTRY.md`, `ledger/starkey_creative_writing_four_genres_3e_2017/{SOURCE.md,UNITS.md,units/ch02_dialogue.md}`, seven new and two updated objects in `library/writing/fiction-dialogue/`, generated library indexes, `docs/worklogs/assignments.md`, and corpus continuity docs.

## 2026-07-30 - OpenStax Intermediate Algebra, Section 6.4

### What changed

Admitted Lynn Marecek's *Intermediate Algebra* as `openstax_intermediate_algebra_2017` by SHA-256, queued its 70 numbered sections, and processed the user-selected Section 6.4, "General Strategy for Factoring Polynomials." Added patterns for factoring a perfect-square trinomial embedded in a four-term expression and verifying a factorization by expansion. Absorbed the direct "undo FOIL" route for monic trinomials as a method-sequence variant of the existing ac-pair pattern. Three overlapping candidates were rejected with their reasoning retained in the v2 unit ledger.

### What was tested or reviewed

Read printed pp. 605-614 / PDF pp. 613-622 twice. Rendered and visually inspected the ten pages: strategy chart, nine worked examples, 40 mixed exercises, and self-check. Manually expanded the source's sum-of-cubes, repeated-difference-of-squares, and embedded-perfect-square examples back to their original polynomials. Ran `python tools/validate.py` (56 objects pass), `python tools/build_index.py` twice (first run changed four indexes; second changed zero), `python -m unittest discover -s tests -v` (26 tests pass), and `git diff --check` (no issues).

### What worked

The same-domain source produced a meaningful merge test rather than a duplicate package. Direct factor-pair selection for x² + bx + c is a faster route than the existing split-and-group method when its constraint holds. The three-plus-one partition in Example 6.43 identifies a genuine new decision that ordinary paired grouping does not cover. The source's repeated multiply-back step separated correctness checking from the existing completeness loop.

### What failed / still open

`tools/render_pdf.py` wrote all ten requested PNGs but returned exit 1 because its expected-output logic assumes three-digit page suffixes while Poppler writes four digits for PDF pp. 613-622. The images were present and inspected; the renderer defect is recorded as `PASS-TOOL-RENDER-4DIGIT` rather than fixed within this corpus assignment. SymPy is not installed in this workspace, so the three domain-evidence checks were expanded manually instead of through symbolic algebra.

### Known risks

The direct-pair variant is limited to the intended integer-coefficient, monic-trinomial context; it must not displace the ac-pair foundation for a non-unit leading coefficient. The source's statement that sums of squares are prime has the same real/integer factoring scope already recorded for Math152.

### Next safe step

Review the two new patterns and absorbed variant against the Math152 factoring package. If another unit from this source is selected, retrieve against these cards first; Section 6.5 is the closest application extension and Sections 6.1-6.3 are the closest overlap tests.

### Files changed

`ledger/REGISTRY.md`, `ledger/openstax_intermediate_algebra_2017/{SOURCE.md,UNITS.md,units/ch06s04.md}`, two new objects and one updated object in `library/mathematics/algebra/factoring/`, generated library indexes, `docs/worklogs/assignments.md`, and corpus continuity docs.

## 2026-07-30 - Ledger v2 and Discoverable Variants

### What changed

Adopted ledger v2 for the Gaddis Section 14.5 and Marvel Chapter 5 unit ledgers. Each now declares `candidate_count` and gives every absorbed variant dedicated learner-decision, basis, method, and tradeoff fields. Documented the v2 migration rule and updated generated indexes to show each variant beneath its foundation.

### What was tested or reviewed

Ran the extended validator against the corpus (54 objects pass), the 26-test tooling suite, and deterministic index generation. Read the generated figure-construction and metaskills indexes to confirm the three Marvel alternatives appear beneath their two foundation objects.

### What worked

The new format preserves the review reasoning that previously fit only in prose, while the index makes alternatives visible at the point where a learner chooses a skill.

### What failed / still open

The legacy TCPL Chapter 19 ledger remains v1 because its recorded 11-candidate report has only ten rows. It is intentionally not presented as reconciled.

### Known risks

Older ledgers will not receive count or rationale checks until they are revised and promoted to v2. A migration must preserve actual source accounting; it must not fill a missing candidate by guesswork.

### Next safe step

Use v2 for every new unit. Promote older ledgers only during a real revision, beginning with the nearest source work rather than a bulk format-only pass.

### Files changed

`docs/PASS/{PASS_RUN.md,PASS_LEDGER.md,PASS_LIBRARY.md}`, the Marvel and Gaddis unit ledgers, generated library indexes, corpus continuity docs, tooling code/tests, and the assignment log.

## 2026-07-30 - How to Draw Comics the Marvel Way, Chapter 5

### What changed

Admitted Stan Lee and John Buscema's *How to Draw Comics the Marvel Way* as `marvel_how_to_draw_comics` by SHA-256 and processed the user-selected Chapter 5, “Let's Draw the Figure.” Added three cards: pose-first stick skeletons, drawing through occluded construction, and a stick-figure pose-invention drill. Absorbed three source-specific methods as variants: pose-first ovoid-and-cylinder blocking and scribble-sculpted blocking into the figure-mass foundation, plus the stick-to-cleaned-contour sequence into the universal construction AP.

### What was tested or reviewed

Visually read printed pp. 51-58 / PDF pp. 44-51 twice after rendering all eight PDF pages at 150 DPI with the direct Poppler executable. Retrieved and read the six existing figure-construction cards and the universal AP before each disposition. Ran `python tools/validate.py` (54 objects pass), `python tools/build_index.py` twice (first run changed four indexes; second changed zero), `python -m unittest discover -s tests -v` (22 tests pass), and `git diff --check` (no issues).

### What worked

The chapter's central pose-to-volume sequence supplied a real new skeleton-stage rule and a direct practice drill, while the two body-building approaches correctly became variants of the existing mass-construction decision rather than duplicate cards. Drawing through occlusion was a separate decision that the present library did not yet cover. The chapter's image-led instruction rendered clearly, so the extraction rests on the actual construction sequences rather than text alone.

### What failed / still open

The stale direct Poppler path recorded in the corpus failures log did not exist in this runtime. The executable under `dependencies/native/` rendered the pages successfully; the failure record now names the current path. The PDF does not supply a usable publication date, so the source and object references record it as `Unknown`.

### Known risks

The source's heroic-comics phrasing and exaggerated examples are evidence for pose and construction order, not a universal anatomy standard. Adjacent Chapters 4 and 6 overlap figure construction and action, so any future run must retrieve against this chapter's cards and variants before adding a parallel rule.

### Next safe step

Review the three new cards and three absorbed variants. If another unit from this book is selected, Chapter 4 is the closest figure-construction merge test; Chapter 6 is the closest action/gesture extension.

### Files changed

`ledger/REGISTRY.md`, `ledger/marvel_how_to_draw_comics/{SOURCE.md,UNITS.md,units/ch05.md}`, three new objects and one updated object in `library/art/drawing/figure-construction/`, `library/metaskills/iterative-construction/AP_plan_and_build_work_from_thumbnail_to_final.md`, generated library indexes, `docs/worklogs/assignments.md`, this worklog, `docs/domains/corpus/{failures.md,next_steps.md}`.

## 2026-07-30 - Variant Recovery Checkpoint

### What changed

Added a decision-versus-method recovery checkpoint to the PASS second read and disposition procedure. It requires a runner to name the learner decision, source method or policy, and tradeoff before rejecting or absorbing a candidate. Updated the ledger contract so each variant row records its foundation, `variant_basis`, and concrete contrast. The change follows the recovered Gaddis single-checked-subscript variant.

### What was tested or reviewed

Reviewed the new procedure against the Gaddis `IntArray` example and its two distinct claims: a mutable reference return and an always-checked access policy. Checked that the procedure remains compatible with the closed object schema and current unit-ledger disposition table.

### What worked

The checkpoint makes the missing distinction explicit at the inexpensive second-read and local-retrieval stages. It preserves learning choices—what outcome is needed and which method earns its tradeoff—without adding new card fields or forcing every source example into a variant.

### What failed / still open

The prior Gaddis review missed this split and required a recovery commit. The new check is procedural, so it relies on the runner's grounded judgment; the validator cannot determine whether a source contains an unrecognized alternative method.

### Known risks

Over-applying the check could turn superficial context changes into variants. The method or policy must create a concrete, durable difference in when to use it or its cost, safety, or constraint tradeoff.

### Next safe step

Use the checkpoint on the next same-domain PASS run and review whether it catches a genuine variant without inflating the candidate count with source trivia.

### Files changed

`docs/PASS/PASS_RUN.md`, `docs/PASS/PASS_LEDGER.md`, `docs/domains/corpus/{decisions.md,failures.md,worklog.md,next_steps.md}`, and `docs/worklogs/assignments.md`.

## 2026-07-30 - Gaddis Single Checked-Subscript Variant

### What changed

Reopened the Gaddis Section 14.5 review to absorb its `IntArray` design as `gaddis_single_checked_subscript`, a method variant of `PAT_checked_unchecked_access`. The variant checks every `operator[]` call before returning an element, whereas the foundation separates unchecked brackets from a named checked accessor. Reconciled the unit ledger from ten to eleven candidates: seven new objects, one variant, and three rejections.

### What was tested or reviewed

Reread printed pp. 852-857, including the bounds test, reference return, and the invalid-index example. Reviewed the foundation rule and its ELSE branch against the Gaddis method. Ran the validator and deterministic index generation after the absorption.

### What worked

The two sources now exercise the intended disposition distinction: the reference-return rule remains a new C++ skill, while the checked-on-every-access API is an alternative method for the existing checked-access foundation.

### What failed / still open

The initial review treated the single checked bracket form only as part of the new mutable-reference pattern and failed to record its distinct API-contract choice. No source or schema change was needed to correct this.

### Known risks

The variant's fail-fast rejection is grounded in the source's `IntArray`; it does not endorse that source's process-termination error mechanism for modern production code.

### Next safe step

Review the variant beside its foundation and the mutable-subscript pattern, then keep future class-design candidates at this same rule-versus-method distinction.

### Files changed

`library/software_development/class_design/PAT_checked_unchecked_access.md`, `ledger/gaddis_starting_out_cpp_8e_2015/units/ch14s05.md`, this worklog, and `docs/worklogs/assignments.md`.

## 2026-07-30 - Starting Out with C++, 8th Edition, Section 14.5

### What changed

Admitted Tony Gaddis's *Starting Out with C++*, 8th Edition (`gaddis_starting_out_cpp_8e_2015`) by SHA-256 and divided its unusually broad Chapter 14 into its nine numbered sections. Processed the user-selected Section 14.5, “Operator Overloading,” as a different-author counterpart to the prior Stroustrup Chapter 19 pass. Added seven objects: assignment chaining, familiar operator semantics, normalized value-operation results, composite-value comparison, stream-reference chaining, mutable-subscript references, and a bounded-subscript drill. The candidate ledger records all ten raised candidates; three were deliberately rejected.

### What was tested or reviewed

Read printed pp. 831-857 / PDF pp. 862-888 twice. Rendered and visually inspected Table 14-1 on printed p. 838 / PDF p. 869, including both its allowed and forbidden overload list. Retrieved and read all ten existing `software_development/class_design` objects before dispositions. Checked the source's representative outputs and traces: 6 feet 5 inches plus 3 feet 10 inches normalizes to 10 feet 3 inches; prefix and postfix increment return different values; and `IntArray` supports write, add, and increment through its subscript. Ran `python tools/validate.py` (51 objects pass), `python tools/build_index.py` twice (first changed three indexes; second changed zero), `python -m unittest discover -s tests -v` (22 tests pass), and `git diff --check` (no issues).

### What worked

The section is a close thematic match while contributing distinct material: the original Chapter 19 set already covered traversal increment and narrow friend access, so those candidates correctly became rejections rather than duplicate cards. The source's older delete-before-allocation assignment example was also rejected in favor of the existing stronger exception-safety pattern. The extracted table and code listings were readable, and the unit ledger reconciles exactly.

### What failed / still open

The first validator run rejected all seven new objects because the unquoted source title contains a YAML-significant colon. Quoting that single field fixed the schema error; no invalid card was indexed. No C++ compiler was available in this workspace, so the domain evidence uses the source's executable examples and printed output rather than a local compilation.

### Known risks

The source's assignment overload returns a `const` value; the exported chaining pattern preserves only the source's behavioral lesson, not a prescriptive modern C++ return-type signature. The source's `IntArray` terminates the process on bounds error; the drill requires rejection before access but intentionally leaves the modern error-reporting mechanism open.

### Next safe step

Review the seven C++ objects against the prior Chapter 19 set. If more coverage is wanted from this source, select one queued Chapter 14 section and retrieve against these objects before writing; Section 14.4 on copy constructors is the closest overlap test.

### Files changed

`ledger/REGISTRY.md`, `ledger/gaddis_starting_out_cpp_8e_2015/{SOURCE.md,UNITS.md,units/ch14s05.md}`, seven objects in `library/software_development/class_design/`, generated library indexes, `docs/worklogs/assignments.md`, this worklog, `docs/domains/corpus/failures.md`, and `docs/domains/corpus/next_steps.md`.

## 2026-07-30 - PASS Source Lifecycle and Unit Procedure

### What changed

Formalized source-native units, explicit user selection of a queued unit, a required domain-evidence check, and retirement of fully reconciled payloads to `trash/sources/<source_id>/`. Added `payload_path` to the SOURCE ledger format, revised active-source guidance to permit human-facing collection folders, and replaced the obsolete `sources/!completed/` option. Added a tracked trash README while keeping retired payload ignored by Git. Logged a stable PDF-rendering helper as `PASS-TOOL-RENDER` `spec-needed`; no helper was implemented in this documentation-only assignment.

### What was tested or reviewed

Reviewed the revised run procedure, ledger format, active-source instructions, `.gitignore`, and the new trash documentation against the four completed cross-domain PASS runs. Confirmed the assignment record names the renderer wrapper as a scoped, unimplemented tooling gap.

### What worked

The changes make the procedure match observed practice: user-selected sections can remain small enough for a grounded second read, collection folders no longer contradict source IDs, and completed payloads leave the active queue without being deleted.

### What failed / still open

The repository has no project-owned PDF rendering helper yet. The required behavior is recorded as `PASS-TOOL-RENDER` rather than represented by an environment-specific executable path.

### Known risks

Existing SOURCE ledgers predate `payload_path`; the field is mandatory for new admissions and is added to older records only when those sources are next reconciled or otherwise revised. Retiring a payload before every unit closes remains forbidden.

### Next safe step

Review the procedure update. When visual-PDF work repeats, write a packet for `PASS-TOOL-RENDER` and implement a minimal wrapper; do not hard-code a user-cache runtime path into PASS documentation.

### Files changed

`.gitignore`, `sources/README.md`, `trash/README.md`, `docs/PASS/PASS_RUN.md`, `docs/PASS/PASS_LEDGER.md`, `docs/domains/corpus/{decisions.md,worklog.md,next_steps.md}`, and `docs/worklogs/assignments.md`.

## 2026-07-30 - Beginning and Intermediate Algebra, Section 6.6

### What changed

Admitted Tyler Wallace's *Beginning and Intermediate Algebra* (`math152_beginning_intermediate_algebra_2010`) by SHA-256, queued its 77 numbered lessons, and processed the user-selected Section 6.6, “Factoring Strategy.” Added six factoring patterns, one method-selection AP, and one mixed-polynomial drill covering GCF removal, term-count classification, special products, perfect-square trinomials, ac pairs, grouping, and reclassification after an intermediate step.

### What was tested or reviewed

Read printed/PDF pp. 234-236 twice. Rendered and visually inspected all three pages, including the strategy table, five worked examples, and the 42-problem practice set. Ran `python tools/validate.py` (44 objects pass), `python tools/build_index.py` twice (first run changed four indexes; second changed zero), and `python -m unittest discover -s tests -v` (22 tests pass).

### What worked

The compact lesson contains a genuine decision procedure rather than a disconnected formula list, so it grounded a source-native AP as well as reusable decision rules and a drill. Mathematical notation, examples, and practice problems rendered cleanly. PASS required no schema changes; all three object types and the `mathematics/algebra/factoring` path validate as-is.

### What failed / still open

No source-reading or validation failure occurred. The mathematics package was empty, so this run did not exercise a variant, replacement, or merge decision.

### Known risks

The source's use of “prime” for a sum of squares is scoped to its intended integer-coefficient factoring context. It must not be generalized to complex-factorization tasks. Adjacent lessons 6.1-6.5 teach the individual methods and will overlap this strategy unit if they are later processed.

### Next safe step

Review the eight mathematics objects as the textbook-domain test. If a follow-up is wanted, process an adjacent factoring lesson only with candidate-by-candidate retrieval against this package, or choose a visually richer mathematics lesson to test a different source boundary.

### Files changed

`ledger/REGISTRY.md`, `ledger/math152_beginning_intermediate_algebra_2010/{SOURCE.md,UNITS.md,units/ch06s06.md}`, eight objects in `library/mathematics/algebra/factoring/`, generated library indexes, the assignment log, and this worklog.

## 2026-07-30 - Creative Writing Exercises For Dummies, Chapter 4

### What changed

Admitted *Creative Writing Exercises For Dummies* (`creative_writing_exercises_dummies_2014`) by SHA-256, queued all 28 numbered chapters, and processed the user-selected Chapter 4, “Creating Drama through Dialogue.” Added six dialogue patterns, one scene-building AP, and four practice drills covering turn rhythm, scene endings, nonverbal relationship evidence, setting and time pressure, conflicting speaker goals, terse evasion, phone-call constraints, location rewrites, and subtext.

### What was tested or reviewed

Read printed pp. 47-56 / PDF pp. 63-72 twice. The extracted range contains no figure/table captions or figure references; the only occurrences of “table” are parts of ordinary words, so this text-based chapter did not require rendered-page inspection. Ran `python tools/validate.py` (36 objects pass), `python tools/build_index.py` twice (first run changed three indexes; second changed zero), and `python -m unittest discover -s tests -v` (22 tests pass).

### What worked

The chapter produced all three PASS object types without forcing a schema change: decision rules for scene design and revision, direct drills from the exercises, and a source-native sequence for layering dialogue into a point-of-view scene. The candidate ledger reconciles exactly: 11 raised candidates, 11 `new` dispositions, and 11 exported objects.

### What failed / still open

No source-reading or schema-validation failure occurred. The writing package was empty, so this unit did not exercise merge, variant, or replacement handling.

### Known risks

The adjacent Chapter 6 also teaches dialogue and is likely to overlap. A future run must retrieve this unit's objects candidate-by-candidate rather than adding a second parallel set of general dialogue rules.

### Next safe step

Review the eleven objects as the writing-domain test. If another writing unit is selected, Chapter 6 is the natural merge/variant test; otherwise use a source with a different medium or layout to probe another PASS boundary.

### Files changed

`ledger/REGISTRY.md`, `ledger/creative_writing_exercises_dummies_2014/{SOURCE.md,UNITS.md,units/ch04.md}`, eleven objects in `library/writing/fiction-dialogue/`, generated library indexes, the assignment log, and this worklog.

## 2026-07-30 - Automate the Boring Stuff with Python, Chapter 3

### What changed

Admitted *Automate the Boring Stuff with Python*, 2nd Edition (`atbs_python_2e_2020`) by its SHA-256, queued all 20 numbered chapters, and processed Chapter 3, “Functions.” Added six function-design patterns and two drills: deduplicating repeated behavior, defining input/output contracts, naming optional arguments, tracing call stacks, limiting state to function boundaries, handling expected failures, a return-driven sequence exercise, and invalid-input reprompting.

### What was tested or reviewed

Read PDF pp. 99-118 (printed pp. 57-76) twice. Rendered PDF pp. 105-107 and visually inspected the two call-stack figures. Ran `python tools/validate.py` (25 objects pass), `python tools/build_index.py` twice (first run changed three indexes; second changed zero), and `python -m unittest discover -s tests -v` (22 tests pass).

### What worked

The direct Poppler executable rendered the diagram pages cleanly, so the chapter was grounded in text, code, exercises, and figures rather than text extraction alone. The eight ledger rows reconcile exactly with the eight candidates raised.

### What failed / still open

The first validator run rejected every new object because its locators used `ch03 pp.` rather than the validator's required `ch03, pp.` unit delimiter. Correcting the locators made the processed-unit check pass; no schema or validator rule was changed.

### Known risks

The patterns are general foundations derived from introductory Python examples. A future source may supply a language-specific or more advanced variant, but this unit does not justify one yet.

### Next safe step

Review this eight-object unit before selecting another Python chapter; Chapter 8, “Input Validation,” is the closest queued follow-up for merge and variant testing.

### Files changed

`ledger/REGISTRY.md`, `ledger/atbs_python_2e_2020/{SOURCE.md,UNITS.md,units/ch03.md}`, eight objects in `library/software_development/function_design/`, generated library indexes, the assignment log, and this worklog.

## 2026-07-30 - Made the Universal Workflow Concrete for C++ Work

### What changed

Expanded the universal AP with a C++ random-number-generator application: behavior and constraints at Step 0; API and ownership boundary at skeleton; generator and range behavior at block; boundary and behavior checks at rough; then tests, documentation, and cleanup at final. Updated the source bundle and ledger so this scope is source-recorded.

### What was tested or reviewed

Manually checked the AP's closed frontmatter and required body headings against `docs/PASS/PASS_SCHEMA.md`. No validator exists yet.

### What worked

The example demonstrates that the stages are not art metaphors: they force code decisions to be made in an order that exposes range, reproducibility, state ownership, and constraint errors before implementation polish.

### What failed / still open

No code-specific C++ API is prescribed here. That is intentional: this foundation governs the order of work, while a future C++ object should define any concrete implementation pattern from a verified language source.

### Known risks

The C++ application is supplied by the user, not by the visual source material. It remains recorded in the source bundle for traceability.

### Next safe step

When a C++ RNG source unit is processed, compare its concrete implementation objects against this AP and attach a variant only if it contributes a distinct workflow.

### Files changed

`sources/gen1_art_fundamentals_4step/MIGRATION_NOTE.md`, its source archive, ledger hash records, `library/metaskills/iterative-construction/AP_plan_and_build_work_from_thumbnail_to_final.md`, assignment log, and corpus worklog.

## 2026-07-30 - Corrected the Gen 1 Workflow to Universal Scope

### What changed

Replaced the prematurely narrowed figure-only AP with `AP_plan_and_build_work_from_thumbnail_to_final`. It now starts at Step 0, a cheap thumbnail or concept that fixes the intended composition or outcome, then moves through skeleton, block, rough, and final across any skillset. Expanded the source bundle and ledger to include the staged human, building, dragon, and alien examples plus the user correction.

### What was tested or reviewed

Visually inspected all six staged examples and reread the Gen 1 workflow text. Manually checked the replacement AP against `docs/PASS/PASS_SCHEMA.md`; no validator exists yet.

### What worked

The examples establish the process as an invariant across distinct forms: the early pass sets the intent, each successive pass proves more of the work, and final detail does not substitute for structure.

### What failed / still open

The original migration treated figure drawing as the AP's scope because it inspected only the two canonical figure sheets. That interpretation has been replaced; the old narrow AP was removed before review.

### Known risks

The source is an internal authored workflow, not an external craft book. Its universal coding and writing application comes from the explicit user correction recorded in the source bundle, rather than visual evidence alone.

### Next safe step

Review the universal AP as the library's first metaskill, then decide whether domain-specific variants should be added only when they offer a distinct sequence rather than restating the foundation.

### Files changed

`sources/gen1_art_fundamentals_4step/*`, `ledger/gen1_art_fundamentals_4step/*`, `ledger/REGISTRY.md`, `library/metaskills/iterative-construction/AP_plan_and_build_work_from_thumbnail_to_final.md`, assignment log, corpus worklog, and corpus failures log.

## 2026-07-30 - Gen 1 Four-Step Figure Workflow Migration

### What changed

Admitted the authored Gen 1 four-step workflow and its two canonical figure-progression sheets as one archived source unit. Migrated the sequence into `AP_build_figure_from_gesture_to_final_line_art`, preserving its gesture, blocking, rough, final, and backward-read gates as one usable PASS AP.

### What was tested or reviewed

Read the workflow text and visually inspected both canonical sheets. Manually checked the new AP against `docs/PASS/PASS_SCHEMA.md`; no validator exists yet.

### What worked

The two sheets confirm that the process is a single workflow rather than a list of disconnected construction tips: both retain action, volume, and focal hierarchy through all four stages.

### What failed / still open

No schema validator or index generator exists yet, so the library index was not generated.

### Known risks

`stage_binding` permits one stage only while this AP spans stages 1-4. It is bound to `1 skeleton` because that is the entry point; the full staged scope lives in the AP's flow.

### Next safe step

Review the migrated AP beside the six Dynamic Figure Drawing Chapter 1 objects, then decide whether a focused practice drill should be extracted from the same Gen 1 source.

### Files changed

`ledger/gen1_art_fundamentals_4step/*`, `ledger/REGISTRY.md`, `library/art/drawing/figure-construction/AP_build_figure_from_gesture_to_final_line_art.md`, assignment log, and corpus worklog.

## 2026-07-30 - Dynamic Figure Drawing, Chapter 1

### What changed

Admitted the source and processed Chapter 1 into five construction patterns and one drill.

### What was tested or reviewed

Visually read image pages 10-45 twice and manually checked all six objects against `docs/PASS/PASS_SCHEMA.md`.

### What worked

The ZIP's original page images preserved the diagrams and captions required to ground the extraction.

### What failed / still open

No schema validator or index generator exists yet.

### Known risks

The source's publication date is unknown in the available pages.

### Next safe step

Review this unit before selecting Chapter 2.

### Files changed

`ledger/dynamic_figure_drawing_hogarth/*`; six files in `library/drawing/figure-construction/`; registry, assignment log, and corpus worklog.

## 2026-07-30 - First PASS run: TCPL 4e ch.19 (Special Operators)

### What changed

First real run of the per-unit procedure. Source `tcpl_4e_2013` admitted through
`ledger/REGISTRY.md` (sha256 `f29c5b22356e`), 44 units queued, ch19 chosen as the
test unit rather than ch1 (which is front matter and would have returned `empty`).

10 patterns extracted to `library/`, one unit ledger written, registry row opened.
Re-categorized afterward per `docs/domains/spec/decisions.md` 2026-07-30:
`software-development/cpp-class-design/` -> `software_development/class_design/`,
tag separators normalized to underscore.

### What was tested or reviewed

Manual review of all 10 objects (no validator exists yet - PASS-TOOL-1 unassigned).
Checks run by script, ad hoc:

- Schema: 16 required top-level keys, 7 reference keys, enums, routing_class /
  specialization_axis consistency, placeholder tokens, locator unit, forbidden
  keys. **0 issues.**
- Cross-object sentence reuse (normalized, name/IF/THEN stripped): **0 sentences
  in >3 objects.**
- Shared IF clauses: **0.** Shared ELSE clauses: **0.** No exact duplicates of
  either at any count.
- THEN-recycling (first Do item vs THEN, Jaccard): max **0.20**, mean ~0.09.
- Full name appearing in body text: **none.** Intra-object duplicate items:
  **none.** Source-dependent phrasing ("see page", "as shown above", ...):
  **none.**
- Bodies read individually for the master test: Notes sections are synthesis, not
  assembled `author + locator + keywords` strings; Don't items name source-specific
  failure modes (e.g. treating the terminating null as usable capacity).

### What worked

The per-unit hypothesis. Four prior generations of whole-book runs failed on
template-stamping; this unit produced zero shared templates on any axis. Ten
objects from a ~28-page chapter is a healthy density - not two (unit too large to
hold attention) and not sixty (shape-filling).

Code listings survived PDF extraction intact, which was the main mechanical risk.

`stage_binding` spread across all five stages (0:4, 1:1, 2:1, 3:3, 4:1) rather
than defaulting to one value.

### What failed / still open

1. **One candidate vanished — STILL OPEN.** Run reported 11 grounded candidates;
   ledger holds 10 rows. Discrepancy recorded explicitly in `units/ch19.md`; no
   11th row invented. Resolve by recovering the candidate or recording it as
   `reject`. `PASS_RUN.md` §4 now requires a run to state its candidate count, so
   this is caught at the time rather than on review.
2. **Unverifiable negative — FIXED 2026-07-30.** `PASS_RUN.md` §3 now has a third
   case between "read" and "blocked": when the renderer is unavailable, proceed
   only on proxy evidence you have — absence of `Figure`/`Table` captions and
   in-text figure references in the extracted range — stated explicitly and
   recorded in the unit ledger.
3. **Genericization defaults were wrong — FIXED 2026-07-30.** Rule decided (spec
   decisions 2026-07-30): default to `foundation`/`general`/`none`; mark
   `specialization` only when the IF/THEN needs a language construct. 4 of 10
   flipped to foundation; the other 6 are genuinely C++-bound.
   `specialization` + `foundation_object_id: none` is now explicitly legal.
   Genericization itself deferred until the library holds a second language.
4. Category vocabulary is still uncontrolled (also logged in spec decisions).

### Known risks

Sample size is one chapter of one book, from a terse reference text with heavy code
and almost no figures - close to the easiest case for extraction quality and the
hardest for fact-vs-skill discrimination. A tutorial book with diagrams will test
different failure modes. Merge logic (`PASS_RUN.md` §6) is completely untested:
the library was empty, so all 10 candidates were trivially `new`.

### Next safe step

Second unit of the same source, so density and time-per-unit get a second data
point before anything is generalized. Then a unit from a diagram-heavy source to
test the visual path. Merge logic gets its first real test on the source's third
or fourth unit, once `class_design` has neighbours to retrieve.

Deferred and not blocking: the tier A/B (same chapter, strong vs cheap model, into
scratch folders), PASS-TOOL-1 validator, PASS-TOOL-2 scaffolder, triage/stopping
rule.

### Files changed

- `library/software_development/class_design/PAT_*.md` (10, new + recategorized)
- `ledger/REGISTRY.md`, `ledger/tcpl_4e_2013/{SOURCE.md,UNITS.md,units/ch19.md}`
- `docs/domains/spec/decisions.md`
## 2026-07-30 - How to Draw Comics the Marvel Way, Chapter 1

### What changed

Admitted Stan Lee and John Buscema's *How to Draw Comics the Marvel Way* by SHA-256 and processed Chapter 1, “The Tools—and the Talk of the Trade!” Four objects were added: a traditional inking-station pattern, a comic-page vocabulary pattern, a shot-scale foundation, and a framing-vocabulary drill. One silhouette candidate was rejected because the chapter supplies only a definition, not a usable decision or procedure.

### What was tested or reviewed

Read PDF pp. 8-15 (printed pp. 11-18) twice. Rendered and visually inspected all eight pages at 150 DPI with `pdftoppm.exe`; the output was checked against the tool inventory, annotated sample page, and shot/viewpoint examples. Schema validation and index generation are recorded after their commands run.

### What worked

The visual pages made the difference between glossary terms and usable panel-framing decisions clear. The source supplied a compact, coherent first unit with a physical-media setup plus a teaching route into comic-page vocabulary.

### What failed / still open

`python tools/render_pdf.py` reported a stale-wrapper failure even though it wrote all eight requested PNGs. The resolved direct Poppler executable rendered the same range successfully. The helper inconsistency remains covered by the existing renderer follow-up assignments.

### Known risks

The traditional inking setup is intentionally medium-specific and includes period tools; it is not presented as a requirement for digital comics work. The framing card is a portable foundation but is grounded only in this source's comics examples until a second visual-storytelling source supplies a contrasting route.

### Next safe step

Run Chapter 2, “The Secrets of Form! Making an Object Look Real” (printed pp. 19-28 / PDF pp. 16-25), retrieving the Chapter 1 drawing cards as potential neighbours only where the learner decision overlaps.

### Files changed

`ledger/REGISTRY.md`, `ledger/marvel_how_to_draw_comics/{SOURCE.md,UNITS.md,units/ch01.md}`, four objects under `library/art/drawing/comics/`, `docs/worklogs/assignments.md`, and this worklog.

### Verification update

The scoped Marvel validation passed: 4 objects and the Chapter 1 v2 ledger produced 0 errors. The repository-wide `python tools/validate.py` gate did not pass because six unrelated, uncommitted `library/software-engineering/abstraction/` cards cite a source unit still marked `in-progress`; index generation correctly refused the invalid whole library. No unrelated files were changed.

## 2026-07-30 - How to Draw Comics the Marvel Way, Chapter 2

### What changed

Processed Chapter 2, “The Secrets of Form! Making an Object Look Real.” Added four objects: a simple-solids construction foundation, a figure-mass specialization, a shading-for-form pattern, and a sphere-cube-cylinder drill. Rejected separate cards for the many pictured subjects because they all demonstrate the same construction choice.

### What was tested or reviewed

Read the chapter's instructional pages twice and rendered PDF pp. 16-22 at 150 DPI with `tools/render_pdf.py`, using the resolved Poppler executable through `PASS_PDFTOPPM`. Inspected all seven pages individually. PDF p. 23 is the Chapter 3 title page, so it was excluded even though the supplied Chapter 2 end-page locator reaches farther. Scoped validation and whole-repository gate results are recorded after the commands run.

### What worked

The subject sequence made the source's actual learner decision clear: objects, vehicles, faces, figures, and machines all reduce to a small vocabulary of volumes. The Daredevil and shading studies support separate, specific follow-on applications without turning every example into a card.

### What failed / still open

The initial default-helper invocation reached the known stale-wrapper failure, although its requested PNGs existed afterward. Rerunning the helper with `PASS_PDFTOPPM` set to its resolved renderer completed successfully. The renderer's fallback inconsistency remains covered by the existing tooling follow-ups.

### Known risks

The source's table of contents and PDF boundary disagree: Chapter 3 begins at PDF p. 23, rather than the expected PDF p. 26. The ledger preserves the printed locator from the contents, but Chapter 2 card evidence names the visually confirmed PDF range. The shading guidance deliberately stops at form reinforcement; this source page does not establish a full lighting model.

### Next safe step

Run Chapter 3, “The Power of Perspective!” Starting at PDF p. 24; use the next Chapter 4 title page to establish its end boundary rather than assuming the old printed-to-PDF offset remains stable.

### Files changed

`ledger/REGISTRY.md`, `ledger/marvel_how_to_draw_comics/{UNITS.md,units/ch02.md}`, four objects under `library/art/drawing/construction/`, `docs/worklogs/assignments.md`, and this worklog.

### Verification update

Scoped Marvel validation passed: 8 art objects and both Marvel v2 unit ledgers produced 0 errors, including cross-link and foundation-target checks. `python tools/validate.py` exited 1 and `python tools/build_index.py` exited 1 because six unrelated uncommitted `library/software-engineering/abstraction/` cards still point to a source unit marked `in-progress`; no unrelated file was changed.

## 2026-07-30 - How to Draw Comics the Marvel Way, Chapter 3

### What changed

Processed Chapter 3, “The Power of Perspective!” Added five perspective patterns and one drill: horizon/vanishing-point setup, point-count selection, perspective ellipses, equal-division transfer, figure placement in scene perspective, and a checkerboard-floor exercise. The street and room demonstrations were retained as grounding for the common scene-perspective decision rather than exported as duplicate cards.

### What was tested or reviewed

Read PDF pp. 24-35 twice. Rendered and visually inspected all twelve pages at 150 DPI through `tools/render_pdf.py` with `PASS_PDFTOPPM` set to the resolved Poppler executable. PDF p. 36 was visually confirmed as the Chapter 4 title page and excluded. Scoped validation and whole-repository gate results are recorded after the commands run.

### What worked

The chapter supplies both the conceptual frame and concrete constructions: the horizon gives the viewer's eye level, vanishing points govern receding axes, and the wall and checkerboard examples turn the theory into checkable drawing procedures. Figure overlays demonstrate that characters must share the setting's geometry.

### What failed / still open

No Chapter 3 extraction attempt failed. The repository-wide validator and index gate remain affected by the unrelated uncommitted programming cards described in the Chapter 1 and Chapter 2 entries.

### Known risks

The printed page range in the table of contents does not maintain the initial PDF offset. The unit is therefore grounded by the confirmed PDF boundary, not a guessed page conversion. The perspective cards teach the source's construction methods; they do not claim to cover curvilinear or other advanced systems absent from the chapter.

### Next safe step

Run Chapter 4, “Let's Study the Figure!” beginning at PDF p. 36, and establish its ending from the Chapter 5 title page before extracting.

### Files changed

`ledger/REGISTRY.md`, `ledger/marvel_how_to_draw_comics/{UNITS.md,units/ch03.md}`, six objects under `library/art/drawing/perspective/`, `docs/worklogs/assignments.md`, and this worklog.

### Verification update

Scoped Marvel validation passed: 14 art objects and all three Marvel v2 unit ledgers produced 0 errors, including cross-link and foundation-target checks. `python tools/validate.py` exited 1 and `python tools/build_index.py` exited 1 because the same six unrelated uncommitted `library/software-engineering/abstraction/` cards point to a source unit marked `in-progress`; no unrelated file was changed.

## 2026-07-30 - How to Draw Comics the Marvel Way, Chapter 4

### What changed

Processed Chapter 4, “Let's Study the Figure!” into two patterns and one drill: head-unit and landmark proportion guides, superhero-presence proportion choices, and a three-way proportion comparison exercise. Rejected the chapter's sex-coded figure prescriptions because they are dated appearance conventions, not durable learner decisions. The source registry now records four processed units and seventeen objects.

### What was tested or reviewed

Read PDF pp. 36-43 twice. Rendered and visually inspected all eight pages twice at 150 DPI with `tools/render_pdf.py`, setting `PASS_PDFTOPPM` to `C:\Users\Methuselas\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdftoppm.exe`. PDF p. 44 was visually confirmed as the Chapter 5 title page and excluded. A scoped validator run covering the 17 `library/art/` objects and all Marvel v2 unit ledgers passed with 0 errors. `python tools/validate.py` exited 1 only on six unrelated uncommitted programming cards whose source unit remains `in-progress`.

### What worked

The paired front/profile figure sheets made the measurement method concrete: head units control the overall height while elbow and hanging-hand positions catch local proportion errors. The three comparison pages distinguish role-signalling mass, stance, and head-to-body ratio from surface muscle detail, making the Chapter 4 drill grounded rather than generic.

### What failed / still open

The bundled workspace Python cannot import PyYAML, so it cannot run `tools/validate.py`; the repository's `python` command supplies PyYAML and completed the scoped gate. Whole-repository validation and index generation remain blocked by the six unrelated `library/software-engineering/abstraction/` cards already present in the worktree and deliberately outside this assignment.

### Known risks

The superhero-presence card is intentionally genre-specific: its broad shoulders, heavy chest, planted stance, and compact-heavy construction express this source's superhero-comics roles, not universal anatomy or character-design requirements. The proportion card gives construction checkpoints, not a claim that one fixed head count fits every figure.

### Next safe step

Run Chapter 5, “Let's Draw the Figure!” beginning at PDF p. 44. Establish its ending by visually locating the Chapter 6 title page, retrieve only actual overlap candidates from the Chapter 4 figure-construction and superhero-proportion cards, and preserve the unrelated programming worktree changes.

### Files changed

`ledger/marvel_how_to_draw_comics/{UNITS.md,units/ch04.md}`, `ledger/REGISTRY.md`, two patterns under `library/art/drawing/{construction,comics}/`, one drill under `library/art/drawing/comics/`, `docs/worklogs/assignments.md`, this worklog, `docs/domains/corpus/failures.md`, and `docs/domains/corpus/next_steps.md`.

## 2026-07-30 - How to Draw Comics the Marvel Way, Chapter 5

### What changed

Redid Chapter 5, “Let's Draw the Figure!” after the earlier test output was removed. Added two construction patterns and one drill: stick-figure pose search, transparent draw-through for occluded masses, and repeated action-pose doodling. Added two method-sequence variants to the existing figure-mass foundation: oval-and-cylinder pose blocking and scribble-sculpture blocking. Rejected a standalone foreshortening card because this chapter only names the effect; the source-native Chapter 7 is the proper extraction unit.

### What was tested or reviewed

Read PDF pp. 44-51 twice. Rendered and visually inspected all eight pages twice at 150 DPI with `tools/render_pdf.py`, setting `PASS_PDFTOPPM` to `C:\Users\Methuselas\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdftoppm.exe`. PDF p. 52 was visually confirmed as the Chapter 6 title page and excluded. Scoped validation covering 20 `library/art/` objects and all five Marvel v2 ledgers passed with 0 errors. `python tools/validate.py` exited 1 only on the six unrelated uncommitted programming cards whose source unit remains `in-progress`.

### What worked

The Iron Man and Spider-Man progressions make the construction order explicit: settle the action as a stick figure, build masses over it, keep hidden forms transparent until their placement is checked, then clean up. The Thor sheets provide a genuine contrasting method rather than a duplicate, using exploratory light lines to sculpt and select moving forms after the pose exists.

### What failed / still open

Whole-repository validation and index generation remain blocked by the same unrelated `library/software-engineering/abstraction/` cards already present in the worktree. No Chapter 5 extraction attempt failed, and no generated index was changed.

### Known risks

The scribble-sculpture variant is deliberately marked as an advanced alternative: it preserves movement but removes the explicit primitive-volume checks that make the foundation safer for beginners. Foreshortening remains unexported here so the library does not mistake a label for a method.

### Next safe step

Run Chapter 6, “The Name of the Game Is Action!” beginning at PDF p. 52. Establish its end by visually locating the Chapter 7 title page, then retrieve only actual overlaps with Chapter 5's pose-search, draw-through, and construction-method cards.

### Files changed

`ledger/marvel_how_to_draw_comics/{UNITS.md,units/ch05.md}`, `ledger/REGISTRY.md`, three new objects and one updated pattern under `library/art/drawing/construction/`, `docs/worklogs/assignments.md`, this worklog, and `docs/domains/corpus/next_steps.md`.

## 2026-07-30 - How to Draw Comics the Marvel Way, Chapter 8

### What changed

Processed Chapter 8, “Drawing the Human Head!”, into three patterns and one drill: cranial-mass and jaw construction, comics head design for character role, coordinated facial-expression controls, and mirror-based expression observation. Rejected the source's idealized hero-face and gender-coded beauty/age prescriptions rather than exporting them as universal rules. The source registry now records eight processed units and twenty-eight objects.

### What was tested or reviewed

Visually identified the Chapter 8 title page at PDF p. 73 and the Chapter 9 title page at PDF p. 94 before selecting the bounded range. Read PDF pp. 73-93 twice and rendered and visually inspected all twenty-one pages individually twice at 150 DPI with `python tools/render_pdf.py`, using `C:\Users\Methuselas\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdftoppm.exe`. Scoped validation covering 28 `library/art/` objects and all Marvel v2 ledgers passed with 0 errors; `git diff --check` passed.

### What worked

The profile, front, and oblique construction sheets make the head card concrete: a rounded cranium, narrower jaw, and wrapped center and eye guides survive viewpoint changes. The expression sheets separately show that brows, eyes, and mouth can change the acting while the established head remains stable, and the mirror prompt supplies a direct practice route.

### What failed / still open

Whole-repository validation and index generation remain blocked by the same six unrelated uncommitted `library/software-engineering/abstraction/` cards whose source unit is `in-progress`. No Chapter 8 extraction attempt failed, and no generated index was changed.

### Known risks

The head-construction card treats the source's placement guides as a useful scaffold, not a claim that any one head shape or feature ratio is anatomically universal. The character-role card is deliberately a superhero-comics specialization; it does not equate facial features with a person's real character.

### Next safe step

Run Chapter 9, “Composition!”, by visually locating the Chapter 9 and 10 title pages before setting its PDF range, then retrieve only actual composition overlaps.

### Files changed

`ledger/marvel_how_to_draw_comics/{UNITS.md,units/ch08.md}`, `ledger/REGISTRY.md`, one pattern under `library/art/drawing/construction/`, two patterns and one drill under `library/art/drawing/comics/`, `docs/worklogs/assignments.md`, this worklog, and `docs/domains/corpus/next_steps.md`.

## 2026-07-30 - How to Draw Comics the Marvel Way, Chapter 9

### What changed

Processed Chapter 9, “Composition!”, into three patterns and one drill: unify panel focal elements as a sensed composition mass, choose a camera angle for intended dramatic effect, vary scale/placement/viewpoint across a comics page, and compare a static layout against a purposeful revision. Rejected literal prime-shape templates because the source explicitly treats the shape as a diagnostic consequence of sketching, not a container to fill. The source registry now records nine processed units and thirty-two objects.

### What was tested or reviewed

Visually identified the Chapter 9 title page at PDF p. 94 and the Chapter 10 title page at PDF p. 106 before selecting the bounded range. Read PDF pp. 94-105 twice and rendered and visually inspected all twelve pages individually twice at 150 DPI with `python tools/render_pdf.py`, using `C:\Users\Methuselas\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdftoppm.exe`. Scoped validation covers the 32 `library/art/` objects and all Marvel v2 unit ledgers; `git diff --check` was also run.

### What worked

The prime-shape overlays made the panel grouping decision concrete without turning it into a rigid recipe. The paired camera-angle studies isolate viewpoint from shot coverage, while the paired six-panel pages make page-level variation observable: the same story can use scale, depth, off-center focal placement, and changed viewpoint to create clearer energy.

### What failed / still open

No Chapter 9 extraction attempt failed. No generated index was changed.

### Known risks

The camera-angle and page-variation cards are superhero-comics specializations, not a mandate to tilt every panel or avoid centered staging. Both retain readability as the constraint and preserve the existing shot-scale card's separate coverage decision.

### Next safe step

Run Chapter 10, “Draw Your Own Comicbook Page!”, starting at its visually confirmed title page, PDF p. 106. Locate the Chapter 11 title page before reading its bounded pages, then retrieve only actual overlaps with the Chapter 9 composition package and the existing comics page vocabulary.

### Files changed

`ledger/marvel_how_to_draw_comics/{UNITS.md,units/ch09.md}`, `ledger/REGISTRY.md`, three patterns and one drill under `library/art/drawing/comics/`, `docs/worklogs/assignments.md`, this worklog, and `docs/domains/corpus/next_steps.md`.

## 2026-07-30 - How to Draw Comics the Marvel Way, Chapter 10

### What changed

Processed Chapter 10, “Draw Your Own Comicbook Page!”, into one comics construction pattern and one drill. Added `VAR_ch10_page_wide_staged_pencilling` to the general plan-to-final AP, preserving the source's distinct method of completing each construction pass across the entire page before moving forward. Rejected duplicate stand-alone cards for stick figures, primitive masses, and fleshing out because the chapter deliberately reuses the existing construction package. The source registry now records ten processed units and thirty-four objects.

### What was tested or reviewed

Visually identified the Chapter 10 title page at PDF p. 106 and the Chapter 11 title page at PDF p. 115 before selecting the bounded range. Read PDF pp. 106-114 twice and rendered and visually inspected all nine pages individually twice at 150 DPI with `python tools/render_pdf.py`, using `C:\Users\Methuselas\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdftoppm.exe`. Scoped validation covers the 34 `library/art/` objects and all Marvel v2 unit ledgers; `git diff --check` was also run.

### What worked

The staged Captain Britain page makes the page-wide pass concrete: first action placement across six panels, then mass construction, then fleshing out. The Spider-Man prompt preserves the same six-beat action while requiring independent work before comparison, and the explicit instruction to draw the whole figure distinguishes panel cropping from an unresolved construction boundary.

### What failed / still open

No Chapter 10 extraction attempt failed. No generated index was changed.

### Known risks

The page-wide pencilling route is a method variant of the general staged workflow, not a new universal construction order. The full-figure pattern supports a panel crop's structural clarity; it does not mean every final comics panel must show the whole figure.

### Next safe step

Run Chapter 11, “The Comicbook Cover!”, starting at its visually confirmed title page, PDF p. 115. Locate the Chapter 12 title page before reading its bounded pages, then retrieve only actual overlaps with Chapter 9 composition and any existing cover-design package.

### Files changed

`ledger/marvel_how_to_draw_comics/{UNITS.md,units/ch10.md}`, `ledger/REGISTRY.md`, one updated AP under `library/metaskills/iterative-construction/`, one pattern and one drill under `library/art/drawing/comics/`, `docs/worklogs/assignments.md`, this worklog, and `docs/domains/corpus/next_steps.md`.

## 2026-07-30 - How to Draw Comics the Marvel Way, Chapter 11

### What changed

Processed Chapter 11, “The Comicbook Cover!”, into four cover-design patterns and one thumbnail-comparison drill: cover reader hierarchy, production zones, open color treatment, story teasing without resolution, and comparative cover-layout diagnosis. Added `VAR_ch11_editorial_cover_layout_review` to the general plan-to-final AP, preserving the source's multi-thumbnail editor-review route. Rejected the claim that one layout can be objectively correct. Corrected this source's unit-scheme note so it requires visual title-page bounds rather than a printed-page offset. The source registry now records eleven processed units and thirty-nine objects.

### What was tested or reviewed

Visually identified the Chapter 11 title page at PDF p. 116 and the Chapter 12 title page at PDF p. 122 before selecting the bounded range. Read PDF pp. 116-121 twice and rendered and visually inspected all six pages individually twice at 150 DPI with `python tools/render_pdf.py`, using `C:\Users\Methuselas\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdftoppm.exe`. Retrieved only decision-level overlaps with the comics composition, cover-adjacent production, and general construction AP cards. Scoped validation of the Marvel art library plus the referenced general AP and their source ledgers passed 40 objects with 0 errors; `git diff --check` passed.

### What worked

The four Nova layouts made cover hierarchy testable: lead-character visibility, figure scale, useful space, and eye level can be compared without pretending that one composition is universally right. The cover construction pages make logo, copy, trim, color, and suspense constraints concrete before final penciling.

### What failed / still open

The initial overbroad title-boundary render requested pages past the actual PDF end and therefore failed completeness verification, although it retained images through PDF p. 137. It was used only to locate the Chapter 12 title page; two fresh, complete six-page renders supplied the Chapter 11 visual evidence. No extraction attempt failed and no generated index was changed.

### Known risks

The new cards are comic-cover specializations, not universal marketing or print-production rules. The color card constrains black use before full-color reproduction; it does not replace the separate inking chapter's decisions about black placement in a finished panel.

### Next safe step

Run Chapter 12, “The Art of Inking!”, starting at its visually confirmed title page, PDF p. 122. Visually locate the following boundary before selecting its range, then retrieve only genuine inking overlaps.

### Files changed

`ledger/marvel_how_to_draw_comics/{SOURCE.md,UNITS.md,units/ch11.md}`, `ledger/REGISTRY.md`, one updated AP under `library/metaskills/iterative-construction/`, four patterns and one drill under `library/art/drawing/comics/`, `docs/worklogs/assignments.md`, this worklog, and `docs/domains/corpus/next_steps.md`.

## 2026-07-30 - Dynamic Figure Drawing, Chapter 1 redo

### What changed

Admitted Burne Hogarth's *Dynamic Figure Drawing* by SHA-256 and created its six-chapter queue. Reprocessed Chapter 1 into two figure-construction patterns and one torso-turn drill, while adding the source's organic body-form chain as a variant of the existing figure-mass construction card. Rejected an invented limb-copying drill and dated categorical sex-proportion claims.

### What was tested or reviewed

Visually read PDF pp. 11-46 twice, using the PDF renderer's resolved Poppler executable; the parallel image ZIP was extracted to scratch as a visual cross-check. `python tools/validate.py` found no Dynamic Figure Drawing errors, but the whole-library gate remains blocked by two unrelated untracked software-engineering cards whose locators name an unprocessed unit. `git diff --check` passed.

### What worked

The torso barrel-and-wedge method changes the existing construction route rather than duplicating it. Limb rhythm and extremity mass decisions remain distinct, independently usable cards.

### What failed / still open

`python tools/build_index.py` correctly refused to generate indexes while the unrelated invalid cards remain present.

### Known risks

Hogarth's exaggerated and categorical anatomical presentation is retained only where it gives a general construction check; it is not treated as a universal body-proportion rule.

### Next safe step

Run Chapter 2, “Figure Notation in Deep Space,” bounded by printed pp. 45-64 / PDF pp. 47-66.

### Files changed

`ledger/REGISTRY.md`, `ledger/burne_hogarth_dynamic_figure_drawing/`, the updated figure-mass pattern, two new patterns and one drill under `library/art/drawing/figure-construction/`, `docs/worklogs/assignments.md`, this worklog, and `docs/domains/corpus/next_steps.md`.

## 2026-08-01 - Dynamic Figure Drawing, Chapter 1 guided run

### What changed

Admitted the user-supplied OCR payload for Burne Hogarth's *Dynamic Figure Drawing* under `burne_hogarth_dynamic_figure_drawing_ocr`, recorded Ch 0 as an empty orientation unit, and processed Chapter 1 after a full first read, expert review, full second read, and candidate reconciliation. Added twelve new figure-construction patterns and five drills, absorbed Hogarth's ovoid/column/spatulate mass-selection method into the existing Stage 2 blocking pattern, and rewrote that pattern to preserve Step 0 intent, Step 1 landmarks, viewpoint, attachment, and the backward test. Rejected a new full-figure AP because Chapter 1 supplies form vocabulary rather than the ordered notational workflow introduced in Chapter 2. Added three original teaching plates with provenance sidecars for head/torso masses, limb chains/rhythms, and hand/foot wedges.

### What was tested or reviewed

Read printed pp. 9-44 twice from `Burne_Hogarth_Dynamic_Figure_Drawing_OCR.txt` and inspected every aligned image in `Ch 1.zip`; the user reviewed the first-pass interpretation and corrected chest placement, rear pelvic visibility, underarm rhythm, S/B leg selection, guideline use, neck attachment, foot mechanics, and soft-tissue arch construction before the second pass. Ran `python tools/validate.py` (231 objects passed), `python tools/verify_grounding.py --source burne_hogarth_dynamic_figure_drawing_ocr` (1 processed unit grounded), `python tools/verify_references.py` (passed after restoring the pre-existing gitignored Gen 1 comparison image locally from `teaching.zip`), `python -m unittest discover -s tests -v` (35 passed), and `python tools/build_index.py` twice (4 index files changed on the first run, 0 on the second).

### What worked

The guided review prevented the prior art-domain failures from becoming cards: the neck root is fixed inside the chest opening; terminal rotation follows the carrying limb segment; rear pelvic butterfly lines remain conditional surface rhythms inside one wedge; the foot arch is a filled soft-tissue rise rather than a hollow bone bridge; and Stage 2 guides are retained only while they explain one coherent construction. Candidate-level reconciliation kept Chapter 1 from inventing the Chapter 2 workflow and preserved the organic mass families as a method variant rather than a duplicate foundation.

### What failed / still open

The first local SVG helper passed `None` as `stroke_dasharray` and failed before writing the teaching plates; the helper was corrected to omit that attribute when unused. The first full reference gate also failed because the base snapshot omits the gitignored Gen 1 comparison image named in an existing sidecar; the exact image was restored locally from the supplied `teaching.zip`, after which the gate passed. The three new teaching plates have passed a vision review but still require the user's expert art review before merge.

### Known risks

The source identity is the supplied OCR text hash plus chapter page-image evidence, not the unavailable 26 GB original source archive. Mechanical grounding proves the cited page images existed and decoded; it does not prove artistic judgment. Guided additions about age, body mass, gravity, terminal rotation, and the foot's soft-tissue arch are recorded in the unit ledger as expert review corrections. The temporary torso triangle/box diagnostic is not yet a separate card because it is not mechanically grounded in the current first-party source payload; preserve it for a rebuilt guided-teaching source rather than silently attributing it to Hogarth.

### Next safe step

Have the user review the 18 candidate card files and the three teaching plates. Revise any wording, anatomy, or construction they reject; rerun all gates; then merge the overlay. Do not start Chapter 2 until Chapter 1 reaches user acceptance.

### Files changed

`docs/worklogs/assignments.md`, `docs/domains/corpus/{worklog.md,next_steps.md,failures.md}`, `ledger/REGISTRY.md`, `ledger/burne_hogarth_dynamic_figure_drawing_ocr/`, the revised `PAT_build_gesture_into_clear_masses.md`, seventeen new cards and three generated reference images plus sidecars under `library/art/drawing/figure-construction/`, and generated `INDEX.md` files.

## 2026-08-02 — Guided PASS Run: Dynamic Figure Drawing, Chapter 2

### What changed

Processed Chapter 2 after two full reads with expert correction between and after
reads. Added one subordinate Stage 2 AP, five local Patterns, and three Drills.
Updated the main onion-skinned figure AP to route human action figures through the
new structural-order AP. Added the Chapter 2 unit ledger and marked the unit
processed.

### What was reviewed

Reviewed printed pages 45-64 and all supplied page images, including torso-first
notation, pelvic leg attachment, foot bearing, front and rear arm yokes, head-last
trials, action-sequence editing, both notation development routes, and the final
segmentation diagnosis.

### What worked

The guided review separated strict construction order from later-stage freedom,
clarified the action line as the governing torso centerline, established Stage 2
exit conditions for terminal forms and yokes, and preserved reference-free work as
a Drill condition rather than a production ban.

### What remains deliberately open

Chapter 3 must supply the unity remedy for lumpy deep-space forms. Every Chapter 2
object is subject to a book-wide consolidation pass after Chapter 6 because later
chapters may change boundaries, wording, or dependencies. Chapter-specific visual
references remain deferred until the foundational curriculum is complete and
successfully practised.

### Validation

`python tools/validate.py` passes 241 objects. Grounding verifies both processed
Hogarth units against the supplied OCR and chapter images. The 35 repository tool
tests pass, generated indexes are deterministic on a second run, art-scoped
resolver checks retrieve the new structural-order AP and local patterns, and
`git diff --check` passes. `verify_references.py` still reports the two pre-existing
missing Gen 1 source-render files referenced by the four-step AP and the general
figure-mass Pattern; Chapter 2 adds no reference entry and does not change that
condition.

### Next safe step

Review the nine new objects, then begin the same guided two-read process for
Chapter 3 before restructuring any Chapter 2 object around unity methods.
