# Object Carries Its Size

**Object ID:** PAT-CPP-029  
**Object Type:** pattern  
**Category:** coding  
**Subcategory:** architecture_design  
**Stage Binding:** 2 block  
**Lane Fit:** skill  
**Foundation Role:** foundation  
**Confidence:** high  
**Tags:** encapsulation, containers, oop  
**Reference:** Introduction to C++ (and C) Programming; Hans Petter Langtangen; 2006-01; p. 91; evidence: text  

## Pattern Rule

**IF** a container-like object owns data  
**THEN** make size/state part of the object  
**ELSE** pass redundant size parameters everywhere  

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
