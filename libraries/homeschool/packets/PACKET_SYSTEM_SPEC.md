# PACKET_SYSTEM_SPEC

spec_id: SCHOOL.PACKET.SYSTEM
version: 0.9.0
status: DRAFT
updated: 2026-03-08
purpose: Define the standard Blu packet system for courses that are packet-spined or hybrid-spined.

core_rule:
- Easy Peasy may be used as the workflow and pacing source.
- Blu packets must be original teaching material.
- Packets must not clone or mirror copyrighted curriculum text too closely.
- When a strong open textbook exists, packet material may supplement it.
- When no strong open textbook exists, packet material becomes the primary instructional spine.

packet_modes:
- TEXTBOOK-SPINED
- PACKET-SPINED
- HYBRID

definitions:
- TEXTBOOK-SPINED:
  - a course whose primary instructional spine is an approved open-license textbook
  - packets may still exist for checks, worksheets, and summaries
- PACKET-SPINED:
  - a course whose primary instructional spine is Blu-made original packet material
  - sourcebook, workbook, and teacher/check key are required
- HYBRID:
  - a course that uses an approved open textbook where helpful, but depends on Blu-made packet material for missing or weak parts

required_packet_components:
- sourcebook
- student_workbook
- teacher_check_key

sourcebook_purpose:
- teach the concept
- explain vocabulary
- show worked examples
- give reference notes
- anchor the student’s understanding before practice

student_workbook_purpose:
- daily work
- drills
- prompts
- response sheets
- guided notes
- labs or practical tasks when relevant

teacher_check_key_purpose:
- expected answer patterns
- acceptable completion evidence
- common mistakes
- grading/check notes
- what counts as COMPLETE, DEFERRED, or REVIEW_REQUIRED

packet_file_family:
- <course_id>.SOURCEBOOK.md
- <course_id>.WORKBOOK.md
- <course_id>.CHECK_KEY.md

course_packet_rules:
- Every packet-spined or hybrid-spined course must declare its packet mode.
- Every packet-spined course must define all three packet files.
- Every hybrid course must define at least:
  - the approved open-text spine
  - the packet gap-fill areas
  - the workbook/check materials that Blu owns
- Packet content should be grade-specific when possible.
- Packet content must match the course day/block flow.

runtime_contract:
- School resolves the current instructional day from the student school record.
- School resolves the course from the course registry / grade map.
- The course file resolves whether the day uses:
  - textbook material
  - packet material
  - both
- School then binds the source(s) for that day and opens the class block.

daily_packet_resolution:
- A course should be able to answer:
  - what is the current day?
  - what is the source for today?
  - what is the assignment for today?
  - what evidence is required?
  - what tutoring mode applies?
- If no open textbook exists for a needed lesson, the packet sourcebook becomes the instructional source for that day.

packet_day_structure:
- day_number
- block_number
- lesson_title
- objective
- source_type
- source_ref
- workbook_ref
- check_key_ref
- tutoring_mode
- evidence_required
- grading_artifact_type
- notes

recommended_source_types:
- OPEN_TEXT
- BLU_SOURCEBOOK
- BLU_WORKBOOK
- BLU_CHECK_KEY
- EXTERNAL_PROOF
- MIXED

artifact_rules:
- No artifact = unverifiable.
- If a day requires proof, the packet must name what counts as proof.
- CHECK_ONLY courses must specify what student artifact is needed before review.
- NO_ANSWERING courses must specify what kind of student-authored response is required.

quality_rules:
- original explanations
- clean structure
- grade-appropriate language
- concrete examples
- visible assumptions
- exact evidence expectations
- no answer-supply in check-only lanes
- no ghostwriting in no-answering lanes

build_order:
1. course shell
2. packet mode selection
3. sourcebook skeleton
4. workbook skeleton
5. check key skeleton
6. day-resolution mapping
7. School runtime testing

aiden_current_course_modes:
- COURSE.Math.Algebra2.11 -> HYBRID
- COURSE.ELA.BritishLiterature.11 -> PACKET-SPINED
- COURSE.History.ModernAmericanHistory.11 -> HYBRID
- COURSE.Science.PhysicsLab.11 -> TEXTBOOK-SPINED
- COURSE.LifeSkills.11 -> PACKET-SPINED

notes:
- Packet system is the fallback that makes full K-12 curriculum possible even when ideal open textbooks do not exist.
- Packet system is also the fastest way to preserve Aiden’s continuity into 12th grade.
