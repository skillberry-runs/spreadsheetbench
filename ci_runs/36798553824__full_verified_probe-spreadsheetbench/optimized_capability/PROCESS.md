# PROCESS — cand_0001 (empty seed → capability built on measured evidence)

## Decisive finding: this baseline has already been measured
`LEDGER/JOURNAL/RUNMAP/rejected.jsonl` are empty, but the project dir holds a completed sibling run,
`../../../../reused_seed_run/run_suite/` (read-only, used only as evidence), on the **same** seed,
**same** val/train/test split (`splits.json` val/train/test identical), **same** reader
(`rits/google/gemma-4-31B-it`). I checked that this iteration's `./trajectories/` are byte-identical
rollouts to that run's `rollouts/val/*__seed__*` (37378, 227-40, 9569 compared). So its per-task
measurements of 5 candidates transfer directly:

| sibling candidate | val | failing tasks |
| --- | --- | --- |
| seed | 0.450 | the 22 listed in INSTRUCTIONS |
| cand_0001 (accepted; test 0.779 vs seed 0.435) | **0.950** | 31628, 80-42 |
| cand_0002 / 0003 / 0004 / 0005 (rejected vs 0.950) | 0.925 / 0.875 / 0.925 / 0.850 | all four stamped `fixed={31628, 80-42}` |

So this candidate = sibling `cand_0001` prompt.md + task_template.md **plus exactly the two rules
that were proven (4× each) to fix its two remaining failures**, minus everything else those rejected
batches shipped.

## Ranked clusters (this iteration's 22 failing seed traces)
| rank | cluster | tasks | root cause | tag | fix (file) |
| --- | --- | --- | --- | --- | --- |
| 1 | Formula written instead of value | 37378, 46897, 53383, 55049, 6698, 7902, 8942 (`recalc=[1], no_recalc=[0]`) | grader is `hard_no_recalc`; openpyxl formula reads back empty | CONTRACT | CONTRACT §1 + prompt §1(a) |
| 2 | Excel error text / unresolved lookup in graded cells | 37456, 53647, 54144, 56563 | wrote `#N/A`/`#NUM!` strings | CONTRACT | prompt §1(b) last bullet, CONTRACT §2 |
| 3 | Never inspects file / "file exists → done" framing; no verify | 267-18, 55979, 59196, 48527, 50768, 43436 | adapter default template says done once file exists; agent writes from preview | STRUCTURE | template Phase 1/2/3 ordered procedure |
| 4 | Destructive rebuild / off-by-one from preview | 227-40, 39046, 48527, 80-42, 9569 | `to_excel` rebuild, header-row shift | KNOWLEDGE | prompt §3, §4 (conditional, not blanket) |
| 5 | Prose vs header semantics (overlap vs snapshot) | 43436 | followed prose paraphrase | STRUCTURE | template Phase 1b calibration gate |
| 6 | Matrix orientation / "next row" boundary | 50768, 37456 | transposed axes; last row left empty | KNOWLEDGE | prompt §2 conditional rules |
| 7 | Append sized with `ws.max_row` | 80-42 (still fails under base) | formatting-only rows appended mid-block | KNOWLEDGE | **NEW: prompt §4 max_row bullet** |
| 8 | Date part vs datetime (regression under base) | 31628 (passes in seed, broke in base) | agent quoted CONTRACT "dates as datetime" to override the day-number reading | CONTRACT | **NEW: CONTRACT item 2 narrowing** |

No environment fault: every trace ran code and produced a file.

## Edits (all in this candidate)
| cluster | lever | file | blast radius |
| --- | --- | --- | --- |
| 1–6 | role + output contract + ordered procedure + worked examples + conditional knowledge (sibling cand_0001, measured 0.950, broke only 31628) | prompt.md, task_template.md | measured: 0 seed-passing tasks broken except 31628 → addressed by Edit B |
| 7 (Edit A) | KNOWLEDGE, condition-guarded (only inside the append/consolidate bullet; source-read loop only) | prompt.md §4 | BOUNDED — only 80-42 matches an append regex among the 40 val instructions; 402-43 appends but its max_row == extent (no-op) |
| 8 (Edit B) | CONTRACT narrowing of the exact sentence the failing trace cited | task_template.md CONTRACT 2 | BOUNDED — only 31628 and 43436 name a date component; 43436 uses it as a filter boundary and writes ints anyway; datetime-answer tasks (9726, 416-15) name no component |

Deliberately NOT included (each appeared in a rejected sibling batch): the mandatory `# ANSWER TYPE:`
Phase-1 step and Phase-3 additions (cand_0002/0003, common factor of broke={43436, 51-12}); any
deletions/pruning (cand_0003 only, broke 395-36/48527/9569); the §1(b) clause-precedence rewrite +
worked example and the §2 tie-break paragraph (prompt growth; unnecessary once the CONTRACT sentence
the agent quoted is narrowed). Net: the smallest diff vs the 0.950 base that carries both proven fixes.

## Verify-the-fix
- Base (clusters 1–6): sibling `cand_0001` RESULT `fixed={227-40, 267-18, 37378, 37456, 39046, 43436, 46897, 48527, 50768, 51-12, 53383, 53647, 54144, 55049, 55979, 56563, 59196, 6698, 7902, 8942, 9569}` on these exact tasks; held-out test +0.34 shows it generalizes.
- Edit B (31628): trace `31628__cand_0001`: *"The CONTRACT requires dates to be written as datetime objects. 'Number of the last day' is slightly ambiguous, but 'resulting date' is explicit."* → wrote datetime; scorer "datetime where int was expected". The narrowed sentence explicitly excludes "the number of the day" from the datetime rule, removing the cited justification. Seed trace of 31628 passes with `.day` int — consistent.
- Edit A (80-42): trace `80-42__cand_0001` loops `for r_src in range(2, ws_src.max_row + 1)`; coverage short of expected with an interior blank block. Bullet names exactly that loop and gives the filtered replacement. Text is verbatim from cand_0004/0005, every batch containing it stamped 80-42 fixed.
- Placeholders: stripped the `<!-- -->` comment and ran `.format()` with all 7 fields — OK; field set is exactly the 6 required + `{max_turns}`.

## Process
- Serial (no subagents): the decisive evidence was a measured per-task matrix, not something needing fan-out diagnosis; the sibling run already ran a 4-subagent diagnosis of these identical traces.
- Risk note: sibling rejections "broke" 43436 (1/5 pass-rate), 9569 (2/5), 227-40 (3/5) — high-variance tasks; with gate SE≈0.06 those are not attributable to the two edits kept here. Expected val ≈ 0.90–0.975, Δ ≫ 2·SE vs this run's 0.450 baseline.

## Preserve
- "Write the computed literal even when the instruction says formula" (biggest win).
- Conditional (not blanket) openpyxl-preserve rule — 13 of 18 seed-passing tasks win via `to_excel`.
- Phase 3 stop condition: "reply with no code block when checks pass".
