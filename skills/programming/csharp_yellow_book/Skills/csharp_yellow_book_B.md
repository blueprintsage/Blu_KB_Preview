---
title: "C# Programming Yellow Book (Rob Miles, 7th ed., 2015) — Skills (Lane B)"
source: "C# Programming Yellow Book (Rob Miles, 7th ed., 2015)"
run_date: 2026-03-04
dated: YES
dated_reason: "2015 edition (>=8 years old as of 2026-03-04)"
modernize_eligible: YES
---

# Skills (Lane B) — Enforceable Patterns

## Pattern Set
### CSYB-PAT-001
- IF: IF you name identifiers (variables, methods, classes).
- THEN: THEN use clear, intention-revealing names and keep naming consistent within a scope.
- CHECK: CHECK a new reader can infer purpose without extra comments.
- FAIL: FAIL rename to reflect domain meaning; avoid single-letter names except short loops.
- REF: REF Yellow Book: Creating Programs

### CSYB-PAT-002
- IF: IF you write a console program that needs input.
- THEN: THEN prompt the user before reading input, and validate/parse the input explicitly.
- CHECK: CHECK every ReadLine has a prior prompt and parse path (TryParse where possible).
- FAIL: FAIL add a prompt + TryParse + retry/exit path.
- REF: REF Yellow Book: Simple Data Processing

### CSYB-PAT-003
- IF: IF you convert user input to a number.
- THEN: THEN prefer TryParse over Parse to avoid exceptions on bad input.
- CHECK: CHECK invalid input does not crash; program handles failure case.
- FAIL: FAIL replace Parse with TryParse and implement failure branch.
- REF: REF Yellow Book: Simple Data Processing

### CSYB-PAT-004
- IF: IF a calculation uses constants (rates, thresholds).
- THEN: THEN define them as named constants (const) near the top of scope.
- CHECK: CHECK magic numbers are replaced with named constants.
- FAIL: FAIL introduce consts and update expression.
- REF: REF Yellow Book: Simple Data Processing

### CSYB-PAT-005
- IF: IF your code repeats a block 2+ times with small differences.
- THEN: THEN extract a method and pass differences as parameters.
- CHECK: CHECK duplication reduced; method has a single clear purpose.
- FAIL: FAIL refactor into method; rename parameters to meaning.
- REF: REF Yellow Book: Creating Programs

### CSYB-PAT-006
- IF: IF you choose between multiple cases on a single value.
- THEN: THEN use switch when it improves readability over chained if/else.
- CHECK: CHECK cases are exhaustive or include default for unexpected values.
- FAIL: FAIL add default or convert to if/else when conditions are complex.
- REF: REF Yellow Book: Creating Programs

### CSYB-PAT-007
- IF: IF you use a loop with a known iteration count.
- THEN: THEN prefer for; IF unknown/until condition, use while.
- CHECK: CHECK loop type matches intent; termination condition is obvious.
- FAIL: FAIL rewrite loop to match intent; add guard against infinite loop.
- REF: REF Yellow Book: Creating Programs

### CSYB-PAT-008
- IF: IF you write a loop.
- THEN: THEN ensure loop termination is guaranteed by state change inside the loop.
- CHECK: CHECK at least one variable in condition changes every iteration or loop breaks.
- FAIL: FAIL add state update or explicit break with documented condition.
- REF: REF Yellow Book: Creating Programs

### CSYB-PAT-009
- IF: IF you need to stop processing early on invalid state.
- THEN: THEN use guard clauses (early returns) at the top of the method.
- CHECK: CHECK method reads top-down: validate → work → return.
- FAIL: FAIL refactor nested if blocks into guards.
- REF: REF Yellow Book: Creating Solutions

### CSYB-PAT-010
- IF: IF a method performs more than one conceptually distinct task.
- THEN: THEN split it into smaller methods with single responsibilities.
- CHECK: CHECK each method can be described in one sentence.
- FAIL: FAIL decompose and write small unit-like checks (even informally).
- REF: REF Yellow Book: Creating Solutions

### CSYB-PAT-011
- IF: IF you store a collection of same-typed items.
- THEN: THEN use an array for fixed size; use List<T> for dynamic size.
- CHECK: CHECK resizing needs are met without manual copying.
- FAIL: FAIL migrate to List<T> when size changes during runtime.
- REF: REF Yellow Book: Creating Programs

### CSYB-PAT-012
- IF: IF you index into an array/list.
- THEN: THEN validate bounds before access when index can vary.
- CHECK: CHECK no path can produce index <0 or >=Count/Length.
- FAIL: FAIL add bounds checks or constrain index creation.
- REF: REF Yellow Book: Creating Programs

