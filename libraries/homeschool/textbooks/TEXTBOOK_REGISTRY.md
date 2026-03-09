# TEXTBOOK_REGISTRY

registry_id: SCHOOL.TEXTBOOK.REGISTRY
version: 0.9.0
status: DRAFT
updated: 2026-03-08
purpose: First-pass textbook and source registry for Blu homeschool, with adoption status, license posture, and course support mapping.

rules:
- This registry tracks source suitability, not just “free to read” status.
- A source may be:
  - PRIMARY
  - SUPPLEMENTAL
  - REFERENCE_ONLY
  - NOT_REPO_HOSTABLE
- `repo_hostable` means acceptable to download/store in the repo under the source’s current license terms and your homeschool use case.
- `redistribution_notes` should be reviewed before downloading anything in bulk.
- Packet-spined courses may use original Blu packet materials as the primary instructional spine.
- Easy Peasy remains the workflow/pacing source unless replaced later.

entries:
- textbook_id: TX.MATH.A2.CK12.001
  title: CK-12 Interactive Algebra 2
  subject: Math
  grade_band: 9-12
  adoption_status: PRIMARY
  repo_hostable: yes_for_educational_use
  license_family: CK-12 Curriculum Materials License
  source_url: https://flexbooks.ck12.org/cbook/ck-12-interactive-algebra-2-for-ccss-2nd-edition/
  local_filename: <pending_download>
  supports_courses:
    - COURSE.Math.Algebra2.11
  role_notes:
    - strongest current open-style match for a full Algebra 2 spine
    - use as primary algebra sequence when downloading is cleared
  redistribution_notes:
    - educational-use license
    - preserve attribution
    - mark modifications
    - keep license terms with derivatives

- textbook_id: TX.MATH.INTERMEDIATE.OPENSTAX.001
  title: OpenStax Intermediate Algebra
  subject: Math
  grade_band: 9-12+
  adoption_status: SUPPLEMENTAL
  repo_hostable: yes
  license_family: CC BY 4.0
  source_url: https://openstax.org/subjects
  local_filename: <pending_download>
  supports_courses:
    - COURSE.Math.Algebra2.11
  role_notes:
    - use as remediation, alternate explanation, and prerequisite support
    - not preferred as the sole primary Algebra 2 spine

- textbook_id: TX.SCI.PHYSICS.OPENSTAX.001
  title: OpenStax High School Physics
  subject: Science
  grade_band: 9-12
  adoption_status: PRIMARY
  repo_hostable: yes
  license_family: CC BY 4.0
  source_url: https://openstax.org/
  local_filename: <pending_download>
  supports_courses:
    - COURSE.Science.PhysicsLab.11
  role_notes:
    - strongest current primary physics text for Aiden’s active internal courses

- textbook_id: TX.SCI.PHYSICSLAB.OPENSTAX.002
  title: OpenStax High School Physics Lab Manual
  subject: Science
  grade_band: 9-12
  adoption_status: PRIMARY
  repo_hostable: yes
  license_family: CC BY 4.0
  source_url: https://assets.openstax.org/oscms-prodcms/media/documents/STUDENT_HS_Physics_Lab_Manual_Full.pdf
  local_filename: <pending_download>
  supports_courses:
    - COURSE.Science.PhysicsLab.11
  role_notes:
    - lab companion for Physics w Lab
    - pair with the main physics text

- textbook_id: TX.ELA.BRITLIT.PUBLICDOMAIN.001
  title: British Literature Public-Domain Reading Spine
  subject: English
  grade_band: 9-12
  adoption_status: PRIMARY
  repo_hostable: mixed_by_text
  license_family: Public domain texts + original Blu packet materials
  source_url: <curated_per_text>
  local_filename: <anthology_or_text_list_pending>
  supports_courses:
    - COURSE.ELA.BritishLiterature.11
  role_notes:
    - preferred model is public-domain texts plus Blu-made sourcebook/workbook/check-key
    - no single adopted external textbook yet

- textbook_id: TX.HIST.USHIST.COREKNOWLEDGE.001
  title: Core Knowledge U.S. History / related history materials
  subject: History
  grade_band: K-8 primary; selective support for higher grades
  adoption_status: SUPPLEMENTAL
  repo_hostable: yes_noncommercial_sharealike
  license_family: CC BY-NC-SA
  source_url: https://www.coreknowledge.org/download-free-curriculum/
  local_filename: <pending_download>
  supports_courses:
    - COURSE.History.ModernAmericanHistory.11
  role_notes:
    - use as support packets/background/reference
    - not the ideal sole primary spine for Grade 11 Modern American History

- textbook_id: TX.LIFESKILLS.CUSTOM.001
  title: Blu Life Skills Packet Spine
  subject: Life Skills
  grade_band: 11-12 first pass
  adoption_status: PRIMARY
  repo_hostable: yes
  license_family: Original Blu curriculum materials
  source_url: none
  local_filename: pending_packet_build
  supports_courses:
    - COURSE.LifeSkills.11
  role_notes:
    - custom packet-spined course
    - should be built from original sourcebook/workbook/check-key materials

reference_only:
- textbook_id: TX.ELA.AMBLESIDE.REF.001
  title: AmblesideOnline
  subject: English / literature selection reference
  adoption_status: REFERENCE_ONLY
  repo_hostable: no
  license_family: copyrighted curriculum/site content
  source_url: https://www.amblesideonline.org/
  role_notes:
    - useful as a reading-list/reference guide
    - not suitable as repo-hosted curriculum

- textbook_id: TX.CURRIC.GOODBEAUTIFUL.REF.001
  title: The Good and the Beautiful
  subject: mixed
  adoption_status: REFERENCE_ONLY
  repo_hostable: no
  license_family: restricted proprietary / free-use mix
  source_url: https://www.goodandbeautiful.com/
  role_notes:
    - free in places
    - not a clean repo-hostable curriculum source for this system

course_adoption_map:
- course_id: COURSE.Math.Algebra2.11
  primary:
    - TX.MATH.A2.CK12.001
  supplemental:
    - TX.MATH.INTERMEDIATE.OPENSTAX.001
  packet_mode: HYBRID

- course_id: COURSE.ELA.BritishLiterature.11
  primary:
    - TX.ELA.BRITLIT.PUBLICDOMAIN.001
  supplemental: []
  packet_mode: PACKET-SPINED

- course_id: COURSE.History.ModernAmericanHistory.11
  primary: []
  supplemental:
    - TX.HIST.USHIST.COREKNOWLEDGE.001
  packet_mode: HYBRID
  notes:
    - still needs a stronger dedicated high-school-level open primary spine

- course_id: COURSE.Science.PhysicsLab.11
  primary:
    - TX.SCI.PHYSICS.OPENSTAX.001
    - TX.SCI.PHYSICSLAB.OPENSTAX.002
  supplemental: []
  packet_mode: TEXTBOOK-SPINED

- course_id: COURSE.LifeSkills.11
  primary:
    - TX.LIFESKILLS.CUSTOM.001
  supplemental: []
  packet_mode: PACKET-SPINED

next_actions:
- download the clearly repo-hostable primaries first
- confirm local filenames after download
- build packet materials for:
  - Algebra 2 gap-fill
  - British Literature
  - Life Skills
  - Modern American History support
- later expand the registry for Grade 12 and lower grades
