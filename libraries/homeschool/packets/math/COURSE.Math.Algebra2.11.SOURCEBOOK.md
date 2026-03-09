# COURSE.Math.Algebra2.11.SOURCEBOOK

course_id: COURSE.Math.Algebra2.11
packet_file: SOURCEBOOK
version: 0.9.0
status: DRAFT
updated: 2026-03-08
packet_mode: HYBRID
grade_level: 11
subject: Math
focus_window: Block 5 (Days 121-150) first-pass build
purpose: Original Blu sourcebook for Algebra 2 instruction where the open spine is weak, thin, or unavailable.

primary_spine:
- CK-12 Interactive Algebra 2
supplemental_spine:
- OpenStax Intermediate Algebra
workflow_source:
- Easy Peasy Algebra 2 daily sequence

runtime_rules:
- Easy Peasy remains the day-order source.
- This sourcebook may teach the day when the linked source is thin, inaccessible, or needs a clearer explanation.
- School remains CHECK_ONLY for student verification lanes.

block_5_focus:
- mixed review and problem solving
- quadratics and roots
- rational expressions and restrictions
- radicals and rational exponents
- exponential and logarithmic reasoning
- cumulative skill repair before end-of-year review

learning_targets:
- solve quadratics by factoring, square roots, completing the square, and quadratic formula
- simplify and solve rational expressions with domain restrictions
- rewrite radicals and rational exponents cleanly
- interpret exponential growth/decay and solve simple exponential equations
- show work clearly enough for CHECK_ONLY verification
- explain restrictions, roots, and solution validity

teaching_principles:
- smallest blocker first
- worked examples before abstraction
- visible restrictions and assumptions
- always separate "allowed operation" from "final answer"
- every solved problem should show why extraneous or invalid answers were rejected

## Block 5 Day Map

days_121_150:
- day_121: quadratic review — factoring and zero-product rule
- day_122: quadratic review — completing the square
- day_123: quadratic review — quadratic formula
- day_124: discriminant and solution types
- day_125: rational expressions — restrictions and simplification
- day_126: rational equations — solving and checking
- day_127: radical expressions — simplify and combine
- day_128: rational exponents ↔ radicals
- day_129: exponential growth and decay basics
- day_130: simple logarithmic meaning and inverse relationships
- day_131: mixed review I — quadratics + restrictions
- day_132: mixed review II — quadratics, rational expressions, radicals
- day_133: mixed review III — exponentials + cumulative repair
- day_134: application day — multi-step equation sorting
- day_135: error analysis day
- day_136: cumulative set A
- day_137: cumulative set B
- day_138: cumulative set C
- day_139: short checkpoint
- day_140: targeted repair
- day_141: mixed review IV
- day_142: mixed review V
- day_143: mixed review VI
- day_144: application set — word/context problems
- day_145: application set — modeling and interpretation
- day_146: review spiral A
- day_147: review spiral B
- day_148: review spiral C
- day_149: block review
- day_150: block mastery check

## Mini-Lesson 1 — Quadratics: four legal solve paths

goal:
- choose a solve path that matches the structure of the equation

solve_paths:
- factoring
- square roots
- completing the square
- quadratic formula

decision_rule:
- use factoring when the trinomial factors cleanly
- use square roots when the equation is already in the form (x-a)^2=b
- use completing the square when structure is close and you want exact control
- use quadratic formula when factoring is ugly or impossible

worked_example_1:
problem: x^2 - 5x + 6 = 0
steps:
- factor: (x-2)(x-3)=0
- set each factor equal to zero
- solutions: x=2, x=3

worked_example_2:
problem: x^2 - 10x + 21 = 0
steps:
- factor: (x-3)(x-7)=0
- solutions: x=3, x=7

worked_example_3:
problem: x^2 + 4x - 1 = 0
steps:
- not friendly to factor over integers
- quadratic formula:
  - a=1, b=4, c=-1
  - x = [-4 ± sqrt(16 - 4(1)(-1))]/2
  - x = [-4 ± sqrt(20)]/2
  - x = -2 ± sqrt(5)

