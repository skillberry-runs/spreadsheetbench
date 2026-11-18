# PROCESS — iteration cand_0003 (explainability; REQUIRED)

Parent/champion: **cand_0001** (val 0.900). cand_0002 was REJECTED (Δ+0.000, fixed={227-40,
267-18}, broke={2768, 51-12}) and its whole batch reverted. This iteration starts from cand_0001's
text and re-derives cand_0002's two wins with the two regression mechanisms removed, then adds
three fixes it never tried.

**No environment fault.** All 40 rollouts have `error: null`, executed sandbox code, and produced
an output file at `output_path`. Nothing to hand back as infra; the 4 failures are prose-fixable.

**Verification constraint (differs from cand_0002).** The benchmark `init`/`golden` workbooks are
**not reachable** from this sandbox — `/mnt/data/spreadsheet/<id>/` holds only the one unrelated
task id and a search for `*_golden.xlsx` finds nothing. cand_0002 verified by executing against
gold; I cannot. Every claim below is backed by one of: a quoted trace line, the scorer's own
`feedback` string, or code I executed against a synthetic workbook reproducing the task's
structure. Where a claim is directional rather than exact, I say so.

**Subagents: none used** (session config forbids AgentTool/workflows unless requested).

## Ranked failure clusters (4 failing tasks = 4 distinct root causes, + 2 latent)

| # | cluster | tasks | tag |
| --- | --- | --- | --- |
| A | an INPUT formula inside `answer_position` is erased by `wb.save()` when left untouched | 267-18 | CONTRACT + KNOWLEDGE |
| B | a worked-example block's **geometry** (its header row) is not reproduced in the output block | 227-40 | KNOWLEDGE / worked example |
| C | "open at end of month" tested against the month's FIRST day instead of its LAST | 43436 | KNOWLEDGE |
| D | a literal reading of the prose fills 1 of 4 cells; the agent found the right reading and discarded it | 48527 | DECISION |
| E | the audit declares "clean" on types alone — it cannot see a wrong number | 43436 (+ latent, all) | STRUCTURE |
| F | `isinstance(v,(int,float,bool,str))` mis-flags every date/time as `FORMULA-OBJECT` | latent (416-15, 80-42, 9726) | provably-wrong text |

## Edits kept (7) — lever, verify line, blast radius

### 1. `prompt.md` Rule 1, new subsection "A formula the INPUT put there is unscoreable too" → A
- **Lever:** CONTRACT at point of use (the contract is the *final state* of each cell, not who
  wrote it) + a pasteable two-workbook idiom.
- **VERIFIED:** 267-18's own audit printed
  `G1: value='=CONCATENATE("[","""",E1,...)' type=str` — the agent *saw* the formula and left it;
  the scorer says "FAILED because the answer cells hold FORMULAS". I executed naive vs shipped on a
  synthetic twin: untouched reads back `None` (**ERASED**); the shipped idiom reads back the cached
  literal `'[alpha]'`. **Agent would have done differently:** carried G1's cached value across as a
  literal instead of trusting "untouched = preserved".
- **Blast radius: BOUNDED.** Fires only over *cells I was not asked to change* whose **input** value
  starts with `"="` — deliberately narrower than cand_0002's version, which looped all TARGET_CELLS.
  Note **7902 passes with `COUNTS: {'FORMULA': 16, 'ok': 12}`**: its 16 input formulas are outside
  the graded cells and this edit does not touch them.

### 2. `prompt.md` new Rule 2b — demo-block **GEOMETRY only** → B
- **Lever:** KNOWLEDGE + worked example (a comment block showing the row arithmetic).
- **VERIFIED:** 227-40's trace prints the demo block at `A9:E12` with `A9='Site Name'` (a header
  row) under `C7="The Result I'm after"`. I counted it: **4 rows × 5 cols, exactly 17 non-empty
  cells** — and the scorer says "the expected output has a value in 17" of the 20-cell `A14:E17`.
  Shape and cell count both match exactly. The trace mapped source rows 2-5 → 14-17 with no header
  and filled 12. **Agent would have done differently:** header on row 14, the 3 result rows on 15-17.
