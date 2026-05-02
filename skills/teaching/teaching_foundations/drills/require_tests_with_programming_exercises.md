# Require Tests With Programming Exercises

**Object ID:** DRL-CPP-032  
**Object Type:** drill  
**Category:** coding  
**Subcategory:** teaching/teaching_foundations  
**Stage Binding:** 3 rough  
**Lane Fit:** skill  
**Foundation Role:** specialization  
**Confidence:** high  
**Tags:** teaching, cpp, testing, exercises  
**Reference:** Introduction to C++ (and C) Programming; Hans Petter Langtangen; 2006-01; pp.103-115; evidence: text  

## Practice Task

Convert a programming exercise into a task that includes at least one visible correctness check.

## Target Skill

Teaching programming through executable proof instead of answer-shaped code.

## Setup

Use a small C++ exercise, pseudocode exercise, or language-neutral programming prompt.

## Instructions

1. State what the learner must build.
2. Add one normal input, one edge input, and one failure or misuse case.
3. Define what output, trace, assertion, or timing result proves the exercise was completed.
4. Mark any legacy syntax as mechanics-only if the exercise uses old material.

## Success Check

- The exercise cannot be completed by prose alone.
- The test or proof is visible to the learner.
- The proof checks behavior, not just compilation.

## Common Failures

- Asking for code with no run condition.
- Treating a lecture example as understood without modification.
- Letting dated syntax become the lesson.

## Notes

This drill was merged as a distinct practice object after duplicate lecture-level material was rejected or absorbed.

## Modernization

- Use a current compiler/toolchain and modern C++ defaults unless the exercise is explicitly about legacy mechanics.

## Absorbed Variants

- PPP variant: pair every drill/exercise with visible run evidence, then later elevate the habit into regression, unit, system, and class tests.
