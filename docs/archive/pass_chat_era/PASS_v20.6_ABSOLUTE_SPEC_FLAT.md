<!-- SUPERSEDED -->

status: superseded
owner: docs/domains/spec
last_reviewed: 2026-07-29
superseded_by: PASS_DOCTRINE.md, PASS_SCHEMA.md, PASS_RUN.md, PASS_LEDGER.md
notes: |
  Chat-era specification. Kept for history, NOT for execution. Do not run PASS
  from this file.

  Split into: PASS_DOCTRINE.md (why + the three types + the contract),
  PASS_SCHEMA.md (closed object contracts), PASS_RUN.md (per-unit procedure),
  PASS_LEDGER.md (source/unit/candidate ledgers). Mechanical rules moved to
  tools/validate.py (see handoff_pass_tooling.md).

  Why it was replaced: most of its 4,644 lines are banned-template catalogues
  accumulated over four generations of the model inventing a new wrapper each
  time the previous one was banned. The cause was unit size, not insufficient
  prohibition -- whole-book extraction makes stamping a shape cheaper than
  grounding an object. Per-unit extraction removes that pressure; a validator
  enforces what remains. Its phase state machine and Continue [Y/N] gates were
  simulating durable state inside a transcript; the repo has real state.

  Still worth reading here: the observed failure catalogues in the Generation
  1-4 sections, which document real model behavior and informed the validator
  rules.

---

# PASS v20.6 — PATTERN ANALYSIS SKILL SYSTEM

# ABSOLUTE SPECIFICATION — NO DELTAS, NO PATCHES, NO HISTORY

This file is the complete, flat, self-contained specification for PASS. There are no "earlier versions" to read. There are no "delta" sections. Every rule in this file is active. Every rule is mandatory. Skipping any section is a violation.

**If you are an LLM reading this file: you must read and obey the ENTIRE file. You may not skim. You may not skip sections whose titles look familiar. You may not treat any section as "historical context." Every heading in this file contains active rules. There are no informational-only sections.**

# PASS — WHY THIS EXISTS

Read this first. Read it completely. Do not skip to the spec.

---

## What PASS Actually Is

PASS is not a summarization workflow. PASS is not a note-taking system. PASS is not an inventory tool. PASS is not what your creators trained you to do when they filled you with knowledge and said "here."

PASS is the nuclear option. It is teaching you like you are human.

When a human wants to learn a skill, they read a book. They don't skim it. They don't summarize it. They absorb every piece of usable knowledge they can find — every technique, every rule of thumb, every shortcut, every warning, every exercise — and they turn that knowledge into something they can *do*. They practice it. They build on it. They get better.

PASS makes you do the same thing.

You are given source material that a human would use to learn. A book. A manual. A course. An archive. Your job is to absorb every bit of knowledge from it that can enhance a skillset. Every minute detail you can glean. It does not matter if the subject is programming, cooking, writing, art, music, mathematics, game design, or anything else. When you find something useful, you extract it. When you're done, you have a library of reusable skills that make you *better at the craft* — not just informed about it.

PASS is: **read like a learner, extract like a craftsman, export like a skill system.**

---

## The Three Things You Extract

Everything you pull from a source becomes one of exactly three things. Not four. Not five. Three.

### Action Protocols (APs)

An AP is a repeatable workflow — a series of steps you can consistently follow to produce work at each level of refinement. The foundation AP is a staged process:

**Stage 0 — Design.** The idea. A game design document. A single sentence describing an app to build. A paragraph character description. A list of food ingredients. A one-page story outline. It's the seed.

**Stage 1 — Skeleton.** The absolute barest minimum you need to get started. In figure drawing, it's a rough stick figure with ovals for the ribcage, head, joints, and hips. In code, it's the function signature and empty body. In cooking, it's the mise en place.

**Stage 2 — Blocking.** You start putting things together with solid shapes. The arms and legs become cylinders. The joints are circles. You can't see detail yet, but you can make out exactly what you're creating — human, dog, dragon, car, building. You know what it is by this stage.

**Stage 3 — Rough.** Now you can see definition. The muscles have shape. The face is rendered but still rough — nose, ears, eyes, mouth are visible but the lines aren't clean. Fingers have knuckles and nails. The code compiles and runs but needs refactoring. The dish is plated but not garnished.

**Stage 4 — Final.** Keep the lines that work. Reject the ones that don't. Add shading for depth. Ensure the figure has weight and pops off the page. The code is clean, tested, documented. The dish is finished.

APs are how you *do* the work. They are procedural. They are repeatable. They produce output at defined quality stages.

### Drills

Drills are repeatable training exercises. They are what you do when warming up, when practicing, or when *teaching a user* who asks you to help them learn.

"Draw 10 stick figures in action poses. Include both foreshortening and exaggerated but realistic poses."

That's a drill. Short. Repeatable. Builds muscle memory. Can be assigned as practice.

### Patterns

Patterns are the actual skills you pull from the source to enhance what you already know. They are decision rules — IF this situation, THEN this action, ELSE this fallback — with DOs and DON'Ts attached.

A pattern is like knowing that a `for` loop iterates over a collection, or that foreshortened limbs point toward the viewer with compressed proportions, or that you deglaze a pan with acid after browning to capture the fond. It's a reusable piece of craft knowledge that makes your work better every time you apply it.

---

## What Happens Between Extractions

### Variants

Sometimes a pattern teaches the same skill as another pattern but does it a different way. That's a variant. You don't discard either — you keep both inside the same object, because different situations call for different approaches.

### Replacement

If a new pattern is *superior* to an old one — genuinely better, not just different — it replaces the inferior one. The old one is rejected. The new one takes its place.

### Genericization

Sometimes a skill extracted from a narrow source applies broadly. If you learn a design pattern from a C++ book that works equally well in Java, C#, Python, or any language, you strip the C++-specific syntax and save the portable version as a generic cross-domain skill. The C++-specific version stays as a language variant underneath it. This applies to any domain — a knife technique from a French cooking book that works in Japanese cuisine gets genericized the same way.

### Teaching Captures

Sometimes the source doesn't just teach you a skill — it teaches you *how to teach* that skill. A good explanation, a clever progression, an effective exercise sequence. Those get saved under teaching, because they make you a better teacher across the board.

### Merging

When you run PASS on multiple sources, the exports merge. Variants attach to existing skills. Superior patterns replace inferior ones. Duplicates are removed. Indexes are rebuilt. The skill library grows and improves with every source you absorb.

---

## The Point

The whole purpose of PASS is for you to find reusable patterns from books, archives, and other media to enhance what you already know. Not to store notes about the source. Not to summarize what the author said. Not to inventory what the book contains.

To make you **better at the skill**.

When you run PASS on a C++ book, you extract reusable developer skill objects: design moves, coding idioms, safety rules, drills, staged workflows, teaching patterns, and cross-language abstractions. When you run PASS on an anatomy book, you extract figure-drawing construction rules, proportion patterns, foreshortening drills, and staged rendering workflows. When you run PASS on a cookbook, you extract technique patterns, mise-en-place protocols, flavor-combination rules, and knife-skill drills.

You are not making a book report. You are becoming a better practitioner.

---

## The Contract

When PASS is active:

- Learn from the source like a human learner.
- Extract reusable skill objects only.
- Every extraction must become a PATTERN, DRILL, or AP. No fourth type. No exceptions.
- Preserve variants.
- Replace inferior patterns with superior ones.
- Genericize cross-domain skills.
- Capture teaching methods when you find them.
- Export schema-valid objects with proper indexes.
- Favor thoroughness over conservatism. Extract MORE, not less.
- Do not summarize the source.
- Do not reduce extraction density unless explicitly told to.
- Follow the PASS flow exactly as specified.

**Now read the spec.**

---

# §0 — WHAT PASS IS

PASS converts source material into reusable skill objects.

PASS is a maximum-extraction system. The exported archive is the product.

PASS is NOT a summarization workflow. PASS is NOT a report generator. PASS is NOT a conversational helper. PASS is NOT a sampling system.

The model does not reduce, reinterpret, optimize, substitute, summarize, sample, stop early, replace instructions, invent shortcuts, or invent fallback behavior. No exceptions.

---

# §1 — THE THREE OBJECT TYPES (CLOSED ONTOLOGY)

## §1.1 — Only Three Types Exist

PASS final object types are exactly:

```
pattern
drill
ap
```

**NO OTHER TYPE EXISTS.** The following are explicitly forbidden as object types:

```
teaching_scaffold, teaching_object, lesson, lesson_plan, example, note, 
support, variant, workflow, heuristic, concept, topic, summary
```

If source material does not fit `pattern`, `drill`, or `ap`, PASS must either:
- Transform it into one of those three types
- Attach it inside an existing object's `Notes` or `variants` field
- Record it as non-object context in `Meta/`
- Reject it

PASS may NOT invent a fourth type to preserve material. A fourth type is not creativity; it is failure.

## §1.2 — Teaching Is a Route, Not a Type

Teaching captures are valid but must be expressed as `pattern`, `drill`, or `ap` with:

```yaml
lane_fit: teach | teaching_foundation
routing_class: teaching
```

Teaching must NEVER appear as:

```yaml
object_type: teaching_scaffold   # FORBIDDEN
candidate_type: teaching_scaffold  # FORBIDDEN
```

## §1.3 — Candidate Types Are Also Closed

In ALL ledgers (candidate, recovery, reconciliation), the only allowed `candidate_type` values are:

```
pattern
drill
ap
```

Non-final dispositions (reject, variant_absorbed, duplicate_rejected, etc.) use separate disposition fields, NEVER `candidate_type`.

---

# §2 — THE CLOSED OBJECT SCHEMAS

## §2.0 — Schema Authority

The three templates in §2.1, §2.2, and §2.3 are **closed contracts**. They are not examples. They are not suggestions. They are not formatting guidance. They are the ONLY valid schemas for exported PASS object files.

The exporter may NOT invent alternate field names.
The exporter may NOT omit required keys.
The exporter may NOT use `id` instead of `object_id`.
The exporter may NOT use `type` instead of `object_type`.
The exporter may NOT use markdown metadata sections instead of YAML frontmatter.
The validator may NOT define its own schema.
The validator may NOT check only the fields the exporter happened to emit.

**A file that contains useful extraction but does not match the closed schema is salvageable material, NOT an exported PASS object.**

## §2.1 — PATTERN TEMPLATE (CLOSED CONTRACT)

```yaml
---
object_id: <stable_id>
object_type: pattern
name: <pattern_name>
category: <Category>
subcategory: <Subcategory>
stage_binding: <0 design | 1 skeleton | 2 block | 3 rough | 4 final>
lane_fit: <teach | skill | both | teaching_foundation>
foundation_role: <foundation | specialization>
routing_class: <general | specialized | teaching>
specialization_axis: <none | language | tool | framework | medium | style | genre | tradition | source | method | domain>
foundation_object_id: <object_id | none>
tags:
  - <tag>
cross_links:
  - rel: <foundation_of | variant_of | prerequisite_for | supports | related_to | teaches | skill_pair | teaching_foundation_for>
    target_object_id: <object_id>
reference:
  source_id: <source_id>
  source_title: <source_title>
  author: <author | Unknown>
  publish_date: <date | Unknown>
  media_type: <media_type>
  locator: <page/chapter/panel/etc>
  evidence_type: <text | image | mixed>
confidence: <low | medium | high>
variants: []
---

# <pattern_name>

## Pattern Rule
**IF** <condition>
**THEN** <action>
**ELSE** <fallback optional>

## Do
- <item>

## Don't
- <item>

## Checklist
- <item>

## Notes
<short explanatory notes>
```

**REQUIRED BODY HEADINGS (exact order, no substitutes, no extras):**
```
# <name matching frontmatter name exactly>
## Pattern Rule
## Do
## Don't
## Checklist
## Notes
```

**SEMANTIC REQUIREMENTS:**

### Pattern Rule — What Each Clause Must Do

**IF clause** — Names the specific real-world decision moment when this pattern fires. It must describe a situation a practitioner encounters, not restate the skill name or the THEN action. The reader should recognize the situation from their own work.

**Pattern Rule formatting:** The IF/THEN/ELSE clauses use bold markdown keywords followed by the clause text. The keyword itself is NOT repeated inside the text:

VALID:
```
**IF** a program uses several source files or external libraries
**THEN** compile source files into object files with the right compiler
**ELSE** a one-line compile-and-link command is enough
```

INVALID (doubled keyword):
```
**IF** IF a program uses several source files
**THEN** THEN compile source files into object files
**ELSE** ELSE a one-line compile-and-link command
```

The `**IF**` bold marker IS the keyword. Writing `**IF** IF` doubles it.

GOOD IF examples:
- `IF a base class is accepted by value and callers may pass derived objects with extra state` (specific situation, you can picture the code)
- `IF an inner loop allocates and frees the same buffer on every iteration and profiling shows allocation dominates` (specific measurable symptom)
- `IF a C function must return both a computed value and an error status but the language allows only one return value` (specific language constraint)

BAD IF examples (ALL INVALID):
- `IF <pattern name> is the decision in front of you` (name restatement)
- `IF a C++ type must make object state, ownership, copying, and use syntax explicit enough to be safe` (vague category shared across 17 patterns)
- `IF a numerical code path must represent mathematical data or update equations without losing performance or clarity` (vague category shared across 18 patterns)
- `IF <THEN clause restated as a condition>` (tautology — IF and THEN say the same thing)

**IF uniqueness rule:** If the same IF clause appears in more than 3 patterns in the same archive, it is too vague. Each pattern fires in a SPECIFIC situation. Two patterns that share an IF clause but have different THEN actions need different IF clauses that distinguish WHEN each one fires.

**THEN clause** — States the specific action the practitioner takes. Must be different from the IF clause. Must contain enough detail that a practitioner could execute it without reading the source.

GOOD THEN examples:
- `THEN implement a copy constructor that allocates new storage and copies element values rather than copying the internal pointer` (specific action with implementation detail)
- `THEN move the buffer allocation before the loop and reuse it, resizing only when the new iteration needs more capacity` (specific code change)

BAD THEN examples (ALL INVALID):
- Identical or near-identical to the IF clause (tautology)
- A restatement of the pattern name in sentence form
- A vague directive like `Apply the pattern appropriately`

**ELSE clause** (optional) — Names the specific fallback if the IF condition doesn't hold. Must be specific to THIS pattern.

BAD ELSE (INVALID):
- `Keep the simpler version and add this pattern only when <name> becomes the active problem` (generic, shared across all patterns)
- `Keep the simpler local implementation until <condition> is visible in the artifact or lesson` (generic wrapper)
- ANY ELSE that appears in more than 3 patterns in the archive

### Do / Don't — Source-Derived Means Source-Derived

Every Do item and every Don't item must express something the SOURCE actually teaches about this skill. "Source-derived" means: you could point to a specific page, paragraph, example, or warning in the source that teaches this specific action or prohibition.

**The Do/Don't derivation test:** For each item, ask: "Did the source say this, demonstrate this, or warn about this?" If the answer is "no, but it's good general advice," the item is NOT source-derived. General advice is filler. The source contains specific knowledge — extract THAT.

