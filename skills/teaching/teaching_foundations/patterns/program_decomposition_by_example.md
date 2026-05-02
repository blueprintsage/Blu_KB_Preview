# Program Decomposition By Example

**Object ID:** PAT-CPP-079  
**Object Type:** pattern  
**Category:** teaching  
**Subcategory:** teaching_foundations  
**Stage Binding:** 1 skeleton  
**Lane Fit:** skill  
**Foundation Role:** foundation  
**Confidence:** high  
**Tags:** teaching, code_reading, sequence  
**Reference:** Introduction to C++ (and C) Programming; Hans Petter Langtangen; 2006-01; pp. 24-32, 45-48; evidence: text  

## Pattern Rule

**IF** teaching a complete program  
**THEN** present goal, structure, code, dissection, and variant  
**ELSE** drop the code without a reading path  

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


### Variant: Goal-Structure-Code-Dissection

**Variant Axis:** teaching sequence  
**Use When:** introducing a complete example  
**IF** learners need to understand a program  
**THEN** show goal, structure, code, then dissection  
**ELSE** avoid raw code dumps  

### Variant: Compare-And-Transfer

**Variant Axis:** teaching sequence  
**Use When:** two implementations reveal one concept  
**IF** two languages solve the same task  
**THEN** compare them around one shared idea  
**ELSE** teach them separately
