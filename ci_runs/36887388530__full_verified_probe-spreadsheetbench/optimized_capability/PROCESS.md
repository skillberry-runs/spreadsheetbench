# PROCESS — cand_0003 (iteration 3)

Diagnosis was done solo (no subagents). I read all 11 failing traces plus 45707 and checked each claim cell by cell against the init/golden workbooks in the local data cache (`/tmp/w3/cmp.py`: init value, init formula, golden value). Parent cand_0002 is at val 0.725 (29/40). Its LEDGER row broke 11276 and 41978, both passed by cand_0001.

## Ranked issue list
| rank | cluster | tasks | shared root cause (verified against golden) | tag | change |
| --- | --- | --- | --- | --- | --- |
| 1 | Filled target cells misread: kept when they should be recomputed, or not used as the format oracle | 279-23, 45707, 51680, 11276 | 279-23: the processed copy B17:B26 = 'tig' (no brackets); the agent wrote '(tig)'. 45707: filled D32=5 (January's count); the agent's function gives 4 (the next month) and it never checked. 51680: hand-typed G5 'Red purple', G3 'Green' (stripped); golden = header join verbatim ('Green , Red Purple'). 11276: filled 'TU','W' are wrong for the dates; golden = `%a` per the instruction's "Mon, Wed" | BEHAVIORAL + STRUCTURE | Phase 1c test-on-filled-cells procedure, plus the three-outcome rule in prompt §2 and the before/after-pair rule |
| 2 | Instruction spelling over workbook spelling (rule existed, not followed) | 203-15, 1925 | 'Transport Allowance' written vs data 'Transport Allowances'; 'New' vs formula literal "NEW" | STRUCTURE (pre-save check) | Phase 2 `SPELLING:` check code + a prompt pointer |
| 3 | Non-instruction formula cells re-interpreted | 183-8 | J7:L7 `=AVERAGE(J3:J6)`; golden = the mean of the new J3:J6 (21.0197), the agent wrote an overall weighted avg (21.3097). I3:I7 SUMIFS/SUM cached values; the agent skipped the `left` check | KNOWLEDGE + CONTRACT | prompt §2 "which logic a formula cell gets"; Phase 3 requires the `left` line |
| 4 | Header vs self-contradicting prose | 188-39 | result!B header 'Designation'; the agent put Name in it after reasoning through the contradiction | DECISION NARROWING | prompt §2 header bullet: the clause agreeing with the header wins; print header↔source mapping |
| 5 | Substring lookup done as prefix | 524-31 | `startswith` + split on `*` missed keys appearing mid-text | KNOWLEDGE + WORKED SNIPPET | prompt §2 keyword bullet: `key in text` + code |
| 6 | Case-sensitive criteria emulation | 41978 | `== 'Open'` vs data 'Open'/'open'; golden [..,26,9,2] = case-insensitive (Excel COUNTIFS) | KNOWLEDGE | prompt §5 bullet |
| 7 | Side-by-side list comparison keyed by the wrong list | 45944 | golden G11:G13 = T,F,T = for D-list row r, look up its name in A:B and compare. The agent did it the other way (T,T,F) | KNOWLEDGE | prompt §2 bullet |

## Changes made (file and lever)
| cluster | lever | file | generalizes because | blast radius |
| --- | --- | --- | --- | --- |
| 1 | ordered procedure (code) | task_template Phase 1c | Any task with already-filled target cells: test f on them before writing | BOUNDED: no-op when nothing is filled. Passing tasks with worked examples already reproduce them, so the test prints OK |
| 1 | decision narrowing (3 outcomes) | prompt §2 after the Rule | Substance DIFF → fix f; case/space-only DIFF on label-built text → overwrite all; instruction-quoted format → overwrite all | BOUNDED: the overwrite cases need (a) text built from workbook labels with a case/space-only diff, or (b) the instruction quoting an example format the filled cells contradict. The default (preserve) is unchanged |
| 1 | worked example | prompt §2 before/after pair + Phase 1c paragraph | A raw block and a processed copy with the same index | BOUNDED: requires a duplicate block |
| 2 | structure (pre-save check code) | task_template Phase 2 | Flags written strings whose normalized form matches a workbook string spelled differently; skips kept input values | BOUNDED: print-only. Simulated on real workbooks: flags 203-15 J1 and 1925 C6, and nothing for a correct 51680 output |
| 2 | consolidation pointer | prompt §2 spelling bullet | Ties the existing rule to the check | BOUNDED |
| 3 | knowledge | prompt §2 formula exception | Formula cells not named by the instruction are evaluated as written / keep cached values | BOUNDED: only formula cells inside answer_position. Consistent with cand_0002's `left` rule |
| 3 | contract | task_template Phase 3 | The checklist needs the `left` output line and no SPELLING line | BOUNDED |
| 4 | decision narrowing | prompt §2 header bullet | Self-contradicting prose doesn't override a header | BOUNDED: only when a target header exists |
| 5 | knowledge + snippet | prompt §2 keyword bullet | Substring semantics; the snippet reproduces 52/53 golden cells of 524-31 offline (the 53rd is its default 'amazon' self-row, a header-row quirk) | BOUNDED: keyword-lookup tasks only |
| 6 | knowledge | prompt §5 | Excel criterion semantics; matching only, writing keeps the exact spelling | BOUNDED: text-criterion counting/lookup. cand_0001 passed 41978 with `.lower()` |
| 7 | knowledge | prompt §2 side-by-side lists | Result keyed by the adjacent list's row | BOUNDED: two parallel record blocks with the target beside one |

## Verify-the-fix
- 279-23: the trace wrote '(tig) this is good' → '(tig)'. Golden B3 = 'tig', the processed twin B17 = 'tig'. The before/after rule plus the Phase 1c raw→processed comparison gives a DIFF ('(tig)' vs 'tig') until the brackets are dropped.
- 45707: the agent counted the month of the NEXT date (D32 → Feb = 4) while the filled D32 holds 5 (Jan = 5, verified). Phase 1c prints `D32 5 4 DIFF`; the prompt names "the next row's month instead of the row's own month" as the typical cause.
- 51680: the agent stripped 'Green ' and kept hand-typed G5 'Red purple'. Golden G3 = 'Blue, Green , Red Purple', G5 = 'Red Purple'. Outcome 2 says to write the label-built value everywhere and not strip.
- 11276: the agent copied 'TU'/'W' styles. Golden = 'Wed','Thu',… (`%a`). Outcome 3: the instruction quotes "Mon, Wed" and the filled cells contradict the dates.
- 203-15 / 1925: the SPELLING check, run on the real init workbooks with the agent's strings, printed `SPELLING: J1 'Transport Allowance' -> {'Transport Allowances'}` and `SPELLING: C6 'New' -> {'NEW'}`.
- 183-8: the agent wrote J7 = 21.3097 (overall weighted). Golden 21.0197 = AVERAGE of its own J3:J6. The new bullet says `=AVERAGE(J3:J6)` → the plain mean. I3:I7 keep cached values.
- 188-39: trace line "I will put the Name in the 'Designation' column". The bullet now addresses exactly the self-contradicting-prose case.
- 524-31: the agent used prefix matching; `key in text` + the longest-key snippet matches golden for all graded data rows (checked offline).
- 41978: `== 'Open'` gave 24/8/0 where golden is 26/9/2; the case-insensitive compare reproduces it (cand_0001 evidence).
- 45944: the agent keyed by the A:B row (T,T,F for block 2); golden T,F,T = keyed by the D:E row. Covered by the side-by-side bullet.

## Process & features used
- Serial, solo: the system note forbids AgentTool/workflows unless the user asks. Golden-backed offline checks via small scripts in /tmp/w3 (`cmp.py`, `sp.py` simulating the SPELLING snippet on real workbooks). The template still renders with `.format()`, and all six placeholders are present.
- Read prior_iterations/cand_0001 and cand_0002 (PROCESS + diff). cand_0002's "workbook wins" and worked-example rules are kept; this iteration adds the narrow exceptions that broke 11276 instead of removing them.

## Good things to PRESERVE
- The cand_0002 `vs`/`ws` read/write split, the `left` check, the result-sheet / today / delete-rows / extent rules. The default "keep filled cells" rule stays the default; only two narrowly conditioned exceptions were added.

## Deliberately skipped
- 486-17, 59160 (passing now). No change.
- I did not loosen the preserve rule globally; that would risk the 29 passing tasks.
