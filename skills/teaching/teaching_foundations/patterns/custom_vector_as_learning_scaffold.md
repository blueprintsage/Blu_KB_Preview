# Custom Vector As Learning Scaffold

**Object ID:** PAT-CPP-107  
**Object Type:** pattern  
**Category:** coding  
**Subcategory:** teaching/teaching_foundations  
**Stage Binding:** 2 block  
**Lane Fit:** skill  
**Foundation Role:** foundation  
**Confidence:** high  
**Tags:** teaching, cpp, containers, scaffold  
**Reference:** Introduction to C++ (and C) Programming; Hans Petter Langtangen; 2006-01; pp.132-243; evidence: text  

## Pattern Rule

**IF** a custom container is used to teach allocation, indexing, operators, or class design  
**THEN** label it as a learning scaffold and point production code toward standard containers  
**ELSE** let students mistake the teaching container for the preferred production abstraction  

## Do

- Keep the rule tied to a concrete programming pressure.
- Prefer modern C++ defaults unless the goal is to expose mechanics.
- Separate the reusable design lesson from dated syntax.

## Don't

- Do not preserve legacy technique as a production recommendation.
- Do not add abstraction before the responsibility boundary is clear.
- Do not copy the source phrasing or examples as content.

## Checklist

- Is the condition explicit?
- Is the modern production form clear?
- Is the educational mechanics form labeled when needed?
- Is the boundary testable?

## Notes

The source uses custom vector and array classes to expose C++ mechanics; this pattern preserves the teaching value while modernizing the recommendation.

## Modernization

- Treat older C/C++ examples as mechanics demonstrations first.
- Prefer standard containers, RAII, type-safe interfaces, current build tooling, and explicit tests for production use.

## Variants


### Variant: Mechanics Lesson

**Variant Axis:** lesson role  
**Use When:** teaching ownership, indexing, or operator overloads  
**IF** the point is to see what a container hides  
**THEN** build the small container with clear limits  
**ELSE** recommend it as general production infrastructure


### Variant: Production Recommendation

**Variant Axis:** lesson role  
**Use When:** solving ordinary storage problems  
**IF** standard containers fit  
**THEN** use standard containers first  
**ELSE** rewrite vector-like storage without a specific reason


## Absorbed Variants

- PPP variant: use the custom vector sequence as a temporary mechanics lab, then explicitly migrate learner guidance back to `std::vector`, RAII, and standard-library vocabulary.
