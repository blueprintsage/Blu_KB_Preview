# C Pointer InOut Variant

**Object ID:** PAT-CPP-035  
**Object Type:** pattern  
**Category:** coding  
**Subcategory:** language_contexts/c  
**Stage Binding:** 2 block  
**Lane Fit:** skill  
**Foundation Role:** foundation  
**Confidence:** high  
**Tags:** c, pointers, functions  
**Reference:** Introduction to C++ (and C) Programming; Hans Petter Langtangen; 2006-01; pp. 89, 92-94; evidence: text  

## Pattern Rule

**IF** a C function must mutate caller data  
**THEN** pass an address and dereference inside  
**ELSE** pretend C has references  

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
