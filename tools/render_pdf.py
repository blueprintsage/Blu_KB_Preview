#!/usr/bin/env python3
"""Render a PDF page range for PASS visual review with Poppler's pdftoppm."""

from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path


PAGE_RANGE_RE = re.compile(r"^(\d+)-(\d+)$")


def parse_page_range(value: str) -> tuple[int, int]:
    match = PAGE_RANGE_RE.fullmatch(value)
    if not match:
        raise ValueError("page range must use START-END, for example 44-51")
    first, last = (int(part) for part in match.groups())
    if first < 1 or last < first:
        raise ValueError("page range must begin at page 1 or later and end at or after its start")
    return first, last


def sibling_direct_renderer(renderer: Path) -> Path | None:
    if renderer.name.lower() != "pdftoppm.cmd" or len(renderer.parents) < 3:
        return None
    return renderer.parents[2] / "native" / "poppler" / "Library" / "bin" / "pdftoppm.exe"


def renderer_candidates(explicit: Path | None) -> list[Path]:
    if explicit is not None:
        if explicit.is_file():
            return [explicit]
        raise FileNotFoundError(f"renderer does not exist: {explicit}")
    configured = os.environ.get("PASS_PDFTOPPM")
    if configured:
        candidate = Path(configured)
        if candidate.is_file():
            return [candidate]
        raise FileNotFoundError(f"PASS_PDFTOPPM does not exist: {candidate}")
    discovered = shutil.which("pdftoppm")
    if discovered:
        renderer = Path(discovered)
        candidates = [renderer]
        sibling = sibling_direct_renderer(renderer)
        if sibling is not None and sibling.is_file():
            candidates.append(sibling)
        return candidates
    raise FileNotFoundError("pdftoppm was not found; install Poppler, add it to PATH, or set PASS_PDFTOPPM")


def resolve_renderer(explicit: Path | None) -> Path:
    return renderer_candidates(explicit)[0]


def render_command(
    renderer: Path,
    source: Path,
    first: int,
    last: int,
    output_prefix: Path,
    dpi: int,
    *,
    cropbox: bool = True,
) -> list[str]:
    command = [str(renderer), "-f", str(first), "-l", str(last), "-png", "-r", str(dpi)]
    if cropbox:
        command.append("-cropbox")
    return [*command, str(source), str(output_prefix)]


def expected_outputs(output_prefix: Path, first: int, last: int) -> list[Path]:
    return [output_prefix.parent / f"{output_prefix.name}-{page:03}.png" for page in range(first, last + 1)]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, help="PDF source path")
    parser.add_argument("--pages", required=True, help="inclusive page range: START-END")
    parser.add_argument("--output-prefix", required=True, type=Path, help="output path prefix, without page suffix")
    parser.add_argument("--dpi", type=int, default=150, help="render resolution (default: 150)")
    parser.add_argument("--renderer", type=Path, help="explicit pdftoppm executable or wrapper")
    parser.add_argument(
        "--media-box",
        action="store_true",
        help="render the full PDF MediaBox instead of the visible CropBox",
    )
    args = parser.parse_args()
    try:
        first, last = parse_page_range(args.pages)
        if args.dpi < 1:
            raise ValueError("dpi must be positive")
        if not args.source.is_file():
            raise FileNotFoundError(f"source does not exist: {args.source}")
        renderers = renderer_candidates(args.renderer)
    except (ValueError, FileNotFoundError) as exc:
        parser.error(str(exc))
    outputs = expected_outputs(args.output_prefix, first, last)
    existing = [path for path in outputs if path.exists()]
    if existing:
        parser.error(f"output files already exist; choose a new prefix: {existing[0]}")
    args.output_prefix.parent.mkdir(parents=True, exist_ok=True)
    for renderer in renderers:
        command = render_command(
            renderer, args.source, first, last, args.output_prefix, args.dpi,
            cropbox=not args.media_box,
        )
        result = subprocess.run(command, check=False)
        present = [path for path in outputs if path.is_file()]
        if result.returncode == 0 and len(present) == len(outputs):
            print(f"renderer: {renderer}")
            print("command:", subprocess.list2cmdline(command))
            return 0
        missing = [str(path) for path in outputs if path not in present]
        print(f"renderer failed: {renderer} (exit {result.returncode}; missing {len(missing)} output file(s))", file=sys.stderr)
        if present:
            print("partial render retained; choose a new output prefix before retrying", file=sys.stderr)
            return 1
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
