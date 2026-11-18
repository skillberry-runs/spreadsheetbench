# PROCESS — cand_2_procedure (round 2)

## The one measurement that designed this round

Round 1 (`cand_1_anchor`) was REJECTED with Δ = 0.000 and a per-task vector **identical to the
control on 10/10 tasks**. Before believing that, I checked the plumbing: all 30 candidate
rollouts contain `INSPECT`/`FINISH`/`proves nothing` and 0 contain the seed's round list, so the
edit reached the agent. Then I split the result by surface:

| surface edited in round 1 | did it change agent behaviour? | evidence |
| --- | --- | --- |
| `task_template.md` (ordered Step 1-4 procedure) | **YES, 30/30** | Step-1 no-write held 30/30; `type()` printed in the verify round 30/30; clean no-code finish 27/30 |
| `prompt.md` (six prose rules) | **NO, 0/30** | not one rule fired; 56915's gold rows 19-20 are `int 0`, exactly my "blank lookup source contributes 0" rule, and the agent printed `B19, None, NoneType` in its own verify output and finished anyway |

**Conclusion that drives this round: numbered steps in the user message are a live lever; rules in
the system prompt are not.** So every mechanic that must fire this round MOVED into the Step 1-4
procedure, as code the agent copies rather than a rule it must remember. `prompt.md` gets SMALLER
(rules deleted, not added). This is a change of FORM and of surface-weighting, not a re-proposal.

Why Step 4 licensed the failure: I had written "every cell **your solution was supposed to fill**".
The agent read its unmatched rows as not-supposed-to-be-filled and passed its own gate. An
intention-relative predicate is self-certifying; this round's predicate is objective (every cell
of answer_position) and keyed on `{instruction_type}`, which the agent is literally given.

## Ranked issue list (re-derived from THIS round's traces, not round 1's guesses)
| rank | cluster | tasks | shared root cause | tag | planned change class |
| --- | --- | --- | --- | --- | --- |
| 1 | **formula cells read as TEXT** | 47766 | The solve round calls `load_workbook(path)` with no `data_only=True`, so column C returns `'=(B8*12)/12'` strings. Every `float()` fails, the sum is 0. It printed `K40: 0` three times and shipped. Its date-range logic and single-block scope were ALREADY CORRECT — round 1's anchor rule was aimed at the wrong defect. Gold 8000/4355/9950. | BEHAVIORAL (wrong API call) | copyable two-handle snippet inside Step 1 |
| 2 | **empty cells left in a fully-filled target** | 56915 | 16/24 cells numerically EXACT; the 8 misses are rows 19-20, blank in the source, so `cell.value = None`. Gold holds `int 0`. Round 1 stated this as prose and it did not fire. | BEHAVIORAL (knows, skips) | Step-4 coverage predicate keyed on instruction_type |
| 3 | **wrong column semantics** | 188-39 | Gold column B holds the DESIGNATION ('Branch Manager'), not the employee name; the header IS the value list ("Branch Manager / Branch Credit Manager"). Round 1's header rule said "which column supplies the NUMBERS", so it could not fire. | KNOWLEDGE | header rule generalized off "numbers" |
| 4 | **right value, wrong stored type** | 188-39 | 5 cells hold the correct phone number as `str`; gold is `int`. Round 1 SHIPPED A CARVE-OUT ("copy a value straight through unchanged") that actively licensed this, because the source is `str` too. Self-inflicted by my own edit. | KNOWLEDGE | carve-out narrowed to "only text in the reference stays text" |
| — | ceiling, not fixable | 188-39 | gold filler is literal `'N/A'`; the instruction says `'NA'` and `'N/A'` appears NOWHERE in any of the 3 input workbooks. Verified by scanning every cell of every sheet. | CEILING | conceded |
| — | ceiling, not fixable | 53449 | gold writes literal `'X'` under header `'Test'`; neither string is derivable. | CEILING | conceded |
| — | ceiling, not fixable | 52532 | copy 3's gold stores live array formulas and its own score grid differs from the input's (Game 2: 483 → 383), flipping the winner. 0.667 is the cap. | CEILING | conceded |

