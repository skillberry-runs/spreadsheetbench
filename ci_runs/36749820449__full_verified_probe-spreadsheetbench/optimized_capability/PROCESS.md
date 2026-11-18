# PROCESS — what I did this iteration (explainability; REQUIRED)

Iteration cand_0001: the first capability, written from scratch. Baseline: empty prompt.md, built-in template, val 0.450 (18/40).
Metric: hard_no_recalc. The grader loads the output with data_only=True and does no recalculation.

## Ranked issue list (clusters by # failing tasks × trials, biggest first)
| rank | cluster | tasks | shared root cause | tag | planned change class |
| --- | --- | --- | --- | --- | --- |
| 1 | A. Formula written instead of a value | 37378, 46897, 53383, 55049, 6698, 7902, 8942, 55979, 56563, 37456, 53647, 54144, 9569 (~13) | The agent writes "=..." with openpyxl, which has no cached value, so the grader reads None. The instruction often says "formula"/"VBA". | KNOWLEDGE (grading contract) | CONTRACT rule in prompt.md + restated in the template's solve step |
| 2 | B. Rebuilt via to_excel / row-index shift | 48527, 50768, 227-40, 80-42 | pandas index ≠ Excel row, so the header row is dropped and existing cells are overwritten | BEHAVIORAL (method) | METHOD: openpyxl write-in-place pattern + index→row mapping rule |
| 3 | C. Example cells ignored / range not fully filled | 39046, 59196, 54144, 227-40 | Pre-filled cells in the target range are the gold pattern, but the agent wrote a total / partial / None. Headers were on row 2. | KNOWLEDGE | "examples are the spec" + "fill every cell" + "inspect beyond the preview" |
| 4 | D. Wrong interpretation, not verified | 43436, 51-12, 267-18 | Wrong aggregation (per-row instead of per-category×month), wrong color match (red counted as yellow) | BEHAVIORAL | VERIFY step: re-open the output and print the answer range; matrix-aggregation note; rgb[-6:] color rule |
| 5 | E. Repetition loops until 30 turns | 227-40, 37456, 2768 (pass), others | "Code executed with no output", so the agent resubmits the same code. The built-in template says "once that file exists, you are done". | BEHAVIORAL (loop) | Template: ordered inspect→solve→verify→finish; reply without code to stop; never resend identical code |

## Changes made this iteration
| cluster | edit class | file / tool | what & why it generalizes | protects passing? |
| --- | --- | --- | --- | --- |
| A | CONTRACT | prompt.md "How your output is graded" + task_template step 2 | States why formulas score None. Always write computed literal values, even for formula/VBA asks. Recompute any source formula cell whose cached value is missing or an error. Applies to any task under no-recalc scoring. | Yes. All 18 passing traces already write values. |
| B | METHOD | prompt.md "Method" code pattern | Read with a data_only copy, write the target cells on the original workbook, save. Explicit mapping: DataFrame index i = Excel row i+2 (header) or i+1 (header=None). | Worded as "prefer", not "forbid". The 13 passing to_excel users keep a valid path. Blast radius MODERATE: the output-writing style changes. |
| C | KNOWLEDGE | prompt.md "Understand" 1–4 | Existing values are examples to reproduce. Fill every cell. Per-row criteria. Header row when the range includes it. Headers may sit below row 1. | Yes. It only adds inspection/consistency checks. |
| D | BEHAVIORAL + KNOWLEDGE | prompt.md "Verify" + Understand 5–6 | Re-open the output with data_only and print the answer range. Excel semantics notes (EOMONTH, case-insensitive COUNTIF, blank → None). Colors compared on the last 6 hex digits. | Yes. |
| E | BEHAVIORAL | task_template.md tail | Replaces "once that file exists, you are done" with a 4-step procedure. Finish = plain-text reply (the adapter stops on no-code after a solution exists). Do not resend identical code. | Yes. It also cuts the 30-turn loops seen on passing 2768. |

## Verify-the-fix (the trace each change targets → what the capability now does on those inputs)
- A / 55979, 53647, 54144, 37456, 9569: each trace wrote `ws[c] = "=..."` and got None. The contract now requires Python-computed literals. I checked the golden values are plain numbers/strings (e.g. 8.75, 10; 37.46, 48.02), so literals match. 56563: the init source cell is '#NUM!'; the recompute-from-inputs rule covers it.
- B / 50768: `to_excel(header=None)` shifted the grid. The pattern writes by coordinate (H12, F14, G14), and the expected values '4, 6' / '1, 3, 5' / '2' are strings, which the format rule covers. 48527: write-in-place keeps D2/D3, which already match.
- C / 39046: F2:F6 init holds examples 2, 2, 0. The rule "computed values must reproduce the examples" rejects the grand-total answer. 59196: H3 = 'D' example, headers on row 2, handled by "headers may sit on row 2".
- D / 267-18: I verified the init fills: G1 = FF00B050 (green), G2 = FFFFFF00. The yellow = 'FFFF00' rule excludes G1. 43436: the note on one aggregated value per (row, column) plus EOMONTH date semantics targets the I2:K6 dept×month count.
- E: the template renders with all 7 placeholders. `adapter._task_template_error(cand)` returned None, and `_read_system_prompt` returned 5868 chars.

## Process & features used
- Serial fallback: the session instructions forbid the Agent tool / workflows unless the user requests them. The analysis used read-only python scripts in /tmp/me_cmp comparing init vs golden workbooks and the trajectories.
- Prior iterations: none (this is the first candidate). RUNMAP / rejected.jsonl hold no prior rejects.

## Good things to PRESERVE
- The never-write-formulas contract (it decides pass/fail under hard_no_recalc).
- The verify printout + "reply without code to finish" (prevents 30-turn loops).
- Examples-in-range-are-the-spec.

## Deliberately skipped
- 80-42 (large multi-sheet consolidation, 8512 cells). This is a capability/complexity issue. The method edit may help, but it is not specifically targeted.
- 51-12 (obscure "increase marker" logic): only the generic examples/verify guidance applies. There is no task-specific hint, to avoid overfitting.
- A custom tool/helper file: the adapter exposes only prompt.md/task_template.md, so no tool lever is available.

---

# DIAGNOSIS.json — machine-readable diagnosis (OPTIONAL but recommended)

In addition to PROCESS.md, you may write a DIAGNOSIS.json file to make your diagnosis machine-readable for the dashboard. This is optional; if absent, the dashboard will parse PROCESS.md tables when present, or show only outcome data.

The schema:
```json
{
  "candidate": "cand_NNNN",
  "headline": "Brief summary of this iteration's strategy",
  "clusters": [
    {"id": "A", "name": "Short cluster name",
     "detail": "Root cause explanation", "tasks": ["task-id", ...],
     "scope": "BOUNDED|WIDESPREAD|SYSTEMIC", "latent": false,
     "tag": "KNOWLEDGE|BEHAVIORAL|CAPABILITY-GAP"}
  ],
  "edits": [
    {"id": "E1", "title": "What this edit does",
     "files": ["prompt.md"], "lever": "CONTRACT|KNOWLEDGE|BEHAVIORAL|...",
     "clusters": ["A"], "blast_radius": "BOUNDED|MODERATE|WIDE",
     "verified": "How you tested it"}
  ],
  "skipped": [{"title": "What was skipped", "reason": "Why"}],
  "techniques": ["technique 1", "technique 2"]
}
```

Validation is advisory only and never blocks an iteration. Warnings are recorded when:
- A task ID in clusters[].tasks is not in the val split
- An edit references a cluster ID that does not exist
- An edit references a file that does not exist in the candidate
