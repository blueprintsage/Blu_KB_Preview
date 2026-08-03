# Corpus Failures

status: active
owner: docs/domains/corpus
last_reviewed: 2026-08-01

Approaches that were tried and did not work. This file exists so the same wall is
not hit twice. An abandoned branch with no entry here is a trap left armed.

## 2026-08-01 - Extract Dynamic Figure Drawing without art-domain and anatomy review

- Chapter 1 shipped a severely limited selection, and Chapter 2 repeated the
  same narrow extraction while consuming a disproportionate share of the user's
  weekly token budget on generated references.
- The disposition pass treated several long-established figure-drawing
  standards as technically invalid or disposable instead of preserving them as
  source-specific artistic conventions with their proper scope and history.
- The visual-review pass accepted anatomically incorrect teaching images. Of the
  generated set reviewed by the user, only four were usable; mechanical
  reference and similarity gates did not catch the anatomy and construction
  defects.
- Root cause: general-purpose plausibility judgments substituted for
  source-literate art instruction and expert anatomical review. The workflow
  optimized schema placement and image provenance before proving that the
  extracted curriculum and teaching images were faithful and usable.
- All Hogarth-derived ledgers, cards, variants, references, and active registry
  state were removed. Historical worklog entries remain only as superseded
  evidence of the failed attempts and must not be treated as validated output.
- **Do not retry unless:** a new packet defines how established artistic
  standards are retained and scoped, requires anatomy-aware review before any
  image is accepted, and limits batch generation behind an early user-visible
  quality and cost checkpoint. Tracked as
  `PASS-PROC-VISUAL-ART-SOURCE-QUALITY`.

## 2026-07-30 - Treat a fresh-prefix PDF-render exit code as conclusive when PNGs exist

- Rendering Starkey *Creative Writing: Four Genres in Brief* PDF pp. 233-239 to a fresh nested prefix returned exit 3 and reported seven files missing, but the direct renderer created all seven exact `page-233.png` through `page-239.png` outputs.
- A retry then correctly refused to overwrite those files, so it could not supply a clean success result for the same visual review.
- Root cause is unknown; the helper's fallback and expected-output verification disagree on this path.
- **Do not retry:** conclude that a failed fresh-prefix invocation supplied no visual evidence. Enumerate the exact output directory, inspect every requested image if present, and record the helper inconsistency. Follow-up is `PASS-TOOL-RENDER-FRESH-PREFIX`.

## 2026-07-30 - Treat four-digit Poppler suffixes as missing output

- `tools/render_pdf.py` rendered OpenStax *Intermediate Algebra* PDF pp. 613-622 into `page-0613.png` through `page-0622.png`, but returned exit 1 after checking only the three-digit filenames it constructed.
- Root cause: `expected_outputs()` uses `:03`, while Poppler pads page names to the width required by the highest page number.
- **Do not retry:** treat the helper's exit code as proof that no render exists for a four-digit page range. Inspect the exact output directory, then record the visual review only if every requested PNG is present.
- Follow-up is tracked in `PASS-TOOL-RENDER-4DIGIT`.

## 2026-07-30 - Use SymPy for mathematical domain evidence without confirming it is installed

- A symbolic-expansion check for OpenStax *Intermediate Algebra* Section 6.4 failed because `sympy` is not installed in this workspace.
- **Do not retry:** depend on an unrecorded symbolic-math package for a PASS run. For small factoring checks, expand the selected source examples manually and record the algebra; add a project-owned check only through a separately scoped tooling assignment.

## 2026-07-30 - Collapse one excerpt into one learning claim

- The first Gaddis Section 14.5 review treated its `operator[]` example only as
  the new reference-return skill and initially missed its competing
  always-checked access policy.
- Root cause: matching the shared language construct instead of separating the
  learner decision from the method and tradeoff.
- **Do not retry:** before disposition, run the decision-versus-method recovery
  check in `PASS_RUN.md` §§5-6. Split a new decision and a variant when the
  same source evidence genuinely supports both.

## 2026-07-30 - Validate unquoted source titles containing colons

