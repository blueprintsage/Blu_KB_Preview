# Teach Dated Sources With Modern Notes

**Object ID:** PAT-CPP-098  
**Object Type:** pattern  
**Category:** teaching  
**Subcategory:** teaching_foundations  
**Stage Binding:** 1 skeleton  
**Lane Fit:** skill  
**Foundation Role:** foundation  
**Confidence:** high  
**Tags:** teaching, modernization, source_literacy  
**Reference:** Introduction to C++ (and C) Programming; Hans Petter Langtangen; 2006-01; whole PDF; evidence: text  

## Pattern Rule

**IF** a source is old but conceptually strong  
**THEN** teach concept plus modern replacement  
**ELSE** teach dated API as current  

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

## Absorbed Variants

- PPP variant: keep the 2008-era sequence when it teaches fundamentals, but replace obsolete production guidance such as `auto_ptr` or old IDE setup with current C++ defaults.
