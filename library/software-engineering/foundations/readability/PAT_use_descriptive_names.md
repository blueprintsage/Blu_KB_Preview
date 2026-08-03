---
object_id: PAT_use_descriptive_names
object_type: pattern
name: Use Descriptive Names Instead of Comments to Explain What Things Are
library_path:
  - software-engineering
  - foundations
  - readability
stage_binding: 3 rough
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
  - naming
  - readability
  - self_documenting_code
  - comments
cross_links:
  - rel: related_to
    target_object_id: PAT_make_code_readable
reference:
  source_id: gcbc_think_like_swe
  source_title: "Good Code, Bad Code: Think Like a Software Engineer"
  author: Tom Long
  publish_date: 2021
  media_type: PDF
  locator: u05, pp. 106-108
  evidence_type: text
confidence: high
references: []
variants:
  - variant_id: v_cognition_visually_distinct_identifiers
    variant_name: Keep Short Identifiers Visually and Structurally Distinct
    variant_basis: constraint
    source_id: programmers_brain
    source_title: "The Programmer's Brain: What Every Programmer Needs to Know About Cognition"
    locator: u02, p. 17
    difference_from_foundation: Adds a perceptual constraint on top of semantic descriptiveness, requiring a name to also be quick to tell apart from its neighbours and from digits, because unfamiliar or confusable short names defeat the pattern recognition a reader uses to group code.
    when_to_use: Choosing loop counters, temporaries, and other short-lived names, or reviewing code where single letters and lookalike glyphs already appear.
    when_not_to_use: A conventional short name is already unambiguous in context and renaming it would break a convention readers rely on.
    absorbed_from_object_id: none
---

# Use Descriptive Names Instead of Comments to Explain What Things Are

## Pattern Rule
**IF** you are naming a class, function, or variable
**THEN** give it a name that summarizes what it is or does, so the code explains itself, rather than using a short name propped up by a comment.

## Do
- Name for the concept, the way `toaster` tells you far more than `object A`: turn `class T` with `pns` and `s` into `Team` with `playerNames` and `score`.
- Make each call site legible in isolation — `team.containsPlayer(playerName)` is self-explanatory where `t.f(n)` forces a trip to the class definition.
- Let descriptive names replace low-level comments, cutting the clutter and the second thing (the comment) that must be kept in sync with the code.

## Don't
- Don't use a comment to say what a badly-named thing is; a reader deep in a long file then has to scroll back to the declaration to recall what `s` means.
- Don't treat parameter/return documentation as a substitute for names — that documentation can be useful, but it is not where the what-it-is should live.

## Checklist
- Can a reader tell what each name refers to without scrolling elsewhere?
- Is any comment present only to explain a name that could be more descriptive?
- Does a call read clearly on its own line, without opening the callee?

## Notes
Long's before/after is stark: the `T`/`pns`/`s` version is impenetrable, the `Team`/`playerNames`/`score` version is obvious, and adding comments to the bad version only clutters it and adds maintenance. This is the concrete first technique under the chapter-1 readability foundation — names are the cheapest and highest-leverage readability tool, and they remove the clutter and staleness risk that comments carry.

Variant `v_cognition_visually_distinct_identifiers` (The Programmer's Brain, Chapter 2) adds a perceptual constraint the foundation does not cover. Hermans deliberately obfuscates a Java routine using `b` and `l` as loop iterators and reports that readers struggle to reproduce it: `l` is visually almost identical to `1`, and unfamiliar short names slow the detection and recognition of otherwise routine structures. Semantic descriptiveness is therefore necessary but not sufficient — a name also has to survive a fast glance. Use this when picking counters and temporaries or when reviewing code that already contains lookalike glyphs; do not use it to churn a conventional short name that is already unambiguous.
