#!/usr/bin/env python3
import csv
import subprocess
from pathlib import Path

SOURCES_ROOT = Path("D:/Repos/PASS/sources")
SORT_DIR = Path("D:/Repos/PASS/sort")
MANIFEST_CSV = SORT_DIR / "manifest_comprehensive.csv"
MANIFEST_REFINED = SORT_DIR / "manifest_final.csv"

TAXONOMY = {
    "Mathematics": ["math", "algebra", "calculus", "geometry", "linear", "number theory", "statistics"],
    "Physics": ["physics", "quantum", "mechanics", "thermodynamics", "relativity"],
    "Chemistry": ["chemistry", "chemical", "organic", "biochem", "atom"],
    "Biology": ["biology", "cell", "genetics", "evolution", "ecology", "organism", "species"],
    "Computer Science": ["algorithm", "data structure", "complexity", "computation", "compiler"],
    "Programming": ["python", "java", "c++", "c#", "javascript", "ruby", "golang", "kotlin", "code", "programming", "developer", "framework"],
    "Web Development": ["web", "html", "css", "react", "angular", "vue", "node", "django"],
    "AI/Machine Learning": ["machine learning", "deep learning", "neural", "ai", "chatgpt", "llm"],
    "Engineering": ["engineering", "mechanical", "civil", "electrical", "infrastructure"],
    "Psychology": ["psychology", "mind", "behavior", "mental", "cognition"],
    "Art": ["art", "drawing", "painting", "design", "anatomy", "color", "illustration"],
    "Photography": ["photography", "photo", "camera", "lens", "visual"],
    "Music": ["music", "audio", "sound", "instrument", "notation"],
    "Writing": ["writing", "grammar", "novel", "poetry", "storytelling", "author"],
    "Business": ["business", "marketing", "finance", "startup", "trading", "investing", "entrepreneur"],
    "History": ["history", "war", "civilization", "ancient", "medieval"],
    "Philosophy": ["philosophy", "ethics", "logic", "metaphysics"],
    "Medicine": ["medicine", "medical", "health", "disease", "doctor", "clinical"],
    "Linux/Systems": ["linux", "unix", "bash", "shell", "system", "kernel"],
    "Reference": ["reference", "dictionary", "encyclopedia", "handbook"],
}

def extract_pdf_text(filepath, max_pages=2):
    """Extract text from PDF."""
    try:
        result = subprocess.run(
            ["pdftotext", "-f", "1", "-l", str(max_pages), str(filepath), "-"],
            capture_output=True, text=True, timeout=5
        )
        if result.returncode == 0:
            return result.stdout[:2000]
    except:
        pass
    return None

def classify_by_content(filepath, filename):
    """Read file content and classify."""
    ext = Path(filepath).suffix.lower()

    if ext == '.pdf':
        text = extract_pdf_text(SOURCES_ROOT / filepath)
    elif ext == '.epub':
        # For EPUB, we'd need a different parser - skip for now
        return None
    else:
        return None

    if not text:
        return None

    lower_text = text.lower()

    # Score each category
    scores = {}
    for subject, keywords in TAXONOMY.items():
        score = 0
        for keyword in keywords:
            if keyword in lower_text:
                score += 1
        if score > 0:
            scores[subject] = score

    # Return highest scoring category
    if scores:
        return max(scores, key=scores.get)

    return None

def main():
    print("="*70)
    print("REFINING UNSORTED FILES BY READING CONTENT")
    print("="*70)

    # Load manifest
    print("\nLoading manifest...")
    manifest = []
    with open(MANIFEST_CSV, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        manifest = list(reader)

    # Find unsorted files
    unsorted = [m for m in manifest if m['category'] == 'Unsorted']
    print(f"Found {len(unsorted)} unsorted files")
    print(f"Reading content to classify...\n")

    reclassified = 0
    for i, item in enumerate(unsorted):
        old_path = item['old_path']
        filename = Path(old_path).name

        # Try content reading
        new_category = classify_by_content(old_path, filename)

        if new_category and new_category != 'Unsorted':
            print(f"[{i+1}/{len(unsorted)}] {filename[:60]}")
            print(f"  → {new_category}")
            item['category'] = new_category
            # Regenerate new_path with new category
            item['new_path'] = f"{new_category}/{item['new_filename']}"
            reclassified += 1

            if (i + 1) % 20 == 0:
                print(f"  ({reclassified} reclassified so far)\n")

    print(f"\n{'='*70}")
    print(f"Reclassified: {reclassified} files")
    print(f"Still unsorted: {len(unsorted) - reclassified} files")
    print(f"{'='*70}")

    # Write refined manifest
    with open(MANIFEST_REFINED, 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['old_path', 'new_path', 'action', 'reason', 'category', 'new_filename']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(manifest)

    # Final report
    from collections import defaultdict
    by_cat = defaultdict(int)
    for m in manifest:
        if m['action'] == 'MOVE':
            by_cat[m['category']] += 1

    print(f"\nFinal distribution:")
    for cat in sorted(by_cat.keys()):
        print(f"  {cat}: {by_cat[cat]}")

    print(f"\nRefined manifest: {MANIFEST_REFINED}")

if __name__ == "__main__":
    main()
