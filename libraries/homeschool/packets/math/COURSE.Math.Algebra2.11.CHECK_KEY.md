# COURSE.Math.Algebra2.11.CHECK_KEY

course_id: COURSE.Math.Algebra2.11
packet_file: CHECK_KEY
version: 0.9.0
status: DRAFT
updated: 2026-03-08
packet_mode: HYBRID
grade_level: 11
subject: Math
focus_window: Block 5 (Days 121-150) first-pass build
purpose: Teacher/check key for Algebra 2 packet-supported days.

grading_mode_defaults:
- tutoring_mode: CHECK_ONLY
- objective_workflow: auto_record_when_evidence_is_sufficient
- correction_pass_allowed: yes

completion_rules:
- COMPLETE requires:
  - visible work artifact
  - enough shown steps to verify reasoning
  - no unresolved restricted-value issue on rational problems
  - no unchecked radical-equation result
- DEFERRED if:
  - work is partial
  - answers are present without enough verification steps
  - a source/problem page is missing when needed
- REVIEW_REQUIRED if:
  - the artifact is illegible
  - the solve path is ambiguous
  - the student may have an extraneous solution not yet checked

## Day 132 Answer Key

day_number: 132
lesson_title: Mixed Review II — quadratics, rational expressions, radicals

1_q1:
  problem: x^2 - 7x + 10 = 0
  expected:
    - (x-5)(x-2)=0
    - x=5, x=2
  full_credit_requirements:
    - valid factorization or equivalent solve path
    - both solutions present

2_q2:
  problem: x^2 + 6x - 7 = 0
  expected:
    - factors: (x+7)(x-1)=0
    - x=-7, x=1
  full_credit_requirements:
    - valid method
    - both solutions correct

3_q3:
  problem: (x^2 - 4)/(x^2 - x - 2)
  expected:
    - numerator: (x-2)(x+2)
    - denominator: (x-2)(x+1)
    - restrictions: x ≠ 2, x ≠ -1
    - simplified result: (x+2)/(x+1)
  full_credit_requirements:
    - restrictions listed from the original denominator
    - simplified form correct
  common_error_flags:
    - forgot one restriction
    - canceled before writing restrictions

4_q4:
  problem: 4/x = 12/(x+2)
  expected:
    - restrictions: x ≠ 0, x ≠ -2
    - 4(x+2)=12x
    - 4x+8=12x
    - 8=8x
    - x=1
    - x=1 is valid
  full_credit_requirements:
    - restrictions shown
    - x=1 obtained
    - no invalid value accepted

5_q5:
  problem: 81^(3/4)
  expected:
    - 81^(1/4)=3
    - 81^(3/4)=3^3=27
  full_credit_requirements:
    - final answer 27
    - some root/power logic visible

6_q6:
  problem: sqrt(x+1)=5
  expected:
    - x+1=25
    - x=24
    - check: sqrt(25)=5
  full_credit_requirements:
    - x=24
    - check shown or clearly implied
  common_error_flags:
    - forgot the check
    - arithmetic slip to x=26 or x=20

scoring_suggestion:
- 6/6 correct with sufficient work = 100
- 5/6 correct with sufficient work = 83
- 4/6 correct with sufficient work = 67
- below that = correction pass recommended
- if the work is mostly correct but too thin to verify, use DEFERRED rather than guessing

feedback_templates:
- strong:
  - "Work is clear and verifiable. One or two quick spots to tighten, but this is checkable."
- partial:
  - "You may have the right idea, but I still need more shown steps to verify this honestly."
- restriction_issue:
  - "The algebra may simplify correctly, but the original restriction set still has to be shown."
- radical_issue:
  - "After squaring, the result must be checked back in the original equation."

gradebook_write_template:
- course_id: COURSE.Math.Algebra2.11
- title: Algebra 2 Block 5 — Day 132 Mixed Review
- entry_type: ASSIGNMENT
- grading_basis: objective
- status: FINAL when evidence is sufficient
- notes:
  - include misses by problem number
  - include whether a correction pass was assigned

notes:
- This key is for verification and completion control, not answer-supply during student mode.
- School should use this to prevent false completion when work is missing or too thin.
