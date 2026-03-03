# RELEASE_PROTOCOL_v1

This protocol defines how Blu moves from development builds to Release Candidates (RC) and Releases.

## RC Gate (required)
A change may be labeled **RC** only if all conditions below are met:

1) **SIM TAGS present**
- Any new/changed Program / Generator / Module must define scenario tags so it can be covered by simulations.

2) **SMOKE TESTS present**
- Any new/changed Program / Generator / Module must include at least **3** copy/paste smoke tests with expected outcomes.

3) **INVARIANTS DECLARATION present**
- Declare which invariants are touched: **ART / SCHOOL / TEACH / SKILLFORGE / EXEC**
- Mark change as **breaking** or **non-breaking**.

4) **Simulations pass**
- Run fixed regression seeds first, then randomized sims.
- Record results using `protocols/SIM_REPORT_TEMPLATE_v1.md` and save as `reports/UNRELEASED_SIM_REPORT.md`.

5) **Smoke tests pass**
- Run canonical smoke tests for all affected domains.

6) **CHANGELOG updated**
- Update `CHANGELOG.md` under **Unreleased** with a clear summary.

## Release Gate (required)
A build may be labeled **release** only if:
- RC gate passed
- Version is updated in `VERSION.md`
- Artifacts (kernel capsules + KB) are packaged and archived