### CSYB-PAT-013
- IF: IF you build strings repeatedly in a loop.
- THEN: THEN use StringBuilder for performance and clarity.
- CHECK: CHECK concatenation in loops is eliminated for large/unknown iteration counts.
- FAIL: FAIL replace with StringBuilder.Append.
- REF: REF Yellow Book: Advanced Programming

### CSYB-PAT-014
- IF: IF you define a class.
- THEN: THEN keep fields private and expose behavior via methods/properties.
- CHECK: CHECK callers cannot mutate internal state directly without validation.
- FAIL: FAIL encapsulate fields; add properties with validation.
- REF: REF Yellow Book: Creating Solutions

### CSYB-PAT-015
- IF: IF a class has invariants (rules that must stay true).
- THEN: THEN enforce them in constructors and property setters.
- CHECK: CHECK invalid states cannot be constructed or assigned.
- FAIL: FAIL add validation + exceptions or rejection logic.
- REF: REF Yellow Book: Creating Solutions

### CSYB-PAT-016
- IF: IF you use inheritance.
- THEN: THEN model 'is-a' relationships; otherwise prefer composition.
- CHECK: CHECK subclass can substitute for base without surprises (LSP-ish).
- FAIL: FAIL refactor to composition when behavior diverges.
- REF: REF Yellow Book: Advanced Programming

### CSYB-PAT-017
- IF: IF you override a virtual method.
- THEN: THEN preserve base contract and document any stronger preconditions.
- CHECK: CHECK overridden behavior matches caller expectations.
- FAIL: FAIL revise override or avoid override; expose new method instead.
- REF: REF Yellow Book: Advanced Programming

### CSYB-PAT-018
- IF: IF you handle errors from user input or external systems.
- THEN: THEN handle predictable failures without exceptions; reserve exceptions for truly exceptional cases.
- CHECK: CHECK common bad input doesn’t throw.
- FAIL: FAIL use TryParse/validation; keep try/catch narrow.
- REF: REF Yellow Book: Creating Solutions

### CSYB-PAT-019
- IF: IF you catch an exception.
- THEN: THEN catch the most specific exception type you can and include a recovery/exit plan.
- CHECK: CHECK catch blocks are specific; no empty catch; message is useful.
- FAIL: FAIL replace catch(Exception) with specific types or rethrow with context.
- REF: REF Yellow Book: Advanced Programming

### CSYB-PAT-020
- IF: IF you use try/catch.
- THEN: THEN keep the try block minimal (only the statements that may throw).
- CHECK: CHECK try does not wrap large unrelated logic.
- FAIL: FAIL refactor into smaller try regions; move non-throwing code out.
- REF: REF Yellow Book: Advanced Programming

### CSYB-PAT-021
- IF: IF you write output.
- THEN: THEN format for the reader: labels, units, and consistent decimal formatting.
- CHECK: CHECK outputs are self-explanatory without reading source.
- FAIL: FAIL add labels/units; use format strings.
- REF: REF Yellow Book: Simple Data Processing

### CSYB-PAT-022
- IF: IF you change code.
- THEN: THEN compile early and often to catch errors while the change is small.
- CHECK: CHECK you can point to frequent compile/test points.
- FAIL: FAIL break work into smaller edits and compile between them.
- REF: REF Yellow Book: Welcome

### CSYB-PAT-023
- IF: IF you are stuck debugging for ~30 minutes.
- THEN: THEN stop, simplify, and seek help or change tactics (small reproduction).
- CHECK: CHECK you can reproduce the problem in the smallest code sample.
- FAIL: FAIL create minimal repro; rubber-duck the steps.
- REF: REF Yellow Book: Welcome

### CSYB-PAT-024
- IF: IF you need to understand why a value is wrong.
- THEN: THEN use the debugger (breakpoints/watch) before adding print statements.
- CHECK: CHECK you can observe variable states at the failure point.
- FAIL: FAIL set breakpoint at failure; step; inspect state.
- REF: REF Yellow Book: Creating Solutions

### CSYB-PAT-025
- IF: IF you do use print debugging.
- THEN: THEN print labels + values and remove/guard debug output before final.
- CHECK: CHECK debug prints are searchable and not left in production output.
- FAIL: FAIL wrap in DEBUG conditional or delete before submit.
- REF: REF Yellow Book: Creating Solutions

### CSYB-PAT-026
- IF: IF you write a method signature.
- THEN: THEN choose parameter types that prevent invalid states (e.g., int not string).
- CHECK: CHECK caller cannot pass unvalidated raw data by accident.
- FAIL: FAIL change signature to accept validated types or add parsing layer.
- REF: REF Yellow Book: Creating Programs

