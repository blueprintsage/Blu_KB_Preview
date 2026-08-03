# Spec Worklog

status: active
owner: docs/domains/spec
last_reviewed: 2026-08-02

Newest entry first.

## 2026-08-02 - SkillForge balance and limitation-aware consumption

### What changed

Reframed SkillForge as external practice memory that guides native capability
without replacing it. Added scoped authority for retrieved cards, a practical-exam
preflight, medium-appropriate references and examples, explicit AP/Pattern/Drill
use-time roles, an avoidance check for known weaknesses, and diagnosis-led revision
that preserves what already works. Updated the Claude SkillForge adapter and the
resolver's consumption-contract label to match. No object schema or corpus card was
changed.

### What was tested or reviewed

Reviewed the new language against the existing foundation/specialization model, the
optional visual-reference decision, the universal stage scaffold, and the current
resolver behavior. Searched active docs and adapter text for the superseded
unqualified "overrides the prior" wording and corrected the active contradiction in
`PASS_CONSUMPTION.md` that still said a future loader should refuse visual cards with
no reference. `python -m unittest discover -s tests -v` passed 35 tests;
`python tools/validate.py` passed 232 objects; two consecutive
`python tools/build_index.py` runs changed zero repository files; a sample resolver
call loaded the revised scoped-authority contract plus the hand, foot, and staged
figure cards; `git diff --check` passed.

### What worked

The contract now expresses both sides of the intended balance: a model may not ignore
an applicable grounded skill, but a retrieved card cannot govern outside its IF
clause. The same doctrine now covers visual references, code examples, writing
formats, and teaching demonstrations without adding a new object type or widening
the closed schema.

### What failed

The fresh working copy had not persisted in the runtime and had to be restored from
`PASS(1).zip` at base `cfe2419`. The archive preserved the pre-existing deletion of
`sources/README.md` and untracked `.claude/settings.local.json`; neither was touched.
`python tools/verify_references.py` still reports two pre-existing missing-source
issues for `sources/gen1_art_fundamentals_4step/4step_figure_process_1.png`, referenced
by the onion-skin AP and gesture-to-masses Pattern. This assignment did not alter
those cards or their assets.

### Known risks

The resolver can load and order cards, but it cannot mechanically guarantee humble
inspection, avoidance detection, or diagnosis-led revision after context is loaded.
Those remain execution and review responsibilities. Medium-specific non-image
examples currently live in card bodies, variants, and tests rather than a new common
asset field; this is deliberate until real usage proves a schema need.

### Next safe step

Exercise the revised contract on the next art, code, and writing tasks and record
whether it reduces blind retries without over-constraining invention. Add loader
mechanics only for failure modes observed in those runs.

### Files changed

`docs/PASS/PASS_DOCTRINE.md`, `docs/PASS/PASS_CONSUMPTION.md`,
`.claude/skills/skillforge/SKILL.md`, `tools/resolve.py`,
`docs/domains/spec/{decisions.md,worklog.md}`, and
`docs/worklogs/assignments.md`.

## 2026-08-01 - Visual-source cards may ship references-optional

### What changed

Retired the rule-23 mandatory-reference clause: a card from a `visual: true` source
may now ship with `references: []`. Removed the check in
`tools/validate.py::validate_visual_references` and the matching hard-rule bullet in
`PASS_SCHEMA.md §1`; rewrote the `PASS_CONSUMPTION.md` visual section from a hard gate
to first-party-when-present plus a stated text-only ceiling. Set `references: []` on
the 17 Hogarth figure-construction cards that cited the now-deleted generated plates
(`assets/reference_*.png`). Recorded the reasoning in `docs/domains/spec/decisions.md`.

### What was tested or reviewed

