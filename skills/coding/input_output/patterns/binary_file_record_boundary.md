# Binary File Record Boundary

object_id: binary_file_record_boundary
object_type: pattern
category: coding
subcategory: input_output
stage_binding: 1 skeleton
lane_fit: both
foundation_role: foundation
tags:
- binary_files
- records
- file_io
- structured_data
cross_links:
- related_to: skills/coding/input_output
- related_to: skills/coding/structures
reference:
- source_title: Starting Out with C++: From Control Structures through Objects
- author: Tony Gaddis
- publish_date: 2015
- edition: 8th
- media_type: textbook_pdf
- source_pages: 688-741
- evidence_type: text_layer
confidence: high

## Objective
Use binary file records only when layout, record size, and portability limits are explicit.

## Steps / Flow
1. Define the record structure and its fixed-size assumptions.
2. Open the file in binary mode.
3. Read and write whole records intentionally.
4. Avoid treating binary records as self-describing data.
5. Document portability and versioning risks.

## Notes
Advanced file operations include binary files, random access, and records. PASS stores the boundary rule rather than legacy code forms.

## Modernization
Modernized into current C++ teaching practice without copying legacy source wording.
