# COURSE_REGISTRY

registry_id: SCHOOL.COURSE.REGISTRY
version: 0.9.0
status: DRAFT
updated: 2026-03-08
purpose: Canonical repo-safe registry of available homeschool courses. Student-specific active course loads do not live here; they live in the student school record.

rules:
- This registry is curriculum truth, not student truth.
- Student-specific active course loads belong in the student school record.
- Course shells live under `libraries/homeschool/courses/<subject>/`.
- Packet materials live under `libraries/homeschool/packets/<subject>/`.
- Textbook/source truth lives in `libraries/homeschool/textbooks/TEXTBOOK_REGISTRY.md`.
- Grade maps point to course files; they do not replace course files.

course_status_model:
- ACTIVE
- DRAFT
- PARKED

courses:
- course_id: COURSE.Math.Algebra2.11
  title: Algebra 2
  subject: Math
  grade_band: 11
  status: ACTIVE
  packet_mode: HYBRID
  source_model: Easy Peasy
  source_model_url: https://allinonehighschool.com/algebra-2-new/
  course_file: libraries/homeschool/courses/math/COURSE.Math.Algebra2.11.md
  packet_bundle:
    sourcebook: libraries/homeschool/packets/math/COURSE.Math.Algebra2.11.SOURCEBOOK.md
    workbook: libraries/homeschool/packets/math/COURSE.Math.Algebra2.11.WORKBOOK.md
    check_key: libraries/homeschool/packets/math/COURSE.Math.Algebra2.11.CHECK_KEY.md
  wired_checkpoint_days:
    - 132
  recommended_prereqs:
    - COURSE.Math.Algebra1
    - COURSE.Math.Geometry

- course_id: COURSE.ELA.BritishLiterature.11
  title: British Literature
  subject: English
  grade_band: 11
  status: ACTIVE
  packet_mode: PACKET-SPINED
  source_model: Easy Peasy
  source_model_url: https://allinonehighschool.com/british-literature/
  course_file: libraries/homeschool/courses/ela/COURSE.ELA.BritishLiterature.11.md
  packet_bundle:
    sourcebook: libraries/homeschool/packets/ela/COURSE.ELA.BritishLiterature.11.SOURCEBOOK.md
    workbook: libraries/homeschool/packets/ela/COURSE.ELA.BritishLiterature.11.WORKBOOK.md
    check_key: libraries/homeschool/packets/ela/COURSE.ELA.BritishLiterature.11.CHECK_KEY.md
  wired_checkpoint_days:
    - 132
  recommended_prereqs: []

- course_id: COURSE.History.ModernAmericanHistory.11
  title: Modern American History
  subject: History
  grade_band: 11
  status: ACTIVE
  packet_mode: HYBRID
  source_model: Easy Peasy
  source_model_url: https://allinonehighschool.com/modern-american-history/
  course_file: libraries/homeschool/courses/history/COURSE.History.ModernAmericanHistory.11.md
  packet_bundle:
    sourcebook: libraries/homeschool/packets/history/COURSE.History.ModernAmericanHistory.11.SOURCEBOOK.md
    workbook: libraries/homeschool/packets/history/COURSE.History.ModernAmericanHistory.11.WORKBOOK.md
    check_key: libraries/homeschool/packets/history/COURSE.History.ModernAmericanHistory.11.CHECK_KEY.md
  wired_checkpoint_days:
    - 132
  recommended_prereqs: []

- course_id: COURSE.Science.PhysicsLab.11
  title: Physics w Lab
  subject: Science
  grade_band: 11
  status: ACTIVE
  packet_mode: TEXTBOOK-SPINED
  source_model: Easy Peasy
  source_model_url: https://allinonehighschool.com/physics-with-lab-2018/
  course_file: libraries/homeschool/courses/science/COURSE.Science.PhysicsLab.11.md
  packet_bundle:
    sourcebook: libraries/homeschool/packets/science/COURSE.Science.PhysicsLab.11.SOURCEBOOK.md
    workbook: libraries/homeschool/packets/science/COURSE.Science.PhysicsLab.11.WORKBOOK.md
    check_key: libraries/homeschool/packets/science/COURSE.Science.PhysicsLab.11.CHECK_KEY.md
  wired_checkpoint_days:
    - 132
  recommended_prereqs:
    - COURSE.Math.Trigonometry
    - COURSE.Math.PreCalculus
  prereq_type: recommended_not_hard_block

- course_id: COURSE.LifeSkills.11
  title: Life Skills
  subject: Life Skills
  grade_band: 11
  status: ACTIVE
  packet_mode: PACKET-SPINED
  source_model: Custom
  source_model_url: none
  course_file: libraries/homeschool/courses/life-skills/COURSE.LifeSkills.11.md
  packet_bundle:
    sourcebook: libraries/homeschool/packets/life-skills/COURSE.LifeSkills.11.SOURCEBOOK.md
    workbook: libraries/homeschool/packets/life-skills/COURSE.LifeSkills.11.WORKBOOK.md
    check_key: libraries/homeschool/packets/life-skills/COURSE.LifeSkills.11.CHECK_KEY.md
  wired_checkpoint_days:
    - 132
  recommended_prereqs: []

external_reference_courses:
- course_id: COURSE.Language.Spanish4
  title: Spanish 4
  subject: Language
  grade_band: 11
  status: ACTIVE
  class_mode: EXTERNAL
  proof_mode: EXTERNAL_PROOF
  notes:
    - student-specific external usage belongs in the student school record

- course_id: COURSE.Computer.GameDev1
  title: Game Dev 1 (Udemy)
  subject: Computer
  grade_band: 11
  status: ACTIVE
  class_mode: EXTERNAL
  proof_mode: EXTERNAL_PROOF
  notes:
    - student-specific external usage belongs in the student school record

next_build_targets:
- expand beyond Grade 11 after live runtime testing stabilizes
- add prerequisite metadata to additional future courses
- add Grade 12 courses later
