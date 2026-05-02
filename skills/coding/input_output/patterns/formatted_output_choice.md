# Formatted Output Choice

**Object ID:** PAT-CPP-018  
**Object Type:** pattern  
**Category:** coding  
**Subcategory:** input_output  
**Stage Binding:** 2 block  
**Lane Fit:** skill  
**Foundation Role:** foundation  
**Confidence:** high  
**Tags:** formatting, output, precision  
**Reference:** Introduction to C++ (and C) Programming; Hans Petter Langtangen; 2006-01; pp. 51-54; evidence: text  

## Pattern Rule

**IF** output precision and layout matter  
**THEN** choose one formatting system and keep it consistent  
**ELSE** mix iostream state and printf formatting casually  

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


### Variant: Stream Manipulator Formatting

**Variant Axis:** formatting API  
**Use When:** staying fully inside iostreams  
**IF** iostream output must control precision  
**THEN** use manipulators/local formatting  
**ELSE** avoid persistent global stream-state surprises  

### Variant: std::format Formatting

**Variant Axis:** formatting API  
**Use When:** modern C++ toolchain supports it  
**IF** readable modern formatting is available  
**THEN** prefer std::format/std::print style  
**ELSE** fall back to localized iostream formatting
