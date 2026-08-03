# Corpus Next Steps

status: active
owner: docs/domains/corpus
last_reviewed: 2026-08-03

The next safe step, not a wishlist. Anything speculative belongs in
`assignments.md` as `spec-needed` or in a design doc PARKED section.

## Next

**Art lane:** install the Stage 0/Stage 1 lock overlay after the figure-stage hardening overlay in both synchronized SkillForge copies. Stage 0 now stops at a quick marker-like rough idea; Stage 1 stops at a simple skeleton; Stage 2 remains a plain articulated maquette. Review later examples against all three information ceilings before attaching visual precedents. Then begin the guided Chapter 5 sequence. Chapter 4 remains firmed; reopen it only where Chapter 5 length controls must integrate with its width controls.

**`programmers_brain` u01-u02 are reviewed and merged.** Ten new
`foundations/code-comprehension` objects and four variants absorbed into gcbc
readability foundations. The source stays **active at 2/13** with u03-u13 queued;
it is not reconciled and its payload is not retired. Resume at **u03** — one unit
per chat, per `decisions.md` 2026-08-01.

**`PASS-CORPUS-TAG-AUDIT` is packeted and runnable** (`docs/assistants/handoffs/PASS-CORPUS-TAG-AUDIT.md`,
base `master` at `e3dfe64`). It touches `tags` across all 214 objects, so it
collides with any in-progress PASS run — schedule it *between* units, not
alongside one. Highest-payoff targets are the 11 objects with no cross-cutting
tag, 6 of which are the new `foundations/code-comprehension` lane that *Code
Complete* and *The Pragmatic Programmer* are expected to attach variants to.

Carry forward into u08 (*How to get better at naming things*) and u11 (*The act of
writing code*): u02 recorded two deliberate `reject` rows that those chapters are
expected to develop properly — writing a comment as a scaffold before the code it
describes, and naming the information you are looking for before reading. Check
them against the u02 ledger rather than re-deriving them.

1. **C++ Core Guidelines** is admitted (`cpp_core_guidelines`, REGISTRY `queued`, sha256 `be29ae459bc2`; `ledger/cpp_core_guidelines/SOURCE.md` written) but **BLOCKED** on `PASS-TOOL-MD-GROUNDING` — `verify_grounding.py` must support markdown/text sources (locator = rule ID, receipt = verbatim quote grep) before any unit can be `processed`. Do not start it until that tooling lands. When it does, process the highest-yield sections first (`R`, `C`, `ES`, `F`, `I`), after Effective Modern C++, so its modern rules `replace`/`variant` the pre-C++11 Effective C++ cards cleanly.

2. **Craft core as the library-adaptability litmus test.** Next runnable PASS sources (no tooling blocker; all text PDFs in `Practice/`): *The Programmer's Brain*, *Code Complete 2nd ed.*, *The Pragmatic Programmer* — in that reading order. These are language-agnostic craft that overlaps heavily with the existing gcbc foundations, while the 80-card `languages/cpp` lane already specializes and cross-links to those same foundations. So this is the real test of whether the library adapts: expect `variant`/`replace` against gcbc foundations, possibly new foundations, and relinking — and verify that when a gcbc foundation is revised or superseded, the cpp specializations' `foundation_object_id` and `cross_links` still resolve (validate.py catches dangling links). Do these before Effective Modern C++ / the Core Guidelines. Reading-order docs updated to put this craft core first (mirrors the corpus's foundations-first architecture).

3. *Effective C++*, 3rd ed. is **complete** (9/9 units, 80 objects, reconciled 2026-08-01). Review the corpus if desired. Payload retirement was deferred (the book stays in the user's curated `sources/Programming/C++/` shelf); retire to `trash/` only if the user asks. Select the next source for a PASS run. The natural follow-on is **Effective Modern C++** (Meyers): it supersedes several Effective C++ 3rd cards with C++11/14 idioms (`= delete`, `std::unique_ptr`/`std::shared_ptr`, move semantics, `std::function`/`std::bind`), which should be absorbed as variants/replacements against the existing `languages/cpp` lane — the first real exercise of the `replace` disposition in this lane.
2. Review the completed *How to Draw Comics the Marvel Way* source: forty-three cards and six absorbed variants across twelve processed chapters. Select a different admitted source for the next PASS run.
2. Review Starkey's Chapter 2 “Writing dialogue” objects and variants against the existing fiction-dialogue package; select “Setting the scene” next for a prose-dialogue extension or Chapter 4 “Writing convincing dialogue” for a contrasting-medium test.
3. Review the OpenStax *Intermediate Algebra* Section 6.4 cards and absorbed variant against Math152 Section 6.6; if more coverage is wanted, Section 6.5 is the closest application extension.
4. Repair the four-digit output check in `tools/render_pdf.py` before treating its exit code as reliable for page ranges at 1000 or above.
5. Make fresh-prefix PDF-render verification agree with created outputs before treating a nonzero exit as evidence that no pages exist.
6. Use the decision-versus-method recovery checkpoint in the next same-domain PASS run; Chapter 14.4 of *Starting Out with C++*, 8th Edition, is the closest C++ overlap test.
7. Review the *Starting Out with C++*, 8th Edition, Section 14.5 objects against the prior Chapter 19 set.
8. Review the *Beginning and Intermediate Algebra* Section 6.6 objects; adjacent factoring lessons require candidate-by-candidate merge retrieval if selected.
9. Review the *Creative Writing Exercises For Dummies* Chapter 4 objects; Chapter 6 is the closest writing merge/variant test if a follow-up is wanted.
10. Review the *Automate the Boring Stuff with Python* Chapter 3 objects, then decide whether to select Chapter 8 for a Python merge/variant test.
11. Review the guided *Dynamic Figure Drawing* Chapter 2 cards, then start Chapter 3 with the same two-read guided sequence. Preserve Chapter 2's lumpy-form diagnosis, but do not retrofit a unity remedy until Chapter 3 has been studied.
12. Review the *How to Draw Comics the Marvel Way* Chapter 5 cards and absorbed variants; Chapter 4 is the closest figure-construction merge test if a follow-up is wanted.
13. Use ledger v2 for every new or revised unit; leave the TCPL Chapter 19 ledger v1 until its missing candidate is recovered or rejected with grounding.

## Blocked

-

## Parked (with resume trigger)

-
