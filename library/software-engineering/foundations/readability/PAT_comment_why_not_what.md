---
object_id: PAT_comment_why_not_what
object_type: pattern
name: Comment the Why, Not the What
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
  - comments
  - documentation
  - readability
  - maintainability
cross_links:
  - rel: related_to
    target_object_id: PAT_make_code_readable
reference:
  source_id: gcbc_think_like_swe
  source_title: "Good Code, Bad Code: Think Like a Software Engineer"
  author: Tom Long
  publish_date: 2021
  media_type: PDF
  locator: u05, pp. 108-112
  evidence_type: text
confidence: high
references: []
variants:
  - variant_id: v_cognition_high_level_comments_as_chunks
    variant_name: Use High-Level Comments as Chunk Labels
    variant_basis: emphasis
    source_id: programmers_brain
    source_title: "The Programmer's Brain: What Every Programmer Needs to Know About Cognition"
    locator: u02, pp. 27-28
    difference_from_foundation: Gives high-level functional comments a cognitive role as labels for a larger code chunk while showing that line-level what-comments consume attention and burden the same chunking process.
    when_to_use: A concise functional summary helps a reader, especially a newcomer, recognize the purpose of a larger block before processing its details.
    when_not_to_use: The comment merely narrates an obvious statement or duplicates a name the code can express directly.
    absorbed_from_object_id: none
---

# Comment the Why, Not the What

## Pattern Rule
**IF** you are about to write a comment
**THEN** reserve it for the why — context the code cannot convey — and for high-level summaries, and make the line-by-line what self-explanatory through the code itself.

## Do
- Comment context the code cannot show: a product or business decision, a fix for a nonobvious bug, or a counterintuitive quirk of a dependency — for example why users who signed up before v2.0 get name-based IDs, with an issue link.
- Use high-level summaries like a book's back-cover synopsis: a class-level comment noting the `User` relates to the streaming service and may be out of sync with the database helps a reader gauge relevance fast.
- When a comment is only needed because the code is unclear, fix the code instead — pull `data[0]`/`data[1]` into `firstName(data)`/`lastName(data)` rather than explaining the indices.

## Don't
- Don't write redundant what-comments on self-explanatory code; a comment restating `firstName + "." + lastName` just adds clutter and a second thing to keep in sync.
- Don't let a per-line synopsis pile up; a comment on every line is like a synopsis before every paragraph of a book — it harms readability rather than helping.

## Checklist
- Does each comment explain why, or summarize at a high level, rather than restate the code?
- Where a comment explains what, could clearer code remove the need for it?
- Will this comment go stale, and is it worth that maintenance cost?

## Notes

Long splits comment purposes into what and why: the what should mostly come from readable code and names, while the why — business decisions, weird-bug fixes, dependency quirks — genuinely needs prose because the code cannot self-explain intent. He balances this against the standing costs of comments (maintenance, staleness, clutter) and the chapter-3 reality that engineers often do not read documentation, so comments are a supplement to readable code, not a replacement for it.

Variant `v_cognition_high_level_comments_as_chunks` (The Programmer's Brain, Chapter 2) preserves a narrow exception for functional summaries: a comment such as "prints a binary tree in order" gives a reader one label for a larger block and is especially useful to newcomers. The same evidence strengthens the foundation's rejection of line-by-line narration; a comment that only says to increment an index consumes attention and makes chunking harder.
