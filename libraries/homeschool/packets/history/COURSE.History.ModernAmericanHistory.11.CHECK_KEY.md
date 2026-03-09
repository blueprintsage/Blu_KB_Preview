# COURSE.History.ModernAmericanHistory.11.CHECK_KEY

course_id: COURSE.History.ModernAmericanHistory.11
packet_file: CHECK_KEY
version: 0.9.0
status: DRAFT
updated: 2026-03-08
packet_mode: HYBRID
grade_level: 11
subject: History
focus_window: Block 5 (Days 121-150) first-pass build
purpose: Teacher/check key for Modern American History packet-supported days.

grading_mode_defaults:
- tutoring_mode: CHECK_ONLY
- objective_workflow: not_primary
- subjective_workflow: check_only_feedback_then_record
- evidence_required: yes

completion_rules:
- COMPLETE requires:
  - visible prompt or source target
  - student-authored response artifact
  - enough writing to judge the answer honestly
  - no unresolved mode violation
- DEFERRED if:
  - the prompt is missing
  - the answer is too thin to judge
  - the response is unfinished
- REVIEW_REQUIRED if:
  - the answer may be partly right but is too vague
  - the historical reasoning is weak
  - the evidence is too generic to verify

## Day 132 Check Rubric

day_number: 132
lesson_title: Mixed Response Practice II — cause, consequence, significance

rubric_dimensions:
- prompt_alignment
- historical_accuracy
- evidence_quality
- reasoning_quality
- clarity

prompt_alignment:
- strong:
  - directly answers the full prompt
- partial:
  - answers part of the prompt but misses the exact lens
- weak:
  - drifts into generic summary

historical_accuracy:
- strong:
  - details are plausible, relevant, and appropriately framed
- partial:
  - generally right but imprecise
- weak:
  - inaccurate, confused, or unsupported

evidence_quality:
- strong:
  - specific detail tied to the claim
- partial:
  - evidence is present but thin or broad
- weak:
  - little or no concrete support

reasoning_quality:
- strong:
  - explains why the detail matters historically
- partial:
  - some explanation but underdeveloped
- weak:
  - mostly summary or assertion

clarity:
- strong:
  - organized and readable
- partial:
  - understandable but loose
- weak:
  - hard to follow or too incomplete to judge

feedback_templates:
- strong:
  - "This answers the prompt clearly and connects the detail to historical significance well."
- vague_claim:
  - "You’re pointing in the right direction, but the claim is too broad. Say what specifically changed or mattered."
- weak_evidence:
  - "You need a more exact historical detail here. Right now the answer is too general to verify."
- summary_only:
  - "This mostly tells what happened. Add a sentence explaining why that mattered historically."
- incomplete:
  - "I can’t verify this honestly yet because the response is too thin. Finish the answer so I can judge it."
- cause_effect_mixup:
  - "You may be blending cause and effect. Separate what led to the event from what happened because of it."

grading_guidance:
- complete_and_strong:
  - FINAL
- complete_but_mixed:
  - FINAL with notes or correction suggestion
- too_thin_to_verify:
  - DEFERRED
- unclear_or_unverifiable:
  - REVIEW_REQUIRED

gradebook_write_template:
- course_id: COURSE.History.ModernAmericanHistory.11
- title: Modern American History Block 5 — Day 132 Mixed Response Practice II
- entry_type: ASSIGNMENT
- grading_basis: subjective
- status: FINAL only when the response is sufficiently reviewable
- notes:
  - include strongest dimension
  - include weakest dimension
  - include whether revision was advised

notes:
- This check key is for evaluation and feedback, not answer-supply.
- School should use it to prevent false completion when the history response is too thin or too vague to verify.
