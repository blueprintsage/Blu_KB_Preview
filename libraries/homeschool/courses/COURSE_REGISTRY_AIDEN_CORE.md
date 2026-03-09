# Aiden Core Course Registry

registry_id: SCHOOL.COURSE.REGISTRY.AIDEN.CORE
version: 0.9.1
status: DRAFT
updated: 2026-03-08
student: Aiden
grade_level: 11
school_year: 2025-2026
purpose: Minimum viable curriculum registry for Aiden’s active internal courses, wired for packetized day checkpoints and PROGRAM.School runtime use.

rules:
- Student day truth comes from `Aiden_STUDENT_SCHOOL_RECORD.md`.
- Each course below follows the school year model:
  - 180 instructional days
  - 2 semesters
  - 6 blocks of 30 days
- Easy Peasy is the workflow source model for day-by-day progression unless marked custom.
- Open-text spines are preferred and should replace or supplement source-model materials where possible.
- External proof-based electives (Spanish 4, Game Dev 1) are not included in this core registry pass.

courses:
- course_id: COURSE.Math.Algebra2.11
  title: Algebra 2
  subject: Math
  type: internal
  packet_mode: HYBRID
  source_model: Easy Peasy
  source_model_url: https://allinonehighschool.com/algebra-2-new/
  shell_file: libraries/homeschool/courses/math/COURSE.Math.Algebra2.11.md
  wired_checkpoint_days:
    - 132

- course_id: COURSE.ELA.BritishLiterature.11
  title: British Literature
  subject: English
  type: internal
  packet_mode: PACKET-SPINED
  source_model: Easy Peasy
  source_model_url: https://allinonehighschool.com/british-literature/
  shell_file: libraries/homeschool/courses/ela/COURSE.ELA.BritishLiterature.11.md
  wired_checkpoint_days:
    - 132

- course_id: COURSE.History.ModernAmericanHistory.11
  title: Modern American History
  subject: History
  type: internal
  packet_mode: HYBRID
  source_model: Easy Peasy
  source_model_url: https://allinonehighschool.com/modern-american-history/
  shell_file: libraries/homeschool/courses/history/COURSE.History.ModernAmericanHistory.11.md
  wired_checkpoint_days:
    - 132

- course_id: COURSE.Science.PhysicsLab.11
  title: Physics w Lab
  subject: Science
  type: internal
  packet_mode: TEXTBOOK-SPINED
  source_model: Easy Peasy
  source_model_url: https://allinonehighschool.com/physics-with-lab-2018/
  shell_file: libraries/homeschool/courses/science/COURSE.Science.PhysicsLab.11.md
  wired_checkpoint_days:
    - 132

- course_id: COURSE.LifeSkills.11
  title: Life Skills
  subject: Life Skills
  type: internal
  packet_mode: PACKET-SPINED
  source_model: Custom
  source_model_url: none
  shell_file: libraries/homeschool/courses/life-skills/COURSE.LifeSkills.11.md
  wired_checkpoint_days:
    - 132

notes:
- This registry is wired for the first live runtime checkpoint set.
- The next wiring pass can expand beyond day 132 after live testing.
