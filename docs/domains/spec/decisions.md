# Spec Decisions

status: active
owner: docs/domains/spec
last_reviewed: 2026-08-02

Dated, newest first. A decision belongs here once it would be expensive to
re-litigate. Record the REASON, not just the choice - the reason is what tells a
future reader whether the decision still holds.

## 2026-08-02 - SkillForge is scoped external practice memory, not a replacement mind

**Decided.** A retrieved skill is authoritative for the learner decision named by
its IF/THEN, but not for the whole task. The user and active project define the
job; the model retains responsibility for recognition, invention, subject
knowledge, adaptation, and uncovered decisions. SkillForge supplies grounded
practice memory: procedures, known traps, stage boundaries, examples, and checks.

**Why.** The earlier unqualified phrase "the library overrides the model's prior"
correctly prevented the model from ignoring what it had been taught, but it also
implied domination. That is the opposite of the intended balance. A practitioner
uses notes and references to reinforce judgment, not to surrender it. Both silent
improvisation and mechanical over-application are consumption failures.

**Operational consequence.** Treat each non-trivial task as a practical exam:
retrieve a bounded skillset, identify known risks, study medium-appropriate
precedents, work in stage order, inspect the result, and revise the diagnosed
failure while preserving what worked. APs organize workflows, Patterns govern
local decisions, and Drills strengthen weak execution.

**References by medium.** Visual art benefits from staged drawings and spatial
construction studies; code from working examples, tests, and failure cases;
writing from dialogue formats, structural samples, and revision pairs; teaching
from demonstrations and exercise progressions. These precedents are backstops,
not templates.

**Avoidance rule.** A known limitation is a reason to prepare and practise, not a
license to crop, omit, hide, or simplify away a required part of the task. A
legitimate design choice remains allowed; repeated convenience that evades the
request is a failure signal.

**Supersedes in part.** This refines Decision 3 under the 2026-07-31 learning
architecture entry. "Golden truth" now means scoped authority over the decision a
card actually teaches, not replacement of the model's broader capability.

## 2026-08-01 - A visual-source card may ship as a text extraction (references optional)

**Decided.** Rule 23 no longer requires a card from a `visual: true` source to carry
at least one reference. Such a card may ship with `references: []`. References that
ARE present are still fully validated (well-formed, image exists, under the topic
folder, `review: passed`, valid origin, similarity gate).

**Why.** Generated teaching references were removed from the corpus; only first-party
staged references remain. With generated references gone, a mandatory-reference rule
would force generated ones back for every card lacking a first-party image — the
opposite of the intent. A first-party reference is included only when it genuinely
illustrates the card's move, never manufactured to satisfy a gate. The cost is that
the mechanical guarantee "every visual card has a reference" is gone; the consumption
contract now carries that weight as judgment (`PASS_CONSUMPTION.md`, visual section):
work against a first-party reference when present, and recognize that a text-only
model applying a visual card can explain construction but cannot produce the figure.

**Scope.** Removed the mandatory clause in `tools/validate.py::validate_visual_references`
and the corresponding hard-rule bullet in `PASS_SCHEMA.md §1`. The 17 Hogarth
figure-construction cards that cited the deleted generated plates were set to
`references: []`. No change to origin values or the similarity gate.

## 2026-07-30 - Every skill family shares foundation, variant, and specialization relationships

**Decided.** PASS uses one internal relationship model for every skill family.
A foundation carries the portable learner decision; a variant remains inside its
foundation when the decision is unchanged but the method, sequence, emphasis, or
tradeoff differs; a specialization is a separate card only when its IF/THEN
needs a language, tool, framework, medium, style, genre, tradition, method, or
domain constraint. `tags` are the cross-cutting retrieval mechanism, and
`foundation_object_id` makes the relationship explicit when both cards exist.

**Navigation.** `library_path` remains topic-first, but a large package may add
readable lanes such as `foundations`, `languages`, `media`, `styles`, or
`domains`. A language branch is valid only as a branch of genuine
specializations; it does not replace the general foundation or turn the source
language into the package root. The same holds for manga, comics, life drawing,
resume writing, and technical writing. These are paths only when they name a
durable learner route; otherwise they remain tags or variants.

