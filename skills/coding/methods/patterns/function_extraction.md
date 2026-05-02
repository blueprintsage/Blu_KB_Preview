# Function Extraction

**Object ID:** PAT-CPP-034  
**Object Type:** pattern  
**Category:** coding  
**Subcategory:** methods  
**Stage Binding:** 2 block  
**Lane Fit:** skill  
**Foundation Role:** foundation  
**Confidence:** high  
**Tags:** functions, modularity, reuse  
**Reference:** Introduction to C++ (and C) Programming; Hans Petter Langtangen; 2006-01; pp. 88-92; evidence: text  

## Pattern Rule

**IF** a code block represents a reusable step  
**THEN** extract it into a named function with explicit parameters  
**ELSE** copy/paste the block into each example  

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