- **Blast radius: BOUNDED, deliberately re-gated.** cand_0002's Rule 2b is the prime suspect for
  breaking **2768**, so this version (a) fires only when `answer_position` is an **empty multi-row
  block** with a **separate** demo block, and (b) carries an explicit counter-clause: *"Do not turn
  this into 'pre-filled cells prove my reading is right'."* I scanned all 40 previews for
  demo/expected wording — 4 hits: 227-40 (failing) + **2768, 395-36, 48588** (passing). The gate
  excludes all three: 2768's `H2:H18` **is** `answer_position` and is **fully pre-filled**
  (`H2=50, H3=20, H4=0…`), so "Expected outcome" is the answer column's own header, not a separate
  block; likewise 48588's `B1='Unique ID (Expected Result)'`; 395-36's expected block is a separate
  **sheet** and its target sheet `MyResult` does not yet exist.

### 3. `prompt.md` Rule 4, new subsection on period-window endpoints → C
- **Lever:** KNOWLEDGE, as a copyable two-line predicate.
- **VERIFIED:** the trace's comment is
  `cond1 = (rec['closed'] is None) or (rec['closed'] >= first_day)`; the scorer says "5 cells hold a
  number HIGHER than expected". `closed >= first_day_of_P` is strictly more permissive than
  `closed > last_day_of_P`, so the trace's rule can only produce counts that are **too high** —
  exactly the reported direction. Executed on the visible records: dept B / May 2022 → 3 (trace) vs
  2 (shipped). I also reconciled the shipped predicate against the sheet's own anchor column H
  `Open as of today`: **dept A → 1, dept B → 2, both matching** the sheet. **Agent would have done
  differently:** compared against the month's last day.
- **Blast radius: BOUNDED to 1 task.** cand_0002 shipped a *general* `<` vs `<=` phrase→operator
  table — the prime suspect for breaking **51-12**, whose passing trace hinges on a numeric threshold
  `val_j >= ref*1.1 - 1e-9`. This version is scoped to **calendar-period windows over a
  created/closed date pair** and says nothing about comparison operators in general. A scan of all 40
  previews for created/closed/open-period wording returns **exactly one task: 43436**.

### 4. `prompt.md` Rule 2 — "if your reading produces almost nothing, the reading is wrong" → D
- **Lever:** DECISION, as an **additive narrowing condition** on Rule 2 — never a loosening. Rule 2's
  "don't invent values" stands; this only says an empty range is not a legal answer to a Cell-Level
  task.
- **VERIFIED:** 48527's trace reasons its way to the right answer and throws it away — *"Maybe
  'unique text' means the one value among A, B, C that is not 'No'? … This pattern fits the 'unique
  text' description better than 'A == B'"* — then writes `None` over the pre-filled `D2='Apple'`.
  Scorer: "your output has a value in 1 of them; the expected output has a value in 4" and "1 cell(s)
  were CHANGED although the expected value is the cell's own original input". **Agent would have done
  differently:** kept the reading that explains all four rows.
- **Blast radius: BOUNDED, measured.** Gated on `Cell-Level` + near-empty coverage. Every passing
  Cell-Level task that ran the audit reports **zero BLANK** — 12864 `{'ok':11}`, 2768 `{'ok':17}`,
  48588 `{'ok':42}`, 55049 `{'ok':21}`, 9569 `{'ok':1280}`, 7902 — full coverage, so the trigger
  cannot fire on them. 6 of the 7 legitimately-blank-gold tasks (382-10, 395-36, 402-43, 142-12,
  560-12, 80-42) are **Sheet-Level**, which this rule explicitly excludes; the 7th (48921,
  Cell-Level) is fully filled. I deliberately did **not** write "keep pre-filled cells": 2768, 6698
  (`G4=6773`), 56563 (`C14=#NUM!`) and 48620 (`E6` wrong) all have pre-filled targets their gold
  **changes**, so the clause says the example constrains the *interpretation* and "does not freeze
  its own cell".

### 5. `prompt.md` Rule 5 — **"`MUST-FIX: []` is not the same as correct"** → E
- **Lever:** STRUCTURE — a precondition on the *stop condition*, not a restated rule.
- **VERIFIED:** 43436's audit printed `COUNTS: {'ok': 15} / MUST-FIX: [] / BLANK cells: []` on five
  wrong numbers, then stopped. The audit is type-complete and semantics-blind. The new text requires
  re-deriving **one** value by hand (or reproducing a figure the sheet already gives) before
  accepting a clean audit. 43436 had exactly such an anchor and ignored it — column H `Open as of
  today` (A=1,B=2,C=1,D=0,E=1) — and I executed the shipped predicate against it to confirm the
  anchor really does discriminate the right rule from the wrong one.
