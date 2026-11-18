# PROCESS — what I did this iteration (explainability; REQUIRED)

EMPTY SEED iteration. `prompt.md` was 0 bytes and `task_template.md` did not exist. The agent
was running on the adapter's built-in default first-user-message only (visible verbatim as
`trace[0]` in every trajectory) and **no system prompt at all**. I created both files.

Baseline: val 0.600 — 24 pass / 16 fail of 40.

## What the baseline agent was actually reading

`trace[0]` of every trajectory is the adapter default. Two properties of it drive most failures:

- It ends with **"once that file exists, you are done"** — an explicit instruction to stop at
  file-existence rather than at correct values. This is the anti-pattern the task brief warns
  about, and it is in the shipped default.
- It describes the fields but states **no output contract** (no typing rule, no "don't touch
  cells outside the range", no formula guidance) and **no procedure**.

Measured consequences across all 40 traces (I scripted these counts, they are not impressions):

| signal | count |
| --- | --- |
| tasks whose **round-1** block already writes `output_path` (zero inspection) | **38 / 40** |
| assistant blocks containing `print(` anywhere | **6 / 40 tasks** |
| execution results that are `[Code executed successfully with no output]` | **~29 / 30 rounds** on every long task |
| tasks that burn all 30 rounds re-sending a **byte-identical** block (25–27 dups) | 16 |

## Ranked issue list (clusters by # failing tasks × trials, biggest first)

| rank | cluster | tasks | shared root cause | tag | planned change class |
| --- | --- | --- | --- | --- | --- |
| 1 | **pandas round-trip destroys the file** | 341-40, 535-20, 48924, 55817, 5835, 44913, 42354, 51359, 38985, 46646 (10) | `pd.read_excel` → `df.to_excel` regenerates the whole sheet: coerces text→int/date, shifts rows via header/index, drops other sheets, writes `NaN`/`Unnamed: 3`. Scorer says so literally: *"955 cells were CHANGED although the expected value is the cell's own original input"*, *"700 cells hold int where str was expected"* | KNOWLEDGE (+CONTRACT) | output contract + worked example (`prompt.md`) |
| 2 | **blind write, never inspects the real grid** | all 16 (38/40 write on round 1) | The `spreadsheet_content` preview shows 5 rows with pandas' invented headers; real sheets have title rows, side-by-side tables, blank leading rows. Agent guesses indices from the preview | BEHAVIORAL | ordered procedure, inspection as Step 1 precondition (`task_template.md`) |
| 3 | **never verifies the written values** | all 16 | Nothing in the default asks it to re-open the output; "once that file exists, you are done" actively tells it not to. So an off-by-one row offset is never detected | BEHAVIORAL (skipped step) | mandatory Step 3 + explicit checklist (`task_template.md`) |
| 4 | **30 rounds of identical resubmission** — *downgraded, see caveat* | 33722, 48924, 51359, 42354, 46646, 38985, 53647 (7) | Every block ends in a silent `wb.save(...)`, so the result is always `[Code executed successfully with no output]`. The agent reads that as "nothing happened" and resubmits the same code 26×. **CAVEAT I verified: 11 PASSING tasks show the identical churn (30-round churn = 11 passing vs 7 failing).** So the churn is mostly a harness artifact (the loop-break never fires while the block keeps re-saving the output) and is NOT itself a cause of failure. I kept only the cheap, additive part of this fix and did NOT build a procedure around it | KNOWLEDGE + recovery guidance | state what the message means + "change approach, not whitespace" (`prompt.md`) |
| 5 | **array formula written as a plain string** | 33722 | `=MEDIAN(IF($C2:$C$12<=0.01,...))` is a CSE formula; as a plain string it evaluates against one cell → all 5 cells "a different value of the right type" | KNOWLEDGE | narrow additive rule (`prompt.md`) |
| 6 | **formula that resolves to an Excel error** | 53647, 42354 | Scorer: *"1 cell holds an Excel error text — an unresolved formula was written out as its error string"*, *"str where float was expected"* | KNOWLEDGE | narrow additive rule (`prompt.md`) |
| 7 | **blank-cell convention `""` vs empty** | 44913, 42354, 53647 | Wrote `""` into cells the reference leaves genuinely empty; coverage shows *"your output has a value in 12 of them; the expected has 3"* | KNOWLEDGE (+CONTRACT) | one contract line (`prompt.md`) |
| 1b | **SHEET-NAME KILL (subset of cluster 1, distinct mechanism)** | 42354, 51359, 5835 | `pd.read_excel(path, sheet_name='Query')` returns a DataFrame that no longer knows its name, so `to_excel` writes a single sheet called **`Sheet1`**. When `answer_position` names a sheet the grader cannot find it and scores 0 **without comparing any value**. Diagnostic signature, which I confirmed: 42354 and 51359 have full matching coverage and **no MISMATCH line at all** in their feedback | KNOWLEDGE | explicit first bullet under FACT 1 + checklist item 4 |
| 8 | **premature ROUNDING of the stored value** | 46646, 49036, 11842 | Instruction describes *display* (decimal places, commas, "show as") and the agent rounds the **value**. 46646 applied `round(v,9)` and only 2 of 12 values survived; 49036 rendered `f"{x:.0%} WIN RATE"` as a string | KNOWLEDGE | number-format-vs-value contract lines (`prompt.md`) |
| 10 | **multiple code fences in one reply** | 41978, 5835 | Only the FIRST ```python fence is executed; later ones are discarded unrun. Both tasks put their *verification* block second and silently lost it, so they believed they had inspected when they had not. 0 passing tasks emit multiple fences | KNOWLEDGE (adapter mechanic) | interaction-contract line (`task_template.md`) |
| 11 | **matched literal label that is not in the searched column** | 379-36 | The label quoted in the instruction (`"Georgia Its Tax"`) is the column-**K header**; column E holds `Payee`. The `==` test matched nothing, so the range came back byte-identical | BEHAVIORAL | Step 1 addendum: confirm the literal occurs in the column you search |
| 9 | **Sheet-Level range read as a fill target** | 341-40, 535-20, 379-36 | `answer_position` for Sheet-Level is the *maximum permitted* region, not cells to fill. 341-40 rewrote all 955 cells it was merely allowed to touch | KNOWLEDGE | field-semantics line (`task_template.md`) |

**No ENVIRONMENT fault found.** I checked for it explicitly: `rollout.error` is `None` on all
40 tasks, there is no repeated infra error, and the only import failure in the whole set is one
task's own bad import (`from openpyxl.worksheet.formula import Formula` in 11842) which it
self-corrected next round. The 16 failures are genuine capability failures.

## Changes made this iteration

Two files created from scratch. `prompt.md` = system message (facts + output contract);
`task_template.md` = first user message (field semantics + ordered procedure). I chose that
split deliberately: **durable knowledge/contract** goes in the system prompt, **per-task
procedure and the interaction contract** go in the template where the placeholders are, so the
verify snippet can interpolate the task's real `{output_path}`.

| cluster | edit class | file / tool | what & why it generalizes | protects passing? |
| --- | --- | --- | --- | --- |
| 1 | tighten output contract + worked example | `prompt.md` "FACT 1" | Names the mechanism (regenerates the file: coerces types, shifts rows, drops sheets) and gives the 5-line openpyxl-in-place idiom. Stated as a *default with a condition* — pandas may still write if you reproduce every sheet and original value | see blast radius below |
| 2 | ordered procedure | `task_template.md` Step 1 | "Your first block only prints. Do not write output_path yet." Inspection is a precondition of Step 2, not advice | yes — additive round |
| 3 | pre-finish checklist | `task_template.md` Step 3 + 5-item list | Re-open the written file, print `coordinate/repr(value)/type` over the answer_position range; Step 4 (finish) is gated on Step 3 printing clean | yes |
| 4 | recovery guidance + knowledge | `prompt.md` last section | States that `[Code executed successfully with no output]` means success, and "change the approach, not the whitespace" | yes |
| 5 | additive narrow rule | `prompt.md` FACT 2 | "Never write an array/CSE formula as a plain string — compute it in Python." Conditioned on array formulas only | yes (no passer writes one) |
| 6 | additive narrow rule | `prompt.md` FACT 2 | "A formula that can resolve to an error is a zero — if it might error on any row, compute in Python" | yes |
| 7 | contract line | `prompt.md` | "Blank means empty: write `None`. Only write `\"\"` if the instruction literally asks for it" | conditioned on the literal ask |
| 8 | contract line | `prompt.md` | "Apply precision to the stored value, not only the display format — the grader reads the stored value" | yes |
| 9 | field semantics | `task_template.md` | Cell-Level = exact cells to fill; Sheet-Level = a **budget**, not a fill target | yes |
| — | role/goal line | `prompt.md` head | "graded by a program… value and type. A beautiful explanation over a wrong cell scores zero" | yes |
| — | **deleted** the harmful default line | `task_template.md` | Removed "once that file exists, you are done" and replaced it with "finishing fast is worth nothing, only the cell values are scored". This is a *deletion of text shown to be counterproductive* — cluster 3 exists because of it. No constraint was lost: the file-writing requirement survives as Step 2 + `output_path` field semantics | yes — it can only add verification |

Improvement types applied, per the capability SKILL's menu: #1 positive rewrite, #2 rule+reason,
#4 sourced additive rule, #5 worked example, #6 restructure, #7 role/goal line, #8 tighten the
output contract — seven of the nine classes, plus the ordered-procedure and recovery levers from
the brief. Not a single lever repeated across clusters.

## Verify-the-fix (one line per change)

- **C1 (341-40):** trace writes `df.to_excel(output_path, index=False)` after `pd.read_excel`;
  scorer returns *"700 cells hold the CORRECT value stored as text instead of as a number/date"*
  and *"955 cells were CHANGED although the expected value is the cell's own original input"*.
  With FACT 1's openpyxl-in-place idiom the agent assigns only column Q and the other 955 cells
  keep their original stored types — exactly what the scorer says it wanted.
- **C1 (535-20):** `df[cols_to_keep].to_excel(...)` dropped 253 expected values and coerced 4
  str→int; deleting columns via `ws.delete_cols()` in place leaves the rest byte-identical.
- **C1 (5835 / 51359):** `read_excel(header=None)` + `to_excel(header=False)` is the row-shift
  trap; 5835 filled 10 of 17 cells. Addressed by the same in-place idiom.
- **C2 (46646, 38985):** these are the only 2 of 40 that *did* print the grid first — and both
  then needed it (46646's data was on row 8 / col O, nothing like the preview). The other 38
  never printed. Step 1 makes that first print unconditional.
- **C3 (5835):** wrote to `df.iloc[i,2]` for `i in range(2,19)` targeting C3:C19 — a one-row
  offset that produced 7 empty cells. Step 3's `print(c.coordinate, repr(c.value))` over
  `C3:C19` surfaces exactly that; checklist item 1 then sends it back to Step 2. Verified the
  snippet runs: I rendered the template with `.format()`, extracted both code blocks and
  executed them against a synthetic multi-sheet workbook — Step 1 printed the grid and every
  sheet; Step 3 printed `D8 80 int … D11 110 int` plus `SHEETS: ['Sheet1','Data']`.
- **C4 (33722):** 30 blocks, 26 byte-identical to their predecessor, every result
  `[Code executed successfully with no output]`. The new lines tell it that message means
  success and forbid resubmission; Step 3 also converts those silent rounds into informative
  ones, which removes the cause rather than scolding the symptom. **But I checked the control
  group and it disconfirms treating this as a failure cause: 11 passing tasks churn the same
  way.** So this edit is 3 sentences, not a procedure — the expected gain is that Step 3 makes
  the wasted rounds informative, not that churn itself stops.
- **C5 (33722):** wrote `=MEDIAN(IF(($C{row}:$C$12<=0.01)*...))`; all 5 cells wrong. Contract
  now routes array formulas to a Python-computed literal. **Scorer-checked:** 42198 passes
  writing *only* `=IF(COUNTIFS(...))` strings, so formulas ARE recalculated — the defect is
  specifically CSE semantics, not formulas. I did not ban formulas; that would have regressed
  31011, 39515, 41589, 42198, 49801, 52807, 55468.
- **C6 (53647):** `=IF(ISNUMBER(C7), C$3/C7, ...)` → scorer *"1 cell holds an Excel error text
  … str where float was expected"*. Rule routes error-prone formulas to Python values.
- **C7 (44913):** `else ""` → *"your output has a value in 12 of them; the expected output has
  a value in 3"*. `None` produces the 3-value coverage the scorer expects. Conditioned on "only
  if the instruction literally asks for `\"\"`", which is what 44913's own instruction does *not*
  require despite its `blank/empty ("")` phrasing — hence the qualifier rather than a flat rule.
- **C9 (341-40):** Sheet-Level `A1:Q701`; agent treated all 11917 cells as writable and changed
  955. Template now defines Sheet-Level as a permission budget.
- **C1b (42354, 51359) — reproduced end-to-end, the strongest single finding.** I built a
  2-sheet workbook, ran `pd.read_excel(p, sheet_name='Query')` → `df.to_excel(out)` and got
  `input sheets ['Sheet1','Query']` → `output sheets ['Sheet1']`. The named sheet is gone, so
  the grader scores 0 before comparing anything. This explains a signature that had puzzled me:
  42354 and 51359 report *full matching coverage and no MISMATCH line at all*. Both are now
  covered twice over — the first bullet under FACT 1 states the mechanism, and checklist item 4
  makes the agent assert the sheet still exists in the file it wrote.
- **C8 (46646):** applied `round(v, 9)` to full-precision floats; only 2 of 12 values survived
  (10 cells "a different value of the right type"). The contract now separates *number format*
  (display) from *value* and says not to round unless the instruction asks for a rounded value.
  49036 wrote `f"{x:.0%} WIN RATE"`, the same display-vs-value confusion.
- **C10 (41978, 5835):** verified by counting fences — 41978 emitted 3 and 5835 emitted 2 in a
  single reply, and 0 passing tasks emit more than one. Their second (verification) block never
  ran. The template now states that only the first fence executes, which makes Step 1 and Step 3
  genuinely separate rounds rather than two blocks in one reply.
- **C11 (379-36):** confirmed from the preview that `"Georgia Its Tax"` is the column-K header
  while column E holds `Payee`, so `cell_e.value == "Georgia Its Tax"` could never be true and
  the range came back byte-identical. Step 1 now requires confirming the literal actually occurs
  in the column being searched.

## Blast radius per edit

- **BOUNDED / additive** — clusters 2,3,4,5,6,8,9, the role line, and the deletion. They add a
  round, a print, or a rule that fires only under a condition absent from the passing traces
  (no passing task writes an array formula, an error-producing formula, or relies on
  file-existence-means-done). The 24 passers already satisfy the contract; verification cannot
  change a correct value into an incorrect one.
- **BOUNDED-by-condition** — cluster 7. Phrased "only write `\"\"` if the instruction literally
  asks for `\"\"`", so 353-29 / 41265 / 48921 / 51249 (the passers that write `""`) keep their
  behavior where their instruction asks for it.
- **UNBOUNDED — one edit, cluster 1, declared honestly.** "Prefer openpyxl in place" changes the
  *method* on currently-passing tasks that use `to_excel`: 13-1, 297-42, 18645, 47827, 58147,
  353-29, 48588, 48608, 48921, 32902, 41265, 56920, 59639. I read all 13. Two reasons I kept it:
  (a) the multi-sheet passers (13-1, 297-42, 18645, 47827, 58147) already reproduce every sheet
  via `ExcelWriter`, which is exactly the escape hatch the rule states, so their behavior is
  permitted unchanged; (b) for the single-sheet passers, openpyxl-in-place is *strictly
  value-preserving* — it writes the same computed values while additionally leaving untouched
  cells alone, so it cannot turn a correct cell incorrect. The residual risk is a task whose
  gold answer *depends* on pandas' text→number coercion; I found no evidence of one, and the
  scorer's own feedback argues the opposite (*"where a str is expected, KEEP the original text —
  do not parse or convert it"*). This is the iteration's main measured bet.

## Process & features used

- Subagents / worktrees / parallel features used: two parallel read-only diagnostic subagents
  (fast-fail group: 341-40, 379-36, 41978, 44913, 49036, 55817, 5835, 11842; round-cap group:
  33722, 38985, 42354, 46646, 48924, 51359, 53647, 535-20), plus my own scripted cross-trace
  counting (round-1-writes, print-frequency, duplicate-block counts, `to_excel` vs `.save`,
  array-formula detection, multi-sheet crossing). The scripted counts are what I actually
  relied on for ranking — they are reproducible and in the table above.
- Placeholder safety: asserted all six required placeholders present, no invented ones, and
  `.format()` renders without `KeyError` while the `{{name}}` f-string braces survive.
- Prior iterations read: `./prior_iterations/` and `RUNMAP.md` are empty (iteration 1);
  `rejected.jsonl` has no entries to avoid. Nothing to build on, nothing refuted yet.

## Good things to PRESERVE (do not let a future iteration undo these)

- **Formulas are recalculated by the scorer** — proven by 42198 (passes writing only formula
  strings). Never ban formulas wholesale; only CSE/array and error-prone ones.
- **Step 3 verification and Step 1 inspection.** 38/40 traces wrote the graded file blind on
  round 1. Any future edit that lets the agent finish without re-reading the written range
  re-opens clusters 2 and 3.
- **Never restore "once that file exists, you are done."**
- The `{output_path}` interpolation inside the Step 3 snippet — it is why the check is concrete
  rather than advisory.

## Deliberately skipped (cluster + why)

- **11842** (1 of 96 cells, a number LOWER than expected) and **49036** (1 cell, percent-format
  wording) are single-cell near-misses on ambiguous instructions. The precision contract line
  may help; I did not add task-shaped wording for either, because encoding a specific
  rounding/percent convention would overfit and risks the precision-sensitive passers.
- **379-36** ("whole number vs pennies" on a range the scorer reports as byte-identical
  *and* 2-cells-mismatched) — the instruction's intent is genuinely under-determined; the
  in-place + verify edits are the general help available without guessing the gold.
- No edit hardcodes a task id, target range, date, value, or expected answer.