### CSYB-PAT-027
- IF: IF you return a value from a method.
- THEN: THEN define what the return means and how errors are signaled (exception vs bool).
- CHECK: CHECK callers handle failure paths explicitly.
- FAIL: FAIL introduce TryX pattern returning bool + out value.
- REF: REF Yellow Book: Creating Solutions

### CSYB-PAT-028
- IF: IF you store a 'no value' possibility.
- THEN: THEN use nullable types or explicit option patterns; avoid sentinel magic values.
- CHECK: CHECK absence is representable without colliding with valid values.
- FAIL: FAIL use nullable or add explicit 'hasValue' flag.
- REF: REF Yellow Book: Advanced Programming

### CSYB-PAT-029
- IF: IF you comment code.
- THEN: THEN comment intent and constraints, not what the code trivially does.
- CHECK: CHECK comments add information not obvious from code.
- FAIL: FAIL rewrite comment to explain why/assumptions.
- REF: REF Yellow Book: Creating Programs

### CSYB-PAT-030
- IF: IF you create a new project/solution.
- THEN: THEN keep one entry point per executable and organize code into namespaces by feature.
- CHECK: CHECK Program.cs/Main is clear; namespaces are not random.
- FAIL: FAIL reorganize folders/namespaces; rename projects to match purpose.
- REF: REF Yellow Book: Creating Programs

### CSYB-PAT-031
- IF: IF you use floating point for money.
- THEN: THEN use decimal for currency calculations.
- CHECK: CHECK money values use decimal and are rounded appropriately.
- FAIL: FAIL migrate double to decimal; adjust literals with m suffix.
- REF: REF Yellow Book: Simple Data Processing

### CSYB-PAT-032
- IF: IF you compare floating point numbers.
- THEN: THEN compare within a tolerance, not equality.
- CHECK: CHECK comparisons avoid == for doubles unless deliberate.
- FAIL: FAIL introduce epsilon tolerance check.
- REF: REF Yellow Book: Advanced Programming

### CSYB-PAT-033
- IF: IF you use boolean flags.
- THEN: THEN name them as predicates (is/has/can) and avoid double negatives.
- CHECK: CHECK booleans read cleanly in conditions.
- FAIL: FAIL rename flags; invert logic to eliminate !! patterns.
- REF: REF Yellow Book: Creating Programs

### CSYB-PAT-034
- IF: IF you design an API for others to use.
- THEN: THEN prefer small, safe defaults and make unsafe operations explicit.
- CHECK: CHECK typical use-case is short and hard to misuse.
- FAIL: FAIL redesign with safer overloads/defaults.
- REF: REF Yellow Book: Creating Solutions

### CSYB-PAT-035
- IF: IF you need repeated structured data.
- THEN: THEN create a class/struct rather than parallel arrays.
- CHECK: CHECK related fields travel together and are updated together.
- FAIL: FAIL refactor into a data type and collection of that type.
- REF: REF Yellow Book: Creating Solutions

### CSYB-PAT-036
- IF: IF you read/write files.
- THEN: THEN use using statements to ensure resources are closed.
- CHECK: CHECK all streams/readers/writers are disposed.
- FAIL: FAIL wrap in using or try/finally dispose.
- REF: REF Yellow Book: Advanced Programming

### CSYB-PAT-037
- IF: IF you handle text files.
- THEN: THEN specify encoding deliberately when it matters; otherwise rely on UTF-8 defaults consciously.
- CHECK: CHECK encoding assumptions are documented.
- FAIL: FAIL set encoding explicitly where interoperability matters.
- REF: REF Yellow Book: Advanced Programming

### CSYB-PAT-038
- IF: IF you write a program that could crash.
- THEN: THEN define the failure mode: show message + exit code, or retry safely.
- CHECK: CHECK user sees actionable error; program ends predictably.
- FAIL: FAIL add top-level handler and clear error messages.
- REF: REF Yellow Book: Creating Solutions

### CSYB-PAT-039
- IF: IF you build a program incrementally.
- THEN: THEN make it work end-to-end with a tiny feature first, then expand.
- CHECK: CHECK there is always a working version.
- FAIL: FAIL slice features; implement smallest vertical path.
- REF: REF Yellow Book: Welcome

### CSYB-PAT-040
- IF: IF you finish a feature.
- THEN: THEN run a small test checklist: normal case, edge case, and bad input.
- CHECK: CHECK you can name at least 3 test inputs and expected outputs.
- FAIL: FAIL add tests or manual checklist before moving on.
- REF: REF Yellow Book: Creating Solutions