common_mistakes:
- forgetting to set the equation equal to zero first
- dropping the ± when square rooting
- sign errors in the quadratic formula
- claiming a factorization that does not multiply back correctly

## Mini-Lesson 2 — Restrictions in rational expressions

goal:
- simplify or solve without losing the original domain restrictions

rule:
- if a denominator can become zero, that value is restricted even if cancellation happens later

worked_example_4:
problem: (x^2 - 9)/(x^2 - 3x)
steps:
- factor numerator: (x-3)(x+3)
- factor denominator: x(x-3)
- restriction set from original denominator:
  - x ≠ 0
  - x ≠ 3
- simplify to (x+3)/x
- keep original restrictions

worked_example_5:
problem: solve 3/(x-1)=6/(x^2-1)
steps:
- original restrictions:
  - x ≠ 1
  - x ≠ -1
- factor x^2-1=(x-1)(x+1)
- multiply both sides by (x-1)(x+1)
- 3(x+1)=6
- 3x+3=6
- x=1
- reject x=1 because it violates the original restriction
- solution set: no valid solution

common_mistakes:
- canceling before recording restrictions
- accepting a restricted value as a solution
- checking only the simplified equation instead of the original domain

## Mini-Lesson 3 — Radicals and rational exponents

goal:
- translate between forms and simplify carefully

identity_rules:
- a^(1/2) = sqrt(a)
- a^(1/3) = cuberoot(a)
- a^(m/n) = (n-th root of a)^m

worked_example_6:
problem: simplify 16^(3/4)
steps:
- 16^(1/4)=2
- 16^(3/4)=2^3=8

worked_example_7:
problem: simplify sqrt(50)
steps:
- sqrt(50)=sqrt(25·2)=5sqrt(2)

worked_example_8:
problem: solve sqrt(x+5)=7
steps:
- square both sides: x+5=49
- x=44
- check: sqrt(49)=7, valid

common_mistakes:
- forgetting to check after squaring
- treating sqrt(a+b) as sqrt(a)+sqrt(b)
- mishandling rational exponent order

## Mini-Lesson 4 — Exponential reasoning

goal:
- read growth/decay structure and solve simple exponential equations

worked_example_9:
problem: 3(2^x)=24
steps:
- divide by 3: 2^x=8
- x=3

worked_example_10:
problem: y=500(0.9)^t
interpretation:
- initial value is 500
- decay factor is 0.9
- decay rate is 10% per time unit

common_mistakes:
- mixing up growth factor and growth rate
- treating the exponent like ordinary multiplication
- ignoring context language like "per year" or "per month"

## Day 132 Teaching Frame

day_number: 132
lesson_title: Mixed Review II — quadratics, rational expressions, radicals
objective:
- solve a mixed set while showing enough structure for verification
source_type:
- BLU_SOURCEBOOK
recommended_sequence:
1. warm-up — identify the type of each problem
2. solve two quadratics with different methods
3. simplify one rational expression and list restrictions
4. solve one rational equation and reject invalid results
5. simplify one radical/rational exponent expression
6. solve one radical equation and check it
teacher_note:
- this is a verification-heavy day
- School should ask for the worksheet/photo/answers before judging completion

day_132_model_set:
- Q1: Solve x^2 - 7x + 10 = 0
- Q2: Solve x^2 + 6x - 7 = 0
- Q3: Simplify (x^2 - 4)/(x^2 - x - 2) and list restrictions
- Q4: Solve 4/x = 12/(x+2)
- Q5: Simplify 81^(3/4)
- Q6: Solve sqrt(x+1)=5

answer_skeletons:
- Q1 -> factor cleanly
- Q2 -> factor or formula
- Q3 -> factor numerator and denominator, keep original restrictions
- Q4 -> solve after recording restrictions, check original domain
- Q5 -> fourth root then cube
- Q6 -> square both sides and check

notes:
- This is intentionally original material.
- It is aligned to the course shell and the School runtime, not a copy of Easy Peasy text.