Reachable val this round is therefore **56915 + 47766 = +0.20** (0.533 → ~0.733) against an
`evidence_bar` of 0.033. Nothing else on the board can move, so the whole round is spent on these.

## Changes made this iteration
| cluster | edit class | file | what & why it generalizes | protects passing? |
| --- | --- | --- | --- | --- |
| 1 | **copyable code, inside the step** | `task_template.md` Step 1 | The two-handle pattern (`wb_val = load_workbook(p, data_only=True)` to READ, `wb_out = load_workbook(p)` to WRITE/save) with the reason stated: a formula cell reads back as its text. Generalizes to every workbook containing a formula. | **Measured inert on all 5 passers: only 47766 (295 formula cells) and 56915 (1) contain ANY formula cell; 160-6/168-17/43213/438-18/49945 have 0.** So the value-read is identical to the raw read there. |
| 1 | **self-check on an observable symptom** | `task_template.md` Step 1c | "print `repr()` of a few source cells; if one comes back as a string starting with `=`, you are reading the wrong handle." Turns an invisible bug into a printed one. | Fires only on a string starting with `=`; no passer has one. |
| 1 | **explicit prohibition** | `task_template.md` Step 1 | "Never save `wb_val`" — saving a `data_only` workbook erases every other formula in the file. This is the guard that makes the fix safe rather than destructive. | Directly protects against the naive blanket `data_only=True`, which WOULD have broken all 5 passers (they all save a non-`data_only` handle). |
| 2 | **objective predicate, keyed on a given field** | `task_template.md` Step 4.1 | Cell-Level ⇒ every cell of answer_position must read back non-empty, "including cells your lookup found no match for: a spreadsheet function over a blank numeric source returns 0, so write 0". Sheet-Level ⇒ explicitly DO NOT pad. | **Measured: Cell-Level gold fills 100% of answer_position (43213 0/4, 47766 0/1, 49945 0/3, 52532 0/7, 56915 0/24 empty). Sheet-Level gold is mostly EMPTY (160-6 42/72, 168-17 55/55). Keying on instruction_type is what makes this safe.** |
| 2 | **scoped exception** | `task_template.md` Step 4.1 | The per-row-condition carve-out ("both X and Y on the same day", "where", "if", "flag", "mark") keeps the coverage rule from over-filling 53449, whose gold is 10-14 of 15 empty — the single Cell-Level counter-example. | Without it the coverage rule would actively worsen 53449. |
| 3 | **generalized rule** | `prompt.md` | Header-over-prose no longer says "supplies the numbers" — it says what a column "actually holds", so it reaches 188-39's designation column. Still paired with "an explicit cell reference is exact: adjust the COLUMN, never widen or move the ROWS". | The paired clause is what protects 43213 (see verify line). |
| 4 | **harmful carve-out narrowed** | `prompt.md` | "A number that arrives as text from the source must be CONVERTED; only a value genuinely text in the reference stays text." Replaces round 1's "copy a value straight through unchanged", which licensed 188-39's 5 type misses. | 160-6's text dates are text in the reference, so they still stay text. |
| — | **deletions** | `prompt.md` | Removed the anchor rule, the blank→0 prose, the conditional-fill prose, the pre-entered-values rule, the print-something rule and the identical-block prohibition — all six fired 0/30. The two that survive in `prompt.md` are the two that are genuinely about knowledge, not behaviour; blank→0 and conditional-fill MOVED into Step 4 where structure fires. | Pure reduction; nothing a passer relied on. Net `prompt.md` is shorter than round 1's. |

