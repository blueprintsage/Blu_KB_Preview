# PASS Assignment Log

status: active
owner: docs/worklogs
last_reviewed: 2026-08-02

## Purpose

Coordinates parallel work between assistants and the user. Every assistant must
read this before starting work.

## Rules of engagement

1. Check this log BEFORE touching code. Do not work on an assignment owned by
   another assistant unless the user reassigns it.
2. Claim work by setting Owner + Status here in the same session you start it.
3. One owner per assignment. Collision domains are listed per assignment; two
   in-progress assignments must not share a domain.
4. Handoff packets live in `docs/assistants/handoffs/`. If an assignment has a
   packet, follow it exactly; raise conflicts in the worklog, do not improvise.
5. All repo law still applies: the `AGENTS.md` load order, project technical
   guides, build before claiming success, update the worklog after.
6. On completion set Status=`review` and note what was tested. The user verifies.
7. Commit between assignments. An assignment starts from a clean commit so its
   diff is reviewable and revertable on its own. Do not start a new assignment on
   top of another's uncommitted changes.
8. ONE assignment at a time per checkout. True parallel work requires separate
   git worktrees on separate branches; otherwise run sequentially.
9. **Every packet names its base branch.** An assignment branched off the wrong
   base silently loses its predecessor's work and the mistake surfaces days
   later. State the base branch and, where practical, give a verifiable check
   (`git merge-base --is-ancestor <commit> HEAD`).
10. When an assignment reaches `done`/`closed`, MOVE it to the Completed archive
    as one terse line, so the active tables show only open work.

## Status values

`open` (unclaimed, packet ready) · `spec-needed` (do not start; packet must be
written first) · `in-progress` · `review` · `done` · `blocked` · `closed`

`spec-needed` rows are the missing-piece ledger. When a system is scoped but not
built, log it here with enough note to write a packet later. Do not leave gaps
only in someone's head.

---

## Implementation assignments (active)

| ID | Assignment | Owner | Status | Packet | Collision domain / notes |
|----|-----------|-------|--------|--------|--------------------------|
| PASS-TOOL-ART-PREFLIGHT | Preflight visual sources for usable text, page-image access, and vision-capable execution | Codex | review | — | Base: `master` at `533a96d`. Added fail-closed OCR/vision/page-access preflight, weak-page reporting, ZIP page-image grounding, CropBox rendering, and the paired per-page text + image procedure without changing the object schema. 35 tests pass; 214 objects validate; indexes unchanged; text and visual grounding compatibility passed. The OCR Hogarth payload is ready at 177/177 aligned pages; physical page 117 is the sole instructional OCR miss and remains image-readable. |
| PASS-TOOL-1 | Schema validator + index generator (`tools/validate.py`, `tools/build_index.py`) | Codex | review | 20 validator rules covered by one valid fixture plus one failing fixture per rule; 22 tests pass. Current library: 17 objects validate. Recursive root-to-leaf indexes generated deterministically from `library_path`; second generation changes zero files. |
| PASS-TOOL-MD-GROUNDING | Add markdown/text-source support to `tools/verify_grounding.py` | (unassigned) | spec-needed | `verify_grounding.py` today only verifies PDF sources (physical-page extraction via `pdf_page_offset`). Add a text/markdown source mode: locator = rule ID or line range (no `pdf_page_offset`), reading receipt = verbatim quotes verified by searching the source `.md` file directly (no rendering), coverage measured over line span or rule count rather than pages. Trigger: the `cpp_core_guidelines` source (`ledger/cpp_core_guidelines/SOURCE.md`, REGISTRY `queued`, sha256 `be29ae459bc2`) is admitted but cannot be `processed` until this lands — fail-closed. Also generalizes to any future web/markdown source. Tooling domain (`docs/domains/tooling/`). |
| PASS-TOOL-RETRIEVAL | Greppable object manifest for §6 candidate placement | (unassigned) | open | [`PASS-TOOL-RETRIEVAL.md`](../assistants/handoffs/PASS-TOOL-RETRIEVAL.md) | §6 ("place each candidate against the library") is currently manual grep + reading whole objects, which loads O(library) into context and is the dominant context cost of a run. Evidence: Codex (258k window) hit ~89% on one chapter's neighbour comparison, capping it at one unit per chat (see `docs/domains/corpus/decisions.md` 2026-08-01). Scoped down from "ranked ~5-nearest retriever" to **phase 1: extend `build_index.py` to emit `library/MANIFEST.jsonl`** — one greppable row per object carrying tags, `library_path`, the IF/THEN learner decision, foundation route, and already-absorbed variant ids. Ranking is deferred: it is blocked on `PASS-CORPUS-TAG-AUDIT`, and the manifest is most of the value at a fraction of the risk. Note this is a cost fix, not a quality fix — it does not address §5 under-extraction. Tooling domain (`docs/domains/tooling/`). |
| PASS-CORPUS-TAG-AUDIT | Repair the tag vocabulary so tags can carry retrieval | (unassigned) | open | [`PASS-CORPUS-TAG-AUDIT.md`](../assistants/handoffs/PASS-CORPUS-TAG-AUDIT.md) | Doctrine calls tags "the cross-cutting retrieval keys," but nothing has ever depended on them, so the vocabulary rotted unnoticed. Measured at `e3dfe64` with the YAML loader: **every one of the 214 objects carries exactly four tags** — a quota, not a vocabulary, and the direct cause of the rest. 259 distinct tags, **122 singletons (47%)**, **185 (71%) confined to a single `library_path`**, 34 restating a path segment; only **74 (29%)** actually cross-cut. Latent today because §6 retrieval is manual; load-bearing the moment anything ranks on tags, which is why `PASS-TOOL-RETRIEVAL` phase 2 is blocked on it. Corpus domain (`docs/domains/corpus/`). |

