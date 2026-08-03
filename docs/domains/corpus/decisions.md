# Corpus Decisions

status: active
owner: docs/domains/corpus
last_reviewed: 2026-08-01

Dated, newest first. A decision belongs here once it would be expensive to
re-litigate. Record the REASON, not just the choice - the reason is what tells a
future reader whether the decision still holds.

## 2026-08-01 - Artistic drawing requests route through a runtime skill

- `skills/drawing/SKILL.md` is the consumption entrypoint for requests to draw,
  sketch, illustrate, paint, render, or create concept art. It loads the universal
  iterative-construction AP first, then the specialist onion-skinned drawing AP,
  then only the matching Patterns and their reviewed visual references.
- Final-only requests still execute the hidden construction stages. Visible
  process requests use the preceding accepted artifact as the next stage's edit
  source rather than independently regenerating each panel.
- The current figure AP is authoritative for figures and creatures and provisional
  for vehicles, objects, and environments until those domains prove a need for
  specialist APs.
- Reason: creating an AP in the library did not make ordinary image requests
  retrieve it. The surfer used AP language only because it was manually inserted
  into the prompt; the direct Camaro render bypassed the library entirely.

## 2026-08-01 - Step 2 is a structural commitment gate

- Step 1 may retain faint searching alternatives while the artist locates a pose.
  By the end of Step 2, one coherent position must be chosen for every major
  mass, limb, joint, attachment, support/contact point, and overlap. Rejected
  paths are removed or clearly subordinated.
- Step 3 develops the chosen construction; it does not decide competing limb
  positions or relocate load-bearing structure. If it must, the AP returns to
  Step 2 before anatomy or design specificity continues.
- Reason: the first AP field test produced a convincing final figure, but its leg
  position remained undecided through the block and was solved only during the
  specific-form pass. That made Step 3 repair structure while also developing it.

## 2026-08-01 - Figure drawing uses onion-skinned artifact continuity

- A figure-drawing AP chains the relevant patterns through defined refinement
  stages; it does not replace those patterns with one oversized technique card.
  A Drill is a short warm-up, diagnostic, or corrective side study that may run
  before the piece or when a stage exposes a weakness.
- Every visible stage develops the accepted preceding artifact as an underdrawing,
  edit source, or light-board layer. Independent generations that merely restate
  the prompt are not a staged drawing sequence because viewpoint, landmarks,
  attachments, and proportions drift.
- A requested drawing must depict forms occupying pictorial space. Labels, panels,
  arrows, and flat symbols may support an explicitly requested diagram, but they
  cannot substitute for overlap, recession, turning planes, attachment, support,
  and foreshortening in artistic work.
- Reason: the rejected Chapter 1 references explained parts without drawing depth,
  while the turtle tests showed that an artistically constructed final can reduce
  backward to coherent block and framework stages.

## 2026-08-01 - Art books use paired per-page text and visual reading

- An art-book unit is read from two aligned channels: OCR/pdftotext supplies the
  prose and the corresponding page image supplies the instructional art. The
  assistant does not reread rasterized prose unless layout carries meaning.
- Every bounded page is visually scanned at overview resolution; pages that
  ground candidates are revisited at full resolution. First, middle, and last
  page mappings are visually confirmed before a source-provided archive is
  trusted.
- No usable text layer is an admission blocker, not a reason to spend vision
  tokens transcribing the scan. No vision-capable model or page-image path is a
  hard blocker because text cannot substitute for the art.

## 2026-08-01 - Default read method is pdftotext for text sources

- The token-cheapest way to actually read a unit is `pdftotext` page-range
  extraction, not a rendered-page read or a whole-document reader. Codified in
  `PASS_RUN.md` §3.
- Evidence: it kept Claude's Effective C++ runs lean across all 9 chapters;
  Codex, reading pages natively, hit the context wall and paid a compaction tax
  (~11% context bought for ~11% of a weekly token budget) on a two-chapter run.
- Convention: `pdftotext` default for text sources (coding/math/writing);
  `pdftotext -layout` when code alignment, tables, or columns matter; render
  (`tools/render_pdf.py`) only for `visual: true` sources or layout-carrying
  units; empty/garbled extraction means no text layer → render/OCR or `blocked`.
- Caveat: plain `pdftotext` mangles code formatting (wrapped lines, interleaved
  comments), so `-layout` or a spot render is the fallback when exact code layout
  matters. This does not weaken grounding — the reading-receipt and
  visual-inspection rules for layout-carrying units are unchanged.
- Reason: reduces context load so small-window assistants avoid compaction; the
  fix lives in the read procedure, not in each assistant's memory, so every run
  gets it by default (Codex missed it only because the doc had not said it).

## 2026-08-01 - Context window is a first-order PASS constraint; one unit per chat