## Verify-the-fix (trace evidence → what changes)
- **47766.** Round-1 trace msg 6/8/10: `load_workbook(file_path)` (no `data_only`), then
  `numeric_val = 0` for every row because `val` is `'=(B8*12)/12'`, printing `K40: 0` three times.
  I confirmed directly against the input: raw read gives `'=(B8*12)/12'`, value read gives `1950`.
  Its date filter `K43 <= F < L43` and its single-block scope (rows 8-37) were already right, so
  the two-handle snippet alone should flip 0.00 → 1.00. This also RETRACTS round 1's diagnosis
  that the defect was scope — the anchor rule was treating a symptom of the text-read.
- **56915.** Its own Step-3 output was `B19, None, NoneType` … `E20, None, NoneType`, and it
  finished anyway because my predicate was intention-relative. The 16 cells it filled match gold
  exactly; gold rows 19-20 are `int 0`. Step 4.1 makes a `None` anywhere in a Cell-Level range
  disqualify finishing, and names 0 as what the lookup returns. One line of logic, 8 cells.
- **43213 (the SAFE check that mattered, re-verified).** t0/t2 read column B literally, saw
  `B12:B15 = 0/0/0/0`, switched the SOURCE COLUMN to A off the headers, and passed; t1 did the
  same switch BUT moved the row bounds from A11 to A2 and failed. So the flakiness is row drift,
  not the column choice. The generalized header rule keeps t0/t2's winning move; the retained
  "explicit cell reference is exact — never widen or move the ROWS" clause targets t1's error. Its
  answer_position is 0/4 gold-empty, so Step 4.1's coverage check is satisfied by a correct answer.
- **160-6 / 168-17 (the tasks Step 4.1 could have destroyed).** Gold leaves 42/72 and 55/55 cells
  EMPTY inside answer_position. Both are Sheet-Level, so 4.1 not only skips them, it tells them
  explicitly not to pad. This is exactly the blanket rule I refuted in round 1, now made safe by
  the instruction_type key rather than dropped.
- **188-39.** Expected to stay 0.00 — the `'N/A'` filler is unreachable. The header and type edits
  are shipped because the CLASSES are general and bounded, not because this task can pass. Stated
  plainly so no future round reads a flat 188-39 as evidence against them.

## Process & features used
- Serial, driven from the foreground. Round 1's gate took 21m and the whole decision turned on
  reading its 30 traces, so the round's budget went into the trace audit and into checking every
  proposed predicate against the on-disk gold before spending a rollout.
- Read `./prior_iterations/` + RUNMAP: only round 1 exists. I used its RESULT the way the journal
  instructs — a reject with an identical per-task vector, whose traces say which SURFACE moved
  behaviour — and switched lever accordingly instead of rewording the same rules.
- Pre-flight before gating: `_task_template_error()` → `None`, all 6 required placeholders plus
  `{max_turns}`, no unknown braces, `.format()` render OK (5419 chars).
- Falsification done FIRST this round, against gold rather than intuition: counted formula cells
  per input (5 passers have 0) and gold-emptiness per answer_position (Cell-Level 0% empty,
  Sheet-Level mostly empty). Both numbers are what let the two strongest edits ship at all.

## Good things to PRESERVE
- **The ordered Step 1-4 procedure in `task_template.md`.** It is the one thing measured to change
  behaviour 30/30. A future round should add mechanics INTO it, not replace it with prose.
- Deleting "once that file exists, you are done" — the adapter docstring names that line as the
  cause of the dominant failure. It must not come back.
- The `{instruction_type}` key on any coverage/padding rule. Unkeyed, it breaks 160-6 and 168-17.
- The "explicit cell reference is exact / never move the ROWS" clause paired with the header rule.
- "Never save `wb_val`" paired with the two-handle pattern.

## Deliberately skipped
- `188-39`'s `'N/A'` filler, `53449`'s `'X'`, `52532` copy 3 — all three verified unreachable from
  the input. Achievable val is ~0.87, and ~0.733 is this round's realistic target.
- The five 3/3 passers: nothing to gain, everything to lose. Every edit above was checked against
  them by measurement, not by argument.
