# BC-SKILL-012 — Preserve Proven Baseline

## Trigger

Use when continuing from a known-good archive, burn-in result, release candidate, or rollback point.

## Failure Pattern

A patch stacks onto a contaminated build, stale baseline, or long-chat drift and reintroduces old behavior.

## Do

1. Identify the known-good baseline before editing.
2. Do not stack on a contaminated build unless the user explicitly chooses it.
3. Preserve baseline hash/copy when packaging.
4. Patch only the named target files unless the failing proof forces scope expansion.
5. Record changed and unchanged files in the validation report.

## Do Not

- Do not continue from memory when a source archive exists.
- Do not assume latest means best.
- Do not silently widen from command/help cleanup into runtime rewrites.
- Do not claim rollback/rebuild without artifact proof.

## Validation

- Manifest names baseline archive and changed files.
- Unchanged protected files have matching hashes.
- Validation report states static, probe, and live status separately.
- Contaminated builds are not used as parents without explicit approval.

## Example

Good: Rebuild command/help cleanup from r9.3.35 instead of stacking onto contaminated r9.3.36.