- **Blast radius: UNBOUNDED (the only such edit this iteration).** It adds one read-only obligation
  to every task's audit round. Accepted because it can only add a print and a comparison — it cannot
  change which cells are written — and the budget is there: `{max_turns}`=30 while **31 of 40 tasks
  finish in 4 rounds**. The risk I priced in is 51-12 already needing 10 rounds, which is why this is
  one *sentence inside* the existing step 3 rather than a new step.

### 6. `prompt.md` Rule 5 — audit snippet gains `SCALAR` (datetime bugfix) → F
- **Lever:** correction of provably-wrong text.
- **VERIFIED by execution:** on a workbook holding a `datetime`, a `date` and a `time`, the old
  `isinstance(v,(int,float,bool,str))` classifies all three as `FORMULA-OBJECT`; with `SCALAR` they
  classify `ok`, while a real `ArrayFormula`, a formula string and `#NUM!` are still caught
  (`MUST-FIX: [('A7','FORMULA'), ('A8','EXCEL-ERROR'), ('A9','FORMULA-OBJECT')]`). Trace evidence it
  bites in the wild: **80-42 hand-patched it itself** — `elif not isinstance(v, (int, float, bool,
  str)) and not hasattr(v, 'year')`.
- **Blast radius: BOUNDED, strictly safety-increasing** — it removes false alarms only. At-risk
  passing tasks are the date-valued ones (416-15, 80-42, 9726, 59595, 53647); un-fixed, the snippet
  would send them to "fix" correct dates. No trace this iteration reported a FORMULA-OBJECT, so
  nothing currently depends on the buggy behaviour.

### 7. `prompt.md` Rule 5 + `task_template.md` steps 1 & 3 — coverage print, example print, hand-check
- **Lever:** STRUCTURE / code-enforcement (a printed number the agent must look at).
- **What changed:** the snippet now prints `COVERAGE: n of N cell(s) hold a value`; step 1 also prints
  the input state of `answer_position` and any example rows below the data (this is what makes
  clusters A and B *visible*); step 3 gains the hand-check sentence.
- **VERIFIED:** 48527's failure is a coverage failure the scorer describes in exactly those terms
  ("your output has a value in 1 of them"), and no trace ever printed its own coverage.
- **Blast radius: BOUNDED** (additive prints). **I deliberately did not add a 5th step or a new
  mandatory round** — cand_0002 restructured steps 1-3 into extra obligations and broke 51-12, the
  longest trajectory in the set (10 rounds vs 4 for 31/40). The procedure stays at 4 steps.

Lever types used: CONTRACT, KNOWLEDGE-fact, KNOWLEDGE-worked-example, DECISION-narrowing,
STRUCTURE-precondition, STRUCTURE-code-enforcement, provable-text-correction — seven edits, seven
levers, not one lever repeated.

## Considered and deliberately SKIPPED

- **cand_0002's "a pre-filled cell proves the rule covers its row".** Its RESULT broke 2768, whose
  gold **overwrites** the fully pre-filled `H2:H18`. Dropped, and actively countered in edit 4.
- **cand_0002's general `<` vs `<=` phrase→operator table.** Its RESULT broke 51-12, a numeric
  threshold task. Replaced by the date-window-only rule in edit 3.
- **cand_0002's `ERASED` check** (audit compares output against `spreadsheet_path`). Unverifiable
  without gold workbooks, needs a delete-task carve-out that risks the 7 blank-gold tasks, and edit 1
  prevents the erasure upstream. Skipped.
- **An ARGB/format-constants rule for 267-18.** cand_0002's RESULT-backed refutation stands: the
  trace reads the real fill `FFFFFF00` correctly. Would fix nothing.
- **A "restate the unit of aggregation" step.** Refuted for these traces — 43436 already grouped
  per-department correctly.
- **Any new procedure step / 5th round.** See edit 7's blast-radius note.

## Placeholder contract
Re-verified after editing by simulating the adapter's `.format()`: all six of `{instruction}`
`{spreadsheet_path}` `{spreadsheet_content}` `{instruction_type}` `{answer_position}`
`{output_path}` present, `{max_turns}` retained, **no unexpected placeholders**, render succeeds
(4452 chars). Only `prompt.md` and `task_template.md` were modified; no command mutated the
environment.

## Good things to PRESERVE (inherited from cand_0001 — do not undo)
- The stored-value contract + Rule 1's WRONG/RIGHT example (formula-writers were 0/13).
- The absence of any "you are done when the output file exists" line — `task_template.md` existing
  at all is what suppresses the adapter's built-in version of it.
- `SHOW = 30` and the `defects`/`blanks` split in the audit snippet.
- Blank-as-a-judgement, not a ban (5 of 18 passing tasks have legitimately blank gold).
