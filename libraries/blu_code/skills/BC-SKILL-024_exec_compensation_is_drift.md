# BC-SKILL-024 — Exec Compensation Is Drift

## Trigger
Use when a Service, Library, Program, or Command leaks stale prose, bad render output, missing closure, or invalid terminal packets.

## Failure Pattern
Exec is patched to reject, repair, reinterpret, or duplicate the owner’s business logic. This makes Exec bigger and leaves the leaking Component insufficiently closed.

## Do
1. Fix closure inside the owning Component first.
2. Add or repair Component.Ingress and Component.Egress.
3. Add exact_return inside exact-render owners.
4. Add Component-level Law guards when drift risk exists.
5. Let EchoTrace observe the chain instead of making Exec compensate.

## Do Not
- Do not move owner-specific render contracts into RuntimeGate.Egress.
- Do not make Exec a semantic repair layer.
- Do not patch Auth, Mood, Memory, or Program business logic into Exec.
- Do not widen Exec unless the failure cannot be closed anywhere else.

## Validation
- Exec remains limited to Ingress, Scheduler, Egress, route lock, packet validation, and fail-closed authorization.
- Owner-specific strings live in the owner Component.
- Component.Egress blocks branch-local prose.
- EchoTrace can show the owner closure path.

## Example
Bad: Put Auth exact success strings and forbidden Auth prose in Exec Egress.
Good: Put Auth exact_render_contract and exact_return inside `SERVICE.AUTH.001`; Exec validates only the terminal packet contract.