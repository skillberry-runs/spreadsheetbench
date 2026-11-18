# PROCESS — what I did this iteration (explainability; REQUIRED)

## Ranked issue list (clusters by # failing tasks × trials, biggest first)
| rank | cluster | tasks | shared root cause | tag (KNOWLEDGE / BEHAVIORAL / CAPABILITY-GAP) | planned change class |
| --- | --- | --- | --- | --- | --- |
| 1 | Formula-instead-of-Value | 267-18, 37378, 45635, 53383, 55049, 55979, 59595, 6698, 7902, 8942 | Agent writes Excel formulas (e.g. `=SUM(...)`) instead of computed literal values. Grader reads values and does not recalculate. | OUTPUT-CONTRACT | CONTRACT |
| 2 | Excel-Error-Text | 46897, 53647, 54144, 56563, 9569 | Agent writes error strings (e.g. "#N/A") to cells, likely from unresolved lookups or writing formula results as text. | OUTPUT-CONTRACT | CONTRACT |
| 3 | Untouched-Modified | 39046, 48527, 50768, 53647, 54144, 80-42 | Agent modifies cells outside the target range or changes cells that should have remained as their original input. | BEHAVIORAL | STRUCTURE (Checklist) |
| 4 | Value-Mismatch | 51-12, 31628, 37456, 43436, 227-40 | General logic errors leading to wrong computed values (higher/lower/different). | CAPABILITY-GAP | WORKED EXAMPLE / METHOD |
| 5 | Type-Mismatch | 59196, 56563, 9569 | Writing wrong types (e.g. int instead of str, str instead of float). | OUTPUT-CONTRACT | CONTRACT |

## Changes made this iteration (one row per edit — aim for MULTIPLE classes, incl. a NEW tool when a cluster needs one)
| cluster | edit class | file / tool | what & why it generalizes | protects passing? |
| --- | --- | --- | --- | --- |
| Formula-instead-of-Value | CONTRACT | guidance.md | Explicitly forbid writing formulas; require computing values in Python and writing literal values. | Yes, passing tasks already write literals. |
| Excel-Error-Text | CONTRACT | guidance.md | Forbid writing Excel error strings (e.g. #N/A); require handling missing data in Python to write a clean value (0, empty, etc). | Yes, passing tasks don't write error strings. |
| Untouched-Modified | STRUCTURE | prompt.md | Added a pre-finish verification step: "Verify that no cells outside the required target range were modified". | Yes, passing tasks only touch targets. |

## Verify-the-fix (one line per change: the trace it targets → what the guard/computation/new-tool now does on those exact inputs)
- 267-18: wrote formula `="//" & ...` → will now compute the result in Python and write the literal string.
- 54144: wrote formula `=SUM(SUMIFS(...))` → will now perform the sum in Python and write the literal number.
- 9569: wrote `#N/A` strings → will now handle the lookup failure in Python and write the appropriate value (e.g. 0 or empty).
- 39046: changed untouched cells in F2:F6 → will now verify that only the requested changes were applied before saving.

## Process & features used
- Serial execution for diagnosis and drafting.
- Used `bash` for trajectory analysis and clustering.

## Good things to PRESERVE (do not let a future iteration undo these)
- The current baseline is stable on 15 tasks.

## Deliberately skipped (cluster + why — already-passing / needs gold / infra noise)
- Value-Mismatch: These are often task-specific logic errors; focusing on systemic contract/behavioral issues first.
