# Numerical Matrix Vector Kernel

**Object ID:** PAT-CPP-032  
**Object Type:** pattern  
**Category:** coding  
**Subcategory:** methods  
**Stage Binding:** 2 block  
**Lane Fit:** skill  
**Foundation Role:** foundation  
**Confidence:** high  
**Tags:** numerics, matrix, loops  
**Reference:** Introduction to C++ (and C) Programming; Hans Petter Langtangen; 2006-01; pp. 68-87; evidence: text  

## Pattern Rule

**IF** implementing b = A*x  
**THEN** separate initialization, computation, and checking  
**ELSE** interleave setup and math until correctness is opaque  

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