**Why.** A tank and a car share vehicle-construction decisions but tanks require
track, turret, armour, and terrain constraints. That is the same relationship as
a language-specific implementation built on a cross-language programming skill,
or resume-writing tactics built on general writing decisions. Treating every
source context as a parallel tree hides the reusable skill; flattening every
context into a foundation erases real constraints.

**Rejected: source- or style-first taxonomy.** A book, school, or broad context
does not define the skill. Do not create `manga`, `comics`, or `transformers`
folders solely because of source provenance.

**Rejected: mandatory literal folder names.** The relationship is universal, but
a small package need not manufacture an empty `foundations` directory. The
closed frontmatter fields govern meaning; the path is only a human browse route.

**Migration.** Existing topic-first paths remain valid. A controlled library-wide
lane migration is separately tracked before any blanket rehome; no card is moved
as a side effect of this doctrine decision.

**Supersedes in part.** The 2026-07-30 placement decision's ban on language
tokens anywhere below the package is replaced by the specialization-lane rule
above. Its ban on language-first package roots and fused topic names remains.

## 2026-07-30 - Sources demonstrate routes; they do not define exclusive truth

**Decided.** PASS treats a source as grounded evidence for one route through a
craft decision, not as proof that its route is the only correct one. A later
source on the same topic is a contrast opportunity: look for a different method,
sequence, constraint, or tradeoff that changes when a practitioner should choose
it. Preserve that grounded difference as a variant; keep it separate from a new
skill when one example teaches both.

**Why.** A learner becomes better by understanding which route fits the
situation, not by memorizing the first textbook's local convention. Gaddis's
always-checked subscript policy was the concrete counterpoint to Stroustrup's
separate checked-access route.

**Rejected: treating every later source as confirmation.** It turns the library
into a source-ranked restatement of one approach and silently loses alternatives.

**What this forbids.** Do not call a source's route universal without evidence;
do not fabricate alternatives merely to populate variants. Both the route and its
contrast must be grounded in the source material.

## 2026-07-30 - Variable-depth `library_path` replaces fixed two-level placement

**Decided.** Every PASS object uses a required `library_path` list instead of
`category` and `subcategory`. It has at least two lowercase path segments:

```yaml
library_path: [art, drawing, figure-construction]
library_path: [software_development, class_design]
library_path: [metaskills, iterative-construction]
```

The first segment is the **package**: an independently installable skill family.
Every later segment is a human-readable navigation topic. The directory is
derived exactly from that list, so a package may be shallow or deeply nested
without inventing empty taxonomy levels. `metaskills` is the mandatory package;
its universal construction AP is the bootstrap object SkillForge loads before
any selected optional package.

**Why.** A fixed two-level path cannot represent the existing art tree without
lying in frontmatter, and it cannot separate installable packages from their
internal topics. A list keeps one placement source of truth, makes root-to-leaf
indexes mechanical, and preserves human navigation.

**Rejected: fixed three fields (`package` / `category` / `subcategory`).** It
would merely move the same rigidity one level deeper; metaskills need fewer
levels than art, and later domains may need more.

**What this now forbids.** `category` and `subcategory` are not valid object
keys. Hand-maintained indexes and package manifests remain invalid. A path that
does not exactly match `library_path` fails validation.

**Migration.** Convert every current object and template before enabling the
index generator. The former placement decision below is superseded only with
respect to the two fixed fields; its topic-first rule still governs the content
of path segments.

## 2026-07-30 — Placement is topic-first; language rides in frontmatter

**Decided.** `category` is the **craft domain**. `subcategory` is the **topic
within it**. Language, tool, and framework are expressed in `tags` plus
`specialization_axis` — never fused into the path.

```
category:            software_development
subcategory:         class_design
tags:                [cpp, operator_overloading]
specialization_axis: language
```

Separator is **underscore** in `category`, `subcategory`, and `tags`, matching
filenames (`PAT_allocate_before_release.md`) and the earlier DungeonForge corpus
(`architecture_design`, `memory_performance`).