`python tools/validate.py` = PASS, 232 objects (was FAIL, 17 rule-23 image-missing
errors). `python tools/verify_references.py` = OK. `python -m unittest discover -s
tests` = 35 passed (no test asserted the removed clause). `python tools/build_index.py`
twice = 4 changed then 0; the 4 were stale indexes from commit e0f9f6c, which shipped
`AP_draw_a_figure_through_onion_skinned_stages` but an art index still reading 18
objects — now corrected to 19.

### What worked

The rule change and the card edits are consistent: references that remain (the two
first-party `source_staged` cards) still validate fully; the removed ones no longer
force a generated stand-in.

### What failed / still open

Removing the mechanical guarantee shifts weight onto consumption-time judgment, which
is not loader-enforced. Whether `origin: generated` should be banned outright (not
just unused) is a separate decision, not taken here. The 3 surviving `source_staged`
references still carry the whole visual-grounding load for figure construction.

### Known risks

A future visual card can now ship as text with no reference and no warning; the
consumption contract, not the validator, is what says a text-only model must not pass
that off as the drawing.

### Next safe step

If generated references are meant to be permanently disallowed, ban `origin: generated`
in rule 23 and update the schema; otherwise leave the origin vocabulary intact.

### Files changed

`tools/validate.py`, `docs/PASS/PASS_SCHEMA.md`, `docs/PASS/PASS_CONSUMPTION.md`,
`docs/domains/spec/decisions.md`, the 17 figure-construction cards, regenerated art
indexes, this worklog.

## 2026-07-31 - Closed Original-Art References for Visual Skills

### What changed

Added the closed `references:` frontmatter field, the original-art rule, the
narrow cross-craft `metaskills` exemption, and the consumption/release contract.
Added the first reviewed visual card, `Build Gesture Into Clear Masses`, with an
original generated teaching image rather than a source plate.

### What was tested or reviewed

Reviewed the generated diagram against its construction claim and recorded that
review in its sidecar. Ran schema validation, source grounding, visual-reference
review, index generation, and the tooling suite.

### What worked

The initial generated line drawing was rejected as structurally too similar to
the source render. A materially distinct color-manekin diagram passed the
similarity check and the recorded visual review.

### What failed / still open

Loader enforcement remains a SkillForge gap; the repository gate now enforces
release, not use-time loading.

### Known risks

The similarity threshold is a conservative heuristic, so human or vision review
remains required for the image's teaching claim.

### Next safe step

Use the generator and review gate for every new visual-source card before it is
marked for release.

### Files changed

`docs/PASS/{PASS_SCHEMA.md,PASS_GROUNDING.md,PASS_CONSUMPTION.md}`, the visual
card and its source ledger, plus the schema decision and assignment log.

## 2026-07-31 - Authorized First-Party Source Reference Exception

### What changed

Added the user-authorized `rights: first_party` / `origin: first_party_source`
exception and changed the Gen 1 visual card to use the authorized staged figure
plate directly, with provenance and a completed review record.

### What was tested or reviewed

Ran all release gates and the 32-test tooling suite, including the new failure
fixture for a first-party origin without an explicit rights declaration.

### What worked

Direct source reuse is allowed only for the explicitly marked Gen 1 archive;
unmarked visual sources still fail closed.

### What failed / still open

No new gap.

### Known risks

The declaration is deliberately explicit: a source's location, author, or past
assistant involvement is never treated as sufficient rights evidence.

### Next safe step

Mark another archive first-party only when its rights holder gives the same
authorization.

### Files changed

`PASS_SCHEMA.md`, `PASS_GROUNDING.md`, the Gen 1 source/card/assets, validation
tools, tests, and assignment log.

## 2026-07-30 - Universal Foundation and Specialization Placement

### What changed

Defined one relationship model for every PASS skill family: portable foundations,
same-decision method variants, and constraint-bound specializations. The doctrine,
schema, library contract, and run retrieval now name all supported specialization
axes rather than treating language as the implicit norm. Tags are explicitly the
cross-cutting retrieval key, while folder lanes are optional browse aids.