## Design assignments (active — documents, not code)

| ID | Assignment | Owner | Status | Notes |
|----|-----------|-------|--------|-------|
| PASS-DOCTRINE-SKILLFORGE-BALANCE | Define SkillForge as limitation-aware external practice memory that guides without replacing native capability | GPT | review | Base: `master` at `cfe2419`. Scoped authority, practical-exam preflight, medium-appropriate precedents, avoidance checks, and diagnosis-led revision now live in doctrine, consumption, the Claude adapter, and resolver wording. 35 tests pass; 232 objects validate; indexes are deterministic; `diff --check` passes. `verify_references.py` remains blocked by two pre-existing missing Gen 1 source renders. No schema or corpus-card change. |
| PASS-SKILLFORGE-DISCOVERY-BRIDGE | Add GPT/Codex discovery placement and a fail-closed manual SkillForge preflight | GPT | review | Overlay adds `.agents/skills/skillforge/SKILL.md` byte-identical to the Claude adapter and makes `AGENTS.md` require resolver-backed preflight before covered work, especially before image generation. Resolver smoke test retrieves the mandatory construction metaskill and the onion-skinned figure AP. No library, schema, or resolver change. Future `.skillforge/` centralization remains deferred. |
| PASS-RUN-HOGARTH-DYNAMIC-FIGURE-CH01-GUIDED | Guided one-unit PASS run: Burne Hogarth, *Dynamic Figure Drawing*, Chapter 1 | GPT | review | Guided review retained 17 new objects, one absorbed variant, and the revised Stage 2 blocking pattern. The rejected Chapter 1-specific generated plates are absent from the golden repo; only the reviewed first-party four-step process sheets remain as general workflow references. |
| PASS-RUN-HOGARTH-DYNAMIC-FIGURE-CH02-GUIDED | Guided one-unit PASS run: Burne Hogarth, *Dynamic Figure Drawing*, Chapter 2 | GPT | review | Two guided reads and expert question review complete. Added one subordinate AP, five Patterns, and three Drills; updated the parent figure AP; canonical chapter references are deferred until the foundational book is consolidated. `validate.py` passes 241 objects, grounding verifies both processed Hogarth units, 35 tooling tests pass, indexes are deterministic, resolver checks retrieve the new hierarchy, and `diff --check` passes. The reference gate still reports the two pre-existing missing Gen 1 source-render files. |
| PASS-PROC-VISUAL-ART-SOURCE-QUALITY | Define source-literate extraction and anatomy QA for visual art books before another run | (unassigned) | spec-needed | The failed Hogarth runs misclassified established artistic standards as disposable claims, under-extracted the source, and accepted anatomically incorrect generated teaching images. Any future packet must require art-domain review of source conventions, a stricter anatomy/composition review step, and a token/cost checkpoint before batch image generation. |
| PASS-RUN-OPENSTAX-IA-CH06S04 | One-unit PASS run: OpenStax *Intermediate Algebra*, Section 6.4 | Codex | review | Base: master at `0446385`; source SHA-256 begins `e5ac3e24bec7`. Two new patterns, one absorbed method variant, and three rejections. `python tools/validate.py` passes 56 objects, indexes are deterministic, and 26 tooling tests pass. |
| PASS-RUN-TCPL-4E-CH19 | One-unit PASS run: The C++ Programming Language, 4th ed., Chapter 19 | Codex | review | Base: master at `1a64c66`. Ten new patterns; manually checked against PASS_SCHEMA.md because PASS-TOOL-1 is not available. Source SHA-256 begins `f29c5b22356e`; Chapter 19 is printed pp. 549-576 / PDF pp. 564-591. |
| PASS-RUN-EFFCPP-3E | Full-source PASS run: Effective C++, 3rd ed. (all 9 chapters) | Claude | review | COMPLETE 2026-08-01. Source SHA-256 begins `4f983195c37c`; offset 21. Text/technical source (Claude lane). 9/9 units, 80 objects (64 patterns + 16 drills) in the new `software-engineering/languages/cpp` lane across 19 topics, plus 2 variants absorbed into gcbc foundations (Ch.9). One commit per chapter (u01-u09) then reconciliation. All gates green (validate 204, grounding 9/9, build_index). Payload retirement deferred (book stays in the user's curated C++ shelf). Next: Effective Modern C++ to exercise `replace` against this lane. |
| PASS-MIG-GEN1-ART-4STEP | Migrate the Gen 1 Step 0 + four-stage universal construction workflow and canonical reference images | Codex | review | Manually checked against `PASS_SCHEMA.md`; source hash matches the refreshed archive. The AP is a cross-skill foundation with an explicit C++ RNG application example, not a C++ implementation recipe. |
| PASS-SKILLFORGE-PACKAGE-CONTRACT | Specify boot-first indexes and independently installable packages for SkillForge | Codex | review | Resolved in `docs/PASS/PASS_LIBRARY.md`: variable-depth `library_path`, top-level package membership, mandatory `metaskills`, bootstrap object, recursive generated indexes, and cross-package dependency disclosure. |
| PASS-RUN-ATBS-CH03 | One-unit PASS run: *Automate the Boring Stuff with Python*, Chapter 3 | Codex | review | Base: master at `819e2d6`. Eight objects (six patterns, two drills); source and call-stack figures read. `python tools/validate.py` passes 25 objects; 22 tooling tests pass; indexes deterministic. |
| PASS-RUN-CWED-CH04 | One-unit PASS run: *Creative Writing Exercises For Dummies*, Chapter 4 | Codex | review | Base: master at `70d6ab7`. Eleven objects (six patterns, one AP, four drills); `python tools/validate.py` passes 36 objects, index generation is deterministic, and 22 tooling tests pass. |
| PASS-RUN-STARK-CH02-DIALOGUE | One-unit PASS run: *Creative Writing: Four Genres in Brief*, Chapter 2, “Writing dialogue” section | Codex | review | Base: master at `0013442`. Seven new objects, two method variants, and one rejection. `python tools/validate.py` passes 63 objects, indexes are deterministic, and 26 tooling tests pass. |
| PASS-RUN-MATH152-CH06S06 | One-unit PASS run: *Beginning and Intermediate Algebra*, Section 6.6 | Codex | review | Base: master at `e5a5b29`. Eight objects (six patterns, one AP, one drill); rendered examples and practice page inspected. `python tools/validate.py` passes 44 objects, index generation is deterministic, and 22 tooling tests pass. |
| PASS-RUN-GADDIS-8E-CH14S05 | One-unit PASS run: *Starting Out with C++*, 8th ed., §14.5 “Operator Overloading” | Codex | review | Base: master at `8db51d4`; seven new objects, one absorbed method variant, and three deliberate rejections. `python tools/validate.py` passes 51 objects, indexes are deterministic, and 22 tooling tests pass. |
| PASS-PROC-VARIANT-RECOVERY | Add a decision-versus-method recovery checkpoint before PASS dispositions | Codex | review | Base: master at `f5f7889`; recovery check added to second read, disposition, and ledger rules. `python tools/validate.py` passes 51 objects, indexes are deterministic, and 22 tooling tests pass. |
| PASS-DOCTRINE-MULTI-SOURCE-STANCE | State that sources are evidence of routes, not proof that one route is exclusive | Codex | review | Base: master at `320b172`; doctrine and spec decision now require contrast-seeking without inventing unsupported alternatives. |
| PASS-PROC-SOURCE-LIFECYCLE | Formalize source-native units, explicit selection, payload retirement, and domain-evidence checks | Codex | review | Base: master at `22f5063`. Documentation-only update; source retirement is now reversible and gitignored, and the rendering helper is logged as PASS-TOOL-RENDER `spec-needed`. |
| PASS-TOOL-RENDER | PDF renderer + corpus integrity improvements | Codex | review | Base: master at `f8672c8`; renderer verifies every requested PNG and falls back from the broken wrapper. Ledger v2 is enforced for revised ledgers; indexes expose variants. `python tools/validate.py` passes 54 objects; 26 tooling tests pass. |
| PASS-DOCTRINE-UNIVERSAL-PLACEMENT | Define one foundation / variant / specialization placement model for every skill family | Codex | review | Base: master at `e370ea0`; documentation-only. `python tools/validate.py` passes 54 objects; index generation is deterministic (14 files, zero changes); `git diff --check` passes. |
| PASS-MIG-UNIVERSAL-LANES | Rehome existing cards into foundation and specialization browse lanes where actual retrieval needs justify it | Unassigned | spec-needed | Requires a source-grounded placement inventory and one coordinated `library_path` migration; do not move cards mechanically or infer tags from paths. |
| PASS-RECOVER-TCPL-CH19-ACCOUNTING | Recover or reject TCPL Chapter 19's missing candidate, then migrate its ledger to v2 | Unassigned | spec-needed | The 11-candidate report has ten ledger rows. Source grounding must determine the missing row; do not invent a disposition to satisfy accounting. |
| PASS-TOOL-RENDER-4DIGIT | Correct PDF-render expected-output naming for pages 1000 and above | Unassigned | spec-needed | `tools/render_pdf.py` creates valid four-digit Poppler filenames but tests only three-digit names, so visual PASS runs falsely fail. Add a focused regression fixture before changing the helper. |
| PASS-TOOL-RENDER-FRESH-PREFIX | Make PDF-render output verification agree with created fresh-prefix PNGs | Unassigned | spec-needed | Starkey PDF pp. 233-239 wrote all seven PNGs under a fresh nested prefix but returned exit 3 and named them missing; a rerun then refused those existing files. Add a regression fixture for a new nested output directory and make the return code agree with verified outputs. |

| PASS-MIG-SE-FOUNDATIONS | Encode foundations-first read order across the software-engineering corpus | Claude | review | Decision 2 (refined). COMPLETE. All 10 topics carry `prerequisite_for` read-order (foundation -> its techniques); a package spine links the four-goals root -> the six pillars + three theory foundations, giving a single read-first entry point. `tools/build_index.py` now renders a deterministic `## Reading order` per directory (regen is idempotent). `python tools/validate.py` passes 124; build_index second run changes 0 files. |
| PASS-SCHEMA-VISUAL-REFERENCES | Add original-art `references:` to the object schema for visual skills, plus the generate-and-review pipeline | Codex | review | User-authorized first-party exception complete: `rights: first_party` permits only reviewed `origin: first_party_source` assets; unmarked/third-party sources remain generated-art-only. `python -m unittest discover -s tests -v` (32), `validate.py`, `verify_grounding.py --source gen1_art_fundamentals_4step`, `verify_references.py`, and deterministic index regeneration pass. |

| PASS-RUN-HOGARTH-DYNAMIC-FIGURE-CH04 | One-unit guided PASS run: *Dynamic Figure Drawing*, Chapter 4 | GPT | done | Base: `PASS_WuSao_Ch_4.zip` plus SkillForge discovery overlay. Eight new objects, one hand variant, Stage 2 lock and visual-registration safeguards, guided memcap, and full ledger/index updates. The prior portability conclusion was reverted: the hosted project exposed repository files but did not activate SkillForge as a runtime, so the image sequence was an invalid SkillForge test. |

## Completed (archived — full detail in git history)

- _(one terse line per finished assignment)_
- PASS-RUN-PROGRAMMERS-BRAIN-CH01-02 — *The Programmer's Brain* Ch.1-2 (Codex, reviewed by Claude 2026-08-01, `done`). 10 new `foundations/code-comprehension` objects + 4 variants absorbed into gcbc readability; 5 rejections. All 10 of Codex's dispositions upheld on review — no under-linking, no over-forcing. Review added one missed variant (`v_cognition_visually_distinct_identifiers` on `PAT_use_descriptive_names`, p. 17), the p.25 recall-order step in `DRILL_reproduce_code_to_diagnose_knowledge`, two recorded rejections, and fixed paragraph separation in two variant Notes. Source active at 2/13.
- PASS-RUN-HOGARTH-DYNAMIC-FIGURE-CH01 — closed failed 2026-08-01; all Chapter 1 outputs and source state removed after expert review found extraction and image-quality failures.
- PASS-RUN-HOGARTH-DYNAMIC-FIGURE-CH02 — closed failed 2026-08-01; incomplete Chapter 2 drafts and generated references deleted without shipping.

## Standing guardrails for all assignments

Project-wide rules that outlive any single assignment. Keep this list short and
real — every line should have cost something to learn.

- ACCEPTANCE GATE: `python tools/validate.py` (card shape) AND `python
  tools/verify_grounding.py --source <id>` (proof the source was actually read)
  must both exit 0 before a corpus object is described as validated. Regenerate
  navigation with `python tools/build_index.py`; generated indexes must not be
  hand-edited.
- SOURCE ROUTING: **visual** sources (figure drawing, anatomy, comics, diagram-
  heavy books) go to a vision-capable assistant with an image renderer or a
  preflighted page-image set, plus an image generator for shippable references
  (Codex/GPT); **text/technical** sources (coding, math, writing) go to the
  assistant that parses text fastest (Claude). A `visual: true` source is never
  claimed by a text-only checkout. Run `tools/preflight_pdf.py` before admission;
  `NEEDS_OCR` means stop before hashing or scaffolding. Pair per-page OCR text
  with its page image during the run. See `docs/PASS/PASS_GROUNDING.md`.
- ANTI-SKIM: every `processed` unit needs a verified `## Reading receipt`
  (`docs/PASS/PASS_GROUNDING.md`). Structured output is not evidence of grounding;
  verbatim quotes re-checked against the payload are. "Don't skim" as prose does
  nothing — the gate is the enforcement.
- Danger zones: see `AGENTS.md` → Danger zones.
- `docs/PASS/PASS_SCHEMA.md` is the source of truth for card shape. A card that
  disagrees with it is the card's bug — do not widen the schema to accommodate
  one card. `PASS_v20.6_ABSOLUTE_SPEC_FLAT.md` is superseded; do not run from it.
- A schema change is never a local edit. Changing an object template invalidates
  every existing card of that type. Log the decision in
  `docs/domains/spec/decisions.md` before touching cards.
- Extraction is **one unit per run** (`docs/PASS/PASS_RUN.md`). Never a whole book
  in one pass — unit size is what keeps grounding cheaper than template-stamping.
- **Fail closed.** If a unit cannot actually be read, mark it `blocked` with a
  reason and emit no objects. Structured output is not evidence of grounding.
- Never merge "the archive." Merge one candidate against ~5 retrieved neighbours.
- **A source is admitted only through `ledger/REGISTRY.md`, keyed on sha256.**
  Preflight PDFs first, then hash the final readable file and check the registry
  BEFORE creating a source_id or a ledger
  folder. Hash already present = already read; stop. Filenames and titles drift,
  content does not.
- _(add invariants, naming rules, and "never do this again" lessons as earned)_