**Rejected: language-first (`cpp/class_design`).** It breaks genericization, which
is a core doctrine move. A skill stripped of its C++ specifics to become a
portable foundation has nowhere to live under `cpp/` — it would need a parallel
`general/` tree, putting a foundation and its own variant in different branches.
That is precisely what the placement law forbids: cross-domain reusable knowledge
must not stay trapped inside a narrow source or variant bucket. It also duplicates
the whole subcategory tree per language (`cpp/class_design`, `java/class_design`,
…) and makes cross-language relationships invisible in the layout.

**Rejected: language fused into subcategory (`software_development/cpp_class_design`).**
What the first run actually produced. Same objection in milder form — the
subcategory stops being a topic and becomes a topic-language compound, so a
portable version of the same skill cannot share the bucket.

**What this forbids.** No language, library, framework, or version token in
`category` or `subcategory`. If a skill is language-specific, that is what
`specialization_axis: language` and `tags` are for.

**Applied.** The 10 TCPL ch19 objects moved
`software-development/cpp-class-design/` → `software_development/class_design/`.

**Still open — the category vocabulary is uncontrolled.** Nothing stops the next
source inventing `programming/` or `cpp_dev/` beside `software_development/`. This
is the same closed-vocabulary problem as the object schema and probably wants the
same answer: a controlled list the validator checks. Deferred until there are
enough sources to know what the real categories are — inventing a taxonomy before
the content exists is how the old spec went wrong.

**Resolved 2026-07-30 — default to `foundation`; genericization deferred.**

Objects default to:

```
foundation_role:      foundation
routing_class:        general
specialization_axis:  none
foundation_object_id: none
```

Mark `specialization` (with `routing_class: specialized`,
`specialization_axis: language`) **only when the pattern's IF/THEN cannot be stated
without naming a language-specific construct** — `operator""` literals, `friend`,
prefix/postfix `++` overloading, class-scoped `operator new`, C++ member-vs-nonmember
conversion rules. Implementation detail in `Do`/`Don't` may be language-flavoured
without making the pattern a specialization; the test is the rule, not the prose.

`foundation_role: specialization` with `foundation_object_id: none` **is legal.** It
means the portable foundation has not been extracted yet, which is a normal state,
not an error. The link gets made if and when that foundation appears.

**Why genericization is deferred.** Its value scales with language diversity, and
the library currently holds one language. A foundation with no sibling
specializations unifies nothing. Building the hierarchy now would also force a
foundation lookup on every candidate — bounded by subcategory and tags, but real
work serving a case that does not exist. When a second language produces a genuine
collision, genericize *that pair*, against neighbours already retrieved for the
merge step. One case at a time, not a rule enforced hundreds of times.

**Rejected: language-first placement, reconsidered.** Revisited after the retrieval
cost surfaced. It would make lookup trivial and delete the whole genericization
apparatus, but it duplicates the same skill per language with no link between
copies, turning a skill library into per-language notes. Deferring genericization
gets the same simplicity today at none of that cost, and keeps the door open.

**Applied to the ch19 objects.** 4 of 10 flipped to `foundation`/`general`/`none`:
stateful function objects, checked-vs-unchecked access, discriminated short
representation, allocate-before-release — each stateable without a C++ construct.
The remaining 6 are genuinely C++-bound and stay specializations. A 60%
specialization rate is expected for a chapter titled "Special Operators"; it is not
a defect. (An earlier estimate of "two or three" was wrong.)

**Superseded note — orphan specializations.** All 10 objects from the first run carry
`foundation_role: specialization` with `foundation_object_id: none`, so nothing is
a foundation and genericization effectively did not run. At least one of them
("Allocate Replacement Storage Before Release") is a general resource-safety move
that applies in any language with manual buffers; burying it as a C++
specialization is the trapping the placement law warns about. Needs a rule for
when a candidate is a portable foundation versus a language specialization, and
whether `specialization` with `foundation_object_id: none` should be legal at all.
Decide the rule before touching objects — do not fix ten cases by guessing.

## 2026-07-31 — Learning architecture: golden-truth consumption, foundations-first, original visual references

Three user decisions after the art-skim incident. They shape a use-time contract,
not just extraction. Logged before any migration/schema change per repo law.

