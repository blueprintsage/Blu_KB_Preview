# Separate Compile and Link

**Object ID:** PAT-CPP-011  
**Object Type:** pattern  
**Category:** coding  
**Subcategory:** tooling_environment  
**Stage Binding:** 2 block  
**Lane Fit:** skill  
**Foundation Role:** foundation  
**Confidence:** high  
**Tags:** build, linking, tooling  
**Reference:** Introduction to C++ (and C) Programming; Hans Petter Langtangen; 2006-01; pp. 33, 40-41; evidence: text  

## Pattern Rule

**IF** a build involves multiple translation units or libraries  
**THEN** compile objects first and link after  
**ELSE** hide link errors inside one unexplained command  

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
