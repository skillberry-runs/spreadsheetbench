# PROCESS — what I did this iteration (explainability; REQUIRED)

Fill this in as you work. It is the human-readable record of HOW this iteration was done and is snapshotted with the candidate, so anyone — and the next iteration via ./prior_iterations/ — can see your reasoning. Be concrete.

## Ranked issue list (clusters by # failing tasks × trials, biggest first)
| rank | cluster | tasks | shared root cause | tag (KNOWLEDGE / BEHAVIORAL / CAPABILITY-GAP) | planned change class |
| --- | --- | --- | --- | --- | --- |
| 1 | A: formula written instead of value | 37378, 46897, 53383, 53647, 54144, 55049, 55979, 56563, 6698, 7902, 8942, 9569, 37456 (~13) | Scorer reads data_only=True with no recalc, so an openpyxl-written formula reads back as None. The agent follows "give me a formula/VBA" literally. | KNOWLEDGE (grading contract) | CONTRACT in prompt.md |
| 2 | C: existing target/example values ignored or overwritten | 39046, 48527, 59196, 43436, 54144, 53383, 9569, 51-12 | The agent never reads the pre-filled cells / labels that define the expected output shape | BEHAVIORAL | procedure (task_template.md) + KNOWLEDGE (prompt.md) |
| 3 | B: pandas to_excel round-trip corrupts layout | 39046, 43436, 48527, 50768, 227-40, 80-42 | Header-in-row-1 assumption and iloc offsets shift rows; other sheets are dropped; the matrix axes were misread (50768) | KNOWLEDGE | prompt.md: write with openpyxl at explicit coordinates |
| 4 | E: no inspection, no verification, stuck loops | 39046, 43436, 80-42 (+ most of A/C) | "once that file exists, you are done" means writing in round 1-2 and never checking; the same silent code is repeated for 30 rounds | BEHAVIORAL | ordered workflow + verify step in task_template.md |
| 5 | D: specific knowledge gaps | 267-18 (fill color + formula cached value), 80-42 (append despite duplicates), 227-40 (copy example block incl. header), 55979 (verbatim labels) | Missing know-how | KNOWLEDGE | one bullet each in prompt.md |

## Changes made this iteration (one row per edit — aim for MULTIPLE classes, incl. a NEW tool when a cluster needs one)
| cluster | edit class | file / tool | what & why it generalizes | protects passing? |
| --- | --- | --- | --- | --- |
| A | CONTRACT | prompt.md "How the file is graded" | States the actual scorer semantics (values only, data_only, no recalc). Formula/VBA requests are answered with computed values. Applies to every task. | Yes: all 18 passers already write literal values |
| A/D (267-18) | KNOWLEDGE | prompt.md | Load the save-workbook with data_only=True so existing formula cells keep their values. Transform the cached value when changing a formula cell. | Yes: passers overwrite the target cells anyway |
| B | KNOWLEDGE | prompt.md "Write with openpyxl" | Explains the row offset of pandas (iloc i = row i+2), NA-string loss and dropped sheets. Recommends openpyxl cell writes. pandas is still fine for reading. | Yes: phrased as a preference; passers' pandas outputs were correct values anyway |
| C | KNOWLEDGE + BEHAVIORAL | prompt.md "Reading the task" + template step 2 | Existing values/examples are the spec, and the rule must reproduce them. Row/column labels define the cell meaning; check the matrix axes. | Yes: passing tasks have consistent examples, so the check is a no-op |
| D | KNOWLEDGE | prompt.md bullets | Fill colour via fgColor.rgb, copy verbatim labels, reproduce the example layout with its header, append even if the rows repeat, float tolerance | Bounded: each bullet only triggers on its situation |
| E | BEHAVIORAL | task_template.md "How to work" | Inspect → rule check → write values → reopen and print the answer range → no-code reply to end. Fits the adapter's VERIFY_TURNS=3 and its no-code-ends-loop rule. | Yes: adds 1-2 rounds; far below the 30-round cap |

## Verify-the-fix (one line per change: the trace it targets → what the guard/computation/new-tool now does on those exact inputs)
- A: 37378 wrote `'=IF(B{row}<>"", COUNTA($B$2:B{row}), "")'` and the feedback says the answer cells hold FORMULAS. The prompt now says a written formula reads back empty and scores zero, so the agent should compute COUNTA in Python and write ints. Checked against evaluation.py:160 (data_only=True) and compare_cell_value (None vs number → False).
- A/D: 267-18. Init G cells are formulas, and the gold G2 is `//` + computed string. The prompt's "transform its cached value and write the literal result" plus the data_only load matches exactly what gold holds.
- B: 50768. `header=None` + iloc wrote values one row off, and the axes were swapped (gold H12='4, 6', F14='1, 3, 5'). The prompt's pandas row-offset rule plus the "(row label, column header) pair … check which axis" bullet targets both errors. The template's step 1 prints the labels around the range.
- C: 39046. The existing column shows per-row counts, gold [2,2,0,2,2]; the agent wrote a total. Template step 2 ("rule must reproduce every existing example value") would reject a total rule. The same applies to 43436 (existing H pattern), 53383 (Matched/Not Matched) and 9569 (AO9 example).
- C: 59196. The header is in row 2. The "Unnamed: n means the real header sits lower" bullet plus the openpyxl inspection targets this.
- D: 80-42. The gold appends from row 4000 despite the duplicates. The "Always carry out the requested operation … even when similar rows already exist" bullet targets this. 227-40: the gold includes the header row; the "reproduce that layout, header row included" bullet targets this. 55979: the gold uses the sheet name 'Supplier_1'; the verbatim-label bullet targets this.
- E: 39046/43436/80-42 repeated identical silent code for up to 30 rounds. The template says "fix the cause rather than re-sending … Print something in every block". The verify step ends with a no-code reply, which the adapter treats as done (adapter.py: `if solution_code: break`).
- Template placeholder contract validated with the adapter's own `_task_template_error(cand_dir)` → None; `.format(...)` renders cleanly.

## Process & features used
- Subagents / worktrees / parallel features used (or: "serial fallback because …"): none. The work was serial because the session policy forbids AgentTool/workflows unless the user requests them. Diagnosis was done by dumping all 40 traces, then diffing init vs golden cells for each failing task.
- Prior iterations I read from ./prior_iterations/ + ./RUNMAP.md (which, and what I learned): none exist (first iteration; seed capability empty; no rejected.jsonl).

## Good things to PRESERVE (do not let a future iteration undo these)
- The values-not-formulas grading contract (the largest cluster; applies to every task).
- The verify-then-no-code-reply ending (matches the adapter's loop semantics).
- The placeholder layout (all six required + {max_turns}) of task_template.md (validated).

## Deliberately skipped (cluster + why — already-passing / needs gold / infra noise)
- No task-specific rules for individual semantic misreads, such as the exact counting rule in 43436 or 51-12. They are covered only by the generic "reproduce the examples" check, because hardcoding them would be answer-leaking.
- No infra cluster: every rollout had error=None.

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
