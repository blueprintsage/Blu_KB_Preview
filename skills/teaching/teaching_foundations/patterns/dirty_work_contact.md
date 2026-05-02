# Dirty Work Contact

**Object ID:** PAT-CPP-050  
**Object Type:** pattern  
**Category:** teaching  
**Subcategory:** teaching_foundations  
**Stage Binding:** 1 skeleton  
**Lane Fit:** skill  
**Foundation Role:** foundation  
**Confidence:** high  
**Tags:** teaching, low_level, practice  
**Reference:** Introduction to C++ (and C) Programming; Hans Petter Langtangen; 2006-01; p. 6; evidence: text  

## Pattern Rule

**IF** a skill has low-level hidden mechanics  
**THEN** let the learner touch those mechanics safely  
**ELSE** hide all details and leave no mental model  

## Do

- State the condition before choosing the method.
- Keep the smallest correct implementation path.
- Preserve source lesson while updating stale mechanics.

## Don't

- Do not copy dated syntax blindly.
- Do not let language-specific detail override the general skill.

## Checklist

- Is the condition explicit?
- Is the action current for C++?
- Is the fallback safe?

## Notes

Extracted as a reusable programming pattern.

## Modernization

- Replace dated C++98/C APIs with current C++ idioms when the lesson is about production coding.