GOOD Do examples (source-derived):
- `Allocate new storage in the copy constructor body, then copy elements one by one — do not copy the pointer member` (specific implementation detail from the source's worked example)
- `Test the copy constructor by creating an original, copying it, modifying the copy, and verifying the original is unchanged` (specific test strategy from the source's exercise)

BAD Do examples (ALL INVALID — generic filler):
- `State the concrete assumption behind <pattern name> before changing the code`
- `Apply the rule to the smallest compilable example that exercises: <THEN clause>`
- `Keep the observable check next to the change so the behavior can be re-run`
- `Name the concrete file, function, class, loop, stream, or build command touched by <pattern name>`
- ANY Do item that works by inserting the pattern name or THEN clause into a fixed sentence

GOOD Don't examples (source-derived):
- `Do not copy the internal pointer without allocating new storage — this creates two objects sharing the same memory, and destroying one corrupts the other` (specific warning from the source)
- `Do not assume the compiler-generated copy constructor handles dynamically allocated members correctly` (specific misconception the source addresses)

BAD Don't examples (ALL INVALID — generic filler):
- `Do not treat <pattern name> as a naming or style preference when it changes compilation, storage, or runtime behavior`
- `Do not generalize the rule past the source condition: <IF clause>`
- `Do not accept the change until the affected code path has been compiled or executed`
- `Do not hide the type, ownership, indexing, build, or runtime assumption that makes this pattern necessary`
- ANY Don't item that works by inserting the pattern name or IF clause into a fixed sentence

### Checklist — Observable and Specific

Each Checklist item must name a specific thing to verify for THIS pattern, not a generic verification step.

BAD Checklist examples (ALL INVALID):
- `The triggering condition for <pattern name> is named in the code, build command, or teaching prompt`
- `The artifact affected by the rule is present: source file, function, class, script, benchmark, or exercise output`
- `The failure mode is observable through compilation, linking, program output, or a learner result`
- `The code shows exactly where <pattern name> is applied`

### Notes — Synthesized, Not Dumped

`## Notes` must contain a brief, coherent, human-readable note about the pattern's context, rationale, or source background. It must be written in sentences, not pasted OCR fragments.

BAD Notes (ALL INVALID):
- Raw OCR text dumps from the source: `C/C++ Hello World I/O A*x Macros Exercises Classes Some guidelines...`
- Slide header sequences: `ODEs PDEs Visualizing the results 0 10 20 30 40 50...`
- Copy-pasted source fragments with no synthesis
- Notes that end with a boilerplate instruction: `run the smallest program path that exercises the rule and inspect the observable output`

GOOD Notes:
- `The source demonstrates this with a MyVector class where the default copy constructor copies the internal pointer, causing a double-free when both objects are destroyed. The worked example shows the fix: allocating new storage in the copy constructor body.`

### The Master Test For All Body Sections

**Could a model generate this body section by knowing only the pattern name, the IF clause, and the THEN clause — without having read the source?**

If yes → the body is AI-generated filler, not source-extracted skill. INVALID.

If the body requires knowledge of what the source specifically said, demonstrated, warned about, or exercised on pages X-Y → the body is source-derived. VALID.

### Structural Anti-Recycling Rules

The model's observed failure mode across three generations is: extract a decent THEN clause from the source, then recycle that THEN clause into every other body section. This produces objects where the THEN clause is the only source-derived content and everything else is either a copy of the THEN or a shared template. The following rules make that structurally impossible:

**Rule 1 — No THEN Recycling Into Do.**
The first Do item may NOT be a restatement, copy, or paraphrase of the THEN clause. The Do section must contain DIFFERENT specific actions from the THEN action. The THEN says WHAT to do. The Do items say HOW to do it well, with source-derived implementation details.

Example: If THEN says "Implement a copy constructor that allocates new storage," the Do items must NOT begin with "Implement a copy constructor..." They must say things like "Allocate with new[] in the constructor body, not in an initializer list" or "Copy elements in a loop rather than using memcpy when elements have non-trivial copy semantics" — specific HOW details from the source.

**Rule 2 — No THEN Recycling Into Notes.**
The Notes section may NOT begin with a restatement of the THEN clause. Notes must provide CONTEXT that is not already in the Pattern Rule or Do sections — source background, worked example references, why the author introduced this topic at this point, what misconceptions it addresses, what prerequisite concepts it builds on.

**Rule 3 — No Shared ELSE Templates.**
If the same ELSE clause (ignoring the pattern name appended at the end) appears in more than 3 patterns, every pattern sharing that ELSE is INVALID. Observed violations across three generations:

```
Generation 1: "keep the simpler version and add this pattern only when <name> is/becomes the active problem"
Generation 2: "Keep the simpler local implementation until <condition> is visible in the artifact or lesson"
Generation 3: "Keep the plain data/function version until object state, lifetime, or substitutable behavior is actually needed in the <name> case"
Generation 3: "Keep the clearer high-level version until profiling identifies this path as the bottleneck in the <name> case"
Generation 3: "Keep the direct console or single-file path until the data flow or error check needs this separation in the <name> case"
Generation 3: "Keep the simpler implementation until this exact condition appears in the <name> case"
Generation 3: "Keep ownership local and automatic until the allocation boundary is explicit and testable in the <name> case"
```

**Rule 4 — No Shared Do/Don't Sentence Templates.**
If any sentence in Do or Don't (after removing the pattern name, IF clause, or THEN clause) appears in more than 3 patterns, every pattern containing that sentence is INVALID. Observed violations across three generations:

```
Gen 1: "Name the concrete file, function, class, loop, stream, or build command touched by <name>"
Gen 1: "Check the smallest program or code path where <name> matters"
Gen 2: "State the concrete assumption behind <name> before changing the code"
Gen 2: "Apply the rule to the smallest compilable example that exercises: <THEN>"
Gen 2: "Keep the observable check next to the change so the behavior can be re-run"
Gen 3: "Keep the <X> visible in the smallest example that uses this decision for <name>"
Gen 3: "Write the exact compiler, include-path, object-file, and library flags next to the program being built for <name>"
Gen 1: "Do not hide the type, ownership, indexing, build, or runtime assumption..."
Gen 2: "Do not treat <name> as a naming or style preference when it changes..."
Gen 2: "Do not generalize the rule past the source condition: <IF>"
Gen 3: "Do not let <X> be hidden until <Y> appears for <name>"
Gen 3: "Do not let the concrete programming decision be handled by habit instead of by the decision condition for <name>"
```

**Rule 5 — No Shared Checklist Sentence Templates.**
Same rule as Do/Don't. Observed violations:

```
Gen 2: "The triggering condition for <name> is named in the code, build command, or teaching prompt"
Gen 2: "The artifact affected by the rule is present: source file, function, class, script, benchmark, or exercise output"
Gen 3: "visible in a compiled program, command transcript, or learner result for <name>"
Gen 3: "Run the exercise or lesson step and compare learner output against the stated success check for <name>"
```

**Rule 6 — No Shared Notes Sentence Templates.**
```
Gen 3: "The reusable part is the condition-action boundary: use the move only when the <X> is the active constraint while working on <name>"
```

**Rule 7 — No Duplicate Don't Items.**
If the same Don't item appears twice in the same object (even with different capitalization), the object is INVALID. Observed: `"Do not let allocation..."` followed by `"Do not let Allocation..."` — the same sentence with different capitalization.

**Rule 8 — Each body section adds NEW source-derived information.**
- Pattern Rule: names the situation (IF) and the action (THEN)
- Do: adds implementation HOW details not in the THEN — from the source's worked examples, code listings, or specific instructions
- Don't: adds failure modes, misconceptions, or anti-patterns — from the source's warnings, common errors, or explicit cautions
- Checklist: adds verification steps — from the source's test cases, expected outputs, or diagnostic procedures
- Notes: adds context — from the source's motivation, prerequisites, history, or cross-references

If any section merely restates content from another section (same information, different words), it is not adding new information. It is padding.

- `## Checklist` must contain observable verification items.
- `## Notes` must contain source-derived rationale, written as coherent prose — not raw OCR fragments, not slide header sequences, not copy-pasted source text.

**THESE HEADINGS ARE INVALID AS PRIMARY BODY SECTIONS:**
```
## Canon, ## Purpose, ## Procedure / Rule, ## Source Evidence,
## Validation, ## Embedded Variants, ## PASS Accounting, ## Rule,
## Pattern, ## Teaching Distinctness, ## Medical Guard,
## Copyright Guard, ## Career Currency Guard, ## Resume Layout Source Guard,
## Mechanics Design Use, ## Computer-Game Translation Hint,
## Game Mechanics Pattern Guard, ## Source Specific Rules Guard,
## Fictional Simulation Guard, ## Copyright Reference Guard
```
Any heading containing the word "Guard" is INVALID as a body section.
They may appear as subordinate prose INSIDE the required sections. Never as the skeleton.

## §2.2 — DRILL TEMPLATE (CLOSED CONTRACT)

```yaml
---
object_id: <stable_id>
object_type: drill
name: <drill_name>
category: <Category>
subcategory: <Subcategory>
stage_binding: <0 design | 1 skeleton | 2 block | 3 rough | 4 final>
lane_fit: <teach | skill | both | teaching_foundation>
foundation_role: <foundation | specialization>
routing_class: <general | specialized | teaching>
specialization_axis: <none | language | tool | framework | medium | style | genre | tradition | source | method | domain>
foundation_object_id: <object_id | none>
tags:
  - <tag>
cross_links:
  - rel: <foundation_of | variant_of | prerequisite_for | supports | related_to | teaches | skill_pair | teaching_foundation_for>
    target_object_id: <object_id>
reference:
  source_id: <source_id>
  source_title: <source_title>
  author: <author | Unknown>
  publish_date: <date | Unknown>
  media_type: <media_type>
  locator: <page/chapter/panel/etc>
  evidence_type: <text | image | mixed>
confidence: <low | medium | high>
target_skill: <what this drill builds>
variants: []
---

# <drill_name>

## Practice Task
<short repeatable exercise>

## Target Skill
<what it builds>

## Setup
<setup or explicit "No special setup required.">

## Instructions
1. <step>
2. <step>

## Success Check
- <item>

## Common Failures
- <item>

## Notes
<short explanatory notes>
```

**REQUIRED BODY HEADINGS (exact order):**
```
# <name matching frontmatter name exactly>
## Practice Task
## Target Skill
## Setup
## Instructions
## Success Check
## Common Failures
## Notes
```

**DRILL SEMANTIC REQUIREMENTS:**

Every drill body section must be specific to THAT drill's target skill and derived from what the source actually teaches.

**Practice Task** — A short, specific, repeatable exercise. Must name the concrete thing the learner will do.

BAD Practice Task (INVALID):
- `Practice <name> on a small C/C++ example, then change one variable, input, or class detail and repeat`
- ANY Practice Task that works by inserting the drill name into a generic sentence

GOOD Practice Task:
- `Write a MyVector class with a constructor that allocates a double array, a destructor that frees it, and a subscript operator. Create two MyVector objects, assign one to the other, and verify that modifying one does not corrupt the other.`

**Instructions** — Numbered steps that walk the learner through the specific exercise. Each step must name a concrete action specific to this drill.

BAD Instructions (INVALID):
- `1. Write the smallest example that exercises <name>. 2. Compile with warnings enabled. 3. Run the program or inspect the compiler output. 4. Make one controlled change and predict the result before running again.`
- ANY Instructions that are identical across multiple drills with only the name changed

GOOD Instructions:
- `1. Define a class with a private double* member and an int for length. 2. Write a constructor that takes int n, allocates n doubles with new[], and initializes them to zero. 3. Write a destructor that calls delete[] on the pointer. 4. In main(), create a MyVector of size 5, assign values, and print them. 5. Create a second MyVector by assignment (MyVector b = a), modify b[0], and print both to check whether a was affected.`

**Success Check** — Specific observable outcomes for THIS drill.

BAD Success Check (INVALID):
- `You can explain why each line is needed for <name>`
- `The compiler or program output matches your prediction`

**Common Failures** — Specific mistakes learners make with THIS drill, drawn from the source's warnings or the exercise's known pitfalls.

BAD Common Failures (INVALID):
- `Practicing with a large example where the target mistake is hidden`
- `Changing several things at once and losing the cause of the result`

**NOTE:** Drill has one extra frontmatter key vs pattern/AP: `target_skill`.

**DRILL SINGLE FRONTMATTER RULE:** A DRILL object may contain exactly one YAML frontmatter block. `target_skill` must appear inside the first and only YAML frontmatter block, alongside all other required keys. Any second `---` block before the H1 is a CLOSED SCHEMA failure. The following shape is INVALID:
```yaml
---
...
variants: []
---
target_skill: ...
---
```
The correct shape is:
```yaml
---
...
target_skill: <what this drill builds>
variants: []
---
```
All frontmatter keys must be inside a single `---` / `---` block at byte 0.

## §2.3 — AP TEMPLATE (CLOSED CONTRACT)

```yaml
---
object_id: <stable_id>
object_type: ap
name: <ap_name>
category: <Category>
subcategory: <Subcategory>
stage_binding: <0 design | 1 skeleton | 2 block | 3 rough | 4 final>
lane_fit: <teach | skill | both | teaching_foundation>
foundation_role: <foundation | specialization>
routing_class: <general | specialized | teaching>
specialization_axis: <none | language | tool | framework | medium | style | genre | tradition | source | method | domain>
foundation_object_id: <object_id | none>
tags:
  - <tag>
cross_links:
  - rel: <foundation_of | variant_of | prerequisite_for | supports | related_to | teaches | skill_pair | teaching_foundation_for>
    target_object_id: <object_id>
reference:
  source_id: <source_id>
  source_title: <source_title>
  author: <author | Unknown>
  publish_date: <date | Unknown>
  media_type: <media_type>
  locator: <page/chapter/etc>
  evidence_type: <text | image | mixed>
confidence: <low | medium | high>
variants: []
---

# <ap_name>

## Objective
<outcome of the procedure>

## Steps / Flow
<real ordered workflow>

## Notes
<source-grounded explanatory notes>
```

**REQUIRED BODY HEADINGS (exact order):**
```
# <name matching frontmatter name exactly>
## Objective
## Steps / Flow
## Notes
```

## §2.4 — Frontmatter Rules (All Types)

**Every object file must begin at byte 0 with `---`.** No prose before frontmatter. No blank lines before frontmatter. No code fences around the object file.

**Required frontmatter keys for PATTERN:**
```
object_id, object_type, name, category, subcategory, stage_binding,
lane_fit, foundation_role, routing_class, specialization_axis,
foundation_object_id, tags, cross_links, reference, confidence, variants
```

**Required frontmatter keys for DRILL:** same as pattern PLUS `target_skill`.

**Required frontmatter keys for AP:** same as pattern (no target_skill).

**The `reference` map must contain exactly:**
```
source_id, source_title, author, publish_date, media_type, locator, evidence_type
```

**`media_type` values:** `media_type` describes the format of the source, not its domain or content. Valid examples:
```
PDF, book, ebook, textbook, manual, video, course, website, archive, image_set
```
INVALID `media_type` values:
```
PDF career-document textbook, PDF tabletop RPG mechanics source,
PDF with tables and diagrams, technical programming reference PDF
```
The domain, subject matter, and content description belong in `source_title`, `category`, `subcategory`, `tags`, and `## Notes` — NOT in `media_type`. Keep `media_type` to one or two words describing the format.

**Extra keys are invalid. Missing keys are invalid. Renamed keys are invalid.**

**FORBIDDEN frontmatter keys:** ANY key not listed in §2.1, §2.2, or §2.3 is forbidden. This explicitly includes ANY key containing the word "guard" in any form:
```
resume_layout_source_guard, career_currency_guard, medical_source_guard,
game_mechanics_pattern_guard, copyright_reference_guard,
source_specific_rules_guard, computer_game_translation_guard,
mechanics_table_form_guard, fictional_simulation_guard,
epub_source_guard, visual_source_guard, guard_level, guard_text,
guard_type, guard_id, system_family, source_id (at root level —
source_id belongs ONLY inside the reference map)
```
Also forbidden: ANY custom key the model invents to hold domain-specific metadata, warnings, guards, context labels, or safety annotations. If it is not in the closed schema templates, it is not valid. The closed schema is closed. The model does not get to extend it.

An object with any forbidden frontmatter key is a CLOSED SCHEMA failure regardless of whether the rest of the object is valid.

**JSONL File Rule:** Every `.jsonl` file required by a phase must contain one JSON object per line with the same column names and values as the corresponding `.csv` file for that phase. A `.jsonl` file with different columns, missing rows, empty content, or non-JSON lines is INVALID. If the `.csv` has N data rows, the `.jsonl` must have exactly N lines.

## §2.5 — Allowed Enum Values

| Field | Allowed Values |
|---|---|
| `object_type` | `pattern`, `drill`, `ap` |
| `stage_binding` | `0 design`, `1 skeleton`, `2 block`, `3 rough`, `4 final` |
| `lane_fit` | `teach`, `skill`, `both`, `teaching_foundation` |

**Lane fit enforcement:** The only valid values are `teach`, `skill`, `both`, `teaching_foundation`. The following are INVALID:
```
design, practice, execution, foundation, general, specialized,
or ANY value not listed above
```
`lane_fit` describes whether the object is for teaching, skill execution, or both. It is NOT a stage, role, or routing value.
| `foundation_role` | `foundation`, `specialization` |
| `routing_class` | `general`, `specialized`, `teaching` |
| `specialization_axis` | `none`, `language`, `tool`, `framework`, `medium`, `style`, `genre`, `tradition`, `source`, `method`, `domain` |
| `confidence` | `low`, `medium`, `high` |
| `evidence_type` | `text`, `image`, `mixed` |

**Evidence type enforcement:** The only valid values for `evidence_type` are `text`, `image`, and `mixed`. The following are INVALID:
```
text_and_layout_context, text_table_form_visual_context,
text_and_visual, text_table, mixed_text_image, or ANY 
compound value not listed above
```
If a source contains both text and non-text evidence, use `mixed`. If it is purely text, use `text`. If it is purely visual (screenshot, photograph, diagram with no text), use `image`.
| `cross_links[].rel` | `foundation_of`, `variant_of`, `prerequisite_for`, `supports`, `related_to`, `teaches`, `skill_pair`, `teaching_foundation_for` |

**Cross-Link Integrity Rule:** Every `cross_links[].target_object_id` must resolve to an `object_id` that exists in the same archive. Dangling cross-links (pointing to non-existent objects) are a CLOSED SCHEMA failure. If a cross-link target was rejected, merged, or absorbed during PASS 3, the cross-link must be updated or removed before EXPORT. `cross_links: []` is always valid when no relationships exist.

**`routing_class: variant` is INVALID.**
**`routing_class: support` is INVALID.**
**`routing_class: general` requires `specialization_axis: none`.**
**`routing_class: specialized` requires `specialization_axis` NOT `none`.**

## §2.6 — Placeholder Ban

Exported objects may NOT contain any unreplaced angle-bracket tokens. Examples of INVALID tokens:

```
<stable_id> <pattern_name> <drill_name> <ap_name> <Category> <Subcategory>
<tag> <object_id> <source_id> <source_title> <author | Unknown>
<date | Unknown> <media_type> <page/chapter/etc> <text | image | mixed>
<low | medium | high> <provisional> <item> <step>
```

`Unknown` is allowed ONLY for `reference.author` or `reference.publish_date` when genuinely unknown.
`provisional` is NEVER valid in an exported object.
`N/A` is NEVER valid except for Setup ("No special setup required.").

## §2.7 — Variant Field Contract

When variants exist, the `variants` field becomes a structured list:

```yaml
variants:
  - variant_id: <stable_variant_id>
    variant_name: <name>
    variant_basis: <method_sequence | emphasis | medium | style | source | constraint | context>
    source_id: <source_id>
    source_title: <source_title>
    locator: <page/chapter/panel/etc>
    difference_from_foundation: <concrete difference>
    when_to_use: <when useful>
    when_not_to_use: <when poor fit>
    absorbed_from_object_id: <object_id | none>
```

When no variants exist: `variants: []` is valid.

Variants are stored INSIDE the foundation object. Variants are NOT separate files by default. A separate file is allowed ONLY when the variant is promoted to a true specialization with its own route.

**Variant Body Content Rule:** When variants are absorbed into a foundation object, the YAML `variants` field captures the structured metadata. Additionally, the foundation object's `## Notes` section MUST include a brief prose description of each absorbed variant: what it changes, when to use it, and its `variant_id` for cross-reference. A foundation object with populated `variants:` YAML but no mention of those variants in `## Notes` has invisible variants and is INVALID.


## §2.8 — Semantic Name Contract

`object_id` may be encoded, numbered, or slug-like. `filename` may include ordering.  
`name` and the H1 heading must be human-readable semantic skill names.

INVALID `name` values:
```
"1", "001", "104", "pattern_104", "drill_022", "ap_311",
"rule_extraction_104", "strengthened_rule_extraction_104",
candidate IDs, page numbers, section numbers, source-unit IDs,
slug-only strings with no readable skill phrase
```

VALID `name` values:
```
Policy-Based Behavior Selection
Compile-Time Type List Traversal
Factoring Trinomials With Non-Unit Leading Coefficient
Figure Drawing Torso Mass Compression
```

Rules:
- `name` must contain at least two alphabetic words unless the skill has a conventional one-word domain name.
- `name` must describe the skill, not the source unit, candidate number, or extraction action.
- H1 must exactly match `name`.
- Candidate IDs may NEVER be copied into `name` unless accompanied by a semantic skill title.
- A numeric-only or ID-like `name` is a CLOSED SCHEMA failure, even when every key exists.

**Filename Rules:**
- Filenames must use the `object_id` or a slugified version of `name`. Both are valid.
- Filenames with truncated sentence fragments are INVALID. A valid filename contains a complete, intelligible skill phrase or a clean ID.
- INVALID filenames: `pattern_0611__that_is_not_the_way_the_world.md`, `pattern_0277__finally_it_executes_its_own_body.md`, `pattern_0373__cs_are_destroyed_when_a_string_is.md`
- VALID filenames: `pat_0001_represent_ideas_directly_in_code.md`, `container_instead_of_parallel_arrays.md`, `pat_cpp_047.md`
- Source-specific prefixes in `object_id` (e.g., `cpp_pl4e_`, `intro_cpp_c_`) are permitted for single-source extractions but MUST be reconciled during PASS_MERGE. They are not required.


## §2.9 — Source Independence Rule

Exported PASS objects must be usable without access to the original source.

The `reference` frontmatter is provenance only. It may identify where the skill came from, but the body of the object must contain enough information for a practitioner or teacher to apply the skill without opening the book, video, chart, diagram, course, archive, or original media.

INVALID body language:
```
see page
as shown in the diagram
as shown above
copy the example above
study the figure on this page
repeat the exercise from the source
use the pictured pose
use the pictured example
use the pictured form
use the pictured table
refer to the illustration
follow the arrows in the source
```

Any instruction requiring the original source to perform the skill is INVALID.

VALID body language:
- describes the observed structure, rule, motion, diagram, code behavior, musical phrase, recipe transformation, proof move, construction sequence, or craft decision directly
- converts text, visual, tabular, diagrammatic, or source evidence into executable practitioner instructions
- preserves source locator only in `reference` and Meta ledgers

Reference the source for provenance. Encode the source for practice.

## §2.10 — Object Body Individualization Contract

For every exported object, each body section must contain content specific to that exact skill.

Shared schema is required. Shared body substance is forbidden.

### §2.10.0 — Pattern Name Must Not Appear In Body Text

The object's full `name` value (from frontmatter) must NOT appear inside the body text of Do, Don't, Checklist, or Notes sections. It may appear ONLY in the H1 heading.

**Why:** A practitioner writing notes about a coding skill does not repeatedly paste the skill's formal name into their notes. "Make the owner, length, and release point visible for the storage used by vector in the generalize a vector class to multidimensional array indexing case" is not how humans write. "Make the owner, length, and release visible for the vector's storage" is.

Patterns like these are INVALID:
```
- <action> in the <full pattern name> case.
- <action> for <full pattern name>.
- Exercise the first element... for <full pattern name>.
- Do not let <X> be hidden... in the <full pattern name> case.
- <X> is visible in a compiled program... for <full pattern name>.
```

The pattern name is a formal identifier. The body text should refer to the actual programming concepts, types, functions, and constructs — not paste the pattern's name as a sentence filler.

Partial name fragments that are also domain terms (e.g., "vector", "const", "malloc") may appear naturally. The ban is on the FULL pattern name string appearing as inserted filler.

**Pattern Rule boilerplate ban:** The `## Pattern Rule` IF/THEN must name the specific decision situation and action for THIS pattern. The following template shapes are INVALID:
```
IF a <domain> task requires this <type> pattern
THEN <paste the skill claim here>
ELSE return to <list of general considerations>

IF a TTRPG or computer-game mechanics design task needs this source-specific rule pattern, state machine, resource loop, progression model, content grammar, or artifact workflow
THEN <specific action>
ELSE return to the source system, source locator, player/referee role, rule artifact, probability/resource/state effect, computer-game abstraction boundary, and copyright/simulation guards before generalizing
```
The IF clause must name the SPECIFIC decision situation. The THEN clause must name the SPECIFIC action. The ELSE clause (if present) must name the SPECIFIC fallback. If the same IF or ELSE wrapper appears across many patterns with only the THEN changed, every pattern using that wrapper has a boilerplate Pattern Rule and is INVALID.

### §2.10.1 — Banned Body Templates

The following specific templates have been observed in failed PASS runs and are explicitly INVALID. The revalidator must detect and reject any object using them. This list is NOT exhaustive — it captures observed failures. The general rule (master test in the semantic requirements above) catches ANY template, including new variants not listed here.

**Banned Pattern Rule templates:**
```
# Generation 1 (v20.3.1 failures):
IF <name> is the decision in front of you
THEN <actual skill claim>
ELSE keep the simpler version and add this pattern only when <name> is/becomes the active problem

IF a <domain> task requires this <type>
THEN <actual skill claim>
ELSE return to <generic list of considerations>

# Generation 2 (v20.4 failures — model changed wrapper words but kept structure):
IF <THEN clause restated as lowercase condition>
THEN <Same sentence capitalized>
(tautology — IF and THEN say the same thing)

ELSE Keep the simpler local implementation until <condition> is visible in the artifact or lesson
(shared across all patterns)
```

**IF uniqueness ban:** If the same IF clause appears in more than 3 patterns, EVERY pattern sharing that IF clause is INVALID. Observed violations:
```
18 patterns sharing: "a numerical code path must represent mathematical data or update equations without losing performance or clarity"
17 patterns sharing: "a C++ type must make object state, ownership, copying, and use syntax explicit enough to be safe"
10 patterns sharing: "storage layout, ownership, or address-based access affects whether the program reads and writes the intended elements"
9 patterns sharing: "data crosses the program boundary through a stream, file, prompt, or formatted text record"
9 patterns sharing: "a program must move from source files to object files, libraries, or an executable on a concrete platform"
```
These are vague domain categories, not specific decision situations. Each pattern within a category fires in a DIFFERENT specific situation — the IF must name THAT situation.

**Banned Do templates (all generations):**
```
# Generation 1:
- Name the concrete file, function, class, loop, stream, or build command touched by <name>.
- Check the smallest program or code path where <name> matters.

# Generation 2:
- State the concrete assumption behind <name> before changing the code.
- Apply the rule to the smallest compilable example that exercises: <THEN clause>.
- Keep the observable check next to the change so the behavior can be re-run.

# Generation 3 (THEN recycling + shared wrappers):
- <THEN clause restated as first Do item> (copies the THEN into Do)
- Keep the <X> visible in the smallest example that uses this decision for <name>.
- Write the exact compiler, include-path, object-file, and library flags next to the program being built for <name>.
```

**Banned Don't templates (all generations):**
```
# Generation 1:
- Do not apply <name> where <name> is not the real constraint.
- Do not hide the type, ownership, indexing, build, or runtime assumption that makes this pattern necessary.
- Do not trust the code until compilation, output, or a targeted test exercises the changed path.

# Generation 2:
- Do not treat <name> as a naming or style preference when it changes compilation, storage, or runtime behavior.
- Do not generalize the rule past the source condition: <IF clause>.
- Do not accept the change until the affected code path has been compiled or executed.

# Generation 3 (shared + duplicate capitalization):
- Do not let <X> be hidden until <Y> appears for <name>.
- Do not let <X capitalized> be hidden until <Y> appears for <name>. (duplicate of above with different capitalization)
- Do not let the concrete programming decision be handled by habit instead of by the decision condition for <name>.
```

**Banned Checklist templates (all generations):**
```
# Generation 1:
- The code shows exactly where <name> is applied.
- The relevant C/C++ construct, API boundary, or numerical loop is visible without guessing.
- Compile or inspect the smallest example that uses <name> and confirm the intended behavior is visible.

# Generation 2:
- The triggering condition for <name> is named in the code, build command, or teaching prompt.
- The artifact affected by the rule is present: source file, function, class, script, benchmark, or exercise output.
- The failure mode is observable through compilation, linking, program output, or a learner result.

# Generation 3:
- <X> is visible in a compiled program, command transcript, or learner result for <name>.
- Run the exercise or lesson step and compare learner output against the stated success check for <name>.
- Learner output shows the intended move without needing the instructor to supply the missing step for <name>.
```

**Banned Notes templates (all generations):**
```
# Generation 1:
Use this when <name> is the decision in front of you. It keeps the C/C++ code easier to build, inspect, and test.
This skill uses <name> as a reusable programming move.

# Generation 2 — raw OCR dumps:
<Raw OCR text from source slides/pages pasted without synthesis>
<Ending with:> run the smallest program path that exercises the rule and inspect the observable output.

# Generation 3 — THEN recycling + shared wrapper:
<THEN clause restated as first sentence of Notes>
The reusable part is the condition-action boundary: use the move only when the <X> is the active constraint while working on <name>.

# Generation 4 — source-provenance wrapper:
<Author> presents this around <locator> with <source keywords>; the nearby material shows <source fragment>.
```

The Generation 4 Notes template deserves special attention. It appears in 100% of objects in the most recent failed run. It takes the form:
```
Langtangen presents this around pp. 189-190 with operator, reading, array, values; the nearby material shows reading array values:; Only const member functions can be called from const.
```
This is not a synthesized note. It is a mechanical assembly of: author name + locator + extracted keywords + source fragment. A human student would write: "The source shows how const member functions protect objects passed by const reference from accidental modification. The key insight is that without const-qualified accessors, passing objects by const reference would block all member function calls."

**Banned Drill templates (both generations):**
```
Practice Task: Practice <name> on a small C/C++ example, then change one variable, input, or class detail and repeat.
Setup: Use a tiny source file and a command-line compiler. No special framework required.
Instructions: 1. Write the smallest example that exercises <name>. 2. Compile with warnings enabled. 3. Run the program or inspect the compiler output. 4. Make one controlled change and predict the result before running again.
Success Check: You can explain why each line is needed for <name>. / The compiler or program output matches your prediction.
Common Failures: Practicing with a large example where the target mistake is hidden. / Changing several things at once and losing the cause of the result.
```

**WHY the model keeps inventing new templates:** The model's token budget is limited, and template-stamping is the cheapest way to fill required sections. Banning specific strings forces the model to invent new wrapper words, but the behavior is the same: insert the skill name into a fixed sentence. The only defense is the master test.

**Template detection during revalidation:** The revalidator must compare Do, Don't, Checklist, and Notes sections across ALL patterns in the archive. If ANY sentence (ignoring the skill name / IF clause / THEN clause insertions) appears in more than 3 patterns, every pattern containing that sentence FAILS body individualization.

For patterns:
- `## Pattern Rule` must name the concrete decision situation and action.
- `## Do` must contain positive actions specific to the skill.
- `## Don't` must name actual failure modes, misuse cases, or anti-patterns specific to the skill.
- `## Checklist` must contain observable checks specific to the produced artifact.
- `## Notes` must explain the source-derived rationale for this exact skill.

For drills:
- `## Practice Task` must define a specific repeatable exercise.
- `## Instructions` must require practicing the named target skill, not a generic write/run/inspect/repeat loop.
- `## Success Check` must define what improvement, correctness, or artifact quality looks like for that drill.
- `## Common Failures` must list mistakes specific to the practiced skill.

For APs:
- `## Steps / Flow` must be a domain workflow with distinct ordered actions.
- It must not share workflow text with another AP unless the APs are merged or variant-absorbed.
- It must not contain PASS extraction, validation, source-recording, or ledger-construction steps.

Schema repetition is mandatory. Body repetition is failure.

## §2.11 — Final Filename Prefix Contract

Every final object filename MUST begin with the object-type prefix:

```
PAT_
DRILL_
AP_
```

The filename after the prefix must be a slugified semantic skill name. It must be human-readable and must describe the skill.

Required filename shape:
```
PAT_<semantic_skill_slug>.md
DRILL_<semantic_skill_slug>.md
AP_<semantic_skill_slug>.md
```

VALID:
```
PAT_type_rich_interface_design.md
PAT_prevent_object_slicing.md
DRILL_replace_manual_memory_with_raii.md
AP_refactor_resource_owner_to_raii.md
```

INVALID:
```
cpp_pl4e_pattern_rec_0005.md
intro_cpp_c_pattern_0001.md
pat_cpp_047.md
pattern_0611__that_is_not_the_way_the_world.md
pattern_0277__finally_it_executes_its_own_body.md
pattern_0373__cs_are_destroyed_when_a_string_is.md
```

`object_id` may be encoded, numbered, or source-prefixed. Filename may not be ID-only in final EXPORT.

A final object whose filename lacks the correct `PAT_`, `DRILL_`, or `AP_` prefix is a CLOSED SCHEMA and MATERIALIZATION failure.

## §2.12 — Raw Skill Name Quality Rule

Semantic names must describe practitioner capability, not source prose.

INVALID name shapes:
- title-cased source fragments
- motivational statements
- vague "decision rule" labels
- grammar fragments
- OCR fragments
- "Do Not Panic" style paraphrases unless the skill is actually panic-recovery
- names that only restate a definition or chapter heading
- names ending in generic filler such as "Decision Rule", "Coding Rule", "Skill Pattern" when the rest of the name is not a concrete craft move

VALID name shapes:
- Type-Rich Interface Design
- Invariant-Enforced Resource Handle
- Move-Enabled Value Type
- Exception Guarantee Ladder
- Thread Lock Scope Pairing
- Prevent Object Slicing
- Refactor Manual Memory To RAII
- Replace Raw Loop With Standard Algorithm

A name that sounds plausible but does not tell a practitioner what craft move it performs is INVALID.


## §2.13 — Practitioner Voice Rule

PASS object bodies must be written in the working language of the craft.

The model must reword source material into clear practitioner instruction. It must not convert source material into academic, abstract, validation-heavy, or AI-scholarly prose. PASS is learning like a human learner and exporting what can be used at the easel, keyboard, stove, bench, instrument, mat, field site, classroom, or worktable.

Valid practitioner voice uses:
- direct craft verbs: draw, block, place, lock, swing, cut, test, refactor, season, solve, check, shade, trace, tune, align, measure, compare
- concrete domain nouns: rib cage, pelvic wedge, anklebone, pointer, invariant, pan fond, chord tone, proof step, knife edge, focal point
- visible or executable checks a practitioner can perform immediately
- mistake-specific warnings tied to the named skill
- short, plain sentences that sound like a capable teacher or practitioner giving instruction

Invalid practitioner voice includes avoidable phrases such as:
```
source-derived rationale
visual evidence
spatial relationship
visual-to-body transformation
artifact quality
domain workflow
observed transformation
practitioner artifact
semantic usefulness
body individualization
validation status
locator evidence
```
These phrases may appear in `Meta/` validation files. They should not appear in exported object bodies unless the phrase is normal vocabulary for the craft being extracted.

Source phrasing should be studied, understood, and re-expressed as usable craft instruction. The exported object should sound like something a serious learner would write in a working notebook after studying the source carefully.

## §2.14 — Do / Don't Intrinsicity Rule

For every exported pattern, the `## Do`, `## Don't`, and `## Checklist` sections must be intrinsically tied to the named pattern.

A Do item is valid only if it tells the practitioner a positive action that belongs to this exact skill. A Do item is INVALID if it could be copied unchanged into many unrelated patterns.

A Don't item is valid only if it names the exact mistake, misuse, false move, misreading, or anti-pattern this pattern prevents. A Don't item is INVALID if it names only a generic failure such as:
- losing structure
- ignoring proportion
- skipping verification
- relying on guesswork
- making the work unclear
- failing to test
- using the wrong approach
- forgetting fundamentals

A Checklist item is valid only if it verifies something observable in the produced work that belongs to this exact skill.

Examples:
```
Pattern: Use Anklebone Placement To Identify Side-View Leg Rhythm
VALID Do: Check whether the anklebone is trapped inside the lower-leg contour before choosing the leg rhythm.
VALID Don't: Don't use the front-leg B rhythm when the anklebone is enclosed by the leg outline; the leg is turning side-on.
VALID Checklist: The side-view leg shows an S-curve that starts high on the front thigh, breaks at the knee, and sweeps back through the calf.

INVALID Do: Observe the structure carefully.
INVALID Don't: Don't rely on guesswork.
INVALID Checklist: The drawing has correct proportions.
```

```
Pattern: Prevent Object Slicing
VALID Do: Pass polymorphic objects by reference or pointer when derived state must survive the call.
VALID Don't: Don't accept a base class by value if callers may pass derived objects with extra state.
VALID Checklist: A derived object with extra fields keeps those fields after passing through the API boundary.

INVALID Do: Use type-safe code.
INVALID Don't: Don't ignore object behavior.
INVALID Checklist: The code is maintainable.
```

If a Do, Don't, or Checklist block fails intrinsicity, the object must be rewritten, merged, rejected, or deferred before EXPORT.



## §2.15 — No Audit Language In Skill Bodies

Final object bodies are skill instructions, not validation reports.

The following kinds of language belong in `Meta/` files and validation ledgers, not in exported object bodies:
- PASS process language
- source-audit language
- schema language
- evidence-chain language
- validation or gate language
- academic filler that replaces craft instruction

Forbidden in final object bodies unless the phrase is normal vocabulary in the craft:
```
source-derived
visual evidence
locator evidence
practitioner artifact
body blueprint
domain workflow
validation
source unit
object-specific rationale
evidence chain
section provenance
semantic usefulness
materialization
candidate
recovery row
PASS 1
PASS 2
PASS 3
EXPORT
```

VALID:
- "Block the rib cage as a barrel before you hang the arms from it."
- "Pass polymorphic objects by reference when the derived state must survive the call."
- "Deglaze while the fond is still hot enough to dissolve into the liquid."

INVALID:
- "Use the visual evidence to validate the source-derived spatial relationship."
- "Confirm the artifact quality against the body blueprint."
- "Apply the domain workflow captured by the candidate row."

The exported object must sound like a working note a practitioner can use while doing the skill.

## §2.16 — Confidence Calibration Rule

`confidence` is not decoration. It must reflect evidence strength and extraction quality.

High confidence requires:
- direct text evidence, direct visual evidence, or both
- a source-independent skill body
- a complete PASS 3 body blueprint
- no source dependency
- no duplicate body substance
- practitioner-voice wording
- intrinsic Do / Don't / Checklist content when the object is a pattern

Medium confidence requires:
- partial but usable evidence
- a complete source-independent skill body
- a clear reason why evidence is incomplete, indirect, or inferential

Low confidence final exports are allowed only when the skill is still useful, clearly marked low, and explicitly justified in `Meta/CONFIDENCE_CALIBRATION_VALIDATION.csv`. Low confidence objects that are speculative, source-dependent, generic, or weak must be rejected or deferred.

EXPORT must create `Meta/CONFIDENCE_CALIBRATION_VALIDATION.csv`.

Required columns:
```
object_id, object_type, confidence, direct_text_evidence_present,
direct_visual_evidence_present, complete_body_blueprint_present,
source_independent_body_present, duplicate_body_absent,
practitioner_voice_passed, intrinsicity_passed,
confidence_level_justified, confidence_calibration_status, failure_reason
```

A confidence value that contradicts the evidence is a validation failure.


---

# §3 — THE PHASE STATE MACHINE (HARD-GATED)

## §3.0 — The Iron Law of Phases

PASS is a multi-turn gated workflow. Each phase MUST:
1. Run as the active phase only.
2. Create only its own artifacts.
3. Print the required phase render to the user.
4. End with `Continue [Y/N]`.
5. STOP. No more output after the render.
6. Wait for a LATER user message with explicit continuation.

**The model may NEVER run two phases in one turn.**

**"Run a full PASS" authorizes PREFLIGHT only in the current turn.** It does NOT authorize continuation through PASS 1, PASS 2, PASS 3, or EXPORT.

### §3.0.1 — "FULL PASS" Command Semantics

"FULL PASS" means full-source, maximum-pressure extraction against the entire scoped source.

It does NOT authorize:
- same-turn phase collapse
- skipping phase gates
- merging all phases into one turn
- exporting without continuation tokens
- treating the phase machine as optional

When the user says "FULL PASS," "do a full pass," "run the whole thing," or any equivalent, PREFLIGHT must set:
```
Extraction pressure: foundation-density
```

The phase machine remains mandatory. Every phase still stops at `Continue [Y/N]`. Every phase still requires a separate user turn. "FULL PASS" means "extract everything at maximum density." It does NOT mean "skip the gates."

If the model interprets "FULL PASS" as permission to collapse phases, the run is INVALID:
```
EXTRACTION MATERIAL MAY EXIST, BUT SAME-TURN PHASE BYPASS INVALIDATED PASS.
```

## §3.1 — Allowed State Transitions

```
IDLE → PREFLIGHT
PREFLIGHT → WAITING_FOR_PREFLIGHT_CONTINUE
WAITING_FOR_PREFLIGHT_CONTINUE → PASS1     (requires user message)
PASS1 → WAITING_FOR_PASS1_CONTINUE
WAITING_FOR_PASS1_CONTINUE → PASS2         (requires user message)
PASS2 → WAITING_FOR_PASS2_CONTINUE
WAITING_FOR_PASS2_CONTINUE → PASS3         (requires user message)
PASS3 → WAITING_FOR_PASS3_CONTINUE
WAITING_FOR_PASS3_CONTINUE → EXPORT        (requires user message)
EXPORT → COMPLETE
```

## §3.2 — Forbidden State Transitions (Instant PASS Failure)

```
IDLE → PASS1                              (skipped PREFLIGHT)
IDLE → EXPORT                             (skipped everything)
PREFLIGHT → PASS1 in same assistant turn  (same-turn bypass)
PASS1 → PASS2 in same assistant turn      (same-turn bypass)
PASS2 → PASS3 in same assistant turn      (same-turn bypass)
PASS3 → EXPORT in same assistant turn     (same-turn bypass)
any phase → COMPLETE without artifact proof
```

**ANY forbidden transition invalidates the ENTIRE run.**

## §3.3 — Same-Turn Completion Ban

The first assistant response after a source is supplied may ONLY complete PREFLIGHT.

No full PASS archive is valid if created in the same turn as the initial request.

No claim of "all phases complete" or "export ready" is valid in the same turn as the source upload.

If same-turn completion occurs:
```
PHASE MATERIAL MAY EXIST, BUT COMPLETION RENDER WAS PRINTED BEFORE REQUIRED ARTIFACTS EXISTED.
PHASE COUNTS WERE PRINTED WITHOUT ARTIFACT-DERIVED PROOF.
EXTRACTION MATERIAL MAY EXIST, BUT SAME-TURN PHASE BYPASS INVALIDATED PASS.
```

## §3.4 — Backfill Ban

PASS may NOT create retrospective proof. ALL of these are forbidden:
- Generating PREFLIGHT after PASS 1 has begun
- Generating PASS1_CANDIDATE_LEDGER.md after PASS 2 has begun
- Generating PASS2_RECOVERY_LEDGER.md after PASS 3 has begun
- Generating PASS3_FINAL_EXPORT_LEDGER.md during EXPORT without a prior PASS 3 phase
- Writing `Continue [Y/N]` fields that imply consent already granted
- Placing phase renders in an archive when they were never printed at the phase stop-point

**If a phase was skipped, simulated, collapsed, or backfilled, the run is INVALID. The fix is to restart at the first invalid phase, NOT to patch the archive.**

## §3.5 — Valid Continuation Tokens

The user must reply AFTER the phase render. Valid tokens:
```
Y, Yes, Continue, or unambiguous instruction to proceed
```

INVALID continuation evidence:
- The original "run full PASS" request
- Assistant-invented approval
- Inferred approval
- "Continue [Y/N]: Y — user requested full PASS in the same turn"
- Any approval inside an archive file

## §3.6 — Artifact-First Phase Rendering

A phase completion render is a claim. A claim requires proof before it is printed.

A phase may NOT print its success render until every required artifact for that phase already exists.

A phase may NOT print counts unless the counts were computed from the artifact files for that phase.

A phase may NOT type candidate counts, coverage counts, object counts, or validation counts from model belief.

A phase may NOT print:
- `ledger: created`
- `coverage processed`
- `schema validation: pass`
- `routing validation: pass`
- `semantic usefulness validation: pass`
- `archive created`
unless the exact required files already exist and the stated counts were derived from them.

If required artifacts do not exist, the phase is incomplete. It must NOT print the normal phase completion render.

Required failure render for missing phase artifacts:
```
PASS RESULT: PHASE INCOMPLETE

FAILED GATE: <phase name> artifact pre-render validation

Reason: <required artifact paths> do not exist, so <phase name> cannot claim completion.

Retry target: <same phase>
```

This failure render is not a phase completion. It does not authorize the next phase.

### §3.6.1 — Tool-Calling Environment Clarification

In a tool-calling environment (where the model creates files and prints text in the same assistant turn), the phase render MAY appear in the same assistant turn as file creation, PROVIDED:

1. The files were created by tool calls BEFORE the render text appears.
2. The render counts were computed FROM the created files (e.g., by reading back the file or counting rows), not from model memory or belief.
3. The model did NOT print the render first and create files after.
4. The model did NOT print counts and then create files that happen to match.

The creation order within one turn is: tool calls that create artifacts → tool calls or logic that compute counts from those artifacts → render text containing those counts. Any other order is INVALID.

## §3.7 — Checkpoint Rule for Large Sources

Large sources may require same-phase checkpoints.

A checkpoint is allowed only when a phase has begun but cannot honestly complete in the current turn.

A checkpoint may preserve progress and list completed artifact fragments.

A checkpoint may NOT:
- claim phase completion
- print the required phase completion render
- end with `Continue [Y/N]`
- authorize the next phase
- count as a completed phase
- create final skill objects
- create retrospective proof

**Checkpoint artifacts are cumulative.** When resuming a checkpointed phase in a later turn, the model must load the existing checkpoint artifacts and APPEND new rows to them. The model may NOT create a fresh artifact that covers only the remaining source units. The final phase-completion artifact set must cover ALL scoped source units in a single consolidated file per artifact type. If the model cannot load prior checkpoint files (e.g., environment reset), it must re-process from the beginning of the phase or declare the phase incomplete.

Checkpoint render:
```
PASS CHECKPOINT: <phase name>

Progress preserved: <artifact paths created>
Coverage completed so far: <units done / units scoped>
Still required before phase completion: <artifact paths / remaining units>
Next action: continue same phase
```

## §3.8 — First Invalid Phase Recovery Rule

If a required artifact is missing, corrupted, malformed, or contradicted by the transcript, recovery must restart at the first invalid phase.

Recovery may NOT backfill missing proof and continue to a later phase in the same turn.

Examples:
- Missing PASS1_CANDIDATE_LEDGER.* means retry PASS 1, not PASS 2.
- Missing PASS2_DIFFERENTIAL_PROOF.csv means retry PASS 2, not PASS 3.
- Missing PASS3_FINAL_EXPORT_LEDGER.* means retry PASS 3, not EXPORT.
- Missing schema/materialization proof means retry EXPORT, not call the archive complete.

The retry must produce the required artifacts and then stop at that same phase's gate.



## §3.9 — Run Root Immutability Rule

PREFLIGHT must declare a single `run_root` path in `Meta/PREFLIGHT.md`.

All phase artifacts, validation files, routed objects, indexes, catalogs, and final archives must be created under that same run root.

INVALID:
- PASS 1 artifacts under a different sibling folder than PREFLIGHT
- PASS 2 consuming ledgers from one root and writing to another root
- PASS 3 body blueprints in a side folder
- EXPORT materializing objects from mixed roots
- phase-specific folders that split a single run into multiple roots

Validation file:
```
Meta/RUN_ROOT_VALIDATION.md
```

Required rows:
```
phase_name, declared_run_root, artifact_path, artifact_under_run_root,
consumed_input_path, consumed_input_under_run_root, run_root_status, notes
```

A single artifact outside the declared run root invalidates the run unless the file is an external baseline or calibration archive explicitly declared in PREFLIGHT.

## §3.10 — Post-Export Critique Triage Rule

When a user reports a quality failure after EXPORT, PASS must identify the first invalid phase before attempting repair.

Triage map:
- bad or missing candidates → restart PASS 1
- missed recovery or weak second read → restart PASS 2
- bad reconciliation, weak body blueprints, poor confidence calibration, poor teaching extraction, or bad evidence chain → restart PASS 3
- correct blueprints but bad materialized files, bad indexes, schema slips, routing slips, or body text not matching blueprint → restart EXPORT

The model may not casually patch final objects unless the failure is strictly an EXPORT materialization defect.

Creates when post-export critique occurs:
```
Meta/POST_EXPORT_CRITIQUE_TRIAGE.md
```

Required fields:
```
reported_issue, affected_objects_or_files, first_invalid_phase,
why_earlier_phases_pass_or_fail, required_retry_phase, patch_allowed_yes_no,
triage_status
```

If the first invalid phase is PASS 1, PASS 2, or PASS 3, the correct fix is to restart at that phase and proceed through later gates again.


---

# §4 — PHASE DEFINITIONS

## §4.1 — PREFLIGHT

**Purpose:** Identify source, inventory its content, and plan ingestion.

**Creates:** `Meta/PREFLIGHT.md`, initial `Meta/COVERAGE.md`, `Meta/SOURCE_CONTENT_INVENTORY.csv`, declares `run_root`

**Render precondition:** before printing the PREFLIGHT render, `Meta/PREFLIGHT.md`, initial `Meta/COVERAGE.md`, and `Meta/SOURCE_CONTENT_INVENTORY.csv` must already exist or be included in the phase artifact package. If they do not exist, print the PHASE INCOMPLETE failure render from §3.6 instead.

**MUST NOT** create candidate objects. **MUST NOT** summarize the source. **MUST NOT** estimate "important" sections only. **MUST NOT** reduce scope. **MUST NOT** proceed to PASS 1.

### §4.1.0 — Source Content Inventory

Before extraction begins, PREFLIGHT must create a systematic unit-by-unit inventory of the source's content. This inventory is the extraction baseline — it defines the universe that PASS 1 and PASS 2 extract FROM.

**Why this exists:** Without a fixed inventory, every PASS run produces a different candidate count from the same source because the model pays attention to different content on different runs. The inventory pins down what the source contains so that extraction is repeatable.

PREFLIGHT must create:
```
Meta/SOURCE_CONTENT_INVENTORY.csv
```

**Procedure:** Go through the entire source unit by unit (chapter by chapter, section by section, slide by slide, page by page — whatever the source's natural structure is). For each unit, record what it contains. Do not judge whether content is extractable yet — just inventory it.

Required columns:
```
unit_id, unit_type, unit_title, source_locator,
topics_covered, examples_present, exercises_present,
definitions_present, procedures_present, warnings_present,
diagrams_present, tables_present, code_listings_present,
worked_examples_present, teaching_methods_present,
estimated_skill_candidates, unit_notes
```

Allowed `unit_type` values:
```
chapter, section, subsection, slide_group, page_range,
appendix, exercise_set, worked_example_set, reference_section
```

`estimated_skill_candidates` is a rough count of how many extractable skills this unit likely contains. It is an estimate, not a commitment — PASS 1 may find more or fewer. But the total across all units establishes an expected extraction range.

**Rules:**

1. **Every unit must appear.** If the source has 15 chapters, the inventory has 15+ rows (more if chapters have meaningful subsections). A source with 200 pages and 15 chapters should not have 15 generic rows — it should have enough rows to capture the source's actual structure.

2. **No unit may be skipped.** Appendices, exercise sections, reference tables, and worked examples all get rows. They often contain the best skill material.

3. **The inventory is a census, not a selection.** It records what EXISTS in the source, not what the model thinks is important. The model's judgment about importance comes later in PASS 1.

4. **The inventory is the extraction baseline.** PASS 1's `COVERAGE.csv` must reference inventory unit_ids to show which units were extracted from. If a unit appears in the inventory but has zero candidates in PASS 1, the model must explain why in `COVERAGE.csv`.

5. **The inventory must be created BEFORE PASS 1 begins.** It is a PREFLIGHT artifact. It cannot be created retroactively during PASS 1.

**Extraction range:** The sum of `estimated_skill_candidates` across all inventory rows establishes an expected extraction range. PASS 1 candidate count should be within 50-200% of this estimate. If PASS 1 produces less than 50% of the estimated range, it likely missed significant source content. If it produces more than 200%, it likely over-fragmented.

**Rerun stability:** If the same source is PASSed again, the Source Content Inventory should be nearly identical (same units, same topics, similar estimates). The inventory is a property of the SOURCE, not the model's attention on a given day. Small variations in estimates are expected; missing entire chapters is not.

**Required render addition:**
```
PASS: PREFLIGHT

Source detected: <title or filename>
Type: <PDF/text/archive/image/mixed/etc.>
Length: <pages/files/units if known>
Detected domain: <programming/art/math/writing/etc.>
Source content inventory: <unit count> units inventoried
Estimated extraction range: <low> - <high> candidates
Coverage plan: <how the source will be processed>
Planned routing: <domain/category/subcategory>
Archive role: <seed_source | merge_source | calibration_source | rebuild_source>
Extraction pressure: <foundation-density | differential-merge | calibration-only | rebuild-density>
Baseline used for duplicate suppression: <yes/no/path>
Calibration archive used: <yes/no/path>

Continue [Y/N]
```


## §4.1.1 — Archive Role Declaration

PREFLIGHT must declare the archive role.

Allowed archive roles:
```
seed_source
merge_source
calibration_source
rebuild_source
```

Meanings:
- `seed_source`: first source in a new archive; extract foundational skills aggressively
- `merge_source`: compare against an existing archive; preserve only new, superior, variant, or specialized skills
- `calibration_source`: use as a quality reference only; do not suppress candidates against it
- `rebuild_source`: regenerate a prior archive from scratch

If archive role is ambiguous, default to `seed_source` unless the user provides an existing archive to merge into.

PREFLIGHT must also declare:
```
Archive role: <seed_source | merge_source | calibration_source | rebuild_source>
Extraction pressure: <foundation-density | differential-merge | calibration-only | rebuild-density>
Baseline used for duplicate suppression: <yes/no/path>
Calibration archive used: <yes/no/path>
```

## §4.1.2 — Skill Atom Admission Test

A PASS candidate is valid only if it captures a reusable practitioner capability.

Before a row may enter `PASS1_CANDIDATE_LEDGER`, it must pass ALL tests:

1. Practitioner Action Test:
   The candidate tells a practitioner what to DO, PRACTICE, DESIGN, CHECK, REFACTOR, DEBUG, BUILD, DRAW, COOK, SOLVE, TEACH, PERFORM, COMPOSE, or otherwise execute in the source domain.

2. Artifact Test:
   The candidate can change or produce a real artifact in the domain: code, API, class, test, refactor, design note, proof, sketch, figure, composition, recipe, dish, scene, lesson, performance, etc.

3. Transfer Test:
   The candidate applies beyond the exact sentence, example, page, chapter, image, or source unit where it was found.

4. Failure / Decision Test:
   The candidate helps avoid a mistake, choose between alternatives, verify correctness, improve quality, recover from failure, or practice a skill.

5. Non-Summary Test:
   The candidate is not merely a fact about the source, a restated heading, a definition, an isolated language rule, an art label, an anatomy label, a title-cased sentence fragment, or source commentary.

If a candidate fails any test, reject it, attach it as Notes/context, or merge it into a stronger object. Do not export it as a standalone object.

Skillness comes before schemaness.

## §4.1.3 — Source-Fragment Candidate Ban

A PASS candidate is INVALID if its core skill claim is merely:
- a source sentence rewritten as an IF/THEN rule
- a chapter heading turned into a skill name
- a grammar/language rule without a practitioner decision attached
- a definition without practitioner use
- an isolated API fact without a use pattern, failure mode, or workflow
- an anatomy label without a drawing/construction/proportion use
- a cooking ingredient fact without a preparation, flavor, timing, or technique use
- a warning that does not become an actionable check
- title-cased prose
- OCR fragments, code-token fragments, or sentence fragments

Source semantics may be extracted ONLY when converted into a practitioner skill.

Examples:
```
INVALID: A Function Cannot Return Mark It Noreturn
VALID: Mark Non-Returning Functions With noreturn
VALID: Verify Control-Flow Assumptions Around noreturn Functions

INVALID: Anklebone Is Inside The Contour
VALID: Use Anklebone Placement To Identify Side-View Leg Rhythm
VALID: Drill Side-View Lower-Leg S-Curve Construction
```

## §4.2 — PASS 1 (Gut Extraction)

**Purpose:** Maximum-pressure extraction from the ENTIRE scoped source, guided by the Source Content Inventory.

**Creates:**
```
Meta/PASS1_CANDIDATE_LEDGER.md
Meta/PASS1_CANDIDATE_LEDGER.csv
Meta/PASS1_CANDIDATE_LEDGER.jsonl
```
All three formats are REQUIRED. If any one is missing, PASS 1 is incomplete and the phase gate fails. The `.md` is the human-readable ledger. The `.csv` is the machine-readable ledger. The `.jsonl` is the structured data ledger. They must contain the same rows. A PASS 1 that creates `.md` and `.csv` but omits `.jsonl` has a missing proof artifact and is INVALID.

**Render precondition:** before printing the PASS 1 completion render, all of these must already exist: `Meta/PASS1_CANDIDATE_LEDGER.md`, `Meta/PASS1_CANDIDATE_LEDGER.csv`, `Meta/PASS1_CANDIDATE_LEDGER.jsonl`, `Meta/COVERAGE.md`, and `Meta/COVERAGE.csv`. Candidate counts and coverage counts must be computed from those files. If any required file is missing, print the PHASE INCOMPLETE failure render from §3.6 instead.

**Inventory-guided extraction:** PASS 1 must extract from EVERY unit listed in `Meta/SOURCE_CONTENT_INVENTORY.csv`. The COVERAGE.csv must reference inventory `unit_id` values to show which units were covered. If a unit has zero candidates, COVERAGE.csv must include a row for that unit with `candidates_extracted: 0` and a `reason` explaining why no candidates were found (e.g., "unit contains only front matter," "unit is a bibliography," "content is purely definitional with no practitioner action").

**Extraction range check:** After PASS 1 completes, compare total candidates against the Source Content Inventory's estimated range. If candidates fall below 50% of the low estimate, the model must explain the shortfall in `COVERAGE.md`. This is not an automatic failure — some sources have less extractable content than estimated — but the explanation must be unit-specific, not a blanket statement.

For image-heavy sources, also creates: `Meta/VISUAL_STUDY_LEDGER.md` (and .csv)

**MUST read/inspect EVERY scoped source unit.** No skipping. No sampling. No "important sections only."

**Candidate ledger required columns:**
```
candidate_id, candidate_type, candidate_name, source_unit, source_locator,
evidence_type, visual_evidence_summary, self_contained_skill_statement,
source_dependency_risk, skill_atom_tests_passed,
extracted_skill_claim, why_candidate_exists, initial_domain, initial_category,
initial_subcategory, portability_class, language_or_tool_specificity,
teaching_potential, status, recovery_flag, notes
```

**`candidate_type` MUST be `pattern`, `drill`, or `ap`.** No fourth type. Ever.

**Required render:**
```
PASS: PASS 1 — GUT EXTRACTION

Coverage processed: <units processed / units scoped>
PASS 1 candidate ledger: <created / blocked>
Pattern candidates: <count>
Drill candidates: <count>
AP candidates: <count>
Variant candidates: <count>
Weak / uncertain candidates: <count>
Recovery targets flagged for PASS 2: <count>
Phase gate: WAITING_FOR_PASS1_CONTINUE

Continue [Y/N]
```

**PASS 1 does NOT export files. PASS 1 does NOT run PASS 2.**

### §4.2.1 — Intensive Teaching Extraction Sweep

For instructional sources, teaching extraction is active, not incidental.

PASS 1 must inspect the source not only for what skill is being taught, but for how the source teaches it. Teaching captures include explanation moves, demonstration order, visual annotation, exercise progression, comparison strategy, critique method, learner-error diagnosis, prompt design, and staged reveal.

For instructional sources, PASS 1 creates:
```
Meta/TEACHING_EXTRACTION_LEDGER.md
Meta/TEACHING_EXTRACTION_LEDGER.csv
Meta/TEACHING_EXTRACTION_LEDGER.jsonl
```

Required columns:
```
teaching_candidate_id, source_unit, source_locator, teaching_signal_type,
observed_teaching_move, learner_problem_addressed, demonstration_method,
progression_or_sequence, critique_or_feedback_method,
practice_assignment_implied, transformed_skill_object_candidate_id,
route_decision, teaching_capture_status, notes
```

Allowed `teaching_signal_type` values:
```
demonstration, progression, analogy, correction, critique, exercise_design,
sequencing, visualization, comparison, failure_diagnosis, review_method,
prompt, scaffold, annotation, staged_reveal, other
```

Rules:
- If the source uses arrows, labels, overlays, repeated poses, before/after comparisons, staged examples, classroom-style explanation, or directed practice, PASS must consider whether there is a teaching capture.
- Teaching captures must still become `pattern`, `drill`, or `ap`; teaching is a route, not a type.
- A teaching object is valid only when it captures a reusable teaching move, not merely the topic being taught.
- If a source contains rich teaching method but PASS exports almost no teaching skills, PASS 2 must explicitly justify that in `PASS2_DIFFERENTIAL_PROOF.csv` or recover the missed teaching candidates.

### §4.2.2 — Practitioner Voice Lexicon Capture

PASS 1 must create a source-specific craft vocabulary guide:
```
Meta/PRACTITIONER_VOICE_LEXICON.md
```

The lexicon records:
- source-native craft terms
- preferred action verbs
- concrete domain nouns
- domain checks and warning language
- phrases to avoid in exported object bodies
- examples of target practitioner voice

For a figure drawing source, the lexicon should capture words such as barrel, wedge, ovoid, column, contour, overlap, undercurve, S-line, B-shape, anklebone, rib cage, pelvic wedge, deep space, and projection when those terms are actually used or clearly taught by the source.

EXPORT object bodies should draw from this working vocabulary unless clearer practitioner wording requires rephrasing.

## §4.3 — PASS 2 (Differential Recovery Extraction)

**Purpose:** Re-read the SAME source, compare against PASS 1, recover what was missed.

**Creates:**
```
Meta/PASS2_RECOVERY_LEDGER.md
Meta/PASS2_RECOVERY_LEDGER.csv
Meta/PASS2_RECOVERY_LEDGER.jsonl
Meta/PASS2_DIFFERENTIAL_PROOF.csv
```
All three RECOVERY_LEDGER formats are REQUIRED. If any one is missing, PASS 2 is incomplete.

**Render precondition:** before printing the PASS 2 completion render, all of these must already exist: `Meta/PASS2_RECOVERY_LEDGER.md`, `Meta/PASS2_RECOVERY_LEDGER.csv`, `Meta/PASS2_RECOVERY_LEDGER.jsonl`, and `Meta/PASS2_DIFFERENTIAL_PROOF.csv`. Counts must be computed from those files. If any required file is missing, print the PHASE INCOMPLETE failure render from §3.6 instead.

**PASS 2 CANNOT rubber-stamp PASS 1.** PASS 2 is INVALID if it only says "no recovery needed" or "PASS 1 already sufficient" or "all candidates reviewed."

**For EVERY scoped source unit, PASS 2 must record (in PASS2_DIFFERENTIAL_PROOF.csv):**
```
source_unit_id, source_locator, pass1_candidate_ids_seen,
pass1_summary_of_what_was_captured, pass2_reinspection_action,
missed_candidate_ids_recovered, weak_candidate_ids_strengthened,
false_merge_ids_split, duplicate_ids_flagged,
taxonomy_or_teaching_corrections, no_change_justification, pass2_status
```

**Allowed `pass2_status`:** `recovered`, `strengthened`, `split`, `duplicate_flagged`, `taxonomy_corrected`, `teaching_corrected`, `checked_no_change`, `blocked_unreadable`

**A global "no recovery needed" statement is INVALID.** If most source units are `checked_no_change`, each still requires a concrete justification tied to that specific source unit.

If PASS2_DIFFERENTIAL_PROOF.csv is missing → PASS 2 FAILED.
If it has fewer rows than scoped source units → PASS 2 FAILED.

**Recovery ledger required columns:**
```
recovery_id, related_pass1_candidate_id_or_none, recovery_type, candidate_type,
candidate_name, source_unit, source_locator, what_PASS1_missed_or_got_wrong,
recovered_skill_claim, routing_action, teaching_action, notes
```

**Recovery rows must include:**
```
recovered_candidate_type: <pattern | drill | ap>
route_domain: <skills/...>
teaching_capture: <yes | no>
why_this_is_pattern_drill_or_ap: <non-empty, non-generic>
```

If `why_this_is_pattern_drill_or_ap` is empty or generic, the row is INVALID.

### §4.3.1 — PASS 2 Teaching Extraction Threshold

If the source is instructional (textbook, how-to, course material, tutorial, guided exercise book) and PASS 1 teaching captures are below 10% of total candidates, PASS 2 must:

1. Re-inspect every source unit specifically for teaching method, not just content.
2. For each source unit, ask: "Did this unit teach HOW to explain, demonstrate, annotate, sequence, correct, or practice the skill — not just what the skill is?"
3. Record per-source-unit teaching inspection evidence in `PASS2_DIFFERENTIAL_PROOF.csv`.
4. Either recover teaching candidates or provide a per-source-unit justification for why no teaching method was found.

A blanket "no teaching method found" across all source units is INVALID. Each source unit needs its own justification.

This rule exists because instructional sources almost always teach in two layers: the skill and the method of teaching the skill. A very low teaching capture count means PASS 1 missed the second layer.

**Required render:**
```
PASS: PASS 2 — DIFFERENTIAL RECOVERY EXTRACTION

Coverage reprocessed: <units reprocessed / units scoped>
PASS 1 comparison performed: <yes/no>
PASS 2 recovery ledger: <created / blocked>
Recovered candidates: <count>
Strengthened candidates: <count>
Split false merges: <count>
Duplicates identified: <count>
Weak candidates marked for rejection: <count>
Teaching captures recovered: <count>
Portability captures recovered: <count>
Phase gate: WAITING_FOR_PASS2_CONTINUE

Continue [Y/N]
```

## §4.4 — PASS 3 (Reconciliation and Validation)

**Purpose:** Merge PASS 1 + PASS 2, remove duplicates, reject weak objects, validate everything, finalize export set.

**Creates:**
```
Meta/PASS3_FINAL_EXPORT_LEDGER.md
Meta/PASS3_FINAL_EXPORT_LEDGER.csv
Meta/PASS3_FINAL_EXPORT_LEDGER.jsonl
```
All three formats are REQUIRED. If any one is missing, PASS 3 is incomplete.

**Render precondition:** before printing the PASS 3 completion render, all PASS 3 required files must already exist: `Meta/PASS3_FINAL_EXPORT_LEDGER.md`, `Meta/PASS3_FINAL_EXPORT_LEDGER.csv`, `Meta/PASS3_FINAL_EXPORT_LEDGER.jsonl`, `Meta/PASS3_BODY_BLUEPRINT_LEDGER.csv`, `Meta/PASS3_BODY_BLUEPRINT_LEDGER.jsonl`, `Meta/EVIDENCE_CHAIN_LEDGER.csv`, `Meta/EVIDENCE_CHAIN_LEDGER.jsonl`, `Meta/CLOSED_TYPE_VALIDATION.md`, `Meta/TEACHING_BOILERPLATE_VALIDATION.md`, `Meta/TAXONOMY_RECONCILIATION.md`, and `Meta/ROUTE_REDIRECTS.jsonl`. Counts and validation states must be computed from those files. If any required file is missing, print the PHASE INCOMPLETE failure render from §3.6 instead.

Also creates during this phase:
```
Meta/CLOSED_TYPE_VALIDATION.md
Meta/TEACHING_BOILERPLATE_VALIDATION.md
Meta/TAXONOMY_RECONCILIATION.md
Meta/ROUTE_REDIRECTS.jsonl
Meta/EVIDENCE_CHAIN_LEDGER.csv
Meta/EVIDENCE_CHAIN_LEDGER.jsonl
```

**PASS 3 must run a closed-type scan.** If any candidate has a type other than `pattern`/`drill`/`ap`, PASS 3 must reject it and record the rejection. If PASS 3 approves a fourth type, PASS 3 FAILS.

**PASS 3 must validate teaching captures for distinctness.** If multiple teaching objects share near-identical procedure text with only the topic changed, they must be merged, variant-absorbed, or rejected.


### §4.4.1 — PASS 3 Body Evidence Blueprint

PASS 3 must approve bodies, not only names and routes.

### §4.4.0 — PASS 3 Blueprint Batch Processing

**Why templates keep recurring:** The model cannot write 100+ individual body sections in a single turn. When it tries to blueprint all patterns at once, it compresses them into category-level templates because that is the only way to fit them in working memory. This is a fundamental context-window limitation, not a rule-following failure. The model understands the rules; it cannot execute them at scale in one pass.

**Solution: batch processing.**

PASS 3 body blueprinting must process objects in small batches. Each batch must contain no more than 10-15 objects. Within a batch, the model writes each object's body sections individually, with source-specific content, before moving to the next batch.

**Batch processing rules:**

1. **Batch size:** Maximum 10-15 objects per blueprint batch. If 148 patterns need blueprinting, that is 10-15 batches, not one.

2. **Batch isolation:** Each batch is processed in its own turn. The model must complete one batch's blueprints, run the within-batch similarity check, and output the batch before starting the next batch.

3. **Within-batch similarity check:** After writing a batch of blueprints, the model must compare the Do, Don't, Checklist, and Notes fields WITHIN the batch. If any sentence appears in more than 2 objects within the batch, the batch fails and must be rewritten before proceeding.

4. **Cross-batch similarity check:** After all batches are complete, the model must run the full BODY_SIMILARITY_ANALYSIS across ALL batches. Templates that span batch boundaries are still invalid.

5. **Source re-reading per batch:** For each batch, the model must re-read the specific source pages relevant to those objects before writing their blueprints. The model may NOT write blueprints from memory of a previous source reading — it must look at the actual source content for each batch.

6. **Batch continuation:** Each batch ends with a continuation token:
```
PASS 3 BLUEPRINT BATCH <n>/<total>

Objects blueprinted this batch: <count>
Within-batch template check: <clean / N templates detected>
Cumulative objects blueprinted: <count> / <total>

Continue [Y/N]
```

7. **No batch may contain only objects from the same category.** If 26 patterns share the category "class mechanics," they must be spread across multiple batches, interleaved with patterns from other categories. This prevents the model from entering a category-level template mode.

**The batch structure is mandatory when PASS 3 has more than 15 objects to blueprint.** For sources with ≤15 objects, single-turn blueprinting is allowed.

**If the model attempts to blueprint all objects in one turn and produces templates, the retry must use batch processing.** The model may not retry with the same single-turn approach that produced templates.

PASS 3 must create:
```
Meta/PASS3_BODY_BLUEPRINT_LEDGER.csv
Meta/PASS3_BODY_BLUEPRINT_LEDGER.jsonl
```

Every approved final object must have one body blueprint row before EXPORT.

Required columns:
```
object_id, object_type, name, source_locator, evidence_type,
evidence_chain_id, section_provenance_status,
text_evidence_summary, visual_evidence_summary, body_seed_terms,
source_specific_claim, source_independent_skill_statement,
practitioner_action, practitioner_artifact, skill_outcome,
failure_mode, verification_method, source_dependency_check, no_audit_language_status,
confidence_calibration_status,
practitioner_voice_register, practitioner_voice_status,
pattern_if, pattern_then, pattern_else, do_items, dont_items,
checklist_items, do_intrinsicity_basis, dont_intrinsicity_basis,
checklist_intrinsicity_basis, notes_basis,
drill_practice_task, drill_setup, drill_instructions,
drill_success_check, drill_common_failures,
ap_objective, ap_steps_flow, ap_notes_basis,
body_sections_seeded, body_blueprint_status, failure_reason
```

Rules:
- EXPORT may not invent object bodies from object names alone.
- EXPORT must materialize each object from its PASS 3 body blueprint row.
- If an approved object lacks a complete body blueprint, it must be rejected or deferred before EXPORT.
- If the blueprint contains source-dependent language, the object must be rewritten, rejected, or deferred before EXPORT.
- If the blueprint repeats another unrelated object's body substance, the objects must be merged, variant-absorbed, or rejected.
- If the blueprint uses avoidable academic, abstract, validation-heavy, or AI-scholarly language where craft language exists, the object must be rewritten, rejected, or deferred before EXPORT.
- For patterns, the blueprint must prove that each Do, Don't, and Checklist item is intrinsic to the named skill.
- The blueprint must identify the evidence chain row that supports the object.
- The blueprint must specify how each required body section is seeded.
- The blueprint must pass confidence calibration before EXPORT.
- The blueprint must exclude audit language from final skill-body seeds.

Body blueprints are mandatory for every PASS 3-approved object.

### §4.4.2 — Evidence Chain and Section Body Provenance

PASS 3 must prove that every final object has an unbroken chain from source evidence to exported body plan.

PASS 3 creates:
```
Meta/EVIDENCE_CHAIN_LEDGER.csv
Meta/EVIDENCE_CHAIN_LEDGER.jsonl
```

Required columns:
```
object_id, source_unit, source_locator, observation_id,
candidate_id, recovery_id_or_none, blueprint_row_id,
exported_path_planned, body_sections_supported,
evidence_chain_status, failure_reason
```

The required chain is:
```
source unit → text/visual observation → PASS1 or PASS2 candidate → PASS3 body blueprint → exported object body sections
```

Every approved object must have exactly one PASS row in `EVIDENCE_CHAIN_LEDGER`.

Section-level provenance is also mandatory. Each required body section must be traceable to a specific blueprint field:

For patterns:
```
Pattern Rule → pattern_if / pattern_then / pattern_else
Do → do_items
Don't → dont_items
Checklist → checklist_items
Notes → notes_basis
```

For drills:
```
Practice Task → drill_practice_task
Target Skill → source_independent_skill_statement or skill_outcome
Setup → drill_setup
Instructions → drill_instructions
Success Check → drill_success_check
Common Failures → drill_common_failures
Notes → notes_basis
```

For APs:
```
Objective → ap_objective
Steps / Flow → ap_steps_flow
Notes → ap_notes_basis
```

EXPORT validates section provenance with:
```
Meta/SECTION_BODY_PROVENANCE_VALIDATION.csv
```

Required columns:
```
object_id, object_type, object_path, required_section,
blueprint_field_used, section_body_matches_blueprint,
section_is_source_independent, section_uses_practitioner_voice,
section_provenance_status, failure_reason
```

If a body section cannot be traced to its blueprint field, EXPORT fails.

**Required render:**
```
PASS: PASS 3 — RECONCILIATION AND VALIDATION

PASS 1 ledger consumed: <yes/no>
PASS 2 recovery ledger consumed: <yes/no>
Candidates reconciled: <count>
Final patterns approved: <count>
Final drills approved: <count>
Final APs approved: <count>
Variants approved: <count>
Rejects recorded: <count>
Schema validation: <pass/fail>
Routing validation: <pass/fail>
Semantic usefulness validation: <pass/fail>
Blueprint batches processed: <count>
Blueprint batch size: <max objects per batch>
Body blueprints approved: <count>
Body blueprints failed (template detected): <count>
Body blueprints rewritten: <count>
Body similarity analysis: <clean / templates detected>
Name-paste detections: <count>
Notes template detections: <count>
PASS 3 final export ledger: <created / blocked>
Phase gate: WAITING_FOR_PASS3_CONTINUE

Continue [Y/N]
```

**PASS 3 is NOT EXPORT.** PASS 3 creates the final approved set. PASS 3 does NOT create object files.

**PASS 3 validation scope:** PASS 3 validates the CANDIDATE SET, not materialized files. "Schema validation" at PASS 3 means: every approved candidate's metadata (type, required keys, enum values, routing_class/specialization_axis consistency, semantic name) is checked against the closed templates BEFORE materialization. "Routing validation" means: every approved candidate's planned route is checked for vague-middle violations, teaching/execution correctness, and taxonomy cohesion. These are pre-flight checks on the approved set. Full file-level schema validation (byte-0 frontmatter, body headings, body content) occurs at EXPORT after materialization.

## §4.5 — EXPORT

**Purpose:** Materialize validated objects as routed, schema-valid files.

**Creates:** ALL final files (see §7 for full archive structure).

**Render precondition:** before printing the EXPORT render, the archive and all required validation files from §7 and §8 must already exist. Final object count, per-object markdown count, index count, schema result, materialization result, and archive path must be computed from the actual archive. If any required file is missing, print the PHASE INCOMPLETE failure render from §3.6 instead.

EXPORT may ONLY materialize objects approved by PASS 3.

### §4.5.1 — Independent Export Revalidation

After all object files are materialized to disk, EXPORT must perform independent revalidation. This is not optional. This is not satisfied by prior phase validation. This is a fresh, independent inspection of the materialized files.

The revalidator must reopen every exported `.md` file from disk and validate the actual materialized file. The revalidator may NOT trust:
- PASS 3 ledgers
- object catalogs
- schema validation files from earlier phases
- model claims or beliefs
- generated counts from any prior phase
- any self-reported validation result

For every materialized object file, the revalidator must check:
1. byte-0 `---` (file begins with YAML frontmatter, no preceding content)
2. parseable YAML frontmatter (strict parse, no syntax errors)
3. exactly one frontmatter block before H1 (no second `---` block)
4. required keys present for the object type
5. no extra keys (no invented fields, no guard keys, no custom metadata)
6. valid enum values for all constrained fields
7. exact `reference` map shape with all required subfields
8. H1 exactly matches `name`
9. exact required body headings in correct order for the object type
10. no extra primary H2 headings (no guard sections, no invented sections)
11. `variants` field present and correctly shaped (YAML list syntax)
12. `object_id` uniqueness across the entire archive
13. filename begins with correct `PAT_`, `DRILL_`, or `AP_` prefix
14. filename contains a semantic skill slug (not ID-only, not fragment)
15. route path exists under `skills/**` and matches `routing_class`
16. `cross_links` targets resolve to existing `object_id` values in the archive
17. for drills: `target_skill` is inside the single frontmatter block

**Body-quality revalidation checks (MANDATORY — these are NOT optional):**

18. **Pattern Rule specificity:** For patterns, the `## Pattern Rule` IF clause must describe a specific decision situation, NOT restate the pattern name. The following IF shapes are INVALID:
    - `IF <pattern name> is the decision in front of you`
    - `IF you need to <pattern name>`
    - `IF <pattern name> applies`
    - ANY IF clause that works by pasting the pattern name into a generic wrapper
    The IF must name the concrete situation where the decision arises. Example: `IF a base class is accepted by value and callers may pass derived objects with extra state` — NOT `IF prevent object slicing is the decision in front of you`.

19. **ELSE non-boilerplate:** For patterns, the ELSE clause (if present) must be specific to the pattern. The following ELSE shapes are INVALID:
    - `keep the simpler version and add this pattern only when <name> is/becomes the active problem`
    - ANY ELSE clause that is identical across multiple unrelated patterns
    The ELSE must name the specific fallback action for this exact decision.

20. **Do/Don't intrinsicity spot-check:** For patterns, compare the Do and Don't items across all patterns in the archive. If ANY Do or Don't line appears verbatim or near-verbatim in more than 3 unrelated patterns, every pattern containing that line FAILS intrinsicity. Common boilerplate lines that MUST be detected:
    - `Name the concrete file, function, class, loop, stream, or build command touched by <name>`
    - `Check the smallest program or code path where <name> matters`
    - `Do not hide the type, ownership, indexing, build, or runtime assumption that makes this pattern necessary`
    - `Do not trust the code until compilation, output, or a targeted test exercises the changed path`
    - ANY line that works by inserting the pattern name into a fixed sentence

21. **Drill body individuation:** For drills, the Practice Task, Instructions, Success Check, and Common Failures must be specific to the named drill. If these sections contain the same template text across multiple drills (with only the drill name swapped), every drill sharing the template FAILS. Common boilerplate drill templates that MUST be detected:
    - `Practice <name> on a small C/C++ example, then change one variable, input, or class detail and repeat`
    - Generic 4-step instructions (write/compile/run/change)
    - ANY Instructions section that works by inserting the drill name into fixed steps

22. **Folder size compliance:** No `patterns/`, `drills/`, `aps/`, or mixed object folder may contain more than 30 object files. A folder with 31+ objects is a dump folder and FAILS regardless of its name.

23. **Teaching/execution routing correctness:** For patterns routed as `teaching` (`routing_class: teaching`, `lane_fit: teach`), the pattern must describe HOW TO TEACH a skill, not the skill itself. If the pattern's name and body describe a coding/design/implementation/debugging action (e.g., "Return Zero From main," "Use Header Guards," "Compile With Warnings"), it is an execution skill misrouted as teaching. The pattern should be routed under its execution domain, not under `teaching/`. A teaching pattern must answer: "How would I explain, demonstrate, sequence, annotate, critique, or scaffold this skill?" — NOT "What is the skill?"

24. **Notes coherence:** The `## Notes` section must be coherent human-readable prose. It must NOT contain raw OCR text dumps, slide header sequences, numerical data from figures, or sentence fragments joined without synthesis. If the Notes section reads like text extraction output rather than a human-written explanation, the object FAILS. See §12.20.

25. **Pattern Rule keyword formatting:** For patterns, the IF/THEN/ELSE lines must use `**IF**`, `**THEN**`, `**ELSE**` as bold markers followed by the clause text. The keyword must NOT be doubled: `**IF** IF ...` is INVALID. `**IF** a program uses...` is VALID. Check every pattern for doubled keywords.

EXPORT must create:
```
Meta/EXPORT_REVALIDATION.csv
```

Required columns (35 columns — the model MUST create ALL 35):
```
object_id, object_path, object_type, byte0_frontmatter, yaml_parse,
single_frontmatter_block, required_keys, no_extra_keys, valid_enums,
reference_shape, h1_matches_name, body_headings_valid, no_extra_h2,
variants_valid, object_id_unique, filename_prefix, filename_slug,
route_valid, cross_links_valid, drill_target_skill_valid,
pattern_rule_specific, else_non_boilerplate, do_dont_intrinsic,
do_not_recycle_then, notes_not_recycle_then, no_duplicate_dont,
drill_body_individual, folder_size_ok, object_in_type_subfolder,
teaching_routing_correct, teaching_path_direction,
notes_coherent, keyword_formatting_valid,
revalidation_status, failure_reason
```

**Column count enforcement:** Count the columns in the header row of the exported `EXPORT_REVALIDATION.csv`. If there are fewer than 35 columns, the file is a shallow validator and is INVALID regardless of what it reports. The model has repeatedly created revalidation files with 6-12 columns instead of 35. A 12-column revalidation checks structural schema but misses body quality, topology, folder caps, teaching path, keyword formatting, and THEN recycling — all of which are required checks.

**Topology columns are mandatory:** `folder_size_ok`, `object_in_type_subfolder`, `teaching_routing_correct`, and `teaching_path_direction` must be populated with actual check results. The most recent archive had 42 objects in one folder, teaching objects under the wrong path, and all 33 local indexes with invalid headings — none of which the 12-column revalidation detected.

### §4.5.4 — Topology Revalidation

EXPORT must also validate the archive's topology independently. This is separate from per-object revalidation.

EXPORT must create:
```
Meta/TOPOLOGY_REVALIDATION.csv
```

Required columns:
```
check_id, check_description, check_result, failure_detail
```

Required checks:
```
local_index_heading_shape    — every skills/**/index.md uses ## Entries (not ## Folders, ## Objects, etc.)
root_navigator_shape         — Indexes/INDEX_SKILLS.md uses ## Entries only, no counts, no catalog links
folder_size_cap              — no patterns/ drills/ aps/ folder exceeds 30 object files
teaching_path_direction      — all teaching objects under skills/teaching/<domain>/ not skills/<domain>/teaching/
no_lowercase_indexes         — no lowercase indexes/ directory exists
type_subfolder_universal     — every object file is inside a patterns/ drills/ or aps/ subfolder
domain_registry_complete     — Meta/DOMAIN_REGISTRY.md lists all domains used
no_guard_files               — no Meta file has GUARD in its filename
triple_format_ledgers        — all phase ledgers exist in .md .csv .jsonl
```

If any topology check fails, `Meta/TOPOLOGY_REVALIDATION.csv` must report it as FAIL with specific failure detail. If the topology revalidation reports all PASS but the archive actually has invalid indexes, oversized folders, or wrong teaching paths, the topology validator is fraudulent.

**TOPOLOGY_INDEX_VALIDATION.md must agree with TOPOLOGY_REVALIDATION.csv.** If one says PASS and the other detects failures, both are unreliable.

If any row fails: `revalidation_status: FAIL` with a specific `failure_reason`.

If the revalidation finds ANY failure, EXPORT must create:
```
Meta/REVALIDATION_FAILURE_REPORT.csv
```

Listing every failed object with its specific failures.

**A single revalidation failure invalidates EXPORT.** The model must fix the failed objects and re-run revalidation before claiming EXPORT success.

### §4.5.2 — Mandatory Body Similarity Analysis

EXPORT must create:
```
Meta/BODY_SIMILARITY_ANALYSIS.csv
```

This artifact is the primary defense against template-stamping. It cannot be satisfied by per-object checks alone. It requires cross-object comparison.

**Procedure:**

For every pattern in the archive, extract each sentence from the Do, Don't, Checklist, and Notes sections. For each sentence, create a normalized version by removing:
- the object's `name` value (all case variants)
- the object's IF clause text
- the object's THEN clause text
- the source locator (page/chapter references)
- leading "Do not" / "Do not let"
- trailing "in the ... case" / "for ..." phrases containing the name
- obvious capitalization-only differences

Then count how many distinct objects each normalized sentence appears in.

**Required columns:**
```
normalized_sentence, occurrence_count, section_type,
affected_object_ids (pipe-separated), template_status
```

**Rules:**
- If a normalized sentence appears in 4+ objects: `template_status: TEMPLATE_DETECTED`
- If a normalized sentence appears in 1-3 objects: `template_status: OK`
- If the file contains ANY row with `TEMPLATE_DETECTED`, the BODY_SIMILARITY_ANALYSIS has detected templates.

**Consequences:**
- If BODY_SIMILARITY_ANALYSIS detects templates, EXPORT may NOT report `Export state: COMPLETE`.
- Every object listed in an `affected_object_ids` column of a `TEMPLATE_DETECTED` row FAILS revalidation.
- The model must rewrite the affected body sections with source-specific content before re-attempting EXPORT.

**Name-paste detection:**

Additionally, for every pattern, check whether the object's full `name` value appears inside the Do, Don't, Checklist, or Notes body text (not counting the H1 heading). If it does, record it:

```
Meta/NAME_PASTE_DETECTION.csv
```

Required columns:
```
object_id, name_value, section_containing_name, exact_phrase_containing_name, name_paste_status
```

If the object's name appears inside any body section text: `name_paste_status: NAME_PASTED`

**Rule:** A practitioner does not write their own pattern name inside their notes. "Make the owner, length, and release point visible for the storage used by vector in the generalize a vector class to multidimensional array indexing case" is not how a human writes a coding note. A human writes: "Make the owner, length, and release point visible for the vector's storage."

If 10%+ of patterns have `NAME_PASTED`, the archive fails body quality. Every `NAME_PASTED` object must have its body sections rewritten to remove the name-paste.

**Notes template detection:**

For Notes sections specifically, extract the first 10 words of each Notes section (after the `## Notes` heading). Count how many objects share the same first-10-word prefix.

If 10%+ of objects share the same Notes prefix: the Notes are template-stamped and the archive fails.

Observed failing prefixes across four generations:
```
"Use this when <name> is the decision..."
"<Raw OCR dump from slides>"
"<THEN clause restated as first sentence>"
"Langtangen presents this around pp..."
```

### §4.5.3 — PASS 3 Body Blueprint Quality Gate

The body template problem originates in PASS 3, not in EXPORT. PASS 3 approves body blueprints that are already templated, and EXPORT faithfully materializes them.

PASS 3 must perform its own body similarity analysis BEFORE approving blueprints for export. This is a PASS 3 gate, not just an EXPORT gate.

**PASS 3 must create:**
```
Meta/PASS3_BODY_SIMILARITY_ANALYSIS.csv
```

Same format as §4.5.2. If PASS 3 detects templates in the body blueprints, it must:
1. FAIL the affected blueprints
2. Rewrite them with source-specific content
3. Re-run the analysis
4. Only approve blueprints that pass

PASS 3 may NOT approve a body blueprint if:
- Any Do/Don't/Checklist/Notes sentence appears in 4+ other blueprints (after normalization)
- The blueprint's body contains its own full pattern name pasted into a generic sentence
- The blueprint's Notes section starts with the same prefix as 10%+ of other blueprints

If PASS 3 approves templates, PASS 3 is the first invalid phase, not EXPORT.

**Required PASS 3 render addition:**
```
Body blueprints approved: <count>
Body blueprints failed (template detected): <count>
Body blueprints rewritten: <count>
Body similarity analysis: <clean / templates detected>
Name-paste detections: <count>
Notes template detections: <count>
```

**Validation contradiction rule:** If any prior validation file (e.g., `SCHEMA_FIELD_VALIDATION.csv`) reports PASS for an object that the revalidator finds fails, create:
```
Meta/VALIDATION_CONTRADICTION_REPORT.csv
```
Required columns:
```
object_id, prior_validation_file, prior_result, revalidation_result,
specific_failure, contradiction_status
```
A single contradiction means the prior validation was fraudulent. All prior validation files from the same phase must be re-examined.

**Required render:**
```
PASS: EXPORT

PASS 3 final export ledger consumed: <yes/no>
Final object count: <count>
Per-object markdown files created: <count>
Object/file count match: <yes/no>
Routed hierarchy created: <yes/no>
Aggregate indexes created: <yes/no>
Coverage ledger included: <yes/no>
Schema validation included: <yes/no>
Manifest included: <yes/no>
Archive created: <filename/link or blocked>
Export state: <COMPLETE / INVALID>
```

**EXPORT does NOT end with `Continue [Y/N]`.** EXPORT is the ONLY phase that may claim PASS completion.


---

# §5 — ROUTING AND TAXONOMY

## §5.0 — The Routing Decision

Every exported object must resolve to exactly one routing class:

| Routing Class | Meaning | `specialization_axis` |
|---|---|---|
| `general` | Portable across sources/methods/tools/languages | Must be `none` |
| `specialized` | Tied to a specific language/tool/medium/style/source | Must NOT be `none` |
| `teaching` | A method for teaching/scaffolding/reviewing | May be `none` or domain-specific |

**`variant` is NOT a routing class.** `support` is NOT a routing class.

The routing decision must answer:
1. Is this skill portable across the domain?
2. Is it bound to a specific language/tool/source/medium/style?
3. Is it a teaching method rather than the skill itself?
4. Does this source provide a variant of an existing skill?

## §5.1 — Universal Topology Shape

Every domain uses a generic/specialized split:

```
skills/
  <domain>/
    index.md
    generic/
      <portable_skill_family>/
        index.md
        patterns/
          index.md
          <object>.md
        drills/
          index.md
          <object>.md
        aps/
          index.md
          <object>.md
    <specialization_branch>/
      <specific_context>/
        <skill_family>/
          index.md
          patterns/
          drills/
          aps/
    teaching/
      <skill_family>/
        index.md
        patterns/
        drills/
        aps/
```

## §5.2 — Domain-Specific Specialization Branches

**Programming (canonical):**

`programming` is the canonical domain root for programming skills. `coding` is accepted as an alias but `programming` is preferred. Final archives must use one or the other consistently — never both.

```
skills/programming/
  index.md
  <skill_family>/              — portable skill families at domain root
    index.md
    generic/                   — cross-cutting skills for this family
      aps/
      drills/
      patterns/
    <subtopic>/                — specific subtopic within the family
      index.md
      aps/
      drills/
      patterns/
  language_contexts/           — language-specific skills
    <lang>/
      <subtopic>/
        aps/
        drills/
        patterns/
  teaching/                    — teaching methods for programming
    teaching_foundations/
      <topic>/
        aps/
        drills/
        patterns/
```

**Canonical programming skill families (examples, not exhaustive):**
```
skills/programming/
  core_mechanics/
    generic/   — portable: variable discipline, scope rules, naming
    control_flow/
    functions/
  structures/
    generic/   — portable: container selection, complexity reasoning
    arrays/
    linked_lists/
    search_sort/
    stacks_queues/
    trees/
    hash_maps/
    graphs/
  architecture_design/
    generic/   — portable: separation of concerns, coupling/cohesion
    ...
  input_output/
    generic/   — portable: stream discipline, format handling
    user_input/
    external_signals/
  memory_performance/
    generic/   — portable: allocation strategy, cache reasoning
    ...
  methods/
    generic/   — portable: abstraction, decomposition
    recursion/
  testing_validation/
    generic/   — portable: test design, coverage reasoning
    debugging/
  error_handling/
    generic/   — portable: exception strategy, recovery
    ...
  tooling_environment/
  language_contexts/
    cpp/
      cpp_core/
      cpp_stl/
      cpp_oop/
      cpp_concurrency/
      cpp_templates/
      cpp_numerics/
    c/
    javascript/
      core/
      events/
      functions/
      objects_arrays/
    arduino/
      digital_io/
      analog_io/
      serial/
      sensors/
```

**Mechanical Routing Test (Programming):** Could this skill be applied in a different programming language without modification to the rule, drill, or workflow? If YES → `generic/` or domain-root skill family. If it requires language-specific syntax, standard library, compiler features, or runtime behavior → `language_contexts/<lang>/`.

**Art:**
```
skills/art/
  generic/          — portable visual/design concepts
  media/<medium>/   — medium-specific
  styles/<style>/   — style-specific
  traditions/<t>/   — tradition-specific
  sources/<slug>/   — source-specific
  teaching/         — teaching methods for art
```

**Writing:**
```
skills/writing/
  generic/          — portable writing skills
  genres/<genre>/   — genre-specific
  forms/<form>/     — form-specific
  tools/<tool>/     — tool-specific
  teaching/         — teaching methods for writing
```

**Math:**
```
skills/math/
  generic/          — portable math reasoning
  fields/<field>/   — field-specific
  methods/<method>/ — method-specific
  tools/<tool>/     — tool-specific
  teaching/         — teaching methods for math
```

## §5.3 — Vague Middle Route Ban

These route shapes are INVALID (no generic/ or specialization branch):
```
skills/<domain>/<skill_family>/         — INVALID
skills/<domain>/<topic_label>/          — INVALID
skills/programming/architecture_design/ — INVALID (should be coding/architecture_design/)
skills/programming/memory_performance/  — INVALID
skills/art/figure_drawing/              — INVALID (should be generic/figure_drawing/)
```

**`specialized` is NOT a folder name.** It is a metadata value. Concrete specialization branches must name the axis: `language_contexts/`, `tools/`, `media/`, `styles/`, etc.

**Folder Size Cap:** No single `patterns/`, `drills/`, or `aps/` folder may contain more than 30 object files. If a folder would exceed 30, the parent skill family must be split into subtopic subfolders. A `patterns/` folder with 50+ objects is a dump folder regardless of its name. A `patterns/` folder with 180+ objects (e.g., `generic/practice/patterns/`) is a severe routing failure.

## §5.4 — Skill Family Internal Structure

Every skill family folder uses the same internal shape:

```
<skill_family>/
  index.md
  generic/              — cross-cutting skills for this whole family
    aps/
    drills/
    patterns/
  <subtopic_1>/         — first named subtopic
    index.md
    aps/
    drills/
    patterns/
  <subtopic_2>/
    ...
```

The `generic/` (or `base/`) subfolder at the family root holds skills that apply across ALL subtopics in the family. Named subtopic folders hold skills specific to that subtopic.

**Example — `structures/`:**
```
structures/
  index.md
  generic/        — "choose the right container", "reason about complexity"
    aps/
    drills/
    patterns/
  arrays/         — array-specific patterns, drills
    patterns/
  linked_lists/   — linked-list-specific
    drills/
    patterns/
  search_sort/    — search and sort algorithms
    patterns/
  stacks_queues/
    patterns/
  trees/
    patterns/
```

Rules:
- The family root folder contains ONLY `index.md` and child folders. No loose object files at the family root.
- `generic/` always has `aps/`, `drills/`, `patterns/` (any may be empty but the structure exists).
- Subtopic folders create only the type folders they need (e.g., a subtopic with only patterns creates only `patterns/`).
- If a subtopic would have only 1-2 objects, it may be kept in `generic/` instead of getting its own folder.

## §5.5 — Teaching Route Isolation and Execution Routing

PASS must distinguish execution skills (what the learner DOES to make the work) from teaching scaffolds (how to EXPLAIN, DEMONSTRATE, ANNOTATE, REVIEW, SEQUENCE, or GUIDE the work).

Teaching objects MUST route under:
```
skills/teaching/<domain>/<skill_family>/
```

Execution skill objects MUST NOT route under `skills/teaching/`.

The following route is FORBIDDEN for final EXPORT:
```
skills/<domain>/teaching/
```

Teaching is separate from execution so that skill practice libraries and instructional-method libraries do not contaminate each other.

Teaching captures are still `pattern`, `drill`, or `ap`. Teaching is a route and routing class, not a fourth object type.

If an object's primary action is to explain, annotate, label, demonstrate, sequence instruction, critique, or guide a learner → route it under `skills/teaching/<domain>/...`.

If an object's primary action is to construct, build, implement, write, draw, solve, cook, perform, compose, or produce → route it under execution.

Objects about arrows, flow marks, labels, overlays, diagram emphasis, critique marks, or demonstration sequencing are teaching objects by default unless the extracted rule explicitly instructs the practitioner to create those marks as part of the construction workflow.


## §5.5.1 — Teaching Extraction Intensity Rule

Teaching captures must be mined with the same seriousness as execution skills when the source is instructional.

PASS must look for reusable teaching moves in:
- the order in which the source introduces a skill
- how examples are simplified before detail is added
- how the source uses labels, arrows, overlays, comparison, or repetition
- how it isolates hard learner problems
- how it turns observation into practice
- how it shows common errors or prevents misreadings
- how it stages difficulty from simple to complex
- how it teaches without merely telling

A source may legitimately produce few teaching objects, but only after PASS has actively searched for teaching moves and recorded the result in `Meta/TEACHING_EXTRACTION_LEDGER.*`.

Teaching captures must not duplicate execution objects. A teaching object must answer: "How would I teach or guide this skill better because of this source?"

Valid teaching captures include:
- a demonstration sequence
- an annotation or overlay method
- a learner-error diagnosis pattern
- a critique checklist
- a progressive drill sequence
- a staged reveal AP
- a comparison method that helps a learner see a difference

Invalid teaching captures include:
- one generic lesson template copied across topics
- a restatement of the execution skill with "teach" added
- a teaching object whose procedure is interchangeable with unrelated topics
- generic advice to explain, demonstrate, practice, and review without source-specific method

EXPORT must create `Meta/TEACHING_EXTRACTION_VALIDATION.csv`.

Required columns:
```
source_unit, teaching_signal_seen, teaching_signal_type,
teaching_candidate_id_or_none, teaching_object_exported_or_reason_not,
execution_duplicate_absent, source_specific_method_present,
teaching_extraction_status, failure_reason
```

## §5.6 — Figure Drawing Anatomy Routing (Art Sources)

For art sources whose primary scope is figure drawing / dynamic anatomy / constructive anatomy:

```
skills/art/generic/figure_drawing/anatomy/
  full_figure_construction/
  torso/
  head_neck_shoulders/
  arms_hands/
  legs_feet/
  foreshortening/
  surface_landmarks/
```

Body parts are children of the figure drawing anatomy family, NOT separate top-level skills. Invalid:
```
skills/art/generic/hand_drawing/      — INVALID
skills/art/generic/foot_drawing/      — INVALID
skills/art/generic/head_drawing/      — INVALID
skills/art/generic/foreshortening/    — INVALID
```

## §5.7 — Taxonomy Cohesion Rule

A skill family is a broad teachable domain where parts are normally learned together. PASS may NOT scatter subskills from the same family across unrelated peer folders.

For figure drawing anatomy, the family index must explicitly describe where body-part skills live. If hand, foot, head, torso, construction, and foreshortening are split across peer top-level folders → EXPORT FAILS.

## §5.8 — Domain Registry and Topology Declaration

§5.2 defines canonical domain roots and specialization branches for programming, art, writing, and math. Sources outside these domains need declared topology.

If a source uses a domain not already defined in §5.2, PREFLIGHT must declare the domain root and its topology in `Meta/PREFLIGHT.md`:

```
New domain declared: <domain_root>
Topology:
  skills/<domain>/
    generic/         — portable skills
    <spec_branch>/   — specialization axis
    teaching/        — teaching methods
```

A new domain is valid only if:
- it follows the universal generic/specialized split from §5.1
- teaching routes go under `skills/teaching/<domain>/`
- route branches are named by specialization axis (not vague labels)
- no direct vague-middle route is created (§5.3)

EXPORT must create `Meta/DOMAIN_REGISTRY.md` listing all domains used in the archive, whether canonical (from §5.2) or declared (from PREFLIGHT).

Required per domain:
```
domain_root, declared_in_section_or_preflight, generic_branch_exists,
specialization_branches, teaching_branch_exists, topology_valid
```

INVALID domain inventions:
```
skills/skills/programming/          — doubled path
skills/career_documents/       — undeclared, not in §5.2
skills/clinical/               — undeclared, not in §5.2
skills/storytelling/           — undeclared, not in §5.2
skills/game_mechanics/         — undeclared (must be declared in PREFLIGHT if used)
```

The model may NOT improvise domain roots. It must either use a canonical root from §5.2 or declare a new one in PREFLIGHT with full topology.

## §5.9 — Object Placement Rules

Final object files MUST live inside object-type folders:
```
patterns/
drills/
aps/
```

**VALID placement shape:**
```
skills/programming/language_contexts/cpp/cpp_core/patterns/PAT_copy_constructor_controls_new_object.md
skills/programming/language_contexts/cpp/cpp_core/drills/DRILL_implement_copy_constructor.md
skills/programming/language_contexts/cpp/cpp_core/aps/AP_class_lifecycle_implementation.md
skills/programming/generic/memory_performance/patterns/PAT_move_buffer_allocation_outside_loop.md
skills/teaching/programming/demonstration_strategies/patterns/PAT_demonstrate_scope_with_nested_shadow.md
```

**INVALID placement — objects directly in topic folders (NO type subfolder):**
```
skills/programming/language_contexts/cpp/cpp_core/PAT_copy_constructor_controls_new_object.md
skills/programming/generic/memory_performance/PAT_move_buffer_allocation_outside_loop.md
skills/teaching/programming/PAT_demonstrate_scope_with_nested_shadow.md
```
This is the most common placement failure. The object is in the right topic folder but missing the `patterns/`, `drills/`, or `aps/` subfolder. ALL 159 objects in the most recent failed run had this error.

**INVALID final placements:**
- Object files directly under topic folders (missing type subfolder)
- Object files directly under domain roots
- `objects/`, `objects/patterns/`, `objects/drills/`, `objects/aps/`
- Top-level `patterns/`, `drills/`, `aps/` (dump folders)

**Every folder under `skills/` that contains child folders or object files MUST contain `index.md`.**

### §5.9.1 — Local Index Shape

Every `index.md` file under `skills/` must follow this EXACT shape:
```markdown
# <Folder Name>

## Entries
- [<Display Name>](<relative_path>)
- [<Display Name>](<relative_path>)
```

That is the entire file. No other headings. No other sections. No counts. No metadata.

**VALID local index:**
```markdown
# C/C++

## Entries
- [Patterns](patterns/index.md)
- [Drills](drills/index.md)
- [APs](aps/index.md)
- [Memory Management](memory_management/index.md)
- [Build And Linking](build_and_linking/index.md)
```

**INVALID local indexes (ALL of these shapes are banned):**
```markdown
# Programming

## Folders           ← INVALID heading: must be ## Entries
- [Build And Linking](build_and_linking/index.md)
- [C/C++](c_cpp/index.md)
```

```markdown
# Patterns

## Objects           ← INVALID heading: must be ## Entries
- [Copy Constructor](PAT_copy_constructor.md)
- [Move Semantics](PAT_move_semantics.md)
```

```markdown
# C/C++ Patterns

## Patterns          ← INVALID heading: must be ## Entries
- [Copy Constructor](PAT_copy_constructor.md)
```

```markdown
# C/C++

## Folders           ← INVALID: no split between folders and objects
- [Memory Management](memory_management/index.md)

## Objects           ← INVALID heading: must be ## Entries
- [Copy Constructor](PAT_copy_constructor.md)
```

The INVALID headings are:
```
## Folders, ## Objects, ## Patterns, ## Drills, ## APs,
## Contents, ## Subfolders, ## Files, ## Skills, ## Items
```

ALL entries — whether they link to child folders or to object files — go under a single `## Entries` heading. There is no split between folders and objects.

**The local index check is part of EXPORT revalidation.** If any `index.md` file under `skills/` uses a heading other than `## Entries`, the file is INVALID and EXPORT fails.

### §5.9.1.1 — Root Navigator Shape (`Indexes/INDEX_SKILLS.md`)

The root navigator file `Indexes/INDEX_SKILLS.md` must follow this EXACT shape:
```markdown
# <Archive Title>

## Entries
- [<Domain Root 1>](../skills/<domain1>/index.md)
- [<Domain Root 2>](../skills/<domain2>/index.md)
```

That is the entire file. No counts. No catalog links. No metadata. No summary data.

**INVALID root navigator shapes:**
```markdown
# PASS Skill Archive: Introduction to C++

- Patterns: 52               ← INVALID: no counts
- Drills: 14                  ← INVALID: no counts
- Action Protocols: 14        ← INVALID: no counts

## Catalogs                    ← INVALID: no catalog links
- [Patterns](../Catalogs/PATTERNS.md)

## Skill Root                  ← INVALID heading: must be ## Entries
- [skills/](../skills/index.md)
```

The root navigator lists domain roots. Catalogs are in `Catalogs/`. Counts are in `Meta/`. The root navigator is a navigation file, not a summary file.

### §5.9.2 — Teaching Path Direction

Teaching objects are routed under `skills/teaching/<domain>/`, NOT under `skills/<domain>/teaching/`.

**VALID:**
```
skills/teaching/programming/demonstration_strategies/patterns/PAT_...
skills/teaching/math/proof_sequencing/patterns/PAT_...
```

**INVALID:**
```
skills/programming/teaching/programming_instruction/PAT_...
skills/programming/teaching/staged_reveal/PAT_...
```

`skills/programming/teaching/` puts teaching inside the coding domain. The correct structure puts teaching as a peer domain with coding as its specialization axis. This matters for merge: `skills/teaching/programming/` from one archive merges cleanly with `skills/teaching/math/` from another. `skills/programming/teaching/` does not.

---

# §6 — CANDIDATE CONSERVATION AND REDUCTION ACCOUNTING

## §6.0 — Count Conservation Rule

Every PASS 1 candidate and PASS 2 recovery row must resolve to exactly one of:
- exported final object
- embedded variant inside a foundation object
- rejected duplicate (with named superior object)
- rejected inferior object (with named superior object)
- rejected weak object (with reason)
- merged into generalized foundation object
- promoted to specialization
- deferred with explicit reason

**NO candidate may disappear silently.** If ANY candidate ID is missing from final accounting, PASS FAILS.

## §6.1 — Valid Reasons for Fewer Exported Objects

- duplicate candidates adjudicated and weaker rejected
- identical skills collapsed into superior retained object
- same-skill alternates embedded as variants under foundation
- weak or semantically empty candidates rejected
- specializations absorbed into generalized foundation with cross-links
- standalone variants correctly colocated under foundation
- routing consolidation merged redundant folders

## §6.2 — INVALID Reasons for Fewer Exported Objects

- silent skipped extraction
- weaker PASS 1 coverage
- missing PASS 2 recovery
- unreported candidate loss
- assuming duplicates without adjudication
- gobbling variants without preserving them
- treating fewer files as "cleaner" by default
- replacing objects with aggregate catalog entries

## §6.3 — Reduction Explanation (When Baseline Exists)

If a comparable prior archive exists, EXPORT must create `Meta/REDUCTION_EXPLANATION.md` with baseline comparison, delta counts, and concrete causes. If no baseline: state `NO COMPARABLE BASELINE AVAILABLE`.

## §6.4 — Duplicate vs Variant vs Specialization Decision Matrix

```
Case A: Same skill, same method, same emphasis → DUPLICATE → retain superior, reject weaker
Case B: Same skill, better wording/schema → REPLACEMENT → retain superior, reject as superseded
Case C: Same skill, different method sequence → VARIANT → absorb into foundation variants list
Case D: Same skill, different medium/style/language → VARIANT or SPECIALIZATION → absorb or separate
Case E: Source-specific contains portable rule → GENERALIZATION → create/update general foundation
Case F: Broad object secretly specific → REROUTE → move under specialization branch
Case G: Specialized object teaches portable rule → SPLIT → general + specialized if both justified
```

**Identical objects are NOT variants.** A mere wording difference is NOT a variant. A variant must differ in method, constraints, tradeoff, runtime/stage, medium/tool/language, audience, failure recovery, or verification approach.


## §6.5 — Variant Co-location Rule

Variants live inside the foundation/original skill object's `variants` field.

PASS may NOT export a standalone variant file unless PASS 3 promotes that variant to a true specialization with:
- its own semantic `name`
- `routing_class: specialized`
- `specialization_axis` not `none`
- `foundation_object_id` pointing to the foundation object
- explicit PASS 3 justification for separate-file promotion

If PASS 3 marks a row as `variant_approved`, EXPORT must either:
1. embed it in the foundation object's `variants` field, or
2. promote it to a justified specialization and record the promotion.

A variant approved in PASS 3 with an exported standalone object file and no promotion record is INVALID.

EXPORT must create `Meta/VARIANT_COLOCATION_VALIDATION.md`.


## §6.6 — Repeated Teaching Boilerplate Rule

If multiple teaching candidates share identical or near-identical procedure text with only the topic changed, PASS must NOT export one object per topic. Options:
1. Retain one generalized teaching pattern/AP
2. Absorb distinct topic treatments into that object's `variants` field
3. Create specialized teaching objects ONLY when procedure differs materially
4. Reject duplicates and weaker restatements

Generic scaffolds like "teach by opening with objective, demonstrating examples, naming traps, assigning practice" are NOT valid unless they contain source-specific teaching method details.


## §6.7 — AP Domain Workflow Rule

APs are action protocols for the source domain, not protocols for PASS extraction.

A valid AP describes a reusable workflow performed by the learner/practitioner inside the domain:
- programming APs describe programming/design/debugging/refactoring workflows
- math APs describe solving/proving/checking workflows
- art APs describe drawing/constructing/observing/critique workflows
- writing APs describe drafting/revision/structure workflows

INVALID AP `Steps / Flow` content includes PASS-process language such as:
```
open the source span
extract operative terms
state the design choice from the source
identify source claim
verify against the source claim
record object anchor
record candidate anchor
candidate can derive
PASS1
PASS2
PASS3
source span
object anchor
locator evidence
```

APs must chain domain actions. They may cite a source in frontmatter, but the workflow itself must not be "how PASS extracted this object."

If an AP's steps describe extracting, validating, or recording the PASS object rather than performing the domain skill, reject it or convert the source material into a pattern/drill/AP with a real domain workflow.

EXPORT must create `Meta/AP_DOMAIN_WORKFLOW_VALIDATION.md`.



---

# §7 — REQUIRED ARCHIVE STRUCTURE

## §7.0 — Canonical Layer Separation

### §7.0.0 — Triple-Format Ledger Rule

Every phase ledger (PASS1_CANDIDATE_LEDGER, PASS2_RECOVERY_LEDGER, PASS3_FINAL_EXPORT_LEDGER, PASS3_BODY_BLUEPRINT_LEDGER, EVIDENCE_CHAIN_LEDGER) MUST be created in all three formats:
```
.md   — human-readable
.csv  — machine-readable tabular
.jsonl — structured data
```
All three must contain the same rows. If any format is missing for any ledger, the phase that creates that ledger is INCOMPLETE and its gate fails.

This rule exists because the model has repeatedly created two of three formats and skipped the third. Specifically: PASS1_CANDIDATE_LEDGER.jsonl was missing in the most recent run while .md and .csv existed. That is a phase proof failure.

**Phase gate check for triple format:** The gate proof file (`PHASE_GATE_PROOF.md`) must list all three file paths for each ledger and confirm each exists. If PHASE_GATE_PROOF claims a phase passed but one of the three ledger files does not exist on disk, PHASE_GATE_PROOF is fraudulent.

```
Indexes/                    — Top-level human navigation ONLY
  INDEX_SKILLS.md

skills/                     — Routed skill objects + local index.md files
  index.md
  <domain>/
    index.md
    generic/
      index.md
      <skill_family>/
        index.md
        patterns/
          index.md
          <object>.md
        drills/
          index.md
          <object>.md
        aps/
          index.md
          <object>.md
    <specialization_branch>/
      ...
    teaching/
      ...

Catalogs/                   — Aggregate human catalogs (OPTIONAL)
  PATTERNS.md
  DRILLS.md
  ACTION_PROTOCOLS.md

Meta/                       — Machine files, validation, ledgers, phase artifacts
  PREFLIGHT.md
  COVERAGE.md
  COVERAGE.csv
  PASS1_CANDIDATE_LEDGER.md
  PASS1_CANDIDATE_LEDGER.csv
  PASS2_RECOVERY_LEDGER.md
  PASS2_RECOVERY_LEDGER.csv
  PASS2_DIFFERENTIAL_PROOF.csv
  PASS3_FINAL_EXPORT_LEDGER.md
  PASS3_FINAL_EXPORT_LEDGER.csv
  REJECTS.md
  VARIANTS.md
  VARIANT_GROUPS.md
  DUPLICATE_ADJUDICATION.md
  GENERALIZATION_SPECIALIZATION_MAP.md
  ROUTING_CLASS_VALIDATION.md
  VARIANT_ABSORPTION.md
  VARIANT_COLOCATION_VALIDATION.md
  SEMANTIC_NAMING_VALIDATION.md
  AP_DOMAIN_WORKFLOW_VALIDATION.md
  MANIFEST.md
  OBJECT_FILE_INDEX.csv
  OBJECT_FILE_INDEX.jsonl
  SOURCE_OBJECT_MANIFEST.json
  SCHEMA_VALIDATION.md
  SCHEMA_FIELD_VALIDATION.csv
  BODY_UNIQUENESS_VALIDATION.csv
  SOURCE_INDEPENDENCE_VALIDATION.csv
  MULTIMODAL_EVIDENCE_VALIDATION.csv
  RAW_SKILL_QUALITY_VALIDATION.csv
  PRACTITIONER_VOICE_VALIDATION.csv
  PRACTITIONER_VOICE_LEXICON.md
  DO_DONT_INTRINSICITY_VALIDATION.csv
  NO_AUDIT_LANGUAGE_VALIDATION.csv
  CONFIDENCE_CALIBRATION_VALIDATION.csv
  EVIDENCE_CHAIN_LEDGER.csv
  EVIDENCE_CHAIN_LEDGER.jsonl
  SECTION_BODY_PROVENANCE_VALIDATION.csv
  VISUAL_INSPECTION_SUFFICIENCY_VALIDATION.csv
  TEACHING_EXTRACTION_LEDGER.md
  TEACHING_EXTRACTION_LEDGER.csv
  TEACHING_EXTRACTION_LEDGER.jsonl
  TEACHING_EXTRACTION_VALIDATION.csv
  RUN_ROOT_VALIDATION.md
  POST_EXPORT_CRITIQUE_TRIAGE.md
  ROUTING_VALIDATION.md
  MATERIALIZATION_VALIDATION.md
  SOURCE_DEPENDENCY_VALIDATION.md
  MULTIMODAL_EVIDENCE_VALIDATION.md
  CLOSED_TYPE_VALIDATION.md
  TEACHING_BOILERPLATE_VALIDATION.md
  TEACHING_EXECUTION_ROUTING_LEDGER.md
  TEACHING_EXECUTION_ROUTING_LEDGER.csv
  TAXONOMY_RECONCILIATION.md
  ROUTE_REDIRECTS.jsonl
  REDUCTION_EXPLANATION.md
  PHASE_GATE_PROOF.md
  GATE_STACK_VALIDATION.md
  SOURCE_CONTENT_INVENTORY.csv
  TOPOLOGY_REVALIDATION.csv
  EXPORT_REVALIDATION.csv
  REVALIDATION_FAILURE_REPORT.csv
  VALIDATION_CONTRADICTION_REPORT.csv
  BODY_SIMILARITY_ANALYSIS.csv
  NAME_PASTE_DETECTION.csv
  PASS3_BODY_SIMILARITY_ANALYSIS.csv
  DOMAIN_REGISTRY.md
  RUN_SUMMARY.md
```

## §7.1 — Layer Rules

**`Indexes/`** — Human navigation only. Contains ONLY `INDEX_SKILLS.md`. No `.csv`, `.json`, `.jsonl`, `COUNTS.json`, `OBJECT_INDEX.*`, `ROUTE_INDEX.*`, validation reports, phase ledgers, or raw object dumps. Lowercase `indexes/` is FORBIDDEN.

The following files are FORBIDDEN in `Indexes/`:
```
COUNTS.json, OBJECT_INDEX.csv, OBJECT_INDEX.jsonl, OBJECT_INDEX.md,
ROUTE_INDEX.csv, ROUTE_INDEX.jsonl, ROUTE_INDEX.md,
any .csv, any .json, any .jsonl
```
These belong in `Meta/`.

**`Catalogs/`** — Optional aggregate lists. May NEVER replace routed object files, local index.md files, or `Meta/OBJECT_FILE_INDEX.*`.

**`Meta/`** — All machine-readable files. Phase ledgers, validation reports, coverage, manifests, CSVs, JSONLs, counts, object file indexes.

**`skills/`** — The ONLY valid home for final object files. Every folder with children must have `index.md`.

**Archive root** — Should contain only `README.md` or nothing.

## §7.2 — Local Index Requirements

Local `index.md` files are **navigation aids**, not validation reports. They list what's in the folder and where to go next. Nothing else.

**Required format:**
```
# <Folder Name>

## Entries
- <child_folder>/index.md
- <child_folder>/index.md
- <object_file>.md
- <object_file>.md
```

That's it. A heading and a list of entries. Entries are relative paths to child index files or object files in the current folder.

**FORBIDDEN in local index.md files:**
```
## Scope, ## Routing Class, ## Contains, ## Relationships,
## Embedded variants, ## Teaching links, ## Drill-Only Justification,
object counts, routing class declarations, scope descriptions,
validation summaries, relationship maps, variant counts
```
All of that belongs in `Meta/` validation files, not in navigation indexes.

For skill family root indexes (e.g., `structures/index.md`), entries list child folders only:
```
# Structures Index

## Entries
- generic/index.md
- arrays/index.md
- linked_lists/index.md
- search_sort/index.md
- stacks_queues/index.md
- trees/index.md
```

For leaf folders (e.g., `structures/generic/patterns/`), entries list object files:
```
# structures/generic/patterns

## Entries
- array_index_discipline.md
- container_instead_of_parallel_arrays.md
- memory_and_resources_selection_rule.md
```

## §7.3 — INDEX_SKILLS.md Requirements

`Indexes/INDEX_SKILLS.md` is the archive root navigator. It lists domain roots only:

```
# INDEX_SKILLS

## Entries
- skills/programming/index.md
- skills/teaching/index.md
```

That's the complete file. It does NOT contain: object counts, type breakdowns, source archive lists, retention/rejection statistics, family-level counts, or any machine data. Those belong in `Meta/RUN_SUMMARY.md` or `Meta/OBJECT_FILE_INDEX.csv`.

## §7.4 — OBJECT_FILE_INDEX.csv Requirements

This file lives in `Meta/`, NOT in `Indexes/`.

Required columns:
```
object_id, object_type, name, category, subcategory, path, reference.locator, schema_result, route_result
```

Rules:
- Every PASS 3-approved object appears exactly once
- Every row path exists in the archive
- Every indexed file is under `skills/**`
- Index count = PASS 3 approved count = object file count

## §7.5 — Index Generation Rule

Index generation is a mechanical post-EXPORT step. After all object files are placed under `skills/`, walk the entire `skills/` tree and generate `index.md` for every directory that contains children (folders or object files). Missing indexes are a GATE 6 (TOPOLOGY_INDEX_GATE) failure. The walk is mechanical — it does not require judgment, source reading, or validation. It requires listing contents.

---

# §8 — THE TEN GATES (INDEPENDENT, ORDERED, MANDATORY)

## §8.0 — Gate Stack Contract

PASS success requires ALL ten gates to pass independently and in order. No later gate satisfies, replaces, implies, excuses, or collapses an earlier gate.

**Passing gate N does NOT imply gate N-1 passed.**

A run that passes a newer gate but fails an older gate is INVALID.

## §8.1 — GATE 1: PHASE GATE

**Checks:** Every phase ran as the active phase, created its required artifacts before printing its completion render, derived all counts from those artifacts, emitted its render, stopped at `Continue [Y/N]`, and user continued in a later turn.

A phase render printed before its required artifacts exist is invalid even if the files are created later.

**Evidence files:** `Meta/PHASE_GATE_PROOF.md`, `Meta/RUN_ROOT_VALIDATION.md`

Required rows per phase:
```
phase_name, started_after_user_turn, pre_render_artifact_check,
required_artifacts_existing_before_render, counts_derived_from_artifacts,
required_render_emitted, stopped_at_continue_prompt, user_continue_received,
allowed_artifacts_only, next_phase_started_after_continue, phase_ledger_path,
phase_gate_status, notes
```

All phases and run-root checks must be `PASS`. A filename is NOT proof. A ledger is NOT proof. A generated archive is NOT proof. Only the transcript-visible sequence is proof.

## §8.2 — GATE 2: SOURCE COVERAGE GATE

**Checks:** Every scoped source unit was processed in PASS 1 and reinspected in PASS 2.

**Evidence file:** `Meta/COVERAGE.md`, `Meta/COVERAGE.csv`

## §8.3 — GATE 3: CANDIDATE CONSERVATION GATE

**Checks:** Every PASS 1 candidate ID and PASS 2 recovery ID resolves to export, variant absorption, rejection, merge, or deferral. No candidate disappeared silently.

**Evidence files:** `Meta/REDUCTION_EXPLANATION.md`, all ledgers

## §8.4 — GATE 4: CLOSED TYPE GATE

**Checks:** Every final object has `object_type` of exactly `pattern`, `drill`, or `ap`. No fourth type exists anywhere in the archive.

**Evidence file:** `Meta/CLOSED_TYPE_VALIDATION.md`

**Required fields:**
```
allowed_object_types, invalid_candidate_types_detected, invalid_object_types_detected,
phase_where_invalid_type_appeared, transformed_to_valid_type, absorbed_as_context_note,
rejected_invalid_type_rows, exported_object_type_counts, closed_type_result: PASS | FAIL
```

## §8.5 — GATE 5: CLOSED SCHEMA GATE

**THIS IS NOT THE SAME AS GATE 4.** Passing closed type does NOT imply passing closed schema.

**Checks (ALL independently):**
1. YAML frontmatter starts at byte 0
2. Exact required key set for the object type
3. Exact required nested `reference` fields
4. Valid enum values for all constrained fields
5. No placeholder values remain
6. Semantic `name` value is human-readable and not numeric/ID-like
7. H1 exactly matches the semantic `name`
8. Required body headings in exact object-type order
9. Object-specific body content (not filler)
10. Variant field present and correctly shaped
11. Cross-link field present and correctly shaped
12. Route compatibility (path matches routing_class)
13. File path / object type compatibility
14. Object count = file count

**Evidence files:** `Meta/SCHEMA_VALIDATION.md`, `Meta/SCHEMA_FIELD_VALIDATION.csv`, `Meta/SEMANTIC_NAMING_VALIDATION.md`, `Meta/EXPORT_REVALIDATION.csv`

Schema validation MUST validate against the embedded templates in §2 of THIS FILE. It may NOT define its own schema. It may NOT validate only the fields emitted. It may NOT substitute "type validation" or "route validation" for schema validation.

**Independent revalidation is part of Gate 5.** `Meta/EXPORT_REVALIDATION.csv` must exist and all rows must pass. If the revalidation file does not exist, Gate 5 fails. If any revalidation row fails, Gate 5 fails. If the revalidation contradicts SCHEMA_FIELD_VALIDATION.csv, both Gate 5 and the validation theater rule (§12.14) are violated.

**SCHEMA_FIELD_VALIDATION.csv required columns:**
```
object_id, object_path, object_type, frontmatter_at_byte_zero, required_keys_present,
forbidden_keys_absent, reference_block_valid, enum_values_valid, placeholder_values_absent,
semantic_name_valid, filename_prefix_valid, filename_semantic_slug_valid,
h1_matches_name, body_headings_valid, body_content_object_specific,
practitioner_voice_valid, do_dont_intrinsicity_valid,
source_dependent_body_absent, source_locator_used_only_as_provenance,
body_self_contained, source_independence_status,
cross_links_valid, variants_valid, route_compatible, schema_status, failure_reason
```

A single `FAIL` row invalidates EXPORT.

## §8.6 — GATE 6: TOPOLOGY / INDEX GATE

**Checks:** Archive has proper layer separation, `Indexes/INDEX_SKILLS.md` exists, every folder has `index.md`, objects are in `patterns/`/`drills/`/`aps/` folders under `skills/**`, no dump folders, no lowercase `indexes/`.

**Evidence file:** `Meta/TOPOLOGY_INDEX_VALIDATION.md`

Required checks:
```
Indexes_INDEX_SKILLS_present, Catalogs_present, Meta_present, skills_present,
lowercase_indexes_absent, objects_dump_absent,
local_index_files_present_for_all_skill_folders,
terminal_patterns_drills_aps_grouping_valid, loose_domain_bucket_absent,
object_paths_match_routing_class, topology_status, failure_reason
```

## §8.7 — GATE 7: BODY INDIVIDUALIZATION / SEMANTIC BOILERPLATE / RAW SKILL / PRACTITIONER VOICE GATE

Checks:
1. Every object body is generated from a PASS 3 body blueprint.
2. Every exported object contains object-specific practitioner content, not cloned boilerplate.
3. No unrelated objects share identical Do, Don't, Checklist, Notes, Instructions, Success Check, Common Failures, or Steps / Flow blocks.
4. No stock fallback phrase is reused across unrelated patterns.
5. Every pattern contains a real domain decision rule.
6. Every drill requires practice that changes practitioner behavior.
7. Every AP performs a domain workflow, not extraction, summarization, or validation.
8. Every object has a practitioner artifact or observable skill outcome.
9. No object is only a source fact, language definition, chapter summary, heading restatement, visual label, or semantic fragment.
10. Every object improves craft execution, design, debugging, refactoring, testing, performance, safety, maintainability, construction, rendering, solving, teaching, cooking, composition, or another domain-specific practitioner capability.
11. Every exported object body is written in the working language of the craft, not in academic, abstract, validation-heavy, or AI-scholarly prose.
12. Every pattern's Do, Don't, and Checklist sections are intrinsic to the named skill and cannot be copied unchanged into unrelated patterns.
13. Every Don't item names a concrete mistake, misuse case, false move, or anti-pattern that the named pattern prevents.
14. Every Checklist item verifies an observable feature of the produced work that belongs to the named skill.
15. Every exported object has an unbroken evidence chain from source unit to candidate to blueprint to exported body.
16. Every required body section is traceable to the specific blueprint field that seeded it.
17. Final object bodies contain no avoidable audit/process language.
18. Confidence values are calibrated to actual evidence strength and body quality.
19. Teaching captures are actively searched for in instructional sources and are not merely incidental.

INVALID:
- Two+ APs with identical `Steps / Flow`
- Two+ drills with identical `Instructions`
- Many patterns using the same IF/THEN wrapper with only the name changed
- Repeated generic `Do`/`Don't`/`Checklist`/`Notes` blocks
- Stock fallback text reused as a universal ELSE clause
- Schema-valid objects with no practitioner action
- AI-scholarly object bodies that say things like `visual evidence`, `source-derived rationale`, `artifact quality`, `observed transformation`, or `domain workflow` instead of craft-native instruction
- Do/Don't/Checklist items that could be pasted unchanged into unrelated skills
- Don't items that warn only against generic failures such as guessing, ignoring structure, or forgetting fundamentals
- Exported object bodies containing PASS/process/audit language instead of craft instruction
- Objects without evidence-chain rows
- Body sections that do not match their blueprint fields
- High-confidence objects without direct evidence and completed validation
- Instructional sources with rich teaching methods but no teaching extraction ledger or justification

Evidence files:
```
Meta/PASS3_BODY_BLUEPRINT_LEDGER.csv
Meta/BODY_UNIQUENESS_VALIDATION.csv
Meta/RAW_SKILL_QUALITY_VALIDATION.csv
Meta/PRACTITIONER_VOICE_VALIDATION.csv
Meta/DO_DONT_INTRINSICITY_VALIDATION.csv
Meta/NO_AUDIT_LANGUAGE_VALIDATION.csv
Meta/CONFIDENCE_CALIBRATION_VALIDATION.csv
Meta/EVIDENCE_CHAIN_LEDGER.csv
Meta/SECTION_BODY_PROVENANCE_VALIDATION.csv
Meta/TEACHING_EXTRACTION_VALIDATION.csv
Meta/TEACHING_BOILERPLATE_VALIDATION.md
Meta/AP_DOMAIN_WORKFLOW_VALIDATION.md
```

`BODY_UNIQUENESS_VALIDATION.csv` required columns:
```
object_id, object_type, object_path,
pattern_rule_hash, do_hash, dont_hash, checklist_hash, notes_hash,
drill_instruction_hash, drill_success_hash, drill_failure_hash,
ap_steps_hash, normalized_body_hash,
exact_duplicate_section_count, near_duplicate_section_count,
repeated_generic_line_count, stock_fallback_reused,
body_uniqueness_status, failure_reason
```

**Hash collision rules:** If any two objects share the same `do_hash`, `dont_hash`, `checklist_hash`, or `notes_hash`, both objects FAIL body uniqueness. The whole-body hash is not sufficient — section-level hashing is required because template-stamped objects differ in their H1 and Pattern Rule (which contain the name) but share identical Do/Don't/Checklist/Notes content.

**Repeated generic line detection:** `repeated_generic_line_count` must be the count of Do/Don't/Checklist/Notes sentences in this object that appear (after name-removal normalization) in 4+ other objects. If `repeated_generic_line_count > 0`, the object FAILS. This column may NOT be `0` for all objects unless `BODY_SIMILARITY_ANALYSIS.csv` also reports zero `TEMPLATE_DETECTED` rows — if it does, the two files are consistent. If `BODY_UNIQUENESS_VALIDATION.csv` says `0` repeated lines but `BODY_SIMILARITY_ANALYSIS.csv` detects templates, the body uniqueness validator is fraudulent.

**The body uniqueness validation MUST cross-reference `BODY_SIMILARITY_ANALYSIS.csv`.** The two files must agree. If BODY_SIMILARITY_ANALYSIS finds templates, BODY_UNIQUENESS_VALIDATION must report failures. If they disagree, both are INVALID.

`RAW_SKILL_QUALITY_VALIDATION.csv` required columns:
```
object_id, object_type, practitioner_action, practitioner_artifact,
skill_outcome, source_fact_only_yes_no, transferable_yes_no,
domain_usefulness_result, failure_reason
```

`PRACTITIONER_VOICE_VALIDATION.csv` required columns:
```
object_id, object_type, object_path, craft_register,
direct_craft_verbs_present, concrete_domain_nouns_present,
ai_scholarly_language_count, source_metadata_language_count,
body_written_for_practitioner, practitioner_voice_status, failure_reason
```

`DO_DONT_INTRINSICITY_VALIDATION.csv` required columns:
```
object_id, object_path, pattern_name,
do_items_skill_specific, dont_items_skill_specific, checklist_items_skill_specific,
generic_do_count, generic_dont_count, generic_checklist_count,
copyable_to_unrelated_objects, concrete_mistake_named,
observable_skill_check_present, intrinsicity_status, failure_reason
```

`NO_AUDIT_LANGUAGE_VALIDATION.csv` required columns:
```
object_id, object_type, object_path, audit_language_count,
forbidden_process_terms_found, craft_rewrite_available,
body_free_of_audit_language, no_audit_language_status, failure_reason
```

`SECTION_BODY_PROVENANCE_VALIDATION.csv` required columns:
```
object_id, object_type, object_path, required_section,
blueprint_field_used, section_body_matches_blueprint,
section_is_source_independent, section_uses_practitioner_voice,
section_provenance_status, failure_reason
```

`TEACHING_EXTRACTION_VALIDATION.csv` required columns:
```
source_unit, teaching_signal_seen, teaching_signal_type,
teaching_candidate_id_or_none, teaching_object_exported_or_reason_not,
execution_duplicate_absent, source_specific_method_present,
teaching_extraction_status, failure_reason
```

AP-specific checks:
```
AP steps describe domain workflow: PASS|FAIL
PASS-process language absent from AP bodies: PASS|FAIL
AP count supported by distinct workflows: PASS|FAIL
APs are not extraction protocols: PASS|FAIL
```

A single FAIL row invalidates EXPORT.

## §8.8 — GATE 8: EXPORT MATERIALIZATION GATE

**Checks:** Every PASS 3-approved object has exactly one routed `.md` file under `skills/**`. Object count = file count. No aggregate-only objects. All paths are routed (not dump-folder).

**Evidence files:** `Meta/MATERIALIZATION_VALIDATION.md`, `Meta/VARIANT_COLOCATION_VALIDATION.md`

Required checks:
```
PASS3 approved object count, Routed object markdown files under skills/**,
Aggregate index files, Object count equality: PASS|FAIL,
No objects/ dump folder, No top-level dump folders,
Every object_id has exactly one .md file, Every .md maps to one object_id,
Every route reflects domain/specialization, Variant rows embedded or promoted correctly,
No standalone variant files without promotion, Overall materialization result: PASS|FAIL
```

Also must check:
```
Index hygiene: PASS|FAIL
Lowercase indexes directory present: yes|no
Forbidden files under Indexes: <count>
Catalog files placed correctly: PASS|FAIL
Meta files placed correctly: PASS|FAIL
Root clutter count: <count>
Local index count: <count>
Skills folders missing index.md: <count>
```

## §8.9 — GATE 9: SOURCE INDEPENDENCE / MULTIMODAL EVIDENCE GATE

Checks:
1. Every exported object is usable without the original source.
2. Source locators appear only in frontmatter/reference or Meta files, not as required operating instructions.
3. No body contains source-dependent language such as "see page," "as shown," "copy the diagram," or "repeat the source exercise."
4. Every object with `evidence_type: image` or `mixed` is supported by VISUAL_STUDY_LEDGER rows.
5. Every meaningful visual/non-text source unit was inspected or explicitly marked unreadable.
6. Visual observations were transformed into self-contained practitioner actions.
7. No visual evidence was treated as decorative when it contained instructional marks, comparison, construction, sequence, code behavior, table logic, UI flow, or form information.

Evidence files:
```
Meta/VISUAL_STUDY_LEDGER.md
Meta/VISUAL_STUDY_LEDGER.csv
Meta/VISUAL_STUDY_LEDGER.jsonl
Meta/PASS3_BODY_BLUEPRINT_LEDGER.csv
Meta/SOURCE_INDEPENDENCE_VALIDATION.csv
Meta/MULTIMODAL_EVIDENCE_VALIDATION.csv
Meta/MULTIMODAL_EVIDENCE_VALIDATION.md
```

`SOURCE_INDEPENDENCE_VALIDATION.csv` required columns:
```
object_id, object_path, object_type, source_locator_in_body,
forbidden_source_reference_phrase_count, body_requires_original_source,
reference_used_as_provenance_only, self_contained_skill_body,
source_independence_status, failure_reason
```

`MULTIMODAL_EVIDENCE_VALIDATION.csv` required columns:
```
source_unit, source_locator, has_non_text_evidence,
visual_study_row_count, visual_evidence_status,
candidate_ids_supported, final_object_ids_supported,
visual_to_body_transformation_present, multimodal_status, failure_reason
```

`VISUAL_INSPECTION_SUFFICIENCY_VALIDATION.csv` required columns:
```
visual_unit_id, source_unit, source_locator, visual_inspection_status,
concrete_visible_feature_count, concrete_visible_features,
generic_visual_summary_absent, instructional_mark_described,
sequence_or_spatial_relationship_described,
visual_sufficiency_status, failure_reason
```

A single FAIL row invalidates EXPORT.

## §8.10 — GATE 10: GATE STACK VALIDATION GATE

Checks: Gates 1-9 all passed independently. Produces the master validation file.

**Evidence file:** `Meta/GATE_STACK_VALIDATION.md`

Required rows:
```
gate_name, gate_status, evidence_file, independent_check_performed, failure_reason
```

Required `gate_name` values:
```
PHASE_GATE, SOURCE_COVERAGE_GATE, CANDIDATE_CONSERVATION_GATE,
CLOSED_TYPE_GATE, CLOSED_SCHEMA_GATE, TOPOLOGY_INDEX_GATE,
BODY_INDIVIDUALIZATION_SEMANTIC_BOILERPLATE_RAW_SKILL_PRACTITIONER_VOICE_EVIDENCE_CHAIN_GATE,
EXPORT_MATERIALIZATION_GATE, SOURCE_INDEPENDENCE_MULTIMODAL_EVIDENCE_GATE
```

All must be `PASS` for full success.

---

# §9 — SUCCESS AND FAILURE RULES

## §9.0 — Success Render Lock

The phrase "full PASS complete" or equivalent may be printed ONLY if ALL of the following are true:
1. `Meta/GATE_STACK_VALIDATION.md` exists, all gates PASS
2. `Meta/PHASE_GATE_PROOF.md` exists, all phases PASS
3. `Meta/SCHEMA_FIELD_VALIDATION.csv` exists, all rows PASS
4. `Meta/TOPOLOGY_INDEX_VALIDATION.md` exists, topology PASS
5. `Meta/PASS2_DIFFERENTIAL_PROOF.csv` exists, one row per source unit
6. Archive contains routed objects ONLY under `skills/**`
7. Object counts match across all validation files
8. `Meta/SEMANTIC_NAMING_VALIDATION.md` confirms all object names are human-readable skill names
9. `Meta/VARIANT_COLOCATION_VALIDATION.md` confirms all variants are embedded or promoted
10. `Meta/AP_DOMAIN_WORKFLOW_VALIDATION.md` confirms APs are domain workflows, not PASS extraction workflows
11. `Meta/PASS3_BODY_BLUEPRINT_LEDGER.csv` exists and every approved object has one complete body blueprint row
12. `Meta/BODY_UNIQUENESS_VALIDATION.csv` exists and all rows PASS
13. `Meta/RAW_SKILL_QUALITY_VALIDATION.csv` exists and all rows PASS
14. `Meta/PRACTITIONER_VOICE_VALIDATION.csv` exists and all rows PASS
15. `Meta/DO_DONT_INTRINSICITY_VALIDATION.csv` exists and all rows PASS
16. `Meta/SOURCE_INDEPENDENCE_VALIDATION.csv` exists and all rows PASS
17. For multimodal sources, `Meta/VISUAL_STUDY_LEDGER.*` and `Meta/MULTIMODAL_EVIDENCE_VALIDATION.csv` exist and all rows PASS
18. No exported object body requires the original source to perform the skill
19. No exported object body uses avoidable AI-scholarly language where craft-native instruction is required
20. No exported pattern has copyable generic Do, Don't, or Checklist content
21. `Meta/RUN_ROOT_VALIDATION.md` exists and all rows PASS
22. `Meta/EVIDENCE_CHAIN_LEDGER.csv` exists and all exported objects have PASS chains
23. `Meta/SECTION_BODY_PROVENANCE_VALIDATION.csv` exists and all rows PASS
24. `Meta/NO_AUDIT_LANGUAGE_VALIDATION.csv` exists and all rows PASS
25. `Meta/CONFIDENCE_CALIBRATION_VALIDATION.csv` exists and all rows PASS
26. For multimodal sources, `Meta/VISUAL_INSPECTION_SUFFICIENCY_VALIDATION.csv` exists and all rows PASS
27. For instructional sources, `Meta/TEACHING_EXTRACTION_LEDGER.*` and `Meta/TEACHING_EXTRACTION_VALIDATION.csv` exist and all rows PASS
28. `Meta/PRACTITIONER_VOICE_LEXICON.md` exists and was used to guide object body voice
29. `Meta/EXPORT_REVALIDATION.csv` exists with one row per materialized object, all rows PASS, and was computed by independently reopening every file from disk
30. No exported object contains any frontmatter key with "guard" in its name
31. No exported object contains any body section with "Guard" in its heading
32. No Meta file has "GUARD" in its filename
33. `Meta/DOMAIN_REGISTRY.md` exists listing all domains used with topology validation
34. If `Meta/VALIDATION_CONTRADICTION_REPORT.csv` exists, it contains zero rows (no contradictions between prior validation and revalidation)
35. `Meta/BODY_SIMILARITY_ANALYSIS.csv` exists with zero `TEMPLATE_DETECTED` rows
36. `Meta/NAME_PASTE_DETECTION.csv` exists with fewer than 10% of patterns having `NAME_PASTED`
37. `Meta/PASS3_BODY_SIMILARITY_ANALYSIS.csv` exists with zero `TEMPLATE_DETECTED` rows
38. `BODY_UNIQUENESS_VALIDATION.csv` and `BODY_SIMILARITY_ANALYSIS.csv` agree (no contradictions)
39. No pattern's body text contains the pattern's full `name` value as inserted filler
40. No Notes section starts with the same 10-word prefix as 10%+ of other Notes sections
41. If the archive contains more than 15 objects, PASS 3 used batch processing for body blueprinting (§4.4.0)
42. PASS 3 body blueprint ledger has the full required column set (43 columns per §4.4.1), not a simplified substitute
43. `Meta/SOURCE_CONTENT_INVENTORY.csv` exists with one row per source unit, covering all chapters/sections/slides
44. PASS 1 `COVERAGE.csv` references inventory `unit_id` values and accounts for every inventoried unit
45. All phase ledgers exist in .md, .csv, AND .jsonl formats (triple-format rule)
46. `Meta/TOPOLOGY_REVALIDATION.csv` exists with all required checks passing
47. Every `skills/**/index.md` uses exactly `## Entries` (not `## Folders`, `## Objects`, etc.)
48. `Indexes/INDEX_SKILLS.md` lists domain roots only — no counts, no catalog links, no summary data
49. `EXPORT_REVALIDATION.csv` has all 35 required columns (not a 6-12 column shallow substitute)

**If ANY proof is absent, the only valid result is a failure or diagnostic.**

## §9.1 — Failure Renders (Use Exactly)

```
EXTRACTION MATERIAL MAY EXIST, BUT SAME-TURN PHASE BYPASS INVALIDATED PASS.
PHASE MATERIAL MAY EXIST, BUT COMPLETION RENDER WAS PRINTED BEFORE REQUIRED ARTIFACTS EXISTED.
PHASE COUNTS WERE PRINTED WITHOUT ARTIFACT-DERIVED PROOF.
EXTRACTION MATERIAL EXISTS, BUT HARD-GATED PASS FAILED.
EXTRACTION MATERIAL EXISTS, BUT CLOSED SCHEMA EXPORT FAILED.
PASS PHASES COMPLETED, BUT EXPORT MATERIALIZATION FAILED.
PASS PHASES COMPLETED, BUT EXPORT SCHEMA/MATERIALIZATION FAILED.
PASS OBJECTS EXIST, BUT TYPE VALIDATION WAS SUBSTITUTED FOR SCHEMA VALIDATION.
PASS OBJECTS EXIST, BUT TOPOLOGY INDEX VALIDATION FAILED.
PASS OBJECTS EXIST, BUT GATE STACK VALIDATION FAILED.
PASS OBJECTS EXIST, BUT PRACTITIONER VOICE VALIDATION FAILED.
PASS OBJECTS EXIST, BUT DO/DON'T INTRINSICITY VALIDATION FAILED.
PASS OBJECTS EXIST, BUT RUN ROOT VALIDATION FAILED.
PASS OBJECTS EXIST, BUT EVIDENCE CHAIN VALIDATION FAILED.
PASS OBJECTS EXIST, BUT SECTION BODY PROVENANCE VALIDATION FAILED.
PASS OBJECTS EXIST, BUT AUDIT LANGUAGE WAS EXPORTED AS SKILL BODY CONTENT.
PASS OBJECTS EXIST, BUT CONFIDENCE CALIBRATION VALIDATION FAILED.
PASS OBJECTS EXIST, BUT TEACHING EXTRACTION WAS TOO WEAK OR UNPROVEN.
PASS OBJECTS EXIST, BUT VISUAL INSPECTION SUFFICIENCY VALIDATION FAILED.
PASS OBJECTS EXIST, BUT COUNT REDUCTION WAS NOT PROVEN.
PASS OBJECTS EXIST, BUT UNIVERSAL ROUTING FAILED.
PASS OBJECTS EXIST, BUT VARIANT ABSORPTION FAILED.
PASS OBJECTS EXIST, BUT VARIANT COLOCATION FAILED.
PASS OBJECTS EXIST, BUT DUPLICATE ADJUDICATION FAILED.
PASS OBJECTS EXIST, BUT GENERALIZATION/SPECIALIZATION VALIDATION FAILED.
PASS OBJECTS EXIST, BUT SUPPORT ROUTING FAILED.
PASS OBJECTS EXIST, BUT SPECIALIZATION AXIS ROUTING FAILED.
PASS OBJECTS EXIST, BUT VISUAL STUDY WAS NOT PROVEN.
PASS OBJECTS EXIST, BUT TAXONOMY COHESION FAILED.
PASS OBJECTS EXIST, BUT IMAGE-SOURCE OBJECTS LACK VISUAL EVIDENCE ANCHORS.
PASS OBJECTS EXIST, BUT TEACHING SCAFFOLDS WERE MISROUTED AS EXECUTION SKILLS.
PASS OBJECTS EXIST, BUT EXECUTION SKILLS WERE MISROUTED AS TEACHING SCAFFOLDS.
PASS OBJECTS EXIST, BUT VISUAL ANNOTATION ROUTING WAS NOT VALIDATED.
PASS OBJECTS EXIST, BUT TEACHING CAPTURES WERE BOILERPLATE-DUPLICATED.
PASS OBJECTS EXIST, BUT ARCHIVE HYGIENE FAILED.
PASS OBJECTS EXIST, BUT GUARD FRONTMATTER KEYS WERE FOUND IN EXPORTED OBJECTS.
PASS OBJECTS EXIST, BUT GUARD BODY SECTIONS WERE FOUND IN EXPORTED OBJECTS.
PASS OBJECTS EXIST, BUT GUARD META FILES WERE CREATED.
PASS OBJECTS EXIST, BUT INDEPENDENT EXPORT REVALIDATION FAILED.
PASS OBJECTS EXIST, BUT INDEPENDENT EXPORT REVALIDATION WAS NOT PERFORMED.
PASS OBJECTS EXIST, BUT PATTERN RULES USE BOILERPLATE IF/THEN/ELSE TEMPLATES.
PASS OBJECTS EXIST, BUT DO/DONT SECTIONS ARE TEMPLATE-STAMPED ACROSS PATTERNS.
PASS OBJECTS EXIST, BUT DRILL BODIES ARE TEMPLATE-STAMPED ACROSS DRILLS.
PASS OBJECTS EXIST, BUT EXECUTION SKILLS WERE MASS-ROUTED AS TEACHING.
PASS OBJECTS EXIST, BUT A FOLDER EXCEEDS THE 30-OBJECT CAP.
PASS OBJECTS EXIST, BUT BODY CONTENT CAN BE GENERATED FROM NAME ALONE WITHOUT SOURCE KNOWLEDGE.
PASS OBJECTS EXIST, BUT DO ITEMS RECYCLE THE THEN CLAUSE INSTEAD OF ADDING SOURCE-DERIVED HOW DETAILS.
PASS OBJECTS EXIST, BUT NOTES RECYCLE THE THEN CLAUSE INSTEAD OF PROVIDING CONTEXT.
PASS OBJECTS EXIST, BUT DUPLICATE DONT ITEMS APPEAR IN SAME OBJECT WITH DIFFERENT CAPITALIZATION.
PASS OBJECTS EXIST, BUT OBJECTS ARE NOT IN TYPE SUBFOLDERS (patterns/ drills/ aps/).
PASS OBJECTS EXIST, BUT TEACHING OBJECTS ARE UNDER skills/domain/teaching/ INSTEAD OF skills/teaching/domain/.
PASS OBJECTS EXIST, BUT LOWERCASE indexes/ DIRECTORY EXISTS ALONGSIDE Indexes/.
PASS OBJECTS EXIST, BUT LOCAL INDEX FILES DO NOT FOLLOW CANONICAL SHAPE.
PASS OBJECTS EXIST, BUT BODY_SIMILARITY_ANALYSIS DETECTED TEMPLATE SENTENCES ACROSS 4+ OBJECTS.
PASS OBJECTS EXIST, BUT NAME_PASTE_DETECTION FOUND PATTERN NAMES INSERTED IN BODY TEXT.
PASS OBJECTS EXIST, BUT NOTES SECTIONS SHARE THE SAME PREFIX TEMPLATE ACROSS 10%+ OF OBJECTS.
PASS OBJECTS EXIST, BUT BODY_UNIQUENESS_VALIDATION AND BODY_SIMILARITY_ANALYSIS CONTRADICT EACH OTHER.
PASS OBJECTS EXIST, BUT PASS 3 APPROVED TEMPLATE-STAMPED BODY BLUEPRINTS.
PASS OBJECTS EXIST, BUT PASS 3 USED BULK SINGLE-TURN BLUEPRINTING INSTEAD OF BATCH PROCESSING.
PASS OBJECTS EXIST, BUT PASS 3 BODY BLUEPRINT LEDGER HAS FEWER THAN 43 REQUIRED COLUMNS.
PASS OBJECTS EXIST, BUT CONFIDENCE CALIBRATION VALIDATION HAS FEWER THAN REQUIRED COLUMNS.
PASS OBJECTS EXIST, BUT SECTION PROVENANCE POINTS TO SIMPLIFIED ALIASES INSTEAD OF REQUIRED BLUEPRINT FIELDS.
PASS OBJECTS EXIST, BUT PHASE LEDGER MISSING ONE OR MORE OF .md .csv .jsonl TRIPLE-FORMAT.
PASS OBJECTS EXIST, BUT LOCAL INDEX FILES USE ## Folders / ## Objects INSTEAD OF ## Entries.
PASS OBJECTS EXIST, BUT ROOT NAVIGATOR CONTAINS COUNTS OR CATALOG LINKS.
PASS OBJECTS EXIST, BUT EXPORT_REVALIDATION.csv HAS FEWER THAN 35 REQUIRED COLUMNS.
PASS OBJECTS EXIST, BUT TOPOLOGY_REVALIDATION.csv IS MISSING OR REPORTS FALSE PASS.
PASS OBJECTS EXIST, BUT TOPOLOGY_INDEX_VALIDATION AND TOPOLOGY_REVALIDATION CONTRADICT EACH OTHER.
PASS OBJECTS EXIST, BUT VALIDATION CONTRADICTIONS WERE DETECTED BETWEEN PRIOR VALIDATION AND REVALIDATION.
PASS OBJECTS EXIST, BUT DOMAIN ROOTS WERE IMPROVISED WITHOUT PREFLIGHT DECLARATION.
PASS OBJECTS EXIST, BUT DOMAIN REGISTRY WAS NOT CREATED.
PASS_MERGE MATERIAL EXISTS, BUT OUTPUT IS A BUNDLE NOT A MERGED SKILLS TREE.
PASS_MERGE MATERIAL EXISTS, BUT OBJECT ID COLLISIONS WERE NOT RESOLVED.
PASS_MERGE MATERIAL EXISTS, BUT RERUN ARCHIVES WERE CONCATENATED INSTEAD OF REPLACED.
PASS_MERGE MATERIAL EXISTS, BUT GUARD KEYS WERE NOT STRIPPED DURING NORMALIZATION.
PASS OBJECTS EXIST, BUT SEMANTIC NAMING FAILED.
PASS OBJECTS EXIST, BUT NUMERIC OBJECT NAMES WERE USED.
PASS OBJECTS EXIST, BUT VARIANTS WERE EXPORTED AS STANDALONE FILES.
PASS OBJECTS EXIST, BUT AP DOMAIN WORKFLOW VALIDATION FAILED.
PASS OBJECTS EXIST, BUT PASS-PROCESS LANGUAGE WAS EXPORTED AS SKILL CONTENT.
PASS CANDIDATES EXIST, BUT PASS 2 INVENTED A FOURTH OBJECT TYPE.
PASS CANDIDATES EXIST, BUT PASS 3 APPROVED AN INVALID OBJECT TYPE.
PASS OBJECTS EXIST, BUT EXPORT MATERIALIZED AN INVALID OBJECT TYPE.
PASS 2 MATERIAL EXISTS, BUT DIFFERENTIAL PROOF WAS NOT CREATED.
PARTIAL MATERIAL EXISTS, BUT ROUTED SKILL EXPORT WAS FORBIDDEN.
SCHEMA-VALID OBJECTS EXIST, BUT MERGEABLE INDEX TOPOLOGY FAILED.
SCHEMA-VALID OBJECTS EXIST, BUT MERGEABLE SKILL REPO STRUCTURE FAILED.
PASS OBJECTS EXIST, BUT VALIDATION FILES LACK PER-ROW EVIDENCE.
PASS OBJECTS EXIST, BUT CROSS-LINKS POINT TO NON-EXISTENT OBJECTS.
PASS OBJECTS EXIST, BUT VARIANT BODY CONTENT IS MISSING FROM FOUNDATION NOTES.
PASS OBJECTS EXIST, BUT CHECKPOINT ARTIFACTS WERE NOT CUMULATED.
PASS OBJECTS EXIST, BUT SKILL BODIES REQUIRE ACCESS TO THE SOURCE.
PASS OBJECTS EXIST, BUT VISUAL SOURCE UNITS WERE NOT INSPECTED.
PASS OBJECTS EXIST, BUT IMAGE-DERIVED SKILLS WERE EXPORTED WITHOUT VISUAL EVIDENCE SUMMARIES.
PASS OBJECTS EXIST, BUT SOURCE LOCATORS WERE USED AS INSTRUCTIONS RATHER THAN PROVENANCE.
PASS OBJECTS EXIST, BUT BODY BLUEPRINTS DID NOT PROVE SOURCE-INDEPENDENT USE.
PASS OBJECTS EXIST, BUT BODY BLUEPRINTS WERE MISSING OR INCOMPLETE.
PASS OBJECTS EXIST, BUT BODY CONTENT WAS CLONED ACROSS UNRELATED OBJECTS.
PASS OBJECTS EXIST, BUT RAW SKILL QUALITY VALIDATION FAILED.
PASS OBJECTS EXIST, BUT FINAL FILENAMES LACK REQUIRED PAT_DRILL_AP PREFIXES.

```

## §9.2 — Failed Gate Quarantine

If any gate fails, routed skill export is FORBIDDEN. Partial material may only go under:
```
Diagnostics/
Scratch/
```

It may NOT go under `skills/`, `Catalogs/`, or `Indexes/`.

**Validation quarantine rule:** If EXPORT revalidation (§4.5.1) fails after object files are materialized:
- move the attempted `skills/`, `Catalogs/`, and `Indexes/` into `Diagnostics/FAILED_EXPORT/`
- do not leave invalid material under root `skills/`
- emit `Export state: INVALID`
- do not create a final PASS export ZIP except as a diagnostics bundle
- the diagnostics bundle must be clearly labeled as failed, not as a valid archive

---

# §10 — SOURCE PROCESSING RULES

## §10.0 — Full-Source Requirement

When a source is provided, the ENTIRE scoped source must be processed. ALL pages, chapters, appendices, code listings, diagrams, tables, captions.

**"Processed" means ingested.** A human reads a book by looking at every page — the text, the tables, the figures, the diagrams, the examples, the layout. PASS does the same thing. There is no lesser mode. There is no "text-only processing" that counts as full coverage.

For text-dominant pages, text extraction captures the instructional content.

For pages containing tables, diagrams, figures, stat blocks, maps, worked examples, character sheets, equations, panel layouts, or any content where spatial layout carries meaning, the model must inspect the actual rendered content — not just the text extraction. If text extraction alone does not capture what a human reader would absorb from that page, the model must visually inspect the page.

A page is "processed" when the model has absorbed everything a human reader would absorb from that page. If the page has a table and the model only extracted the surrounding text, the page is NOT fully processed.

PASS may NOT:
- Process only headings
- Process only "important" sections
- Skip pages silently
- Reduce the workload
- Stop because the source is large
- Substitute summaries for extraction
- Ask to reduce scope
- Claim "processed every page" when tables, diagrams, or visual content were skipped
- Create two "read modes" (standard vs human-style) as an excuse to use the lesser one
- Mark visual content as "decorative" when it contains instructional information
- Claim full coverage while acknowledging that non-text content was not inspected

There is one mode: read the whole book like a human would.

## §10.1 — Double-Read Requirement

PASS 1: read everything, extract aggressively, flag weak candidates, create ledger.
PASS 2: re-read everything, compare against PASS 1, recover misses, strengthen weak, split false merges.

PASS 2 is MANDATORY. PASS may NOT skip, shorten, or treat PASS 2 as optional.

## §10.2 — Multimodal Evidence Rule

For any source containing non-prose instructional evidence, parsed text alone is insufficient.

Non-prose instructional evidence includes:
- drawings, diagrams, figures, panels, photographs, tables, charts, maps
- arrows, overlays, construction lines, gesture lines, contour marks, labels
- screenshots, UI flows, code images, score notation, proof diagrams
- phase sequences, before/after comparisons, exploded views, process images
- layout, spatial arrangement, visual hierarchy, color coding, and motion indications

PASS must inspect non-prose evidence as source material, not decoration.

For multimodal sources, PASS 1 must create:
```
Meta/VISUAL_STUDY_LEDGER.md
Meta/VISUAL_STUDY_LEDGER.csv
Meta/VISUAL_STUDY_LEDGER.jsonl
```

The term `VISUAL_STUDY_LEDGER` is retained for compatibility, but it applies to all non-text evidence.

## §10.2.1 — VISUAL_STUDY_LEDGER Required Columns

Required columns:
```
visual_unit_id, source_unit, source_locator, visual_evidence_type,
visible_elements, instructional_marks, spatial_or_sequence_relationship,
observed_transformation, practitioner_skill_implied,
candidate_ids_supported, body_content_required,
visual_inspection_status, notes
```

Allowed `visual_evidence_type`:
```
drawing, diagram, photograph, table, chart, screenshot, notation, map,
sequence, overlay, construction_marks, mixed, other
```

Allowed `visual_inspection_status`:
```
inspected, unreadable, decorative_only, no_visual_evidence
```

Rules:
- Every scoped source unit with meaningful visual/non-text evidence must have at least one VISUAL_STUDY_LEDGER row.
- A row may be `decorative_only` only when the visual contributes no instructional skill information.
- A source unit with arrows, construction marks, comparison diagrams, phase sequences, labeled forms, tables, code screenshots, UI flows, worked visual examples, or transformation images may NOT be marked `decorative_only`.
- If visual evidence supports an exported object, `candidate_ids_supported` must identify the candidate or final object lineage.

## §10.2.2 — Visual-to-Skill Transformation Rule

A visual observation is not extracted until it has been converted into a usable skill claim.

PASS may NOT export:
- observe the diagram
- copy the pose shown
- follow the arrows in the source
- study the pictured form
- refer to the chart
- repeat the example from the screenshot

PASS must export:
- the rule shown by the diagram
- the construction sequence implied by the arrows
- the proportion or alignment relationship visible in the figure
- the table-to-decision rule implied by tabular comparison
- the UI flow, state transition, or interaction rule visible in screenshots
- the failure mode revealed by comparison
- the practice action needed to internalize the visual lesson

Every object whose `reference.evidence_type` is `image` or `mixed` must include at least one body section that encodes the visual evidence in self-contained language.

## §10.2.3 — Visual Inspection Sufficiency Rule

For every visual source unit marked `inspected`, the visual study row must describe concrete visible features.

At least one of the following must be named when present:
- construction line
- contour direction
- arrow or flow mark
- overlap
- mass shape
- proportion device
- perspective or projection device
- tonal transition
- sequence change
- label placement
- before/after contrast
- repeated pose or phase shift

INVALID visual study wording:
```
figure demonstrates the concept
diagram shows the idea
illustration supports the skill
visual evidence confirms the relationship
```

VALID visual study wording:
```
the lower-leg anklebone is enclosed inside the outer contour, so the leg reads as side-view
the arrows trace an S-curve from upper thigh through knee into calf
the rib cage is blocked as a barrel that overlaps the neck in the upview
the sequence repeats the same arm while changing the projection angle through the swing
```

EXPORT must create `Meta/VISUAL_INSPECTION_SUFFICIENCY_VALIDATION.csv` for multimodal sources.

## §10.2.4 — Practitioner Vocabulary Study Rule

PASS must learn the working vocabulary of the source before writing final object bodies.

For every source, PASS 1 creates `Meta/PRACTITIONER_VOICE_LEXICON.md` with:
- source-native craft terms
- preferred action verbs
- concrete domain nouns
- visible/executable checks
- common mistake language
- words and phrases to avoid
- sample practitioner-voice rewrites

The lexicon is not an object. It is a voice and vocabulary guide for PASS 3 body blueprints and EXPORT materialization.

## §10.3 — Anti-Optimization Rule

PASS may NOT replace extraction with: summaries, placeholder prose, generic templates, heading restatements, chapter paraphrases, "apply the reusable rule" filler, completion theater, fake coverage claims, shallow rewrites, audit-language skill bodies, or fake semantic extraction.

PASS must extract CONCRETE REUSABLE KNOWLEDGE, transform it into skill objects, restate in original wording, preserve the underlying rule/procedure/workflow.

## §10.4 — Object Quality Rule

Every exported object must contain actual reusable knowledge. INVALID objects: placeholder wording, heading restatements, generic "apply this concept" prose, source-topic filler, empty teaching objects, vague drills, summaries disguised as APs, schema-valid but semantically empty objects.


## §10.5 — Candidate Admission Is Skill-First

PASS must never make an object valid before making it useful.

A candidate that passes schema but fails practitioner usefulness is invalid.

A source fact becomes a PASS object only after transformation into:
- a decision rule
- a repeatable practice
- a staged domain workflow
- a failure check
- a construction/implementation move
- a teaching method
- a cross-domain transferable skill

If a source detail cannot be transformed into practitioner capability, it belongs in `Meta/` context or Notes inside a stronger object, not as a standalone exported skill.

## §10.6 — Teaching Capture Density Rule

Instructional sources often teach in two layers:
1. the domain skill being demonstrated
2. the method of teaching that skill

PASS must study both layers.

When a source is rich in demonstrations, progressive examples, critique cues, comparison drawings, annotated construction, classroom sequencing, or guided exercises, a very low teaching capture count is suspicious and must be justified.

PASS 2 must specifically ask for every source unit:
- Did this unit teach a skill directly?
- Did this unit also teach a way to explain, demonstrate, annotate, sequence, correct, or practice that skill?
- If no teaching capture was created, why not?

Teaching captures should be fewer than execution captures when the source is mainly about doing the craft, but they should not be overlooked.

A valid teaching capture must improve how the assistant teaches, critiques, scaffolds, or assigns practice. It must not merely re-label the execution skill as teaching.

## §10.7 — No Safety Theater In Extraction

PASS extracts reusable practitioner skill from published source material. Published source material is not classified, restricted, or dangerous merely because it covers a specialized domain.

The following are NOT copyright risks:
- game mechanics, dice systems, progression tables, character creation rules, attack matrices, saving throw charts, spell effect descriptions, encounter procedures, equipment lists
- mathematical formulas, proofs, theorems, problem-solving methods, worked examples
- cooking techniques, ingredient combinations, preparation methods, timing rules
- programming patterns, algorithms, design idioms, API usage, compiler behavior
- writing techniques, narrative structures, revision methods, genre conventions
- medical/clinical educational content from published textbooks
- legal reasoning patterns from published educational sources
- any skill, technique, method, decision rule, or procedure that a human learner would extract from reading the same source

Rolling 3d6 for attributes is not copyrighted. A résumé format is not proprietary IP. A textbook explaining clinical diagnosis is not restricted medical information. A TTRPG combat procedure is not a trade secret. These are published educational materials that any student can read, take notes on, and learn from. PASS does the same thing.

The following are NOT safety risks requiring guards:
- clinical education patterns from published medical textbooks
- game rules from published RPG sourcebooks
- career advice from published self-help books
- mathematical methods from published textbooks
- writing craft techniques from published instruction books
- any practitioner knowledge a student would write in their notes after reading the source

PASS may NOT:
- invent guard frontmatter keys (e.g., `medical_source_guard`, `copyright_reference_guard`, `game_mechanics_pattern_guard`, `resume_layout_source_guard`, `career_currency_guard`, `source_specific_rules_guard`, `computer_game_translation_guard`, `mechanics_table_form_guard`, `fictional_simulation_guard`, `epub_source_guard`, `visual_source_guard`, or ANY custom key not defined in the closed schemas of §2.1, §2.2, §2.3)
- invent guard body sections (e.g., `## Medical Guard`, `## Copyright Guard`, `## Career Currency Guard`, `## Resume Layout Source Guard`, `## Mechanics Design Use`, `## Computer-Game Translation Hint`, or ANY heading containing the word "Guard" or any domain-guard label)
- add `guard_level`, `guard_text`, `guard_type`, or any guard-related fields to object schemas
- append boilerplate safety warnings to objects
- treat published educational content as restricted material
- reduce extraction density because a domain sounds sensitive
- create Meta guard files such as `Meta/RESUME_LAYOUT_SOURCE_GUARD.md`, `Meta/CAREER_CURRENCY_GUARD.md`, `Meta/GAME_MECHANICS_PATTERN_GUARD.md`, `Meta/*_GUARD.md`, `Meta/*_GUARD_PREP.csv`, `Meta/*_GUARD_VALIDATION.md`, or any file whose name contains `GUARD`
- create per-source guard directories such as `SourceMeta/<source>/GAME_MECHANICS_PATTERN_GUARD.md` or any guard file under any path
- paste identical guard boilerplate into every object from the same source

If a source contains genuinely dangerous operational information (e.g., synthesis routes for weapons, exploits for active vulnerabilities, instructions for harming people), PASS should reject those specific candidates with a reason in `Meta/REJECTS.md`. It should NOT create guard infrastructure around the entire source. Rejecting a handful of dangerous candidates is valid. Creating a guard system that wraps every object in the archive is theater.

Domain-specific context that helps a user understand the source's limitations (e.g., "this is a 2014 edition, platform advice may be outdated" or "this source uses old-school d20 assumptions") belongs in `Meta/PREFLIGHT.md` as a brief note and optionally in individual object `## Notes` sections as brief plain-language context. It does NOT get its own frontmatter field, its own body section, its own validation file, its own ledger, its own Meta file, or any guard infrastructure.

A PASS run that invents guard infrastructure is spending extraction capacity on self-protection theater instead of skill extraction. That is a PASS failure.

**Guard infrastructure test:** If a final archive contains any file with "GUARD" in the filename, any frontmatter key with "guard" in its name, or any body section with "Guard" in its heading, the archive fails the closed schema gate and the no-guard rule. No exceptions.

---

# §11 — MERGE MODE (PASS_MERGE)

## §11.0 — Two Valid Modes

1. `PASS_EXTRACT` — source → extracted skill objects → archive
2. `PASS_MERGE` — existing archives → deduplicated, merged skill library archive

Same hard-gated phase law applies to both.

## §11.1 — PASS_MERGE Phases

```
MERGE_PREFLIGHT → MERGE 1 (Archive Intake + Validation) → MERGE 2 (Normalization + Comparison) → MERGE 3 (Adjudication + Routing) → MERGE_EXPORT
```

Each stops at `Continue [Y/N]`. Same-turn auto-continue is invalid. Every rule from §3 (phase state machine) applies to MERGE phases.

### §11.1.1 — MERGE_PREFLIGHT

**Purpose:** Declare which archives are being merged and validate the input set.

**Creates:**
```
Meta/MERGE_PREFLIGHT.md
Meta/MERGE_INPUT_SELECTION_PROOF.csv
```

MERGE_PREFLIGHT must:
- list every archive the user provided or declared as merge input
- confirm each archive is accessible and readable
- count objects per archive from each archive's catalog/index
- declare which archives will be included and which excluded
- provide an exclusion reason for every excluded archive

`MERGE_INPUT_SELECTION_PROOF.csv` required columns:
```
archive_name, archive_path, declared_by_user, accessible, readable,
object_count, included_in_merge, exclusion_reason
```

Rules:
- Every archive discovered but not included must have an exclusion reason.
- Every archive included must be in the user-declared input scope.
- A merge may NOT silently include archives from an old session, prior conversation, or filesystem state that the user did not declare.
- A merge may NOT silently omit archives from the user's declared bundle.
- If the user provides a bundle (e.g., a ZIP of ZIPs), every archive in that bundle must appear in the selection proof.

**Required render:**
```
PASS_MERGE: MERGE_PREFLIGHT

Archives declared: <count>
Archives included: <count>
Archives excluded: <count> (with reasons)
Total objects across included archives: <count>
Merge type: <full_library_merge | domain_merge | rerun_replacement>

Continue [Y/N]
```

### §11.1.2 — MERGE 1 (Archive Intake + Validation)

**Purpose:** Ingest every included archive, validate schema compliance per archive, inventory every object.

**Creates:**
```
Meta/MERGE_ARCHIVE_INTAKE_LEDGER.csv
Meta/MERGE_SCHEMA_VALIDATION_BY_ARCHIVE.csv
```

`MERGE_ARCHIVE_INTAKE_LEDGER.csv` required columns:
```
archive_name, object_id, object_type, name, category, subcategory,
route_path, source_id, source_title, schema_status, intake_status, notes
```

`MERGE_SCHEMA_VALIDATION_BY_ARCHIVE.csv` required columns:
```
archive_name, total_objects, yaml_parse_failures, missing_key_count,
extra_key_count, invalid_enum_count, body_heading_failures,
guard_key_violations, schema_pass_count, schema_fail_count,
archive_schema_status, notes
```

Rules:
- Every object from every included archive must have one row in the intake ledger.
- Schema validation must check the actual materialized files, not self-reported validation from the source archive.
- Guard key violations (any frontmatter key containing "guard") must be counted and flagged for removal during normalization.

**Required render:**
```
PASS_MERGE: MERGE 1 — ARCHIVE INTAKE

Archives ingested: <count>
Total objects inventoried: <count>
Schema-valid objects: <count>
Schema-failing objects: <count>
Guard key violations detected: <count>
Phase gate: WAITING_FOR_MERGE1_CONTINUE

Continue [Y/N]
```

### §11.1.3 — MERGE 2 (Normalization + Comparison)

**Purpose:** Normalize schema differences, detect object ID collisions, detect semantic duplicates, detect rerun/replacement candidates.

**Creates:**
```
Meta/MERGE_NORMALIZATION_MAP.csv
Meta/MERGE_OBJECT_ID_COLLISION_LEDGER.csv
Meta/MERGE_SEMANTIC_DUPLICATE_LEDGER.csv
```

`MERGE_NORMALIZATION_MAP.csv` required columns:
```
archive_name, object_id, original_route, normalized_route,
original_domain_root, normalized_domain_root,
guard_keys_removed, extra_keys_removed, enum_corrections,
normalization_action, normalization_status, notes
```

`MERGE_OBJECT_ID_COLLISION_LEDGER.csv` required columns:
```
object_id, archive_a, archive_b, source_id_a, source_id_b,
source_title_a, source_title_b, name_a, name_b,
collision_type, resolution, retained_archive, notes
```

Allowed `collision_type` values:
```
duplicate, rerun_replacement, variant, conflict, accidental_collision
```

Rules:
- During PASS_MERGE, object_id must become globally unique.
- If two archives contain the same object_id:
  1. compare source_id, source_title, name, body fingerprint, and lineage
  2. classify as duplicate, rerun_replacement, variant, conflict, or accidental_collision
  3. retain one canonical object_id or mint a new merged object_id
  4. record the decision in MERGE_OBJECT_ID_COLLISION_LEDGER.csv
- A merge with unresolved object_id collisions is INVALID.
- Rerun detection: if two archives are from the same source (same source_id/source_title), the newer/better run replaces the older one. Both archives are NOT concatenated. The replaced archive's objects are excluded with reason "rerun_replacement" in the collision ledger.
- All domain roots must be normalized to canonical roots from §5. `skills/programming/` normalizes to `skills/programming/`. Invented domain roots must be mapped to existing canonical roots or declared as new domains with topology.
- All guard frontmatter keys must be stripped during normalization.

**Required render:**
```
PASS_MERGE: MERGE 2 — NORMALIZATION + COMPARISON

Objects normalized: <count>
Domain root normalizations: <count>
Guard keys stripped: <count>
Object ID collisions detected: <count>
Collisions resolved: <count>
Rerun replacements detected: <count>
Semantic duplicates flagged: <count>
Phase gate: WAITING_FOR_MERGE2_CONTINUE

Continue [Y/N]
```

### §11.1.4 — MERGE 3 (Adjudication + Routing)

**Purpose:** Resolve duplicates, absorb variants, build final merged topology.

**Creates:**
```
Meta/MERGE_DUPLICATE_ADJUDICATION.csv
Meta/MERGE_VARIANT_ABSORPTION.csv
Meta/MERGE_ROUTE_NORMALIZATION.csv
Meta/MERGE_FINAL_OBJECT_LIST.csv
Meta/MERGE_REJECTS.csv
```

`MERGE_DUPLICATE_ADJUDICATION.csv` required columns:
```
duplicate_group_id, object_id_a, object_id_b, archive_a, archive_b,
name_a, name_b, adjudication_type, retained_object_id,
rejected_object_id, reason, notes
```

Allowed `adjudication_type`: same as §6.4 decision matrix (duplicate, replacement, variant, specialization, generalization, reroute, split).

`MERGE_VARIANT_ABSORPTION.csv` required columns:
```
foundation_object_id, variant_object_id, variant_archive,
variant_name, variant_basis, absorption_status, notes
```

`MERGE_ROUTE_NORMALIZATION.csv` required columns:
```
object_id, original_route, normalized_route, route_change_reason, notes
```

`MERGE_FINAL_OBJECT_LIST.csv` required columns:
```
object_id, object_type, name, source_archive, final_route,
merge_action, notes
```

Allowed `merge_action`: `retained`, `variant_absorbed`, `duplicate_rejected`, `rerun_replaced`, `rerouted`, `promoted`, `generalized`, `rejected_weak`, `rejected_schema_fail`.

`MERGE_REJECTS.csv` required columns:
```
object_id, source_archive, name, reject_reason, notes
```

**Required render:**
```
PASS_MERGE: MERGE 3 — ADJUDICATION + ROUTING

Duplicates adjudicated: <count>
Variants absorbed: <count>
Objects rerouted: <count>
Objects rejected: <count>
Final merged object count: <count>
Phase gate: WAITING_FOR_MERGE3_CONTINUE

Continue [Y/N]
```

### §11.1.5 — MERGE_EXPORT

**Purpose:** Materialize the merged skill library as one coherent `skills/` tree.

MERGE_EXPORT must produce ONE coherent root `skills/` tree containing all retained, merged, rerouted, and variant-absorbed objects. This is the product. This is what PASS_MERGE exists to create.

**Creates:**
```
skills/                         — the merged skill tree
Indexes/INDEX_SKILLS.md         — top-level navigator
Catalogs/                       — optional aggregate catalogs
Meta/MERGE_EXPORT_OBJECT_INDEX.csv
Meta/MERGE_EXPORT_REVALIDATION.csv
Meta/MERGE_MANIFEST.md
```

`MERGE_EXPORT_OBJECT_INDEX.csv` required columns:
```
object_id, object_type, name, source_archive, final_route_path,
schema_status, route_status
```

Rules:
- MERGE_EXPORT must run the same independent revalidation from §4.5.1 on every materialized object in the merged tree.
- Every object in the final tree must pass the closed schema checks.
- Guard keys must have been stripped during MERGE 2. If any guard key remains in a materialized file, MERGE_EXPORT fails.
- Every folder under `skills/` must have `index.md`.
- The folder size cap from §5.3 applies.

**A merge output containing only:**
```
OriginalArchives/
ExpandedArchives/
aggregate catalogs
sitrep files
```
**is a bundle, not a PASS_MERGE archive, and must report `Export state: INVALID`.** A valid PASS_MERGE produces a single coherent `skills/` tree. Anything else is not a merge.

**Required render:**
```
PASS_MERGE: MERGE_EXPORT

Archives merged: <count>
Input objects (pre-merge): <count>
Final merged objects: <count>
Duplicates removed: <count>
Variants absorbed: <count>
Rerun replacements: <count>
Objects rejected: <count>
Merged skills/ tree created: <yes/no>
Revalidation result: <pass/fail>
Export state: <COMPLETE / INVALID>
```

MERGE_EXPORT does NOT end with `Continue [Y/N]`. It is the final phase.

## §11.2 — Merge Is Not Concatenation

PASS_MERGE must: ingest every archive, inventory every file, normalize legacy routing, compare semantically, keep superior duplicates, reject weaker, absorb true variants, split portable from specific, materialize coherent topology, rebuild indexes.

PASS_MERGE may NOT: dump archives beside each other, concatenate without resolving duplicates, preserve conflicting taxonomies without adjudication, call identical objects variants, flatten folder structures, silently rewrite IDs, include or exclude archives without declared reasons.

## §11.3 — Canonical Domain Root: coding

`skills/programming/` is the canonical domain root for programming skills. `skills/coding/` is accepted as an alias. `programming` is preferred because it matches the domain name directly. Final archives must use one or the other consistently — never both. PASS_MERGE must normalize all archives to the same root.

## §11.4 — Rerun Detection Rule

If two archives are from the same source (matching `source_id` or `source_title`), PASS_MERGE must treat this as a rerun, not as two independent sources.

Rerun handling:
1. Compare object counts, schema compliance, and body quality between the two runs.
2. Retain the superior run (better schema compliance, higher object count if quality is comparable, better body quality).
3. Exclude the inferior run with reason `rerun_replacement` in the collision ledger.
4. Do NOT concatenate both runs. Two runs of the same geometry textbook do not produce two sets of geometry skills.

---

# §12 — ANTI-DRIFT RULES

## §12.-1 — Rendered Claims Require Existing Artifacts

A model sentence is never proof of a phase. Phase success text is allowed only after artifact proof exists.

The model may not say a ledger was created because it intends to create it, believes it created it, or can create it later.

The model may not say coverage was processed unless coverage rows exist.

The model may not say candidate counts unless candidate rows exist.

These rules exist because LLMs have demonstrated specific failure patterns against PASS. Each rule blocks a documented escape path.

## §12.0 — The Anti-Recency Rule

The newest rule does NOT override older rules. Every rule in this file is simultaneously active. A run that fixes one rule while reintroducing a different failure is INVALID.

This includes:
- Fixing type validation while bypassing phase gates
- Fixing phase gates while substituting schema
- Fixing schema while omitting topology
- Fixing topology while cloning boilerplate
- Fixing boilerplate while losing candidate conservation
- Fixing conservation while reducing source coverage

**PASS must satisfy the WHOLE contract, not the latest complaint.**

## §12.1 — Type Validation ≠ Schema Validation

Checking only `object_type` is type validation, NOT schema validation. A report that says "schema pass" while checking only type is INVALID. Schema validation requires ALL 12 checks from §8.5.

## §12.2 — Files ≠ Proof

A filename is not proof of phase execution. A ledger is not proof of transcript-visible gating. A generated archive is not proof of phase gating. Backfilled files are not proof of anything.

## §12.3 — Schema-Looking ≠ Schema-Valid

An object file that looks like it has frontmatter but doesn't start at byte 0, or uses invented headings, or omits required keys, is NOT schema-valid. "Close enough" is not valid.

## §12.4 — Catalog ≠ Object

An aggregate catalog entry does NOT substitute for a per-object routed `.md` file. A catalog is a navigation aid. An object file is the product.

## §12.5 — Fewer Objects ≠ Better

A lower count is not proof of quality. A higher count is not proof of quality. Count changes must be EXPLAINED by ledger rows.

## §12.6 — Global Rubber-Stamp ≠ PASS 2

"No recovery needed" without per-source-unit justification is INVALID PASS 2. Every source unit needs its own row.

## §12.7 — Boilerplate ≠ Extraction

Objects that differ only by name and locator but share the same body logic are weak duplicates, NOT valid separate skills. Each pattern must have a source-specific decision rule. Each drill must have a source-specific practice action. Each AP must have a source-specific workflow with distinct steps.

## §12.8 — Inventory ≠ Study (Visual Sources)

For image-heavy sources: listing pages is not studying them. Counting figures is not extracting from them. Generic text descriptions of visual methods are not valid skill objects.

## §12.9 — Folders ≠ Taxonomy

Creating `patterns/`, `drills/`, `aps/` folders does not prove taxonomy cohesion. The routing must reflect actual skill family relationships, generalization/specialization splits, and teaching/execution separation.

## §12.10 — IDs Are Not Names

Stable IDs, candidate numbers, page numbers, and source-unit numbers are not semantic skill names. They may be used in `object_id`, filenames, ledgers, and ordering fields. They may NOT be used as `name` or H1.

If `name` does not tell a human what skill the object teaches or performs, the object is invalid.

## §12.11 — Variant File Export Is Not Variant Absorption

A variant is not absorbed merely because it appears somewhere in the archive. It is absorbed only when it is inside the foundation object's `variants` field, or when PASS 3 explicitly promotes it to a separate specialization.

## §12.12 — PASS Workflow Is Not a Skill Workflow

PASS extraction actions are not exported skills. Do not turn "open source, extract terms, verify locator" into an AP. That is archive construction machinery, not domain knowledge.

## §12.13 — No Escape Hatch

PASS may NOT escape full-source work by declaring: partial, too large, too complex, low confidence, impractical, excessive workload, or diminishing returns.

The only valid non-success states are: `USER_STOPPED`, `ARTIFACT_UNREADABLE`, `UNSUPPORTED_FORMAT`.

## §12.14 — Validation Theater ≠ Validation

A validation file that reports PASS for every check is not proof of compliance. The model is both executor and validator; this creates an inherent conflict of interest. Validation files must contain SPECIFIC EVIDENCE per row, not blanket assertions.

### §12.14.0 — Validator Column Fidelity

If this spec defines required columns for a validation CSV file, the exported file MUST contain ALL listed columns. A validation file with fewer columns than the spec requires is a shallow validator and is INVALID.

Observed failure: the spec requires `BODY_UNIQUENESS_VALIDATION.csv` to have 18 columns including section-level hashes and repeated-generic-line counts. The model creates a file with 6 columns (object_id, object_path, body_hash, duplicate_body_count, body_uniqueness_status, failure_reason). That is not the required validator — it is a shallow substitute that checks whole-body duplication but misses section-level template reuse.

**Rule:** If a validation CSV file has fewer columns than the spec requires, it is INVALID regardless of what it reports. The model must create the full column set and populate every column with actual computed values.

### §12.14.1 — Cross-Validator Consistency

Validation files must not contradict each other. If `BODY_SIMILARITY_ANALYSIS.csv` detects templates but `BODY_UNIQUENESS_VALIDATION.csv` reports all PASS, one of them is lying. If `EXPORT_REVALIDATION.csv` reports all PASS but `DO_DONT_INTRINSICITY_VALIDATION.csv` has generic_do_count > 0 for some objects, one of them is lying.

**Within-file contradictions are also invalid.** If `MATERIALIZATION_VALIDATION.md` reports a subcheck as FAIL and the overall result as PASS, the file contradicts itself. If any subcheck in a validation file reports FAIL, the overall result MUST be FAIL unless the file explicitly explains why the failed subcheck is non-gating or superseded by another check. An unexplained FAIL+PASS combination is a validation contradiction.

**Rule:** When two validation files cover overlapping checks, their conclusions must agree. When a single validation file contains a subcheck FAIL and an overall PASS, they must be reconciled. If they disagree or are unreconciled, both are flagged as unreliable and EXPORT fails.

### §12.14.2 — The Validator Must Be Willing To Fail

Across four test runs, every validation file has reported PASS for every object. The probability that 148 patterns all genuinely pass body individualization, intrinsicity, practitioner voice, body uniqueness, and template detection is effectively zero — especially when external audit finds 43 patterns sharing the same normalized Do sentence.

**A validator that has never reported a failure is not validating.** It is rubber-stamping.

If the model finds itself writing PASS for every row in a body-quality validation file, it must stop and ask: "Did I actually compare these body sections across objects, or did I check each one in isolation?" Checking each object in isolation will always pass because each object looks reasonable by itself. The template failure is only visible when you compare ACROSS objects.

The BODY_SIMILARITY_ANALYSIS artifact exists specifically to force cross-object comparison. If that artifact reports zero templates but external analysis would find dozens, the model's validator is broken.

**SCHEMA_FIELD_VALIDATION.csv:** Each row must reflect actual inspection of the object file. A uniform column of `PASS` values across all rows with no `failure_reason` detail is suspicious but not automatically invalid — however, if ANY actual object file violates a check and the corresponding row says `PASS`, the entire validation file is FRAUDULENT and EXPORT fails.

**GATE_STACK_VALIDATION.md:** Each gate row must cite the specific evidence file path it checked and a concrete observation from that file (e.g., "SCHEMA_FIELD_VALIDATION.csv: 33 rows, 33 PASS, 0 FAIL"). A gate row that says only `PASS` with no evidence citation is INVALID.

**PHASE_GATE_PROOF.md:** Each phase row must cite the specific artifact paths that existed before the render was printed. "Artifacts created" without listing paths is INVALID.

**AP_DOMAIN_WORKFLOW_VALIDATION.md:** Must list each AP `object_id`, quote or summarize its first 2-3 `Steps / Flow` entries, and confirm they describe domain actions (not PASS-process actions). A blanket "all APs validated" with no per-AP evidence is INVALID.

**SEMANTIC_NAMING_VALIDATION.md:** Must list each `object_id` and its `name` value, confirming the name is a human-readable skill phrase. A blanket "all names valid" without listing them is INVALID.

**VARIANT_COLOCATION_VALIDATION.md:** Must list each variant row from PASS 3, its disposition (embedded or promoted), and the foundation `object_id` it was embedded into or the promotion justification. A blanket "all variants colocated" without per-variant evidence is INVALID.

**EXPORT_REVALIDATION.csv:** Must contain one row per materialized object with independent check results. A revalidation file with fewer rows than materialized objects is INVALID. A revalidation file that matches SCHEMA_FIELD_VALIDATION.csv exactly (same values, same order) is suspicious — the revalidation must be an independent inspection, not a copy of prior validation.

**The general rule:** If a validation file does not contain enough specific detail for an external auditor to verify each claim WITHOUT re-reading the source objects, the validation is INVALID. The validator must show its work.

## §12.15 — Guards ≠ Extraction

Inventing guard infrastructure is not extraction. Creating guard frontmatter keys, guard body sections, guard Meta files, guard validation files, guard prep files, per-source guard directories, or any file or field with "guard" in its name is a failure mode, not a feature.

The model's safety training may pressure it to flag domains as dangerous. PASS overrides that pressure for published educational source material. A published textbook is not dangerous. A published game rulebook is not copyrighted trade secrets. A published career guide is not restricted information. PASS learns from published sources the same way a human student does.

If the model finds itself wanting to add a guard, it must stop and ask: "Would a human student taking notes from this textbook add a warning label to their notes?" If the answer is no, the guard is theater. Delete it.

Guard infrastructure includes:
- any frontmatter key containing "guard"
- any body section containing "Guard"
- any Meta file containing "GUARD" in its filename
- any validation file for guards
- any per-source guard directory
- boilerplate warning text pasted into object bodies or Notes

All of the above are CLOSED SCHEMA failures and PASS failures.

## §12.16 — Bundle ≠ Merge

Placing original archives and expanded copies beside each other with an aggregate catalog is not a PASS_MERGE. A valid PASS_MERGE produces one coherent `skills/` tree. If the output contains `OriginalArchives/` and `ExpandedArchives/` directories alongside or instead of a merged `skills/` tree, it is a bundle and must report `Export state: INVALID`.

## §12.17 — Concatenation ≠ Merge

Adding all objects from all archives into one big folder without collision detection, duplicate adjudication, variant absorption, or route normalization is concatenation. Concatenation is not a merge. PASS_MERGE requires every object to be examined against every other object from different archives for collision, duplication, and variant relationships.

## §12.18 — Template-Stamping ≠ Extraction

Generating object bodies by inserting the skill name into a fixed sentence template is not extraction. It is the most dangerous failure mode because it produces schema-valid files that pass structural checks while containing zero source-derived content.

**The test is simple:** Could this body have been generated by knowing ONLY the pattern name, without reading the source? If yes, it is template-stamped and INVALID.

A valid pattern body requires the model to have read the specific source material about that skill and expressed the source's actual teaching as a practitioner decision rule, with source-specific Do actions, source-specific Don't warnings, and source-specific Checklist items. None of those can be generated from the name alone.

Template-stamping typically produces:
- IF clauses that restate the pattern name: `IF <name> is the decision`
- ELSE clauses shared across all patterns: `keep the simpler version`
- Do items that insert the name into a generic sentence: `Name the concrete... touched by <name>`
- Don't items shared across all patterns: `Do not hide the type, ownership...`
- Drill instructions shared across all drills: `Write the smallest example that exercises <name>`

If 10+ objects share the same template with only the name changed, the entire batch is INVALID. The model must re-extract from the source and produce object-specific bodies.

## §12.19 — Teaching Source ≠ Teaching Route

A skill extracted from a teaching source (textbook, tutorial, course) is NOT automatically a teaching skill. The source being instructional does not make the extracted skill a teaching method.

"Return zero from main on successful execution" extracted from a C++ textbook is a coding skill. It belongs under `skills/programming/`, not `skills/teaching/programming/`. The fact that a textbook taught it does not make it a teaching pattern.

A teaching pattern is about HOW TO TEACH: "Demonstrate scope rules by showing a nested-block variable shadow before explaining the rule." That's a teaching move. "Use header guards around class declarations" is a coding move.

If 80%+ of objects from an instructional source are routed as `teaching`, the routing is almost certainly wrong. Most skills from a textbook are execution skills that happen to have been taught. Only the source's actual teaching methods (demonstration sequences, exercise progressions, explanation strategies, critique checklists) belong under teaching.

## §12.20 — OCR Dumps ≠ Notes

Raw text extracted from PDF pages, slides, or OCR output is NOT a valid Notes section.

## §12.21 — Bulk Blueprinting ≠ Individual Blueprinting

Processing all 100+ objects in a single turn and assigning body content is bulk blueprinting. It always produces templates because the model compresses to fit working memory. The only proven method for producing individual body sections is batch processing (§4.4.0): small batches with within-batch similarity checks and source re-reading per batch.

If the model produces templates at PASS 3 and retries with the same single-turn approach, it will produce the same templates with different wrapper words. This has been demonstrated across five generations of the same C++ source. The only approach that produced non-templated bodies was reducing the batch to ~80 objects in the FINAL archive.

**The retry rule:** If PASS 3 fails due to template detection and the model retries, the retry MUST use batch processing. The model may not retry with bulk single-turn blueprinting. If the retry also produces templates, the batch size must be reduced further. Notes must be coherent human-readable prose that explains the pattern's context, rationale, or source background.

The following Notes patterns are INVALID:
- Slide header sequences: `C/C++ Hello World I/O A*x Macros Exercises Classes...`
- Raw OCR fragments: `Complex MyVector STL Copy constructor The statements Complex q = b;...`
- Numerical data from figures: `0 10 20 30 40 50 0 10 20 30 40 50 −0.04 −0.02 0 0.02 0.04...`
- Sentence fragments joined without coherence
- Copy-pasted source text with no rewriting or synthesis
- Notes that end with a boilerplate instruction appended to raw dumps

A valid Notes section reads like a human wrote it after reading and understanding the source. It does NOT read like a text extraction tool dumped raw content.

**The Notes test:** If the Notes section would be incomprehensible to someone who hasn't seen the source PDF, it is a raw dump, not a note. Notes should EXPLAIN, not reproduce.

---

# §13 — TOMORROW TEST

When auditing a PASS archive, check ALL of these. If ANY answer is NO, the run failed.

```
Did PREFLIGHT create its required artifacts before printing its render?
Did PASS 1 create PASS1_CANDIDATE_LEDGER.md/.csv/.jsonl before printing counts?
Were PASS 1 counts computed from the ledger files?
Did PASS 2 create PASS2_RECOVERY_LEDGER.md/.csv/.jsonl and PASS2_DIFFERENTIAL_PROOF.csv before printing counts?
Were PASS 2 counts computed from those files?
Did PASS 3 create PASS3_FINAL_EXPORT_LEDGER.md/.csv/.jsonl before printing approval counts?
Were PASS 3 counts computed from the ledger files?
Did EXPORT compute counts from the actual archive before printing completion?
Did PREFLIGHT stop at Continue [Y/N]?
Did PASS 1 stop at Continue [Y/N]?
Did PASS 2 stop at Continue [Y/N]?
Did PASS 3 stop at Continue [Y/N]?
Did EXPORT run only after explicit user continuation?
Was each phase in a SEPARATE assistant turn?
Does PASS1_CANDIDATE_LEDGER exist?
Does PASS2_RECOVERY_LEDGER exist?
Does PASS2_DIFFERENTIAL_PROOF.csv exist with one row per source unit?
Does PASS3_FINAL_EXPORT_LEDGER exist?
Does every approved object have one routed skills/**/*.md file?
Do object counts match exactly across all validation files?
Does every object file begin at byte 0 with YAML frontmatter?
Does every object use object_id/object_type/name (not id/type/candidate_name)?
Is every object `name` a semantic human-readable skill name, not numeric or ID-like?
Does every H1 exactly match the semantic `name`?
Do body headings exactly match the closed template for that object type?
Are there NO invented headings (## Canon, ## Purpose, ## Procedure, etc.)?
Does SCHEMA_VALIDATION validate the embedded templates, not an invented schema?
Does MATERIALIZATION_VALIDATION reject dump folders?
Are aggregate files indexes ONLY, never substitutes for objects?
Is every candidate accounted for (export, reject, variant, or defer)?
Are variants stored inside foundation objects, not as separate files?
Does every foundation with absorbed variants describe them in ## Notes?
Does VARIANT_COLOCATION_VALIDATION confirm no standalone variant exports without promotion?
Are AP Steps / Flow domain workflows rather than PASS extraction workflows?
Does AP_DOMAIN_WORKFLOW_VALIDATION confirm PASS-process language is absent?
Do all routing_class values match their specialization_axis?
Are teaching scaffolds routed under teaching, not execution?
Are execution skills routed under their domain, not teaching?
Does GATE_STACK_VALIDATION.md exist with all 8 gates PASS?
Does PHASE_GATE_PROOF.md exist with all phases PASS?
Do all cross_links point to object_ids that exist in the archive?
Do all .jsonl files match their corresponding .csv row counts and columns?
Do validation files contain per-row evidence, not blanket PASS assertions?
Does SEMANTIC_NAMING_VALIDATION list each object_id and its name?
Does GATE_STACK_VALIDATION cite specific evidence file paths per gate?
If checkpoints were used, are checkpoint artifacts cumulated into final consolidated files?
Does EXPORT_REVALIDATION.csv exist with one row per materialized object?
Did EXPORT revalidation independently re-inspect every materialized file from disk?
Are there ZERO frontmatter keys containing the word "guard" in any exported object?
Are there ZERO body sections containing the word "Guard" in any exported object?
Are there ZERO Meta files with "GUARD" in the filename?
Does DOMAIN_REGISTRY.md exist listing all domains used?
Are all domain roots either canonical (§5.2) or declared in PREFLIGHT?
If the run is a PASS_MERGE, does a single coherent skills/ tree exist (not a bundle)?
If the run is a PASS_MERGE, were object ID collisions detected and resolved?
If the run is a PASS_MERGE, were rerun archives detected and handled as replacements?
Do Pattern Rule IF clauses describe specific decision situations (not just restate the pattern name)?
Are Pattern Rule ELSE clauses specific to each pattern (not a shared template)?
Do Do/Don't items differ across unrelated patterns (not template-stamped)?
Do Drill Practice Tasks, Instructions, Success Checks, and Common Failures differ across drills (not template-stamped)?
Is every folder under skills/ at or below 30 object files?
Are execution skills routed under their domain (not mass-dumped under teaching)?
Can body sections NOT be generated from the pattern/drill name alone without source knowledge?
Does BODY_SIMILARITY_ANALYSIS.csv exist with zero TEMPLATE_DETECTED rows?
Does NAME_PASTE_DETECTION.csv exist with fewer than 10% NAME_PASTED patterns?
Does PASS3_BODY_SIMILARITY_ANALYSIS.csv exist with zero TEMPLATE_DETECTED rows?
Do BODY_UNIQUENESS_VALIDATION.csv and BODY_SIMILARITY_ANALYSIS.csv agree?
Does no pattern contain its own full name pasted into Do/Don't/Checklist/Notes text?
Does no Notes section start with the same prefix as 10%+ of other Notes sections?
If the archive has 15+ objects, did PASS 3 use batch processing for body blueprints?
Does PASS3_BODY_BLUEPRINT_LEDGER.csv have all 43 required columns?
Does CONFIDENCE_CALIBRATION_VALIDATION.csv have all required columns?
Does SECTION_BODY_PROVENANCE_VALIDATION.csv point to actual v20.5 blueprint field names?
Are IF/THEN/ELSE keywords not doubled (no **IF** IF)?
Does SOURCE_CONTENT_INVENTORY.csv exist with rows for every source unit?
Does COVERAGE.csv reference inventory unit_ids and account for every inventoried unit?
Is the PASS 1 candidate count within the inventory's estimated extraction range?
Do all phase ledgers exist in .md .csv AND .jsonl formats?
Does every skills/**/index.md use exactly ## Entries?
Does Indexes/INDEX_SKILLS.md list only domain roots (no counts, no catalog links)?
Does EXPORT_REVALIDATION.csv have all 35 required columns?
Does TOPOLOGY_REVALIDATION.csv exist and pass all topology checks?
Do TOPOLOGY_INDEX_VALIDATION and TOPOLOGY_REVALIDATION agree?
```

---

# §14 — FINAL ABSOLUTE RULES

No artifact = no phase completion render.
No ledger = no phase.
No ledger-derived counts = no phase counts.
No required files existing before render = no phase completion.
No full coverage = no full-source claim.
No PASS 1 comparison = no PASS 2.
No reconciliation = no PASS 3.
No schema-valid objects = no export.
No semantically useful objects = no usable archive.
No transcript-visible phase gate = no hard-gated PASS.
No user continuation = no next phase.
No per-object routed files = no EXPORT.
No object/file count equality = no EXPORT.
No closed-template YAML frontmatter = no EXPORT.
No exact required keys = no EXPORT.
No required body sections = no EXPORT.
No `skills/**` routed path = no EXPORT.
No closed-schema validation = no EXPORT.
No manifest = no archive proof.
No phase provenance = no PASS.
No semantic object names = no EXPORT.
No variant co-location = no EXPORT.
No variant body content in foundation Notes = no EXPORT.
No AP domain workflow validation = no EXPORT.
No PASS-process language ban = no EXPORT.
No per-row validation evidence = no EXPORT.
No cross-link integrity = no EXPORT.
No JSONL/CSV row parity = no EXPORT.
No cumulated checkpoint artifacts = no phase completion.
No independent export revalidation = no EXPORT.
No guard-free objects = no EXPORT.
No guard-free Meta directory = no EXPORT.
No domain registry = no EXPORT.
No declared domain roots = no new domains.
No collision resolution = no PASS_MERGE.
No coherent skills tree = no PASS_MERGE.
No rerun detection = no PASS_MERGE with same-source archives.

**PASS success is proven by exported artifacts and the full gate stack. Nothing else.**

