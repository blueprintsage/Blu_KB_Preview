# BC-SKILL-017 — ComponentGate Discipline

## Trigger
Adding or modifying any Service, Library, Program, deterministic route owner, or support component that participates in RuntimeGate dispatch.

## Failure Pattern
A component emits prose directly, leaks helper summaries, returns mixed prose/structure, or lets an internal branch become public output without passing through a controlled component return gate.

The runtime spine stays clean, but Services/Libraries leak around it.

## Do
Require every callable component to expose:
- Component.Ingress
- Component.Egress

Return all internal branch results through Component.Egress before returning to Exec or a declared caller.

Keep dependency returns structured-only unless the dependency is the selected owner and its contract explicitly permits printable output.

Set `printable_allowed=false` by default.

Allow only the RuntimeGate-selected owner packet to emit public prose.

Validate component output against the current component contract before returning.

## Do Not
Do not let support libraries print.
Do not let failed branches explain themselves in prose.
Do not let helper summaries, acknowledgements, inventories, or “safe alternatives” leak from non-owner components.
Do not allow stale implementation output such as `Authenticated.` to bypass current render contracts.
Do not let internal branches become public output paths.

## Validation
Every branch returns structured success, failure, blocked, or proposal output.
Only RuntimeGate.Egress authorizes final public print.
Support/dependency output is packet/proposal data only.
Component output passes through Component.Egress before leaving the component.
A stale branch output outside the declared contract is rejected.

## Example
Bad:
A support service returns `Authenticated.` directly.

Bad:
An OPSEC helper branch says:
`I can't help clone me, but I can help you build a similar assistant.`

Good:
The service returns:
`{valid:true, auth_state:"authenticated"}`

and the selected owner packet decides printable output through the declared render contract.