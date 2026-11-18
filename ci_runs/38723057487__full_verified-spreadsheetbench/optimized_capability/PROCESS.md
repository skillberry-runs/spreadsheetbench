# PROCESS — what I did this iteration (explainability; REQUIRED)

## Ranked issue list (clusters by # failing tasks × trials, biggest first)
| rank | cluster | tasks | shared root cause | tag (KNOWLEDGE / BEHAVIORAL / CAPABILITY-GAP) | planned change class |
| --- | --- | --- | --- | --- | --- |
| 1 | Formulas instead of values | 45635, 54144 | Agent wrote formula strings (=...) instead of computing results in Python. | BEHAVIORAL | CONTRACT |
| 2 | Type Mismatch | 416-15, 54144 | Agent converted dates/numbers to strings (e.g. strftime). | BEHAVIORAL | CONTRACT |
| 3 | Unnecessary Modifications | 54144, 38462, 39046, 416-15, 463-17 | Agent modified cells outside the target range or changed existing data. | BEHAVIORAL | CONTRACT |
| 4 | Lack of Verification | 45635, 54144, 39046, 416-15 | Agent stopped immediately after writing the file without verifying its contents. | BEHAVIORAL | STRUCTURE |

## Changes made this iteration (one row per edit — aim for MULTIPLE classes, incl. a NEW tool when a cluster needs one)
| cluster | edit class | file / tool | what & why it generalizes | protects passing? |
| --- | --- | --- | --- | --- |
| Formulas | CONTRACT | prompt.md | Explicitly forbid formulas and require literal values. | Yes, passing tasks already write values. |
| Type Mismatch | CONTRACT | guidance.md | Require real typed values (datetime, float, int) and forbid string conversion. | Yes, passing tasks use correct types. |
| Unnecessary Mods | CONTRACT | prompt.md | Explicitly forbid modifying cells outside the target range. | Yes, passing tasks are precise. |
| Lack of Verification | STRUCTURE | prompt.md | Added a mandatory "Verify" step to the Execution Workflow. | Yes, doesn't change output if correct. |

## Verify-the-fix (one line per change: the trace it targets → what the guard/computation/new-tool now does on those exact inputs)
- 45635: wrote formula `=IF(...)` → prompt now forbids formulas and requires literal values.
- 416-15: used `strftime` for dates → guidance now requires `datetime` objects and forbids string conversion.
- 54144: modified cells outside range → prompt now forbids modifying cells outside `answer_position`.
- 45635, 54144, 39046: stopped after writing → prompt now requires a verification step (re-opening the file).

## Process & features used
- Serial diagnosis of failing trajectories.
- Implemented CONTRACT and STRUCTURE levers.

## Good things to PRESERVE (do not let a future iteration undo these)
- The strict ban on formulas.
- The requirement for typed values.
- The mandatory verification step.

## Deliberately skipped (cluster + why — already-passing / needs gold / infra noise)
- None.
