# Numerical Initialization Isolation

**Object ID:** PAT-CPP-096  
**Object Type:** pattern  
**Category:** coding  
**Subcategory:** methods  
**Stage Binding:** 1 skeleton  
**Lane Fit:** skill  
**Foundation Role:** foundation  
**Confidence:** high  
**Tags:** numerics, testing, functions  
**Reference:** Introduction to C++ (and C) Programming; Hans Petter Langtangen; 2006-01; pp. 85-91; evidence: text  

## Pattern Rule

**IF** initializing test matrices/vectors  
**THEN** isolate initialization in a function  
**ELSE** bury test data inside the multiply kernel  

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
