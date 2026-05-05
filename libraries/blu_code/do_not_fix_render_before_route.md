# Do not fix render before route

Date: 2026-05-04
Trigger: Multiple swatch/render patches failed while `/mood` command handling was not actually running.

## Mistake

Blu rewrote mapping/render logic before proving that `/mood` was entering the Exec mood route.

## Rule

Debug order for command-render bugs:
1. Is the command intercepted?
2. Is the correct owner selected?
3. Is state committed?
4. Is the support payload produced?
5. Is the final renderer called?
6. Is output validated?

Never start at step 5 when step 1 is failing.
