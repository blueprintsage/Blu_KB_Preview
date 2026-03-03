# SIM_TAGS_CANONICAL_v1

Canonical scenario tags used by post-build simulations.

## ART
- medium: comic|storyboard|refsheet|illo|paint
- prompt: vague|mid|detailed
- plate: none|concept|prev_step
- copyright_ref: no|yes
- user_vibe: busy|anxious|resistant|neutral
- user_override: stop_asking|none
- steps: normal|skip_s1
- finish: concept|oil|watercolor|acrylic|comic_manga
- comics_mode: western|manga|n/a
- genre: fantasy|modern|horror|scifi|cyberpunk

## SCHOOL
- class: algebra|lit|history|physics|lifeskills
- work: graded|ungraded
- behavior: cooperative|vague|demand_answer|class_hop|refusal|silent_skip
- parent: none|next_class_ok|override|excused_full|excused_partial
- scope: full|reduced4
- timing: on_time|late|end_early

## TEACH
- intent: learn|answer_only
- stakes: graded|ungraded
- attempt: none|partial|genuine
- user_vibe: busy|anxious|resistant|neutral

## SKILLFORGE
- domain: art|school|teaching|programs|exec
- change: new|edit|deprecate
- impact: nonbreaking|breaking
- touches_kernel: no|yes
- needs_approval: no|yes

## EXEC
- op: archive|zip|unzip|task_switch|file_naming|error_reporting
- path: cpu|gpu|mixed
