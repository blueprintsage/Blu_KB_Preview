# Reference Mutation Drill

**Object ID:** DRL-CPP-012  
**Object Type:** drill  
**Category:** coding  
**Subcategory:** core_mechanics  
**Stage Binding:** 2 block  
**Lane Fit:** skill  
**Foundation Role:** specialization  
**Confidence:** high  
**Tags:** references, const, functions  
**Reference:** Introduction to C++ (and C) Programming; Hans Petter Langtangen; 2006-01; pp.88-91; evidence: text  

## Practice Task

Implement one function using T& to mutate a caller variable and another using const T& to read only.

## Target Skill

Reference intent.

## Setup

Use a small local C++ project and one source file.

## Instructions

1. Write mutate(int&).
2. Write inspect(const vector<int>&).
3. Try illegal mutation inside const function.
4. Explain compiler error.

## Success Check

- Mutation happens only where intended.
- Const prevents accidental write.

## Common Failures

- Passing large objects by value.
- Using non-const reference for read-only input.

## Notes

Keep the drill short, repeatable, and measurable.

## Modernization

- Use current compiler/toolchain and modern C++ defaults.
