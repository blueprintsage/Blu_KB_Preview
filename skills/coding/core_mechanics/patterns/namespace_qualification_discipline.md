# Namespace Qualification Discipline

**Object ID:** PAT-CPP-044  
**Object Type:** pattern  
**Category:** coding  
**Subcategory:** core_mechanics  
**Stage Binding:** 1 skeleton  
**Lane Fit:** skill  
**Foundation Role:** foundation  
**Confidence:** high  
**Tags:** namespaces, cpp, style  
**Reference:** Introduction to C++ (and C) Programming; Hans Petter Langtangen; 2006-01; p. 48; evidence: text  

## Pattern Rule

**IF** using standard library names  
**THEN** qualify names or use scoped using declarations  
**ELSE** dump using namespace std into broad headers  

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
