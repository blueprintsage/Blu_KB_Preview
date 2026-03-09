# GRADE.11

grade_id: GRADE.11
version: 0.9.0
status: DRAFT
updated: 2026-03-08
school_year: 2025-2026
purpose: Grade 11 course map for Blu homeschool, with Aiden’s current active lane as the first live implementation.

rules:
- Grade maps point to course files; they do not replace course files.
- Student runtime truth comes from the student school record.
- Grade maps define the intended curriculum lane.
- External proof-based electives may remain outside the internal curriculum registry until normalized.

grade_level: 11

core_internal_courses:
- course_id: COURSE.Math.Algebra2.11
  title: Algebra 2
  subject: Math
  packet_mode: HYBRID
  source_file: homeschool/courses/math/COURSE.Math.Algebra2.11.md
  status: ACTIVE

- course_id: COURSE.ELA.BritishLiterature.11
  title: British Literature
  subject: English
  packet_mode: PACKET-SPINED
  source_file: homeschool/courses/ela/COURSE.ELA.BritishLiterature.11.md
  status: ACTIVE

- course_id: COURSE.History.ModernAmericanHistory.11
  title: Modern American History
  subject: History
  packet_mode: HYBRID
  source_file: homeschool/courses/history/COURSE.History.ModernAmericanHistory.11.md
  status: ACTIVE

- course_id: COURSE.Science.PhysicsLab.11
  title: Physics w Lab
  subject: Science
  packet_mode: TEXTBOOK-SPINED
  source_file: homeschool/courses/science/COURSE.Science.PhysicsLab.11.md
  status: ACTIVE

- course_id: COURSE.LifeSkills.11
  title: Life Skills
  subject: Life Skills
  packet_mode: PACKET-SPINED
  source_file: homeschool/courses/life-skills/COURSE.LifeSkills.11.md
  status: ACTIVE

external_proof_courses:
- course_id: COURSE.Language.Spanish4
  title: Spanish 4
  subject: Language
  status: ACTIVE_EXTERNAL
  proof_mode:
    - screenshot
    - photo
    - visible course artifact
  notes:
    - external/offline course
    - not yet normalized into the internal curriculum spine

- course_id: COURSE.Computer.GameDev1
  title: Game Dev 1 (Udemy)
  subject: Computer
  status: ACTIVE_EXTERNAL
  proof_mode:
    - screenshot
    - photo
    - visible course artifact
  notes:
    - external/offline course
    - not yet normalized into the internal curriculum spine

school_day_model:
- 180 instructional days
- 2 semesters of 90 days
- 6 blocks of 30 days
- runtime day truth comes from the student school record

block_distribution_guidance:
- block 1: days 1-30
- block 2: days 31-60
- block 3: days 61-90
- block 4: days 91-120
- block 5: days 121-150
- block 6: days 151-180

runtime_priority:
- School should resolve current active class from the student school record first.
- If a course file exists, School should use it to determine packet mode, source model, evidence rules, and daily resolution behavior.
- If a course is ACTIVE_EXTERNAL, School should switch to proof-based review rather than internal curriculum delivery.

textbook_and_packet_policy:
- Use approved open-license textbooks where they are strong.
- Use Blu packets to fill gaps or serve as the full spine where no strong open text exists.
- Easy Peasy remains the pacing/workflow source unless replaced by a stronger internal sequence later.

aiden_live_lane:
- This grade file is the first live implementation target.
- Aiden’s current internal curriculum should be brought to runtime usability first.
- Grade 12 should be built next for continuity.

next_build_targets:
- TEXTBOOK_REGISTRY.md
- GRADE.12.md
- Algebra 2 packet support materials
- British Literature packet set
- Life Skills packet set
