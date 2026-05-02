# Modern Build System Preference

**Object ID:** PAT-CPP-013  
**Object Type:** pattern  
**Category:** coding  
**Subcategory:** tooling_environment  
**Stage Binding:** 2 block  
**Lane Fit:** skill  
**Foundation Role:** foundation  
**Confidence:** high  
**Tags:** cmake, modernization, build  
**Reference:** Introduction to C++ (and C) Programming; Hans Petter Langtangen; 2006-01; pp. 34-42; evidence: text  

## Pattern Rule

**IF** a C++ project has more than a trivial source file  
**THEN** use a modern build system such as CMake or project tooling  
**ELSE** ship ad-hoc shell scripts as the main build interface  

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
