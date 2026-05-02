# Row-Major Traversal

**Object ID:** PAT-CPP-021  
**Object Type:** pattern  
**Category:** coding  
**Subcategory:** memory_performance  
**Stage Binding:** 3 rough  
**Lane Fit:** skill  
**Foundation Role:** foundation  
**Confidence:** high  
**Tags:** cache, matrix, performance  
**Reference:** Introduction to C++ (and C) Programming; Hans Petter Langtangen; 2006-01; pp. 70-73; evidence: text  

## Pattern Rule

**IF** iterating over row-major C/C++ matrices  
**THEN** vary the last index fastest  
**ELSE** traverse columns as if storage were Fortran-style  

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

## Variants


### Variant: C/C++ Row Major

**Variant Axis:** storage order  
**Use When:** data lives in row-major storage  
**IF** row-major matrix is traversed  
**THEN** make column index the inner loop  
**ELSE** expect cache-unfriendly jumps  

### Variant: Fortran Column Major

**Variant Axis:** storage order  
**Use When:** using Fortran-style or column-major storage  
**IF** column-major matrix is traversed  
**THEN** make row index the inner loop  
**ELSE** expect cache-unfriendly jumps
