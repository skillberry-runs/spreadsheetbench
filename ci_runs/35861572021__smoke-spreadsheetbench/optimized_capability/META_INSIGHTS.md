# META-INSIGHTS — about the optimization PROCESS itself (this run)

Not about the capability — about HOW this run is searching for it: which strategies/edit classes/algorithms are helping vs stalling, and what to try next iteration. Update at the end of the run at minimum; sooner if a plateau or a clear strategy shift is worth recording now. Structure each addition as:

    ## Iteration <id> (or 'run so far')
    - Strategy tried, and whether it moved val (cite LEDGER rows):
    - Plateau/stall signal, if any, and the lever switched to:
    - What to try next iteration:

## Round 1 (cand_1a / cand_1b / cand_1c)
- **Strategy tried:** diagnose first with read-only subagents and spend ZERO rollouts on diagnosis,
  then field 3 siblings that attack the SAME diagnosed clusters on DIFFERENT surfaces/forms
  (knowledge-on-prompt.md vs structure-on-task_template.md vs both), so the round learns which FORM
  the reader responds to even if no sibling gates. That part worked: the form signal is clean and
  monotone (1b 0.600 > 1c 0.556 > 1a 0.511), and it is the single most useful thing this round
  produced. The diagnosis itself was strong — one cluster (`data_only=True` on 374-9) was verified
  end-to-end by replaying the agent's own code against the real fixture, no rollout needed.
- **Did it move val?** No, not resolvably. LEDGER: cand_1b inconclusive (0.600, gate_delta ≈ 0.0,
  verdict_stable false, no regressions), cand_1c inconclusive (0.556, −0.044, verdict_stable false),
  cand_1a reject (0.511, −0.089, verdict_stable TRUE, regressions 52216 + 53161).
- **The stall signal is not the candidates — it is the instrument.** Two byte-identical control
  replicates of the SEED differed by 0.1333 (0.600 vs 0.467), and the stored baseline vs a fresh
  control drifted 0.10. On a 10-task val at 3 trials one task = 0.1 reward, so the noise floor is
  wider than a whole task. Two of three siblings came back `verdict_stable: false` for exactly this
  reason: they accept against one control replicate and reject against the other. That is the
  binding constraint on this run, and no amount of better prose fixes it.
- **Lever this implies (and the accounting that blocks it):** the right move after a round like this
  is to buy TRIALS on the best sibling rather than field a fourth guess — resolution, not novelty.
  `grow.py` is the intended instrument, but it only returns `grow_again` when `d.delta > 0`, and the
  two inconclusive siblings sit at 0.0 and −0.044, so its own logic returns `abandon`. Growth
  genuinely cannot help them, which is the documented condition for booking
  `commit.py --decision inconclusive --force`. With `max_iterations = 3` and one iteration charged
  per commit, the three gated siblings ARE the whole budget: there is no round 2 to spend the lever
  on. Recording this so a future run sees the trap, not to excuse it.
- **What to try next iteration (or next run):** (1) Fix the instrument before the capability — on a
  10-task split, budget for more trials per candidate (5–7) or accept that only whole-task flips are
  visible, and size each round to flip a WHOLE task rather than to shave several single trials.
  (2) Go after 347-49 and 32468, the two 0/3 tasks: together they are 0.2 of val, comfortably above
  the noise floor, whereas the 53161/40467 single-trial slips (0.033 each) are invisible by
  construction. (3) Prefer the `task_template.md` structural surface over `prompt.md` prose for this
  reader tier; the round's one stable verdict was the prose-only candidate being REJECTED with
  regressions, while the structural one was the round's best and regressed nothing.
- **Process note on the harness:** `round.py` refused a direct full-val gate until `--skip-screen-
  ladder` was passed. Skipping was correct here (on a 10-task val the tier-1 floor puts the screen's
  break-even kill rate out of reach), but a future run on a small split should expect that prompt
  and budget the argument up front rather than losing a cycle to it.

## Round 1 (cand_1a / cand_1b / cand_1c)
- **Strategy tried:** diagnose first with read-only subagents and spend ZERO rollouts on diagnosis,
  then field 3 siblings that attack the SAME diagnosed clusters on DIFFERENT surfaces/forms
  (knowledge-on-prompt.md vs structure-on-task_template.md vs both), so the round learns which FORM
  the reader responds to even if no sibling gates. That part worked: the form signal is clean and
  monotone (1b 0.600 > 1c 0.556 > 1a 0.511), and it is the single most useful thing this round
  produced. The diagnosis itself was strong — one cluster (`data_only=True` on 374-9) was verified
  end-to-end by replaying the agent's own code against the real fixture, no rollout needed.
