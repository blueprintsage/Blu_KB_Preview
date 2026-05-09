# BC-SKILL-018 — Alias Locality Law

## Trigger
Adding aliases, EchoTrace targets, diagnostic labels, route names, chain names, or component shorthand references.

## Failure Pattern
Aliases are placed in detached registries away from their owning component, creating duplicate alias truth, stale trace routing, registry drift, or mismatched ownership metadata.

## Do
Declare aliases on the owning component block.
Treat alias metadata as ownership metadata.
Resolve EchoTrace aliases from component declarations.
Keep alias truth local to the component that owns the behavior.
Fail validation on duplicate aliases.

Allow runtime lookup caches only as derived data, never as authoritative source truth.

## Do Not
Do not create detached Component Alias Registries.
Do not let aliases float separately from owner blocks.
Do not maintain parallel alias truth.
Do not trace an alias unless its owner declares it locally.
Do not update alias mappings in multiple locations.

## Validation
`/echotrace Auth` resolves from the owning component declaration.
Duplicate aliases fail validation.
Removing a detached registry does not break trace resolution.
No detached registry is required to understand alias ownership.
The owning component remains the source of truth for its alias.

## Example
Bad:
A global alias table declares:
`Auth -> SERVICE.AUTH.001`

while the component itself contains no alias metadata.

Good:
`SERVICE.AUTH.001` declares:

`alias: Auth`

inside its own component block.