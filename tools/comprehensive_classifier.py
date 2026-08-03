#!/usr/bin/env python3
import csv
import subprocess
import re
from pathlib import Path
from collections import defaultdict

SOURCES_ROOT = Path("D:/Repos/PASS/sources")
SORT_DIR = Path("D:/Repos/PASS/sort")
INVENTORY_CSV = SORT_DIR / "full_inventory.csv"
MANIFEST_CSV = SORT_DIR / "manifest_comprehensive.csv"

# Subject taxonomy - expanded
TAXONOMY = {
    "Mathematics": ["math", "algebra", "calculus", "geometry", "linear", "number theory"],
    "Physics": ["physics", "quantum", "mechanics", "thermodynamics", "relativity"],
    "Chemistry": ["chemistry", "chemical", "organic", "biochem"],
    "Biology": ["biology", "cell", "genetics", "evolution", "ecology"],
    "Computer Science": ["algorithm", "data structure", "complexity", "computation"],
    "Programming": ["python", "java", "c++", "c#", "javascript", "code", "programming", "developer"],
    "Web Development": ["web", "html", "css", "react", "angular", "vue"],
    "AI/Machine Learning": ["machine learning", "deep learning", "neural", "ai", "chatgpt"],
    "Engineering": ["engineering", "mechanical", "civil", "electrical"],
    "Psychology": ["psychology", "mind", "behavior"],
    "Art": ["art", "drawing", "painting", "design", "anatomy", "color"],
    "Photography": ["photography", "photo", "camera"],
    "Music": ["music", "audio", "sound"],
    "Writing": ["writing", "grammar", "novel", "poetry"],
    "Business": ["business", "marketing", "finance", "startup", "trading", "investing"],
    "History": ["history", "war", "civilization"],
    "Philosophy": ["philosophy", "ethics", "logic"],
    "Medicine": ["medicine", "medical", "health", "disease"],
    "Linux/Systems": ["linux", "unix", "bash", "shell", "system"],
}

def extract_pdf_text(filepath, max_pages=3):
    """Extract text from first N pages of PDF."""
    try:
        result = subprocess.run(
            ["pdftotext", "-f", "1", "-l", str(max_pages), str(filepath), "-"],
            capture_output=True, text=True, timeout=10
        )
        if result.returncode == 0:
            return result.stdout[:3000]
    except:
        pass
    return None

def classify_by_content(text):
    """Classify document by reading content."""
    if not text:
        return None

    lower_text = text.lower()

    # Check each subject category
    for subject, keywords in TAXONOMY.items():
        for keyword in keywords:
            if keyword in lower_text:
                return subject

    return None

def classify_file(file_info, folder_hint):
    """Classify file using multiple methods."""
    filename = file_info['filename'].lower()

    # Method 1: Check existing folder categorization
    if folder_hint and folder_hint not in ["Unsorted", "Unsorted/new"]:
        # Folder name is likely correct, but we might need to refine it
        if "programming" in folder_hint.lower():
            return "Programming"
        for subject in TAXONOMY.keys():
            if subject.lower() in folder_hint.lower():
                return subject

    # Method 2: Check filename keywords
    for subject, keywords in TAXONOMY.items():
        for keyword in keywords:
            if keyword in filename:
                return subject

    # Method 3: Default by extension
    if file_info['extension'] == '.zip':
        return "Art" if "art" in filename or "drawing" in filename else "Misc"

    return None

