# BC-SKILL-001 — Runtime Spine Purity

## Trigger

Use when modifying `03_Exec.md`, RuntimeGate, scheduler, egress, trace routing, or any route that tempts feature logic back into Exec.

## Failure Pattern

Exec contains feature behavior, render logic, support phases, service bodies, Program bodies, or library internals. The runtime becomes scheduler + firewall + business logic again.

## Do

1. Keep Exec limited to RuntimeGate.Ingress, Exec.Scheduler, RuntimeGate.Egress, packet validation, route lock metadata, trace handoff, state commit boundary, and fail-closed output.
2. Move feature behavior into a self-contained Program, service, or library.
3. Represent Exec routes as owner selection and packet contracts, not implementation bodies.
4. Treat any `EXEC.<feature>` owner as suspect unless it is a true spine function.
5. Add a route trace proving Exec selected exactly one owner and did not render feature output itself.

## Do Not

- Do not patch feature bugs by adding behavior to Exec.
- Do not leave duplicate owner names such as `ExecMood` when the feature has a service owner.
- Do not let support registries, mood/humor/greeting logic, or command bodies live in Exec.
- Do not make Exec big again.

## Validation

- `03_Exec.md` contains spine mechanics only.
- Feature output is produced by the selected owner packet and authorized by Egress.
- `/echotrace all` proves Ingress, Scheduler, and Egress without feature-specific prose.
- No deterministic output can be produced by ordinary completion or hosted fallback.

## Example

Bad: `/mood show` is implemented by `EXEC.MOOD` inside Exec.

Good: `/mood show` routes through Exec, dispatches `SERVICE.MOOD.001`, and Egress prints the returned terminal-valid packet.