- §6 (place each candidate against the library) scales with **library size, not
  unit size**. The per-unit design bounds the reading (one chapter) but not the
  neighbour comparison, which grows as the corpus grows.
- Evidence: Codex (GPT-5.6, 258k window) reached ~89% context on Chapter 2 of a
  two-chapter run and could not hold two units. Claude (1M) has more headroom but
  only postpones the same wall.
- Therefore **run one unit per chat.** State lives in files (ledger + library),
  so a fresh chat resumes cleanly from the ledger — there is no need to hold a
  whole run in one context. Parallel runs use separate worktrees/branches
  (`assignments.md` rule 8); this was observed working (`codex/programmers-brain-ch1-2`).
- §6 discipline that reduces the load: retrieve ~5 neighbours per candidate, not
  the archive ("tighten if it returns 40"); skim 2-3 exemplar cards for the
  quality bar, never a whole lane. Over-broad retrieval, not model size alone, is
  what fills the window fastest.
- Durable fix tracked as `PASS-TOOL-RETRIEVAL` in `assignments.md`: a retrieval
  index so §6 reads O(5), not O(library).

## 2026-07-30 - Ledger v2 stores a variant's choice, method, and tradeoff

- New or revised unit ledgers declare `ledger_format: 2` and a `candidate_count`
  that must reconcile with their candidate rows.
- A variant row keeps its foundation in `object_id` and separately records the
  learner decision, `variant_basis`, method or policy, and tradeoff. The fields
  turn the recovery checkpoint into reviewable evidence rather than a sentence
  that can be omitted or blurred.
- Existing ledgers migrate only when their unit is otherwise revised. The TCPL
  Chapter 19 mismatch remains an explicit historical gap until the missing claim
  is recovered or genuinely rejected.

## 2026-07-30 - Reconcile by learner decision and method, not source construct

- Before a candidate is placed, identify the learner decision it teaches, the
  source's method or policy, and the resulting tradeoff.
- Same decision plus a different valid method, sequence, policy, or constraint
  is a `variant`, not a rejection. A source example can support both a new
  decision and a variant of an existing decision; split them into separate
  candidates even when their locator is identical.
- The Gaddis `IntArray` example exposed the need: returning a reference from a
  mutable subscript was new, while checking every bracket access was a variant of
  the library's separate checked-access policy.
- This preserves PASS as skill acquisition. It retains the competing choice a
  practitioner must learn to recognize, instead of flattening sources into a
  catalogue of language constructs.

## 2026-07-30 - Source-native units and explicit selection

- A numbered lesson, section, or bounded section range is a valid PASS unit when
  it is the smallest coherent instructional scope; a chapter remains the default.
- The first queued unit remains the default choice, but an explicit user-selected
  queued unit may be processed out of order and must be identified in its unit
  notes.
- This avoids treating a source's editorial hierarchy as more important than the
  grounding size that keeps a two-pass extraction viable.

## 2026-07-30 - Retire closed payload to local trash

- After source reconciliation closes every unit and records a final status, move
  the payload to `trash/sources/<source_id>/<original filename>`.
- The move is reversible local quarantine, never deletion, and the payload stays
  ignored by Git.
- `SOURCE.md` records the current repo-relative `payload_path`; SHA-256, not the
  path, remains the source identity and duplicate guard.

## 2026-07-29 - <decision>

- What was decided.
- Why (the constraint or evidence that forced it).
- What was rejected, and why.
- What this now forbids.

## 2026-08-02 — Guided Chapter 2 figure notation is a strict Stage 2 dependency order

**Decided.** For Hogarth Chapter 2, the default human-figure notation order is
`torso → legs → arms → head`. It is not merely an importance ranking. Step 1 may
abbreviate primitives as experience grows, Stage 2 follows the order strictly,
Stage 3 retains it more loosely over solved form, and Stage 4 integrates across
the image as finish requires. Rare exceptions must follow the pose's actual
support mechanics, not convenience.

**Centerline.** The accepted Step 1 action line becomes the Stage 2 torso
centerline. The masses are built around it; the line is not inserted afterward to
explain independently placed forms. It is the action's Wu Sao and constrains the
believable response of every attached form.

**Stage boundary.** Hands, feet, yokes, attachments, weight, balance, and head-neck
range must already read in Stage 2. A front or rear shoulder yoke is a temporary
Stage 2 construction and must not remain necessary in Stage 3. Chapter 2 may
diagnose the lumpy separation of forms in deep recession, but its own Drill does
not pretend to teach the Chapter 3 unity remedy.

**References.** No Chapter 2-specific canonical teaching images are generated now.
The existing four-step sheets are valid apprenticeship artifacts and general
continuity references, but permanent chapter references will be earned only after
all foundational lessons have been studied, practised, and consolidated.
