#!/usr/bin/env python3
"""Propose destinations for unsorted source books. Writes a manifest; moves nothing.

Differs from the earlier sort_classify.py in one important way: a file that no
rule matches stays in Unsorted. There is no catch-all destination. A rule table
with no "I don't know" option is what turned Programming/Algorithms into a dump
of 290 books, only 7 of which were about algorithms.

Usage:
    python tools/sort_classify2.py
"""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCES = ROOT / "sources"
SCOPE = ["Programming/Algorithms", "Unsorted",
         "Humble Book Bundle Coder's Bookshelf by No Starch Press"]
OUT = ROOT / "sort"

# Ordered: first match wins. Specific rules above general ones.
RULES: list[tuple[str, str]] = [
    # --- FALSE FRIENDS: must precede every "programming" rule ---------------
    # "Programming" here means therapy, mathematics, or television.
    (r"neuro-linguistic programming", "Health"),
    (r"non-linear programming|linear programming", "Textbooks"),
    # --- genuine computer science: these STAY in Algorithms -----------------
    (r"introduction to algorithm|encyclopedia of algorithm|algorithms in a nutshell|"
     r"analysis of algorithms|exact exponential algorithm|algorithms and parallel|"
     r"dasgupta.*algorithms|sedgewick", "Programming/Algorithms"),
    # --- languages and stacks ------------------------------------------------
    (r"\bruby\b|\brails\b", "Programming/Ruby"),
    (r"\bscala\b", "Programming/Scala"),
    (r"clojure|little prover|becoming functional|grokking simplicity", "Programming/Functional"),
    (r"go programming language", "Programming/Go"),
    (r"\bwith r\b|\br book\b|using r,|programming with r|wrangling with r", "Programming/R"),
    (r"matlab|labview", "Programming/Scientific Computing"),
    (r"xamarin|android|mobile apps at scale", "Programming/Mobile"),
    (r"html|\bcss\b|wordpress|buddypress|web site|silverlight|\byui\b|gwt in practice",
     "Programming/Web"),
    (r"c# |\.net|net core|visual c|biztalk|windows communication|crystal report|"
     r"weblogic|asynchronous programming with", "Programming/Dot Net"),
    (r"c how to program", "Programming/C"),
    (r"machine learning|deep learning|pytorch|scikit|natural language annotation|"
     r"data science|artificial intelligence", "Programming/Machine Learning"),
    (r"data lake|data engineering|elasticsearch|data-oriented programming|"
     r"data analysis and graphics", "Programming/Data"),
    (r"cloud computing|microservice|scalable systems|chaos engineering|"
     r"flow architecture|distributed architecture", "Programming/Architecture"),
    (r"reverse engineering|reversing|persistent threat|firewall|computer virus|"
     r"information security job|openbsd", "Programming/Security"),
    (r"full stack testing|unit test|software testing", "Programming/Testing"),
    (r"network programming|beej|optical net|over-the-road wireless|networking all-in-one",
     "Programming/Networking"),
    (r"gradle|build automation|scrum|agile|project management|programmer.s brain|"
     r"programming interview|passionate programmer|software engineering and development|"
     r"helping kids with coding|coding all-in-one|beginning programming|"
     r"good code, bad code|blockchain|\bnfts?\b|probabilistic programming",
     "Programming/Practice"),
    # --- consumer computing, not programming ---------------------------------
    (r"chatgpt|\bai &\b", "Computing/AI Tools"),
    (r"windows (11|vista|xp|home server)|macos|\bimac\b|macbook|\blaptops\b|apple watch|"
     r"apple one|build (your own pc|a pc)|troubleshooting and maintaining|"
     r"computers for seniors|motorola|cord cutting|mobile internet|backup for|"
     r"active directory|blackboard|microsoft teams|salesforce|mint\.com|\bxero\b|"
     r"quickbooks|office (2013|365|for seniors)|outlook|powerpoint|excel|"
     r"\bword for dummies\b|act! by sage|sharepoint|iphone|ipad|electronics for|"
     r"do-it-yourself circuit", "Computing"),
    # --- creative software and art -------------------------------------------
    (r"adobe|photoshop|premiere|dreamweaver|blender|inkscape|calligraphy|"
     r"building information modeling|canon eos|graphical programming using labview", "Art"),
    # --- writing --------------------------------------------------------------
    (r"screenwriting|romance novel|apa style|college admission essay|"
     r"writing resumes|fiction writing|songwriting", "Writing"),
    # --- money ----------------------------------------------------------------
    (r"penny stock|exchange-traded|managing debt|personal finance|financial security|"
     r"wills & trusts|\btaxes\b|bookkeeping|accounting|property management|"
     r"buying a property|budget wedding|financial modeling", "Finance"),
    # --- work -----------------------------------------------------------------
    (r"job interview|job search|first job|help desk job|military transition|"
     r"personal branding|employer branding|breaking into acting|people analytics|"
     r"time management|\bresilience\b|mind mapping|athletic scholarshi", "Careers"),
    (r"mapping experiences|advertis|selling|marketing|linkedin|tiktok|facebook|social media|"
     r"supply chain|operations management|nonprofit", "Business"),
    # --- health ---------------------------------------------------------------
    (r"ad & hd|allerg|alzheimer|anger management|addiction|depression|\bibs\b|\bpcos\b|"
     r"multiple sclerosis|nutrition|\bsleep\b|vaccin|immunity|foam rolling|"
     r"self-compassion|self-esteem|cognitive behavioural|\bdbt\b|getting pregnant|"
     r"dash diet|low-carb|anti-inflammatory|mediterranean lifestyle|acupressure|"
     r"later years|cannabis|reflexology", "Health"),
    # --- home, food, animals ---------------------------------------------------
    (r"bathroom remodel|your own home|allotment|gardening|beehive|chicken coop|"
     r"decluttering|organis|organizing|zero waste|raising goats|welding|\brvs?\b|"
     r"bike (repair|maintenance)|campers", "Home"),
    (r"\bbbq\b|\bbeer\b|\bwine\b|coffee|canning|indian cooking|meal prep|\bhoney\b",
     "Cookbooks"),
    (r"beagle|bulldog|poodle|ferret|finche|parakeet|jack russell|adopting a pet",
     "Pets"),
    # --- music, language, leisure ---------------------------------------------
    (r"bass guitar|guitar theory|saxophone|singing|music composition|classical music|"
     r"bollywood", "Music"),
    (r"arabic|japanese|\bpolish\b|spanish|french all|german workbook|linguistics",
     "Languages"),
    (r"baseball|cricket|mahjong|poker|ham radio|astrology|\bweather\b|freemason",
     "Hobbies"),
    (r"designing ttrpg", "Game Dev"),
    (r"\balaska\b|europe for|london for", "Travel"),
    # --- study ------------------------------------------------------------------
    (r"\bged\b|\bgre\b|\blsat\b|asvab|algebra|geometry|pre-calculus|calculus|"
     r"physics|chemistry|biology|statistic|basic math|maths practice|"
     r"english grammar|molecular & cell|plain geometry", "Textbooks"),
    (r"anthropolog|criminolog|neuroscience|geograph|geolog|optics|world war|"
     r"black american history|first ladies|australian politics|indigenous australia|"
     r"social psychology|online education|art history|alternative energy|"
     r"\benneagram\b", "Reference"),
    (r"buddhism|taoism", "Philosophy"),

    # ===== run-together filenames (Humble bundle has no spaces) ============
    (r"crackingcodeswithpython|pythonplayground", "Programming/Python"),
    (r"learnjavatheeasyway", "Programming/Java"),
    (r"practicalsql", "Programming/SQL"),
    (r"theartofrprogramming|thebookofr(?![a-z])", "Programming/R"),
    (r"thelinuxprogramminginterface|wickedcoolshellscripts|"
     r"linux programming interface|wicked cool shell", "Linux"),
    (r"objectorientedjavascript|understandingecmascript|javascript", "Programming/Web"),
    (r"therustprogramminglanguage", "Programming/Rust"),
    (r"thinklikeaprogrammer", "Programming/Practice"),

    # ===== second pass: rules added after reviewing what fell through =======
    (r"quantum computing", "Programming/Quantum"),
    (r"\brust\b", "Programming/Rust"),
    (r"\bqt 4\b|multiprocessor programming|multicore and gpu|"
     r"complete guide to programming in c\b", "Programming/C++"),
    (r"opengl|processing - a beginner|gnuplot|\bgimp\b", "Programming/Graphics"),
    (r"libgdx|lua game|2d game development|level up!|scratch programming", "Programming/Game"),
    (r"ionic 2|app inventor", "Programming/Mobile"),
    (r"tensorflow", "Programming/Machine Learning"),
    (r"hadoop|big data|dynamodb", "Programming/Data"),
    (r"art of deception|network security|hacker playbook|\bgns3\b|penetration testing",
     "Programming/Security"),
    (r"eventstorming|software architecture metrics|operating systems|akka in action",
     "Programming/Architecture"),
    (r"ejb 3|oracle adf|visual basic", "Programming/Java"),
    (r"linq|pro net best practices", "Programming/Dot Net"),
    (r"phoenix 1\.4|django|\bajax\b|\bhaxe\b|\bneko\b", "Programming/Web"),
    (r"code complete|think like a programmer|skills of a successful software engineer|"
     r"software engineering at google|hidden language of computer|math for programmers|"
     r"build a compiler|jira development|vim like a pro|gnu make|art of debugging|"
     r"writing efficient programs|absolute beginner|principles of computer programming|"
     r"\bd cookbook\b|research tools with google", "Programming/Practice"),
    (r"parallel programming|high performance", "Programming/Architecture"),
    (r"\b5g\b|microsoft 365|\boutlo", "Computing"),
    (r"nikon|\bart for dummies\b", "Art"),
    (r"quitting smoking|vaping|\bketo\b", "Health"),
    (r"slow cooker|cake decorating", "Cookbooks"),
    (r"medieval history|medical transcripti", "Reference"),
    (r"\balgorithms for dummies\b", "Programming/Algorithms"),
    (r"building a pc", "Computing"),
]

