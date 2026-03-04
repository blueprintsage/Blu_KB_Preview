# MODERNIZE Overlay — C# Programming Yellow Book (7th ed., 2015)
date: 2026-03-04
scope: additive overlay (no base rewrites)

## 1) What changed since 2015 (high level)
The book targets the pre-.NET Core era mindset. Today, most new C# work is done on **.NET (Core lineage)** with SDK-style projects, `dotnet` CLI, modern language features, and cross-platform tooling.

## 2) Recommended “modern default” stack (2026)
- Target runtime: **.NET 10 (LTS)** for new learning/projects, unless you must match an older environment.
- Language: **C# 14** (default with .NET 10 toolchain).
- Tooling: `dotnet` CLI + Visual Studio / VS Code.

## 3) Project & tooling updates (what to do instead of 2015 steps)
### 3.1 Create / build / run
- Create: `dotnet new console -n HelloCSharp`
- Run: `dotnet run`
- Test: `dotnet new xunit` (or MSTest/NUnit)

### 3.2 SDK-style csproj (key differences)
Modern projects are SDK-style:
- fewer explicit file includes
- `PackageReference` for NuGet
- multi-targeting via `TargetFrameworks`

### 3.3 Namespaces and “boilerplate”
Consider modern defaults when you see lots of scaffolding:
- file-scoped namespaces (`namespace X;`)
- global using directives
- top-level statements (small console apps)

## 4) Language features to add to your toolbox (mapped to book topics)
### 4.1 Safer null handling (biggest real-world upgrade)
- Enable nullable reference types: `<Nullable>enable</Nullable>`
- Learn: `string?` vs `string`, null-forgiving `!`, flow analysis warnings.

### 4.2 Records for “data objects”
When the book builds simple classes to hold data, also learn:
- `record` / `record struct` for immutable-by-default models.

### 4.3 Pattern matching (better switch/if)
Where the book uses long `if` chains or `switch` on ints/strings:
- `switch` expressions
- type/property patterns
- `when` guards

### 4.4 Modern async
The book’s async coverage (if any) predates best practices:
- prefer `async Task` over `async void`
- avoid `.Result`/`.Wait()` (deadlocks)
- use `CancellationToken`

### 4.5 Collections quality-of-life
Newer syntax can simplify many examples:
- collection expressions (when available in your toolchain)
- `Span<T>` / `ReadOnlySpan<T>` for perf-sensitive code (advanced)

## 5) Framework-level changes you should know
### 5.1 .NET Framework vs modern .NET
- .NET Framework is Windows-only and largely “maintenance mode” for new apps.
- Modern .NET is the default for new console/web/services cross-platform.

### 5.2 ASP.NET Core
If the book references older web stacks, translate mental model to ASP.NET Core:
- minimal hosting model (Program.cs)
- built-in DI container

## 6) “Modernize as you read” checklist
When you hit an example, ask:
1) Can I build this as a `dotnet new` project?
2) Should I turn on nullable reference types?
3) Would a `record` better express this data?
4) Can I rewrite the conditional with pattern matching?
5) Is there async work that needs cancellation?

## 7) Optional: modernization exercises (5)
1) Take a book class with fields + constructor; convert to a `record` and rerun.
2) Enable nullable and fix warnings without using `!` except as last resort.
3) Rewrite one long `switch` statement as a `switch` expression + patterns.
4) Add `CancellationToken` to an async method chain and propagate it.
5) Convert a small solution to multi-target: `net10.0;net8.0` (learn compatibility).

## Sources (for the reader)
- Microsoft docs: .NET downloads + C# “What’s new” pages + language versioning.
