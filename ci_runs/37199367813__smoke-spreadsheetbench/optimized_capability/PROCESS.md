# PROCESS — what I did this iteration (explainability; REQUIRED)

## Ranked issue list (clusters by # failing tasks × trials, biggest first)
| rank | cluster | tasks | shared root cause | tag (KNOWLEDGE / BEHAVIORAL / CAPABILITY-GAP) | planned change class |
| --- | --- | --- | --- | --- | --- |
| 1 | Type Mismatch | 32438, 250-20 | Values written as strings instead of Excel numeric/date types | KNOWLEDGE | Tighten output contract / Add explicit rule on types |
| 2 | Range/Coverage Mismatch | 54638, 493-18 | Failing to fill all required cells or writing outside range | BEHAVIORAL | Ordered procedure / Checklist for range verification |
| 3 | Logic/Calculation Error | 47766, 52216, 262-17 | Incorrect filtering or calculation logic | BEHAVIORAL | Structured verification step |
| 4 | Formatting/Prompt Adherence | 48365 | Using wrong tags (\<|python_interpreter\>) instead of markdown code blocks | BEHAVIORAL | Explicit output contract for code blocks |

## Changes made this iteration (one row per edit — aim for MULTIPLE classes, incl. a NEW tool when a cluster needs one)
| cluster | edit class | file / tool | what & why it generalizes | protects passing? |
| --- | --- | --- | --- | --- |
| Type Mismatch | Contract | prompt.md | Explicitly require using native Python types (int, float, datetime) for Excel values | Yes: 32902, 48745 already do this |
| Range/Coverage | Structure | task_template.md | Add a mandatory range-check step in the interaction contract | Yes: 32902, 48745 are simple enough |
| Logic Error | Structure | task_template.md | Strengthen the verification code requirement to print actual cell values | Yes: passing tasks already verify |
| Formatting | Contract | prompt.md | Explicitly forbid XML/special tags; require ONLY ```python blocks | Yes: 32902, 48745 use markdown |

## Verify-the-fix (one line per change: the trace it targets → what the guard/computation/new-tool now does on those exact inputs)
- 32438: wrote time as str "18:08:00" → will now write as datetime.time object; passing 32902/48745 already use numeric/date types.
- 54638: only filled 5 of 9 unique values → will now explicitly check if the number of written cells matches expected unique count.
- 48365: used \<|python_interpreter\> → will now use ```python as mandated by the explicit contract.

## Process & features used
- Subagents: Used a diagnosis agent to cluster failures.
- Prior iterations: Baseline seed.

## Good things to PRESERVE (do not let a future iteration undo these)
- Use of pandas/openpyxl for manipulation.
- Saving to exact output_path.

## Deliberately skipped (cluster + why — already-passing / needs gold / infra noise)
- None.
