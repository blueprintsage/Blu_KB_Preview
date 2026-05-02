# Small Program Return Code

**Object ID:** PAT-CPP-083  
**Object Type:** pattern  
**Category:** coding  
**Subcategory:** testing_validation  
**Stage Binding:** 1 skeleton  
**Lane Fit:** skill  
**Foundation Role:** foundation  
**Confidence:** high  
**Tags:** main, status, programs  
**Reference:** Introduction to C++ (and C) Programming; Hans Petter Langtangen; 2006-01; p. 29; evidence: text  

## Pattern Rule

**IF** main finishes successfully  
**THEN** return zero or allow normal success semantics  
**ELSE** return arbitrary failure codes on success  

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
