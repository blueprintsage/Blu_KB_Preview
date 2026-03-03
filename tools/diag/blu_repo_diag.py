#!/usr/bin/env python3
"""
blu_repo_diag.py — deterministic repo diagnostics for Blu_KB

Goals:
- Catch known parser hazards & repo-law violations before push.
- Be easy to extend (add new rules without rewriting the scanner).

Usage:
  python tools/diag/blu_repo_diag.py --root . --config tools/diag/blu_repo_diag_rules.yaml
  python tools/diag/blu_repo_diag.py --root . --config tools/diag/blu_repo_diag_rules.yaml --fix-whitespace

Exit codes:
  0 = PASS (no errors)
  1 = FAIL (errors found)
  2 = FAIL (bad config / runtime error)
"""
from __future__ import annotations

import argparse, re, sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List, Dict, Tuple, Optional

# -------------------------
# Models
# -------------------------

@dataclass
class Finding:
    rule_id: str
    severity: str  # error|warn|info
    path: str
    line: int
    message: str
    excerpt: str = ""

# -------------------------
# Core scanners
# -------------------------

MODULE_OPEN_RE = re.compile(r'^module:\s+.+$')
MODULE_CLOSE_RE = re.compile(r'^/module\s*$')
HEADER_RE = re.compile(r'^(#{1,6})\s+')
HTML_MODULE_RE = re.compile(r'<!--\s*/?\s*MODULE\b', re.IGNORECASE)
ANGLE_PLACEHOLDER_RE = re.compile(r'<[A-Za-z0-9_\-]+>')
HEADING_ID_RE = re.compile(r'\{#.+?\}')

def iter_files(root: Path, include_globs: List[str], exclude_globs: List[str]) -> Iterable[Path]:
    candidates: List[Path] = []
    for g in include_globs:
        candidates.extend(root.rglob(g))
    out = []
    for p in candidates:
        if not p.is_file():
            continue
        rel = p.relative_to(root).as_posix()
        if any(Path(rel).match(ex) for ex in exclude_globs):
            continue
        out.append(p)
    # de-dup + stable order
    seen=set()
    uniq=[]
    for p in sorted(out, key=lambda x: x.as_posix()):
        if p.as_posix() in seen: 
            continue
        seen.add(p.as_posix())
        uniq.append(p)
    return uniq

def read_lines(p: Path) -> List[str]:
    try:
        return p.read_text(encoding="utf-8").splitlines()
    except UnicodeDecodeError:
        return p.read_text(encoding="utf-8", errors="ignore").splitlines()

def scan_module_balance(lines: List[str]) -> Tuple[int,int]:
    opens=sum(1 for l in lines if MODULE_OPEN_RE.match(l.strip()) and l.startswith("module:"))
    closes=sum(1 for l in lines if MODULE_CLOSE_RE.match(l))
    return opens, closes

def scan_headers_inside_modules(lines: List[str]) -> List[int]:
    bad=[]
    in_mod=False
    for i,l in enumerate(lines, start=1):
        if l.startswith("module:"):
            in_mod=True
            continue
        if in_mod and HEADER_RE.match(l):
            bad.append(i)
        if MODULE_CLOSE_RE.match(l.strip()):
            in_mod=False
    return bad

def scan_leading_space_tokens(lines: List[str]) -> List[Tuple[int,str]]:
    bad=[]
    for i,l in enumerate(lines, start=1):
        if l.startswith(" module:") or l.startswith(" /module"):
            bad.append((i,l))
    return bad

def scan_html_module_tokens(lines: List[str]) -> List[int]:
    return [i for i,l in enumerate(lines, start=1) if HTML_MODULE_RE.search(l)]

def scan_angle_placeholders(lines: List[str]) -> List[int]:
    # Ignore HTML tags like <br> by restricting to single-token placeholders only.
    return [i for i,l in enumerate(lines, start=1) if ANGLE_PLACEHOLDER_RE.search(l)]

def scan_heading_ids(lines: List[str]) -> List[int]:
    return [i for i,l in enumerate(lines, start=1) if HEADING_ID_RE.search(l)]

