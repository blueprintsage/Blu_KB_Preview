#!/usr/bin/env python3
"""SkillForge resolver -- the consumption side of PASS.

Extraction turns a source into grounded skill objects. This does the other half:
given a task, it hands the model the relevant subset of those objects, foundations
first, with the consumption contract on top -- so the model combines what it was
taught with its native capability instead of either improvising blindly or letting
retrieved notes dominate the whole task. See docs/PASS/PASS_CONSUMPTION.md.

What it enforces: which objects enter context, and in what order. What it cannot
enforce: that the model actually applies them once loaded. The resolver moves the
failure from "never consulted the library" to "consulted it and must now use it" --
real progress, not a total fix.

Usage:
    python tools/resolve.py --task "review this C++ API for ownership problems"
    python tools/resolve.py --task "block in a figure from gesture" --lane skill --format full

Output is a bounded, ordered bundle. `--format full` also emits the consumption
contract and every selected card's text, so a calling assistant can load the whole
bundle in one read. `--format paths` (default) lists paths and reasons only.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

FRONTMATTER_RE = re.compile(
    r"\A---\r?\n(?P<front>.*?)\r?\n---\r?\n(?P<body>.*)\Z", re.DOTALL
)
IF_RE = re.compile(r"\*\*IF\*\*(?P<if>.*?)\*\*THEN\*\*", re.DOTALL)

# Retrieval is broad on purpose (retrieve broadly, apply narrowly). These common
# words carry no topic signal and would match everything, so they are dropped
# before scoring. This is a stop-list, not a domain vocabulary.
STOPWORDS = {
    "a", "an", "the", "this", "that", "these", "those", "and", "or", "but", "for",
    "of", "to", "in", "on", "at", "by", "with", "from", "into", "as", "is", "are",
    "be", "been", "being", "it", "its", "my", "your", "our", "their", "how", "what",
    "when", "should", "would", "can", "could", "do", "does", "make", "making",
    "use", "using", "used", "help", "please", "want", "need", "review", "reviewing",
    "build", "building", "write", "writing", "create", "creating", "fix", "fixing",
    "code", "work", "task", "thing", "things", "some", "any", "about", "just", "me",
    "problem", "problems", "issue", "issues",
}

# The user's word for a thing is not always the library's. Map common surface forms
# to the token the library actually files them under, so "c++" finds the `cpp`
# package. Small and hand-curated -- not a thesaurus.
ALIASES = {
    "c++": "cpp", "cxx": "cpp", "cplusplus": "cpp",
    "js": "javascript", "ts": "typescript", "py": "python",
    "oo": "object-oriented", "raii": "resource",
}

# Match weights: where a query term lands decides how much signal it carries.
WEIGHT_TAG = 3
WEIGHT_PATH = 3
WEIGHT_NAME = 2
WEIGHT_BODY = 1

DEFAULT_CAP = 12
MIN_SCORE = 3                  # a lone weak name hit is noise, not a match
MAX_FOUNDATIONS = 6            # foundation expansion never dominates the bundle
FOUNDATION_EXPAND_FROM = 6     # only the top-N scored objects pull foundations
CONSUMPTION_CONTRACT = Path("docs/PASS/PASS_CONSUMPTION.md")

# lane_fit vocabulary is the schema's: teach | skill | both | teaching_foundation.
# A request lane maps to the set of lane_fit values it is allowed to load.
LANE_COMPATIBILITY = {
    "skill": {"skill", "both"},
    "teach": {"teach", "both", "teaching_foundation"},
    "both": {"skill", "teach", "both", "teaching_foundation"},
}

# Relations that, when a card declares them, point from a foundation DOWN to its
# dependent. To find a card's foundations we read these in REVERSE.
FOUNDATIONWARD_RELS = {"foundation_of", "prerequisite_for", "teaching_foundation_for"}


@dataclass
class Card:
    path: Path
    data: dict[str, Any]
    body: str
    if_clause: str = ""
    score: int = 0
    reasons: list[str] = field(default_factory=list)

    @property
    def object_id(self) -> str:
        return str(self.data.get("object_id", self.path.stem))

    @property
    def object_type(self) -> str:
        return str(self.data.get("object_type", ""))

    @property
    def name(self) -> str:
        return str(self.data.get("name", self.object_id))

    @property
    def package(self) -> str:
        lp = self.data.get("library_path") or []
        return lp[0] if lp else ""

    @property
    def is_foundation(self) -> bool:
        return self.data.get("foundation_role") == "foundation"

    @property
    def lane_fit(self) -> str:
        return str(self.data.get("lane_fit", "both"))

    def tag_terms(self) -> set[str]:
        out: set[str] = set()
        for tag in self.data.get("tags") or []:
            out |= _terms(str(tag).replace("_", " ").replace("-", " "))
        return out

    def path_terms(self) -> set[str]:
        out: set[str] = set()
        for seg in self.data.get("library_path") or []:
            out |= _terms(str(seg).replace("-", " "))
        return out

    def name_terms(self) -> set[str]:
        return _terms(self.name)

    def body_terms(self) -> set[str]:
        out = _terms(self.if_clause)
        if self.object_type == "drill":
            out |= _terms(str(self.data.get("target_skill", "")))
        return out


def _tokenize(text: str) -> list[str]:
    """Lowercase, split on non-alphanumerics (keeping '+'), drop noise, singularize."""
    tokens: list[str] = []
    for tok in re.split(r"[^a-z0-9+]+", text.lower()):
        if not tok:
            continue
        tok = ALIASES.get(tok, tok)
        if tok in STOPWORDS:
            continue
        if len(tok) == 1 and tok != "c":
            continue
        if len(tok) > 4 and tok.endswith("s") and not tok.endswith("ss"):
            tok = tok[:-1]  # crude singularize; overlap only needs consistency
        tokens.append(tok)
    return tokens


def _terms(text: str) -> set[str]:
    return set(_tokenize(text))


def discover(library_root: Path) -> list[Path]:
    return sorted(
        p for p in library_root.rglob("*.md")
        if p.name not in {"README.md", "INDEX.md"}
    )


def load_card(path: Path) -> Card | None:
    raw = path.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(raw)
    if not match:
        return None
    try:
        data = yaml.safe_load(match.group("front"))
    except yaml.YAMLError:
        return None
    if not isinstance(data, dict):
        return None
    body = match.group("body")
    card = Card(path=path, data=data, body=body)
    if_match = IF_RE.search(body)
    if if_match:
        card.if_clause = if_match.group("if").strip()
    return card


def score_card(card: Card, query: set[str]) -> tuple[int, list[str], set[str]]:
    """Weighted overlap between query terms and where they land on the card."""
    tag_hits = query & card.tag_terms()
    path_hits = query & card.path_terms()
    name_hits = (query & card.name_terms()) - tag_hits - path_hits
    body_hits = (query & card.body_terms()) - tag_hits - path_hits - name_hits

    score = (WEIGHT_TAG * len(tag_hits) + WEIGHT_PATH * len(path_hits)
             + WEIGHT_NAME * len(name_hits) + WEIGHT_BODY * len(body_hits))

    reasons: list[str] = []
    if tag_hits:
        reasons.append(f"tags: {', '.join(sorted(tag_hits))}")
    if path_hits:
        reasons.append(f"topic: {', '.join(sorted(path_hits))}")
    if name_hits:
        reasons.append(f"name: {', '.join(sorted(name_hits))}")
    if body_hits:
        reasons.append(f"rule: {', '.join(sorted(body_hits))}")
    matched = tag_hits | path_hits | name_hits | body_hits
    return score, reasons, matched


def find_metaskill(cards: list[Card]) -> Card | None:
    for card in cards:
        if card.package == "metaskills" and card.object_type == "ap":
            return card
    return None


def resolve(
    cards: list[Card],
    query: set[str],
    lane: str,
    package_hint: str | None,
    cap: int,
) -> dict[str, Any]:
    by_id = {c.object_id: c for c in cards}
    allowed_fits = LANE_COMPATIBILITY.get(lane, LANE_COMPATIBILITY["both"])

    # Reverse foundation index: foundation_source[T] = ids that declare themselves
    # foundation_of / prerequisite_for T (i.e. T's foundations).
    foundation_source: dict[str, list[str]] = {}
    for c in cards:
        for link in c.data.get("cross_links") or []:
            if isinstance(link, dict) and link.get("rel") in FOUNDATIONWARD_RELS:
                tid = link.get("target_object_id")
                if tid:
                    foundation_source.setdefault(tid, []).append(c.object_id)

    # Score every card; keep those with real signal and a compatible lane. Drills
    # are practice artifacts -- they only belong in teach/practice lanes, so in the
    # skill lane they are dropped here rather than after the cap, where they would
    # otherwise crowd the actual skills out of the bundle entirely.
    matched_terms: set[str] = set()
    scored: list[Card] = []
    for card in cards:
        if card.package == "metaskills":
            continue  # metaskill is added unconditionally below
        if lane == "skill" and card.object_type == "drill":
            continue
        score, reasons, matched = score_card(card, query)
        if score < MIN_SCORE:
            continue
        if card.lane_fit not in allowed_fits:
            continue
        if package_hint and card.package != package_hint:
            continue
        card.score = score
        card.reasons = reasons
        matched_terms |= matched
        scored.append(card)

    # Rank by score, but let patterns/APs win the cap over an equal-scored drill.
    type_rank = {"pattern": 0, "ap": 1, "drill": 2}
    scored.sort(key=lambda c: (-c.score, type_rank.get(c.object_type, 3), c.object_id))
    top = scored[:cap]
    hit_packages = {c.package for c in top}
    selected: dict[str, Card] = {c.object_id: c for c in top}

    # Foundation expansion: from the strongest selections only, pull each card's
    # declared foundation (foundation_object_id, points up) and its reverse
    # foundation sources -- staying inside packages the task actually hit, capped.
    added_foundations = 0
    for card in top[:FOUNDATION_EXPAND_FROM]:
        if added_foundations >= MAX_FOUNDATIONS:
            break
        candidate_ids: list[str] = []
        fid = card.data.get("foundation_object_id")
        if fid and fid != "none":
            candidate_ids.append(fid)
        candidate_ids += foundation_source.get(card.object_id, [])
        for cid in candidate_ids:
            if added_foundations >= MAX_FOUNDATIONS:
                break
            found = by_id.get(cid)
            if not found or cid in selected:
                continue
            if found.package == "metaskills":
                continue  # already the mandatory load-first object
            if found.package not in hit_packages:
                continue
            found.reasons = [f"foundation for {card.object_id}"]
            selected[cid] = found
            added_foundations += 1

    metaskill = find_metaskill(cards)

    # Ordering: foundations -> specializations, patterns -> APs -> drills within each.
    def order_key(card: Card) -> tuple:
        type_rank = {"pattern": 1, "ap": 2, "drill": 3}.get(card.object_type, 4)
        role_rank = 0 if card.is_foundation else 1
        return (role_rank, type_rank, -card.score, card.object_id)

    ordered = sorted(selected.values(), key=order_key)
    if lane == "skill":
        ordered = [c for c in ordered if c.object_type != "drill"]

    unmatched = sorted(query - matched_terms)
    if not scored:
        coverage = "none"
    elif unmatched:
        coverage = "partial"
    else:
        coverage = "full"

    return {
        "metaskill": metaskill,
        "foundations": [c for c in ordered if c.is_foundation],
        "objects": [c for c in ordered if not c.is_foundation],
        "coverage": coverage,
        "hit_packages": sorted(p for p in hit_packages if p),
        "considered": len(scored),
        "unmatched": unmatched,
    }


def render_paths(bundle: dict[str, Any], lane: str, task: str) -> str:
    lines: list[str] = []
    lines.append("# SkillForge bundle")
    lines.append("")
    lines.append(f"task: {task}")
    lines.append(f"lane: {lane}")
    lines.append(f"coverage: {bundle['coverage']} "
                 f"(packages: {', '.join(bundle['hit_packages']) or 'none'}; "
                 f"{bundle['considered']} candidates scored)")
    if bundle["unmatched"]:
        lines.append(f"library silent on: {', '.join(bundle['unmatched'])} "
                     "-- use your own reasoning there and label uncertainty.")
    lines.append("")
    lines.append("## Load first -- consumption contract")
    lines.append(f"- {CONSUMPTION_CONTRACT.as_posix()} -- how to use what follows "
                 "(scoped authority, foundations first, IF-match).")
    meta = bundle["metaskill"]
    if meta:
        lines.append(f"- {meta.path.as_posix()} -- mandatory construction metaskill.")
    lines.append("")
    if bundle["foundations"]:
        lines.append("## Foundations (load before specializations)")
        for c in bundle["foundations"]:
            lines.append(f"- {c.path.as_posix()}  [{c.object_type}] -- {'; '.join(c.reasons)}")
        lines.append("")
    if bundle["objects"]:
        lines.append("## Applicable objects")
        for c in bundle["objects"]:
            lines.append(f"- {c.path.as_posix()}  [{c.object_type}] -- {'; '.join(c.reasons)}")
        lines.append("")
    if bundle["coverage"] == "none":
        lines.append("## Coverage")
        lines.append("- No matching skills. Say so, then fall back to your own reasoning "
                     "and label important uncertainty.")
        lines.append("")
    return "\n".join(lines)


def render_full(bundle: dict[str, Any], lane: str, task: str, repo_root: Path) -> str:
    parts = [render_paths(bundle, lane, task), "\n---\n"]
    contract = repo_root / CONSUMPTION_CONTRACT
    if contract.exists():
        parts.append(f"# === {CONSUMPTION_CONTRACT.as_posix()} ===\n")
        parts.append(contract.read_text(encoding="utf-8"))
        parts.append("\n---\n")
    ordered: list[Card] = []
    if bundle["metaskill"]:
        ordered.append(bundle["metaskill"])
    ordered += bundle["foundations"] + bundle["objects"]
    for card in ordered:
        parts.append(f"# === {card.path.as_posix()} ===\n")
        parts.append(card.path.read_text(encoding="utf-8"))
        parts.append("\n---\n")
    return "\n".join(parts)


def main() -> int:
    parser = argparse.ArgumentParser(description="SkillForge resolver")
    parser.add_argument("--task", required=True, help="natural-language task description")
    parser.add_argument("--lane", choices=["skill", "teach", "both"], default="both")
    parser.add_argument("--package", default=None, help="restrict to one package (e.g. software-engineering)")
    parser.add_argument("--cap", type=int, default=DEFAULT_CAP, help="max scored objects before foundation expansion")
    parser.add_argument("--format", choices=["paths", "full"], default="paths")
    parser.add_argument("--library", type=Path, default=Path("library"))
    args = parser.parse_args()

    # Cards and the contract carry unicode (arrows, em-dashes, accents); don't let
    # a cp1252 console mangle the bundle the assistant is meant to read.
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8")
        except (AttributeError, ValueError):
            pass

    library_root = args.library
    if not library_root.exists():
        print(f"error: library not found at {library_root}", file=sys.stderr)
        return 2

    cards = [c for c in (load_card(p) for p in discover(library_root)) if c]
    if not cards:
        print("error: no cards loaded", file=sys.stderr)
        return 2

    query = _terms(args.task)
    bundle = resolve(cards, query, args.lane, args.package, args.cap)

    if args.format == "full":
        print(render_full(bundle, args.lane, args.task, Path.cwd()))
    else:
        print(render_paths(bundle, args.lane, args.task))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