### What was tested or reviewed

Reviewed the rule against the user's vehicle, figure-construction, manga, comics,
life-drawing, resume-writing, technical-writing, and language examples. Checked
the revised specification documents for a consistent foundation/variant/
specialization distinction and preserved the closed object schema. Ran `python
tools/validate.py` (54 objects pass), generated indexes twice (14 files, zero
changes both times), and ran `git diff --check` (no issues).

### What worked

The rule explains both shared technique and meaningful difference without
creating source buckets. It permits helpful paths such as `languages/python` or
`domains/mechanical_figures` only when a real specialization exists, while the
frontmatter relationship and tags keep the shared foundation discoverable.

### What failed / still open

No cards were moved. Existing paths remain valid, so the physical-library lane
migration is intentionally a separately scoped gap rather than an unreviewed
bulk relocation.

### Known risks

Without a controlled tag vocabulary, equivalent contexts may be tagged with
different spellings and weaken retrieval. Do not add a vocabulary or validator
rule until enough real cross-domain cards establish the needed terms.

### Next safe step

Use the rule on the next cross-context PASS run, then scope the existing-card
lane migration from actual retrieval needs rather than by path churn alone.

### Files changed

`docs/PASS/{PASS_DOCTRINE.md,PASS_SCHEMA.md,PASS_LIBRARY.md,PASS_RUN.md}`,
`docs/domains/spec/{decisions.md,worklog.md,next_steps.md}`, and
`docs/worklogs/assignments.md`.

## 2026-07-30 - Sources Are Routes, Not Exclusive Authority

### What changed

Added the multi-source learning stance to PASS doctrine: a source is evidence for one route, not proof that the route is exclusive. A same-topic source must be treated as a contrast opportunity for grounded alternatives, while unsupported alternatives remain forbidden.

### What was tested or reviewed

Reviewed the doctrine wording against the Gaddis and Stroustrup operator-overloading runs and the new decision-versus-method variant recovery procedure.

### What worked

The rule explains why variants matter without weakening source grounding. It connects the library's purpose—learning when to choose a route—to the actual merge behavior.

### What failed / still open

No doctrinal contradiction was found. Whether the contrast stance finds useful variants without producing noise remains an empirical question for the next same-domain run.

### Known risks

An assistant could mistake every different example for a different route. The decision requires a durable change in method, constraint, or tradeoff, and never permits invented alternatives.

### Next safe step

Run a related C++ unit using the recovery checkpoint, then assess whether its candidate ledger distinguishes genuine routes from merely different examples.

### Files changed

`docs/PASS/PASS_DOCTRINE.md`, `docs/domains/spec/{decisions.md,worklog.md,next_steps.md}`, and `docs/worklogs/assignments.md`.

## 2026-07-30 - Authorized Variable-Depth SkillForge Library Paths

### What changed

Defined `library_path` as the variable-depth placement contract. Its first
segment is the independently installable package; later segments are navigation
topics. `metaskills` is mandatory and carries the universal construction AP as
the SkillForge bootstrap entry.

### What was tested or reviewed

Compared the existing two-level schema with current library paths and the
SkillForge packaging requirement.

### What worked

The new list describes both existing shallow software paths and the deeper art
path without duplicate metadata or empty directory levels.

### What failed / still open

Current cards and templates still use the superseded fields. The validator and
generator do not exist yet.

### Known risks

The package bootstrap can be declared in generated indexes, but a future
SkillForge consumer must enforce the declared load order at runtime.

### Next safe step

Migrate every current object and template to `library_path`, then implement the
validator and recursive index generator.

### Files changed

`docs/domains/spec/decisions.md`, `docs/domains/spec/worklog.md`, and assignment
log.

## 2026-07-29 - <short title>

### What changed

### What was tested or reviewed

### What worked

### What failed / still open

### Known risks

### Next safe step

### Files changed