COMPILED = [(re.compile(p, re.I), dest) for p, dest in RULES]


def classify(text: str) -> str | None:
    for rx, dest in COMPILED:
        if rx.search(text):
            return dest
    return None


def embedded_title(path: Path) -> str:
    """Fallback for truncated filenames like 'Buying a Property F.pdf'."""
    if path.suffix.lower() != ".pdf":
        return ""
    try:
        from pypdf import PdfReader
        md = PdfReader(str(path)).metadata or {}
        return str(md.get("/Title", "") or "")
    except Exception:
        return ""


def main() -> int:
    OUT.mkdir(exist_ok=True)
    rows: list[dict[str, str]] = []
    unmatched: list[str] = []

    for rel in SCOPE:
        base = SOURCES / rel
        if not base.exists():
            continue
        for p in sorted(base.rglob("*")):
            if not p.is_file() or p.name.lower() == "readme.md":
                continue
            dest = classify(p.stem)
            why = "filename"
            if dest is None:
                t = embedded_title(p)
                if len(t) > 4:
                    dest = classify(t)
                    if dest:
                        why = "pdf-title: " + t[:55]
            if dest is None:
                unmatched.append(p.name)
                continue  # NO catch-all: leave it where it is
            old = p.relative_to(SOURCES).as_posix()
            new = f"{dest}/{p.name}"
            if old != new:
                rows.append({"old_path": old, "new_path": new,
                             "confidence": "high", "reason": why})

    with open(OUT / "manifest2.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["old_path", "new_path", "confidence", "reason"])
        w.writeheader()
        w.writerows(rows)

    counts: dict[str, int] = {}
    for r in rows:
        d = r["new_path"].rsplit("/", 1)[0]
        counts[d] = counts.get(d, 0) + 1
    print("manifest rows (files to move): %d" % len(rows))
    print("unmatched, left in place:      %d\n" % len(unmatched))
    for k, v in sorted(counts.items()):
        print("   %-36s %4d" % (k, v))
    if unmatched:
        print("\nunmatched (need a human):")
        for n in unmatched:
            print("   ", n[:98])
    return 0


if __name__ == "__main__":
    sys.exit(main())