- The first Gaddis Section 14.5 card set used the full subtitle unquoted in YAML frontmatter.
- PyYAML rejected each file at the subtitle colon, and index generation correctly refused the invalid library.
- **Do not retry:** quote any YAML scalar that contains a colon, then rerun the validator before indexing.

## 2026-07-30 - Render Chapter 19 with the bundled Poppler wrapper

- The `pdftoppm.cmd` wrapper and its discovered executable path both failed to launch.
- The wrapper reported that the path could not be found, despite the runtime directory listing the binary.
- Root cause is unknown; the source PDF itself is readable through pypdf.
- Commit/branch: pending Chapter 19 run commit on master.
- **Do not retry unless:** the bundled Poppler runtime is repaired or a separately executable renderer is available.

### Update 2026-07-30

- The wrapper remains broken, but the runtime includes a working direct executable at `dependencies/native/poppler/Library/bin/pdftoppm.exe`.
- Used that executable to render and inspect the *Automate the Boring Stuff with Python* Chapter 3 diagram pages successfully.
- Use the direct executable for visual PDF review; do not retry the wrapper.

### Update 2026-07-30 (Marvel Chapter 5)

- The previously recorded path without `dependencies/` no longer exists and fails before rendering.
- The executable at `dependencies/native/poppler/Library/bin/pdftoppm.exe` rendered PDF pp. 44-51 successfully.
- **Do not retry:** the stale path. Use the complete current direct-executable path until `PASS-TOOL-RENDER` supplies a project-owned wrapper.

### Update 2026-07-30 (PASS-TOOL-RENDER)

- `tools/render_pdf.py` now verifies every requested page file and falls back
  from the broken runtime wrapper to the direct executable when no partial files
  exist.
- **Do not retry:** either wrapper path directly. Use the project helper and its
  reported resolved renderer.

## 2026-07-30 - Verify a source ZIP with `Expand-Archive -PassThru`

- The available PowerShell `Expand-Archive` command does not support `-PassThru`; parameter binding fails before archive enumeration.
- This was a verification-command mismatch, not a source archive failure.
- **Do not retry unless:** PowerShell is upgraded to a version that supports `-PassThru`. Enumerate the extraction directory after `Expand-Archive` instead.

## 2026-07-30 - Run PASS validation with the bundled workspace Python

- The bundled workspace Python can render and extract the Marvel PDF, but it cannot import PyYAML, so both scoped validation and `tools/validate.py` stop with `ModuleNotFoundError: No module named 'yaml'`.
- The repository's `python` command imports PyYAML and ran the Chapter 4 scoped validation successfully.
- **Do not retry:** use the bundled workspace Python for PASS validation until its dependency set includes PyYAML. Use the repository's `python` command for `tools/validate.py` and `tools/build_index.py`.

## 2026-07-29 - <what was attempted>

- What was tried.
- How it failed (symptom, not guess).
- Root cause, if known.
- Commit/branch, if one exists.
- **Do not retry unless:** <what would have to change first>.

## 2026-08-01 - Pass a null SVG dash pattern while generating Chapter 1 teaching plates

- The first local SVG helper always emitted `stroke_dasharray`, including when its value was `None`; `svgwrite` rejected the attribute before any plate was written.
- Root cause: the helper treated an optional SVG attribute as mandatory.
- The helper was corrected to omit `stroke_dasharray` when no dash pattern is requested, and all three plates were regenerated and reviewed.
- **Do not retry:** passing `None` to optional `svgwrite` attributes. Build the attribute dictionary conditionally.

## 2026-08-01 - Run the full reference gate without the gitignored Gen 1 comparison image

- `python tools/verify_references.py` initially failed on the pre-existing `source_staged_figure_process_1.png` sidecar because `sources\\gen1_art_fundamentals_4step\\4step_figure_process_1.png` was absent from the snapshot.
- This was not a new Chapter 1 reference failure; the base archive omits the gitignored source payload used for originality comparison.
- The exact first-party comparison image was restored locally from the user-supplied `teaching.zip`; the full gate then passed.
- **Do not retry:** claiming the full reference gate is green from the repository snapshot alone. Restore the matching local source image or run in the full source workspace first.