- **Did it move val?** No, not resolvably. LEDGER: cand_1b inconclusive (0.600, gate_delta ≈ 0.0,
  verdict_stable false, no regressions), cand_1c inconclusive (0.556, −0.044, verdict_stable false),
  cand_1a reject (0.511, −0.089, verdict_stable TRUE, regressions 52216 + 53161).
- **The stall signal is not the candidates — it is the instrument.** Two byte-identical control
  replicates of the SEED differed by 0.1333 (0.600 vs 0.467), and the stored baseline vs a fresh
  control drifted 0.10. On a 10-task val at 3 trials one task = 0.1 reward, so the noise floor is
  wider than a whole task. Two of three siblings came back `verdict_stable: false` for exactly this
  reason: they accept against one control replicate and reject against the other. That is the
  binding constraint on this run, and no amount of better prose fixes it.
- **Lever this implies (and the accounting that blocks it):** the right move after a round like this
  is to buy TRIALS on the best sibling rather than field a fourth guess — resolution, not novelty.
  `grow.py` is the intended instrument, but it only returns `grow_again` when `d.delta > 0`, and the
  two inconclusive siblings sit at 0.0 and −0.044, so its own logic returns `abandon`. Growth
  genuinely cannot help them, which is the documented condition for booking
  `commit.py --decision inconclusive --force`. With `max_iterations = 3` and one iteration charged
  per commit, the three gated siblings ARE the whole budget: there is no round 2 to spend the lever
  on. Recording this so a future run sees the trap, not to excuse it.
- **What to try next iteration (or next run):** (1) Fix the instrument before the capability — on a
  10-task split, budget for more trials per candidate (5–7) or accept that only whole-task flips are
  visible, and size each round to flip a WHOLE task rather than to shave several single trials.
  (2) Go after 347-49 and 32468, the two 0/3 tasks: together they are 0.2 of val, comfortably above
  the noise floor, whereas the 53161/40467 single-trial slips (0.033 each) are invisible by
  construction. (3) Prefer the `task_template.md` structural surface over `prompt.md` prose for this
  reader tier; the round's one stable verdict was the prose-only candidate being REJECTED with
  regressions, while the structural one was the round's best and regressed nothing.
- **Process note on the harness:** `round.py` refused a direct full-val gate until `--skip-screen-
  ladder` was passed. Skipping was correct here (on a 10-task val the tier-1 floor puts the screen's
  break-even kill rate out of reach), but a future run on a small split should expect that prompt
  and budget the argument up front rather than losing a cycle to it.


## Growth round on cand_1b — the lever I said to reach for, and its actual limit
- I predicted the right lever (buy TRIALS on the best sibling, not a fourth guess) and it still did
  not resolve, for a reason worth writing down: **growth shrinks the CANDIDATE's stderr, but the
  instability on this run lives in the REFERENCE.** cand_1b went 3 -> 9 trials; its stderr fell
  0.1633 -> 0.1438 and the gate threshold fell with it, yet the verdict still flips between the two
  byte-identical control replicates (Δ=−0.011 vs ctl_null_i0, Δ=+0.122 vs ctl_null_i0r1). No number
  of extra candidate trials can close a gap that belongs to the thing being compared against.
- **Corollary for a future run: grow the CONTROL, not (only) the candidate.** The cheap fix is more
  control replicates — `gate_check.py --current a,b,...` already pools them into one lower-variance
  reference for free, and pooling the two existing replicates alone cut the threshold from 0.0452/
  0.0730 to 0.0448 with a mid-point delta of +0.0622. Three or four control replicates at the same
  trial count would have bought more resolution per rollout than the 6 candidate trials I spent.
- **Trap to flag: `grow.py` gates against `best_id` (the STORED parent reward), not against a
  concurrent control.** It returned `promote` (Δ=+0.0889 vs the stored seed) on a candidate that a
  same-round control says is flat. A driver that books grow.py's recommendation without re-checking
  against the concurrent control will manufacture an accept out of measurement drift — this run's
  drift was 0.10, larger than the effect. Always re-run gate_check.py against each control replicate
  after growth.
- **Regression to the band is real:** the 0.600 first reading became 0.5889 at n=9, drifting toward
  the pooled-control value 0.5333. Treat any single 3-trial reading on a 10-task split as the top of
  a band, not as a point estimate.

<!-- cap-evolve:meta-insights-append-below -->