def maybe_fix_whitespace(p: Path, lines: List[str]) -> bool:
    changed=False
    new=[]
    for l in lines:
        if l.startswith(" module:"):
            new.append("module:" + l[len(" module:"):])
            changed=True
        elif l.startswith(" /module"):
            new.append("/module" + l[len(" /module"):])
            changed=True
        else:
            new.append(l)
    if changed:
        p.write_text("\n".join(new) + "\n", encoding="utf-8")
    return changed

# -------------------------
# Runner
# -------------------------

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".", help="Repo root")
    ap.add_argument("--config", default="tools/diag/blu_repo_diag_rules.yaml", help="Rules config yaml")
    ap.add_argument("--fix-whitespace", action="store_true", help="Auto-fix leading space on module tokens")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    cfg_path = Path(args.config)
    if not cfg_path.is_absolute():
        cfg_path = (root / cfg_path).resolve()
    if not cfg_path.exists():
        print(f"Config not found: {cfg_path}", file=sys.stderr)
        return 2

    import yaml  # local dependency; standard in many envs; if missing, fall back to stdlib parse.
    cfg = yaml.safe_load(cfg_path.read_text(encoding="utf-8"))
    include = cfg.get("include_globs", ["**/*.md"])
    exclude = cfg.get("exclude_globs", [".git/**", "node_modules/**", "**/.DS_Store"])
    rules = cfg.get("rules", {})

    findings: List[Finding] = []

    for p in iter_files(root, include, exclude):
        rel = p.relative_to(root).as_posix()
        lines = read_lines(p)

        # R001 html module markers
        if rules.get("R001_no_html_module_markers", {}).get("enabled", True):
            for ln in scan_html_module_tokens(lines):
                findings.append(Finding("R001", "error", rel, ln, "HTML module marker found", lines[ln-1].strip()[:200]))

        # R002 leading space tokens
        if rules.get("R002_no_leading_space_module_tokens", {}).get("enabled", True):
            for ln, ex in scan_leading_space_tokens(lines):
                findings.append(Finding("R002", "error", rel, ln, "Leading space on module token", ex.strip()[:200]))

        # optional auto-fix
        if args.fix_whitespace:
            if maybe_fix_whitespace(p, lines):
                lines = read_lines(p)

        # R003 module balance
        if rules.get("R003_module_balance", {}).get("enabled", True):
            opens, closes = scan_module_balance(lines)
            if opens != closes:
                findings.append(Finding("R003", "error", rel, 1, f"Module imbalance: opens={opens} closes={closes}", ""))

        # R004 headers inside module
        if rules.get("R004_no_headers_inside_modules", {}).get("enabled", True):
            for ln in scan_headers_inside_modules(lines):
                findings.append(Finding("R004", "error", rel, ln, "Header inside module block", lines[ln-1].strip()[:200]))

        # R005 no heading IDs {#...}
        if rules.get("R005_no_heading_ids", {}).get("enabled", True):
            for ln in scan_heading_ids(lines):
                findings.append(Finding("R005", "error", rel, ln, "Nonstandard heading id {#...} found", lines[ln-1].strip()[:200]))

        # R006 no angle placeholders <name>
        if rules.get("R006_no_angle_placeholders", {}).get("enabled", True):
            for ln in scan_angle_placeholders(lines):
                findings.append(Finding("R006", "warn", rel, ln, "Angle-bracket placeholder found (prefer {name})", lines[ln-1].strip()[:200]))

    # Report
    if not findings:
        print("PASS: no findings.")
        return 0

    # Group by rule
    by_rule: Dict[str, List[Finding]] = {}
    for f in findings:
        by_rule.setdefault(f.rule_id, []).append(f)

    print("FAIL: findings detected\n")
    for rid in sorted(by_rule.keys()):
        items = by_rule[rid]
        sev = items[0].severity
        print(f"{rid} ({sev}) — {len(items)} finding(s)")
        for f in items[:10]:
            loc = f"{f.path}:{f.line}"
            ex = f" | {f.excerpt}" if f.excerpt else ""
            print(f"  - {loc} — {f.message}{ex}")
        if len(items) > 10:
            print(f"  … +{len(items)-10} more")
        print()

    # exit non-zero if any error
    if any(f.severity == "error" for f in findings):
        return 1
    return 0

if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except KeyboardInterrupt:
        raise
    except Exception as e:
        print(f"Runtime error: {e}", file=sys.stderr)
        raise SystemExit(2)
