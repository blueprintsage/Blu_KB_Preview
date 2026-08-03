#!/usr/bin/env python3
import csv
import subprocess
from pathlib import Path
from collections import defaultdict

SOURCES_ROOT = Path("D:/Repos/PASS/sources")
SORT_DIR = Path("D:/Repos/PASS/sort")
MANIFEST_CSV = SORT_DIR / "manifest_textbooks.csv"

# Textbook subjects - create these categories
TEXTBOOK_SUBJECTS = {
    "Mathematics": ["math", "algebra", "geometry", "calculus", "linear"],
    "Physics": ["physics", "quantum", "mechanics", "thermodynamics"],
    "Chemistry": ["chemistry", "chemical"],
    "Psychology": ["psychology", "psychiatric", "mental", "behavioral"],
    "Engineering": ["engineering", "metal", "mechanical", "civil"],
    "Biology": ["biology", "cell", "organism"],
    "Environmental": ["environmental", "ecology", "climate"],
    "Medicine": ["medicine", "medical", "health", "clinical"],
}

def classify_textbook(filename):
    """Classify textbook by filename."""
    lower_name = filename.lower()

    for subject, keywords in TEXTBOOK_SUBJECTS.items():
        for kw in keywords:
            if kw in lower_name:
                return subject

    return None  # Will need content reading

def extract_pdf_text(filepath, max_pages=3):
    """Extract text from first N pages of PDF using pdftotext."""
    try:
        # Use pdftotext if available
        result = subprocess.run(
            ["pdftotext", "-f", "1", "-l", str(max_pages), str(filepath), "-"],
            capture_output=True, text=True, timeout=10
        )
        if result.returncode == 0:
            return result.stdout[:2000]  # First 2000 chars
    except:
        pass

    try:
        # Fallback: try PyPDF2 if installed
        import PyPDF2
        with open(filepath, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            text = ""
            for page_num in range(min(max_pages, len(reader.pages))):
                text += reader.pages[page_num].extract_text()
            return text[:2000]
    except:
        pass

    return None

def classify_by_content(filename, filepath):
    """Read PDF content to determine subject."""
    text = extract_pdf_text(filepath)
    if not text:
        return None

    lower_text = text.lower()

    # Check for subject keywords in content
    for subject, keywords in TEXTBOOK_SUBJECTS.items():
        for kw in keywords:
            if kw in lower_text:
                return subject

    # Fallback for general programming/unsorted
    if any(x in lower_text for x in ["python", "java", "code", "program"]):
        return "Programming"

    return None

def main():
    print("="*70)
    print("ORGANIZING TEXTBOOKS AND NEW FILES")
    print("="*70)

    manifest = []
    textbook_count = 0
    unsorted_count = 0

    # Scan Textbooks folder
    textbooks_path = SOURCES_ROOT / "Textbooks"
    if textbooks_path.exists():
        for pdf_file in sorted(textbooks_path.glob("*.pdf")):
            filename = pdf_file.name
            rel_path = f"Textbooks\\{filename}"

            # Classify by filename first
            subject = classify_textbook(filename)

            if subject:
                new_path = f"Textbooks/{subject}/{filename}"
                reason = f"Matched subject: {subject}"
                confidence = "high"
            else:
                # Try content reading
                subject = classify_by_content(filename, pdf_file)
                if subject:
                    new_path = f"Textbooks/{subject}/{filename}"
                    reason = f"Content analysis: {subject}"
                    confidence = "medium"
                else:
                    new_path = f"Unsorted/{filename}"
                    reason = "Could not determine subject"
                    confidence = "low"

            manifest.append({
                'old_path': rel_path,
                'new_path': new_path,
                'confidence': confidence,
                'reason': reason,
            })
            textbook_count += 1
            print(f"[{confidence.upper():6}] {filename[:60]}")
            print(f"       → {new_path.split('/')[-2]}/{new_path.split('/')[-1]}")

    # Scan !Programming Books/Unsorted folder for new files
    unsorted_path = SOURCES_ROOT / "!Programming Books" / "Unsorted"
    if unsorted_path.exists():
        print(f"\nNew unsorted files:")
        for pdf_file in sorted(unsorted_path.glob("*")):
            filename = pdf_file.name
            if filename.startswith('.'):
                continue

            rel_path = f"!Programming Books\\Unsorted\\{filename}"

            # For new unsorted, try to classify intelligently
            subject = classify_textbook(filename)
            if subject:
                new_path = f"Textbooks/{subject}/{filename}"
                reason = f"Textbook detected: {subject}"
                confidence = "high"
            else:
                # Try content reading
                subject = classify_by_content(filename, pdf_file)
                if subject and subject != "Programming":
                    new_path = f"Textbooks/{subject}/{filename}"
                    reason = f"Content analysis: {subject}"
                    confidence = "medium"
                else:
                    # Programming books or keep in Unsorted
                    if any(x in filename.lower() for x in ["python", "java", "c++", "programming"]):
                        new_path = f"!Programming Books/Programming/{filename}"
                        reason = "Programming book"
                        confidence = "high"
                    else:
                        new_path = f"Unsorted/{filename}"
                        reason = "No matching category"
                        confidence = "low"

            manifest.append({
                'old_path': rel_path,
                'new_path': new_path,
                'confidence': confidence,
                'reason': reason,
            })
            unsorted_count += 1
            print(f"[{confidence.upper():6}] {filename[:60]}")
            print(f"       → {'/'.join(new_path.split('/')[-2:])}")

    # Write manifest
    with open(MANIFEST_CSV, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['old_path', 'new_path', 'confidence', 'reason'])
        writer.writeheader()
        writer.writerows(manifest)

    # Report
    print(f"\n{'='*70}")
    print(f"Textbooks scanned: {textbook_count}")
    print(f"New unsorted files: {unsorted_count}")
    print(f"Total to organize: {len(manifest)}")
    print(f"Manifest: {MANIFEST_CSV}")
    print(f"{'='*70}")

    # Destination summary
    dests = defaultdict(int)
    for row in manifest:
        dest = row['new_path'].split('/')[0]
        dests[dest] += 1

    print(f"\nDestinations:")
    for dest in sorted(dests.keys()):
        print(f"  {dest}: {dests[dest]}")

if __name__ == "__main__":
    main()
