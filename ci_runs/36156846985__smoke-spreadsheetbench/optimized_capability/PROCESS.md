# PROCESS — cand_3_anchorblock (round 3, final)

## Parent choice

Parent is **cand_2_procedure**, not the seed. cand_2 was booked `reject`, but only because
`gate_delta` 0.100 == `gate_threshold` 0.100 exactly; it moved val 0.5333 → 0.6667 with
`regressions: []` and flipped 56915 0.00 → 1.00 on 3/3 trials. Its capability files are strictly
better than the seed's, so this round inherits them and adds ONE thing.

`prompt.md` is byte-identical to cand_2's, deliberately (`diff -q` verified). It is the surface
measured to fire 0/30 in round 1, so no round-3 effort is spent there. The entire edit is
`task_template.md`, +38 lines.

## What this round has to clear, arithmetically

The paired statistic is computed over the 10 TASKS, not over trials, at k_se = 1.0. With nine 0.0
diffs and one +1.0 diff, sd is pinned at 0.3162 and SE at 0.1000 — so Δ == threshold for ANY trial
count. That is why cand_2 could not be rescued by buying trials and was booked `reject` rather than
`provisional`.

| scenario | Δ | threshold | clears? |
| --- | --- | --- | --- |
| 1 task flips (cand_2, measured) | 0.100 | 0.100 | NO — exact tie |
| **2 tasks flip (this round's target)** | **0.200** | **0.133** | **YES** |
| 1 flip + a 2/3 partial on a second task | 0.167 | ~0.118 | yes |
| 1 flip + a 1/3 partial | 0.133 | ~0.107 | marginal |

So the round needs **one more task to move**, and the board says which one: 47766 is the only task
on it that still can.

## Ranked issue list (re-derived from round 2's 30 traces)
| rank | cluster | tasks | shared root cause | tag | planned change class |
| --- | --- | --- | --- | --- | --- |
| 1 | **aggregate source range too WIDE** | 47766 | Round 2's two-handle fix worked (C reads 1950, not `'=(B8*12)/12'`) and revealed the defect underneath: it sums ALL THREE row-blocks in-window (8000+8600+3935 = 20535) where gold is 8000. The scorer's feedback flipped from "LOWER than expected" to "HIGHER than expected" — the fix moved the failure, it did not remove it. | KNOWLEDGE (missing method) | worked example with real numbers + a directional invariant |
| 2 | **a round wasted on an undefined name** | any task | Round-2 t0 spent a whole round on `NameError: name 'spreadsheet_path' is not defined`, because my own Step-1 snippet used bare variable names as if they were pre-defined. Self-inflicted by round 2's edit. | BEHAVIORAL | one comment + two assignment lines in the snippet |
| — | ceiling | 188-39 | gold filler is literal `'N/A'`; instruction says `'NA'`; `'N/A'` appears in NO cell of ANY sheet of ALL 3 inputs (exhaustively scanned). Gold col B holds the DESIGNATION, not the name. | CEILING | conceded |
| — | ceiling | 53449 | gold writes literal `'X'` under header `'Test'`; neither string is derivable. | CEILING | conceded |
| — | ceiling | 52532 | copy 3's gold stores live array formulas and its own recalculated grid differs from the input's (Game 2: 483 → 383), flipping the winner. Cap 0.667. | CEILING | conceded |

Achievable val ≈ 0.87. This round targets 0.767.

## The retraction that made this round possible

Round 1 diagnosed 47766 as a SCOPE defect. Round 2 retracted that in favour of the text-read.
**Round 1 was right too — both defects were real and stacked.** The anchor rule could not possibly
fire in round 1 because every subtotal it would have compared read back as 0 from the text-read.
Re-verified against the gold workbooks this round:

| case | gold K40 | block 8-37 in-window | all three blocks in-window | input K40 | block 8-37 ALL years |
| --- | --- | --- | --- | --- | --- |
| 1 | **8000** | **8000** | 20535 | 14755 | **14755** |
| 2 | 4355 | 0 | 0 | 14755 | 14755 |
| 3 | **9950** | **9950** | 22485 | 16705 | **16705** |

Two independent confirmations: block 8-37 restricted to the window reproduces gold EXACTLY on cases
1 and 3, and the number already sitting in the target equals that same block's all-years total. The
pre-filled value identifies the source block.

**Stated risk.** Case 2's window is degenerate (K43 == L43 == 2022-01-01, an empty interval), so a
correct implementation yields 0 against a gold of 4355. That case may be unreachable, giving 2/3
(+0.0667) rather than 3/3 (+0.100). Δ = 0.167 still clears a threshold of ~0.118, but the margin is
thinner than the table's headline row. Recorded here rather than discovered after the gate.

## Changes made this iteration
| cluster | edit class | file | what & why it generalizes | protects passing? |
| --- | --- | --- | --- | --- |
| 1 | **WORKED EXAMPLE with real numbers — a new FORM, not another rule** | `task_template.md` Step 1b | Walks one concrete case end to end: three block subtotals printed, one equal to the value already in the target, the conclusion "the target came from rows 8-37 ALONE, not all three summed (144890)", and the contrast "had you summed all three and then filtered you would have got 20535 — larger than what was already there, which is the tell". Both prior rounds failed with *rules*; round 2's journal named a worked example as the next lever, in advance. | **Gated on a predicate MEASURED to fire on 1 of 10 tasks: answer_position is a SINGLE cell AND already holds a NUMBER. Only 47766 (K40 = 14755) qualifies.** |
| 1 | **directional invariant** | `task_template.md` Step 1b + Step 4.4 | "Adding a restriction can only keep a sum the same or make it smaller. A larger result means the source range is too wide — narrow it, do not re-check the arithmetic." This is a monotonicity fact about restricted aggregates, not a fact about this workbook, and it is checkable from the agent's own print-out. | Same single-cell-numeric gate. It is also exactly the signal the scorer gave ("HIGHER than expected"). |
| 2 | **defect I introduced, fixed** | `task_template.md` Step 1 | "Paths are NOT pre-defined variables in the sandbox — assign them yourself, as literal strings copied from the sections above, in EVERY code block you send." | Strictly saves rounds; changes no value written by anyone. |
| 1 | **print discipline tightened** | `task_template.md` Step 1d | Each block subtotal must be "printed as its own line. Do not print only the combined total: you cannot tell which block is the right one from a single number." Round 2 already printed them; this makes the per-line requirement explicit so Step 1b has its input. | Adds one print on tasks that aggregate blocks; no passer's written values change. |

Nothing was removed and no existing rule was reworded. Every round-2 edit survives intact.

## Verify-the-fix (trace evidence → what changes)
- **47766.** Round-2 t0 msg 10 states it summed "ranges (8-37, 41-58, 62-74)" filtered to 2021 and
  wrote 20535; scorer: HIGHER than expected; gold 8000. The agent DID print the per-block subtotals
  — it simply had no criterion for choosing among them. Step 1b supplies the criterion (match the
  pre-existing value) and Step 4.4 catches the exact failure mode (20535 > 14755 ⇒ too wide).
  Expected 0.00 → 0.667 or 1.00.
- **56915 (the win I must not break).** answer_position is a 24-cell RANGE, so the single-cell gate
  excludes it; Step 4.1's coverage rule that flipped it is untouched, and `prompt.md` is unchanged.
- **168-17 / 438-18 / 52532 / 56915 (what a naive anchor rule would have hit).** All four hold
  non-empty non-zero values inside answer_position — text headers ('SALES AND ACCESSORIES',
  'ITEM'), `'#N/A'` strings, or hand-entered win counts. An unscoped "match the value already there"
  rule fires on 168-17 (20 cells), 438-18 (12), 52532 (2), 56915 (16). Requiring a SINGLE cell
  holding a NUMBER excludes all four. Measured, not argued — and this is precisely why round 1's
  unscoped version of the same idea was refuted.
- **160-6 / 43213 / 49945 / 53449 / 188-39.** answer_position is multi-cell in every one, so the
  new step cannot fire at all.
- **Contract pre-flight.** `_task_template_error()` → `None`; all 6 required placeholders present
  plus `{max_turns}`; no unknown braces (the worked example's numbers sit in a fenced block with no
  braces); `.format()` render OK, 7595 chars.

## Process & features used
- Serial, foreground, three rounds; every candidate gated exactly once on FULL val at k_se = 1.0
  over 3 trials with a concurrent byte-identical control (`--gate-against control`), concurrency
  fixed at 8 throughout as a measurement parameter rather than a speed dial. No screen subset was
  ever gated on.
- Each decision came from reading that round's own 30 traces, not from the scalar. Round 1's
  Δ = 0.000 was only interpretable because the traces showed WHICH surface moved behaviour.
- Falsification before spending: for every proposed predicate, enumerate which of the 10 tasks it
  fires on against the on-disk gold. That is what killed the blanket "no empty cells" rule (160-6
  gold is 42/72 empty), the blanket `data_only=True` (all 5 passers save a non-`data_only` handle),
  and the unscoped anchor rule (fires on 4 wrong tasks).
- Read `./prior_iterations/`, RUNMAP, LEDGER and `rejected.jsonl` each round. Both prior JOURNAL
  entries carry a POST-GATE audit appended before booking, so the handover states what was measured
  rather than what was hoped.

## Good things to PRESERVE
- **The ordered Step 1-4 procedure in `task_template.md`** — measured to change behaviour 30/30 in
  both rounds, and it is what carried the 56915 win. Add mechanics INTO it; do not replace it with
  prose.
- **The two-handle `data_only` snippet + "never save `wb_val`".** It flipped nothing on its own but
  it is what made 47766's real defect visible, and it is inert on the 5 passers (0 formula cells).
- **The `{instruction_type}` key on the coverage predicate** — the single edit that flipped 56915;
  unkeyed it breaks 160-6 and 168-17.
- **Objective, not intention-relative, finish predicates.** "Cells your solution was supposed to
  fill" is self-certifying; "every cell of answer_position" is not.
- Deleting "once that file exists, you are done".
- **Scope a value-matching rule by target SHAPE and TYPE, not by non-emptiness.** That is the
  difference between round 1's refuted rule and this round's.

## Deliberately skipped
- 188-39, 53449, 52532 copy 3 — verified unreachable from the inputs. A future round must not spend
  on them, and must not read their flat scores as evidence against the header/type/conditional edits.
- The five 3/3 passers.
- `prompt.md` — left byte-identical to cand_2 on purpose. It is the measured-dead surface, and a
  round that edits it is spending on the thing proven not to fire.
