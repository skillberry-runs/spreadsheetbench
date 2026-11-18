# PROCESS — what I did this iteration (explainability; REQUIRED)

## Ranked issue list (clusters by # failing tasks × trials, biggest first)
| rank | cluster | tasks | shared root cause | tag (KNOWLEDGE / BEHAVIORAL / CAPABILITY-GAP) | planned change class |
| --- | --- | --- | --- | --- | --- |
| 1 | Formula instead of Value | 37378, 46897 | Agent writes Excel formulas instead of calculating values in Python and writing literals. Scorer does not recalculate formulas. | BEHAVIORAL | Output Contract / Format |
| 2 | Incomplete/Empty Range | 227-40, 48527, 50768 | Agent fails to fill all required cells in the answer range, leaving some empty. | BEHAVIORAL | Ordered Procedure / Checklist |
| 3 | Value Mismatch (Precision/Logic) | 267-18, 39046, 43436, 51-12 | Agent calculates slightly wrong values (too high, too low, or different type). | KNOWLEDGE / BEHAVIORAL | Worked Example / Explicit Logic |
| 4 | Excel Error Text | 37456 | Agent writes cells containing Excel error strings (e.g., #VALUE!). | BEHAVIORAL | Output Contract / Recovery |

## Changes made this iteration (one row per edit — aim for MULTIPLE classes, incl. a NEW tool when a cluster needs one)
| cluster | edit class | file / tool | what & why it generalizes | protects passing? |
| --- | --- | --- | --- | --- |
| Formula instead of Value | Tighten Output Contract | prompt.md | Explicitly forbid writing formulas to answer cells; require literal values. | Yes (passing tasks already use literals) |
| Incomplete/Empty Range | Ordered Procedure | task_template.md | Add a mandatory verification step to check if all cells in the answer range are filled. | Yes |
| Value Mismatch | Worked Example | prompt.md | Provide an example of reading, calculating, and writing a value correctly. | Yes |
| Excel Error Text | Output Contract | prompt.md | Explicitly forbid writing error strings; require handling of NaN/Errors in Python. | Yes |

## Verify-the-fix (one line per change: the trace it targets → what the guard/computation/new-tool now does on those exact inputs)
- 37378, 46897: wrote formulas → contract "Write only literal values, never formulas" prevents this.
- 227-40, 48527: left cells empty → checklist "Verify all cells in {answer_position} are filled" forces filling.
- 39046, 43436: wrong values → worked example on precise calculation reduces logic errors.
- 37456: wrote error text → contract "Ensure no cell contains Excel error strings" prevents this.

## Process & features used
- Serial diagnosis of trajectories.
- Drafted a comprehensive initial prompt and task template.

## Good things to PRESERVE (do not let a future iteration undo these)
- Use of `openpyxl` for writing to preserve formatting.
- Left join/merge for lookups.

## Deliberately skipped (cluster + why — already-passing / needs gold / infra noise)
- None.
