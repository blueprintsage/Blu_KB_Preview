# Operator Temporary Cost Drill

**Object ID:** DRL-CPP-033  
**Object Type:** drill  
**Category:** coding  
**Subcategory:** memory_performance  
**Stage Binding:** 3 rough  
**Lane Fit:** skill  
**Foundation Role:** specialization  
**Confidence:** high  
**Tags:** operators, performance, temporaries, numeric_types  
**Reference:** Introduction to C++ (and C) Programming; Hans Petter Langtangen; 2006-01; pp.145-205, 244-276; evidence: text  

## Practice Task

Inspect a small numeric class and identify where overloaded operators create temporary objects.

## Target Skill

Seeing cost boundaries behind clean arithmetic syntax.

## Setup

Use a minimal vector, complex-number, or matrix class with overloaded arithmetic.

## Instructions

1. Write or inspect two chained arithmetic expressions.
2. Mark every temporary object that would be created by the naïve implementation.
3. Rewrite one operation using a compound operation or expression-aware API.
4. Explain which version is clearer and which version is cheaper.

## Success Check

- Temporary objects are named or diagrammed.
- Clarity and cost are discussed separately.
- Optimization does not hide the original mathematical intent.

## Common Failures

- Assuming operator syntax is automatically cheap.
- Removing readable operators before measuring or reasoning about cost.
- Confusing natural operator meaning with implementation efficiency.

## Notes

This drill was merged as a distinct practice object after duplicate lecture-level material was rejected or absorbed.

## Modernization

- Use a current compiler/toolchain and modern C++ defaults unless the exercise is explicitly about legacy mechanics.
