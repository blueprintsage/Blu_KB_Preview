# COURSE.ELA.BritishLiterature.11.CHECK_KEY

course_id: COURSE.ELA.BritishLiterature.11
packet_file: CHECK_KEY
version: 0.9.0
status: DRAFT
updated: 2026-03-08
packet_mode: PACKET-SPINED
grade_level: 11
subject: English
focus_window: Block 5 (Days 121-150) first-pass build
purpose: Teacher/check key for British Literature packet-supported days.

grading_mode_defaults:
- tutoring_mode: NO_ANSWERING
- objective_workflow: not_primary
- subjective_workflow: check_only_feedback_then_record
- ghostwriting_forbidden: yes

completion_rules:
- COMPLETE requires:
  - visible prompt or source target
  - student-authored response artifact
  - enough writing to judge the answer honestly
  - no tutoring-mode violation
- DEFERRED if:
  - the prompt is missing
  - the answer is too thin to judge
  - the response is unfinished
- REVIEW_REQUIRED if:
  - the answer may be partially right but is too vague
  - the evidence is weak or unsupported
  - the response appears heavily copied or non-student-authored

## Day 132 Check Rubric

day_number: 132
lesson_title: Mixed Response Practice II — evidence, explanation, revision

rubric_dimensions:
- prompt_alignment
- claim_quality
- evidence_quality
- reasoning_quality
- originality / student authorship
- clarity

prompt_alignment:
- strong:
  - directly answers the full prompt
- partial:
  - answers only part of the prompt
- weak:
  - drifts into summary or generic comments

claim_quality:
- strong:
  - specific, arguable, text-rooted
- partial:
  - relevant but vague
- weak:
  - generic or off-target

evidence_quality:
- strong:
  - specific details from the text or prompt
- partial:
  - evidence is present but thin or loosely connected
- weak:
  - little or no text support

reasoning_quality:
- strong:
  - explains what the evidence does and why it matters
- partial:
  - some explanation but underdeveloped
- weak:
  - mostly summary or unsupported conclusion

originality_check:
- acceptable:
  - clearly student-authored wording
- concern:
  - response sounds imported, over-polished, or unlike the student's actual level
- action:
  - if authorship is doubtful, do not mark COMPLETE until clarified

feedback_templates:
- strong:
  - "This answers the prompt clearly and uses evidence well. The explanation ties the detail back to the claim."
- vague_claim:
  - "Your idea points in the right direction, but the claim is too broad. Tighten what the author is doing specifically."
- weak_evidence:
  - "You need a more exact detail from the text. Right now the answer sounds mostly general."
- summary_only:
  - "You’re retelling more than analyzing. Add a sentence explaining what the detail shows."
- incomplete:
  - "I can’t verify this yet because the response is too thin. Finish the answer so I can judge it honestly."
- no_answering_guard:
  - "I can check and guide, but I can’t write the answer for you."

grading_guidance:
- complete_and_strong:
  - FINAL
- complete_but_mixed:
  - FINAL with notes or correction suggestion
- too_thin_to_verify:
  - DEFERRED
- likely copied / not authentic:
  - REVIEW_REQUIRED

gradebook_write_template:
- course_id: COURSE.ELA.BritishLiterature.11
- title: British Literature Block 5 — Day 132 Mixed Response Practice II
- entry_type: ASSIGNMENT
- grading_basis: subjective
- status: FINAL only when the response is sufficiently student-authored and reviewable
- notes:
  - include the strongest dimension
  - include the weakest dimension
  - include whether revision was advised

notes:
- This check key is for evaluation and feedback only.
- School must not cross NO_ANSWERING by turning this into ghostwritten content.