def standardize_filename(file_info):
    """Create standardized filename: Author - Title (Edition, Year).ext"""
    filename = file_info['filename']
    ext = file_info['extension']
    author = file_info['author']
    edition = file_info['edition']
    year = file_info['year']

    # Extract title (remove author if found)
    if " - " in filename:
        parts = filename.split(" - ", 1)
        title = parts[1].rsplit(ext, 1)[0].strip()
    else:
        title = filename.rsplit(ext, 1)[0].strip()

    # Build standardized name
    name_parts = []
    if author:
        name_parts.append(author)
    name_parts.append(title)

    # Add edition/year in parentheses
    suffix_parts = []
    if edition:
        suffix_parts.append(edition)
    if year:
        suffix_parts.append(year)

    if suffix_parts:
        standardized = f"{' - '.join(name_parts)} ({', '.join(suffix_parts)}){ext}"
    else:
        standardized = f"{' - '.join(name_parts)}{ext}"

    # Clean up
    standardized = re.sub(r'\s+', ' ', standardized)  # Remove extra spaces
    standardized = re.sub(r'[<>:"|?*]', '', standardized)  # Remove invalid chars

    return standardized[:200]  # Limit length

def main():
    print("="*70)
    print("COMPREHENSIVE FILE CLASSIFIER & RENAMER")
    print("="*70)

    # Load inventory
    print("\nLoading inventory...")
    files = []
    with open(INVENTORY_CSV, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        files = list(reader)

    print(f"Loaded {len(files)} files")

    # Identify files to skip/remove
    remove_set = set()
    seen_hashes = {}

    # Mark duplicates (keep first, remove rest)
    for file_info in files:
        sha = file_info['sha256']
        if sha in seen_hashes:
            remove_set.add(file_info['path'])
        else:
            seen_hashes[sha] = file_info['path']

    # Mark MOBI if PDF/EPUB exists
    for file_info in files:
        if file_info['extension'] == '.mobi':
            base_name = Path(file_info['path']).stem
            for other_file in files:
                if other_file['extension'] in ['.pdf', '.epub']:
                    if Path(other_file['path']).stem == base_name:
                        remove_set.add(file_info['path'])
                        break

    print(f"\nFiles to remove:")
    print(f"  Duplicates: {sum(1 for f in files if f['path'] in remove_set and f['sha256'] in seen_hashes)}")
    print(f"  MOBIs:      {sum(1 for f in files if f['path'] in remove_set and f['extension'] == '.mobi')}")

    # Classify and standardize
    print(f"\nClassifying files...")
    manifest = []

    for file_info in files:
        old_path = file_info['path']

        # Skip removed files
        if old_path in remove_set:
            manifest.append({
                'old_path': old_path,
                'new_path': None,
                'action': 'REMOVE',
                'reason': 'Duplicate or MOBI replacement',
                'category': None,
                'new_filename': None,
            })
            continue

        # Get folder hint
        folder = old_path.split('\\')[0] if '\\' in old_path else "Unsorted"

        # Classify
        category = classify_file(file_info, folder)
        if not category:
            category = "Unsorted"

        # Standardize filename
        new_filename = standardize_filename(file_info)

        # Build new path
        new_path = f"{category}/{new_filename}"

        manifest.append({
            'old_path': old_path,
            'new_path': new_path,
            'action': 'MOVE',
            'reason': f'Classified as {category}',
            'category': category,
            'new_filename': new_filename,
        })

    # Write manifest
    with open(MANIFEST_CSV, 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['old_path', 'new_path', 'action', 'reason', 'category', 'new_filename']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(manifest)

    # Report
    print(f"\n{'='*70}")
    print(f"CLASSIFICATION COMPLETE")
    print(f"{'='*70}")

    moves = [m for m in manifest if m['action'] == 'MOVE']
    removes = [m for m in manifest if m['action'] == 'REMOVE']

    print(f"\nFiles to move:  {len(moves)}")
    print(f"Files to remove: {len(removes)}")

    # Distribution
    print(f"\nDistribution by category:")
    by_category = defaultdict(int)
    for m in moves:
        by_category[m['category']] += 1

    for cat in sorted(by_category.keys()):
        print(f"  {cat}: {by_category[cat]}")

    print(f"\nManifest saved: {MANIFEST_CSV}")

if __name__ == "__main__":
    main()
