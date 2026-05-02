# Generic Stream Interface

**Object ID:** PAT-CPP-016  
**Object Type:** pattern  
**Category:** coding  
**Subcategory:** architecture_design  
**Stage Binding:** 2 block  
**Lane Fit:** skill  
**Foundation Role:** foundation  
**Confidence:** high  
**Tags:** interfaces, streams, abstraction  
**Reference:** Introduction to C++ (and C) Programming; Hans Petter Langtangen; 2006-01; p. 55; evidence: text  

## Pattern Rule

**IF** the same operation should work for console and files  
**THEN** accept istream/ostream references  
**ELSE** duplicate print/scan functions per medium  

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