**Decision 1 — original visual references only.** A card for a visual craft must
carry a reference *image*, because text ("a hand has four fingers and a thumb")
names a skill without teaching its execution. But the reference must be **original
art the model generates**, using the copyright source page plus the card text as
guidance — never a reproduction of the copyrighted plate. No fan art, no embedded
source figures. This needs a `references:` schema field (a real schema change:
decisions-log + validator + card migration) and an image-generation capability
with a vision-review guardrail, since figure generation is exactly where models
fail (the "AI hands" problem). Capability honesty: this environment cannot
generate images; the field and pipeline are specified, execution waits on the
capability. Tracked as PASS-SCHEMA-VISUAL-REFERENCES.

**Decision 2 — foundations first, always, as a standard for every skill.** A human
drawing a figure does not start at step 3: thumbnail, then skeleton, then block,
then tighten, then finalize. The model must do the same. Concretely: the Ch.1
pillar/goal cards are the package foundations; the Ch.5-11 technique cards are
`specialization`s that name their foundation via `foundation_object_id` and link
`prerequisite_for`, so a reading order is encoded, not implied. The current GCBC
corpus flattens this — everything was marked `foundation`/`none` and linked only
`related_to`, which is a defect in the shipped output. Fix is a deliberate
re-roling pass plus a validator rule (a `specialization` must resolve to a real
foundation) and a generated reading-order index. Tracked as PASS-MIG-SE-FOUNDATIONS.

**Decision 3 — the library is golden truth; select skills by task.** Consumption
contract (`docs/PASS/PASS_CONSUMPTION.md`): on any task, check the library for a
matching skillset first. As refined on 2026-08-02, a matching card is authoritative
for the learner decision it actually covers; the model retains subject knowledge,
invention, adaptation, and responsibility for decisions outside the card's IF
clause. Load only the relevant subset — debugging work does not pull RNG skills —
then run foundations-first in the universal stage scaffold. The goal is to train
the model the way a human is taught, not to hand it a pile of notes or replace its
judgment. Like the grounding gate, the enforceable parts must eventually be
loader-controlled (SkillForge mechanics), because a prose rule the model is asked
to remember is exactly what fails.

**Correction to Decision 2 (same day).** My first framing said to re-role the
Ch.5-11 technique cards to `foundation_role: specialization`. That is wrong and
would misuse the schema. The schema's foundation/specialization axis is about
*portability* — a card is a `specialization` only when its IF/THEN needs a
language/tool/framework/medium/etc. constraint. The GCBC technique cards are
portable general craft, so `foundation`/`general`/`none` is correct for all 122.
"Foundations first" is a *reading-order* relationship, a different axis. Encode it
with `prerequisite_for` cross-links (Ch.1 pillar/goal card -> its downstream
technique cards) and a read-first designation for the pillar set, plus a
reading-order view from build_index — do NOT touch `foundation_role`. Assignment
PASS-MIG-SE-FOUNDATIONS is updated to match. Earlier self-criticism that "I
flattened the hierarchy" was half-wrong: the portability roles are right; the
reading-order links are the genuine gap.

## 2026-07-31 â€” Visual references are a closed, reviewed release contract

**Decided.** `references:` is a required common frontmatter field. It is empty
for ordinary text cards and non-empty for visual-source cards that teach visual
execution. Each reference is original generated art, stored inside the owning
card topic with a provenance sidecar, and may ship only after a recorded claim
review and a mechanical source-similarity check pass.

**Why.** A visual card needs an image to teach, but a source plate cannot become
that image without crossing the copyright boundary. A review record catches
incorrect generated anatomy or construction; the similarity check catches the
tempting but unacceptable near-copy.

**Narrow exemption.** The cross-craft general `metaskills` AP may remain
text-only. It teaches a universal process rather than visual execution. No art
pattern, drill, or subject-specific AP receives this exemption.

**What this forbids.** `origin: reproduced`, hand-setting `review: passed`,
shipping a pending review, storing an image outside its card topic, and treating
a grounding render as the reference image.

**Refined 2026-07-31 â€” first-party exception.** The source rights holder
authorized reuse of the Gen 1 art archive. A source that explicitly declares
`rights: first_party` may therefore supply a reviewed
`origin: first_party_source` reference. This is a fail-closed exception: no
rights declaration, no source reuse; all other visual sources remain
generated-art-only and subject to similarity rejection.
