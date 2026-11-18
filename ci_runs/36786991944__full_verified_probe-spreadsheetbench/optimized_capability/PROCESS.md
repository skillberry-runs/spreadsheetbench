# PROCESS — what I did this iteration (explainability; REQUIRED)

Candidate cand_0001. The seed was EMPTY: prompt.md was blank, so no system message was sent, and the built-in task template was used. Baseline val = 0.450, i.e. 18/40 tasks. The metric is hard_no_recalc: the grader opens the output with openpyxl `data_only=True` and never recalculates.

## Ranked issue list (clusters by # failing tasks × trials, biggest first)
| rank | cluster | tasks | shared root cause | tag | planned change class |
| --- | --- | --- | --- | --- | --- |
| 1 | A. Formula strings written as answers | 37378, 37456, 46897, 53383, 53647, 54144, 55049, 55979, 56563, 6698, 7902, 8942, 9569 (13) | Asked for "a formula", the agent writes `=...` text into cells. The grader reads the cached value without recalculating, so it gets None | KNOWLEDGE (grader contract unknown to agent) | add sourced rule + output contract + worked example |
| 2 | B. Whole-sheet pandas rewrite / row offset / clobbering | 227-40, 48527, 39046, 50768, 43436, 80-42, 59196 (7) | `df.to_excel` shifts rows by the header/index offset, writes NaN, and overwrites cells outside the target; wrong pandas-to-Excel row mapping | KNOWLEDGE + BEHAVIORAL | contract (openpyxl in place, exact coordinates) + coordinate-mapping rule |
| 3 | D. Interpretation / logic (labels, pre-filled examples, float threshold, append semantics) | 51-12, 80-42, 39046, 59196 (overlap with B) | Agent never inspects the real cells, ignores pre-filled example answers, uses exact float `>=`, and decides "already done" instead of appending | BEHAVIORAL | ordered procedure in template (inspect → solve → verify → finish) + rules |
| 4 | C. Cached values lost by loading in formula mode | 267-18 | `load_workbook()` without data_only drops the cached values of the answer-range cells that hold original formulas | KNOWLEDGE | rule: always save the data_only copy |
| 5 | E. No verification / identical-code loops to 30 turns | many of the above | Template said "once that file exists, you are done"; there was no verify step and no finish signal | BEHAVIORAL | replace line with verify + "reply without code to finish" |

## Changes made this iteration
| cluster | edit class | file / tool | what & why it generalizes | protects passing? |
| --- | --- | --- | --- | --- |
| A | add sourced rule + reason; tighten output contract | prompt.md "How your work is graded" + Output contract #1 | States the grader's actual behavior (data_only, no recalculation, 2-decimal rounding, exact text) and requires computed literal values even when a formula, VBA or macro is requested. This holds for every task under hard_no_recalc | Yes. All 18 passers already write literal values, as their passing proves |
| B | contract (recommended method) + reason | prompt.md Output contract #2–#4 | Recommends openpyxl `data_only=True` in place, writing only answer_position at Excel coordinates. Says why to_excel fails, keeps pandas for reading, and covers creating a missing target sheet | Framed as a recommendation, not a ban. Passers whose to_excel output was correct stay correct under openpyxl. 402-43 (target sheet absent from the input) is covered by the create_sheet line |
| C | add rule | prompt.md Output contract #2 + "existing formulas" bullet | Load data_only. Read formulas from a second copy only; never save that copy | Neutral for passers |
| D | ordered procedure + rules | task_template.md "How to work" step 1–2; prompt.md "Getting the logic right" | Inspect real cells (headers, labels, pre-filled examples, max_row); use the examples as a test; float tolerance; append semantics; copy names exactly; "Unnamed: N" preview hint | Inspection is read-only; it does not change any passer's answer |
| E | replace an over-strong line; add finish signal | task_template.md steps 3–4; prompt.md "Finishing" | Replaces "once that file exists, you are done" with: reopen and verify, then reply with NO code to finish. This matches the adapter loop: a no-code reply after a solution ends the episode, and a verify round does not change the solution code | The adapter replays the code from the last round that changed the output, so verify rounds cannot overwrite a solution |
| all | role/goal line; worked example | prompt.md role line + `<example>` | A single compact example that pins the shape: load data_only, literal write, save, read back | — |

## Verify-the-fix
- A (37378, 46897, 56563, 8942): I replayed corrected solutions locally with the real `compare_workbooks` (`/tmp/dx/v/t*.py`). Pattern: openpyxl data_only, compute in Python, literal write, save. Each went from FAIL to PASS. The original trajectories wrote `=...` strings, which graded as None.
- B (227-40, 48527, 39046, 50768, 80-42, 59196): the same harness with the openpyxl in-place write at exact coordinates gave PASS. The agents' to_excel outputs had shifted rows or clobbered cells and FAILED.
- C (267-18): data_only load + save keeps the cached G1 value → PASS. A formula-mode load + save → G1=None → FAIL. Reproduced both locally.
- D (51-12): the float-tolerance comparison gives PASS. A plain `>=` misses the exact 110% row → FAIL (reproduced). For 80-42, appending after the last used row → PASS.
- E: cannot be replayed offline because it is model behavior. I checked it against the adapter source (lines ~1419–1460): a no-code reply after solution_code is set → break. Verify rounds decrement verify_left without changing solution_code.
- Template contract: the adapter's own `_task_template_error(cand_dir)` returns None, and `.format(...)` renders correctly.
- Blast radius: UNBOUNDED, because the prompt changes for all 40 tasks. Passing tasks most exposed: Sheet-Level passers that used to_excel (142-12, 382-10, 395-36, 402-43, 416-15, 463-17), which may now switch to openpyxl. I checked 382-10: the golden sets removed cells to None, which matches the new "set each removed cell to None" rule. I checked 402-43: Sheet2 is absent from the input, which the create_sheet rule covers.

## Process & features used
- Subagents / worktrees: none. Serial work, because the system instructions forbid Agent/Workflow unless the user requests them.
- Local replay harness against the vendored grader (`third_party/spreadsheetbench/evaluation/evaluation.py`) on init/golden pairs, to confirm each cluster's fix pattern before writing prose.
- Prior iterations: none. RUNMAP, LEDGER and rejected.jsonl are empty; this is the first iteration.

## Good things to PRESERVE
- The grader-contract section (data_only, no recalculation, literal values even when a formula is requested). It targets the largest cluster (13 tasks).
- Recommending openpyxl in place over to_excel, together with its reason.
- Template steps 3–4: verify, then finish with a no-code reply. Never restore "once that file exists, you are done".
- Pre-filled examples used as a test; float tolerance.

## Deliberately skipped
- Preview format changes ("Unnamed: N" headers, the 5-row limit): these live in the adapter, which is not editable. I mitigated them with prose instead.
- Task-specific logic for individual tasks (e.g. specific lookups): any such fix would be hardcoding. I covered them only through the general inspect/oracle procedure.
- I did not run a full evaluation, per the rules.

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
