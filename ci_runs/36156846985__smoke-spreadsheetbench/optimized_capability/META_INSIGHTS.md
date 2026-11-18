# META-INSIGHTS — about the optimization PROCESS itself (this run)

Not about the capability — about HOW this run is searching for it: which strategies/edit classes/algorithms are helping vs stalling, and what to try next iteration. Update at the end of the run at minimum; sooner if a plateau or a clear strategy shift is worth recording now. Structure each addition as:

    ## Iteration <id> (or 'run so far')
    - Strategy tried, and whether it moved val (cite LEDGER rows):
    - Plateau/stall signal, if any, and the lever switched to:
    - What to try next iteration:

## Run so far (3 rounds, 1 accept — the strategy that produced it)
- Strategy tried, and whether it moved val:
  - R1 `cand_1_anchor` — one wave, BOTH surfaces at once (a restructured procedure in
    `task_template.md` + six bounded rules in `prompt.md`). REJECTED, Δ 0.000, per-task vector
    identical to control on 10/10. Val unmoved.
  - R2 `cand_2_procedure` — move every mechanic INTO the numbered steps and SHRINK `prompt.md`.
    REJECTED on an exact tie (Δ 0.100 == threshold 0.100), but reward 0.5333 → 0.6667 with
    `regressions: []` and 56915 flipped 0 → 1 on 3/3.
  - R3 `cand_3_anchorblock` — same surface, new FORM (worked example with real numbers), built on
    R2's files rather than the seed. **ACCEPTED**: 0.6889, Δ 0.1222 > threshold 0.1104,
    `verdict_stable`, `regressions: []`.
- The single most valuable process move of the run: **splitting a null result BY SURFACE instead of
  reading it as "the edit didn't work."** R1's Δ was exactly 0.000, which normally reads as a dead
  end. Grepping all 30 traces for the new text first proved the plumbing was sound, and then the
  per-surface audit (template 30/30 vs prompt 0/30) turned a zero into the finding that directed
  both remaining rounds. A rejected round with 30 readable traces is worth more than its scalar.
- Plateau signal and the lever switched to: after two rejects the scalar looked flat, but Δ was
  rising monotonically (0.000 → 0.100 → 0.1222) with zero regressions — the gate bar rises with the
  diff spread, so a rising Δ can still read as "rejected". Diagnose a plateau from the per-task
  vector, not the verdict. The lever each round was chosen from the PRIOR round's traces, and R1's
  journal named R3's lever (worked example) in advance — writing the next lever down before seeing
  the result made the choice mechanical rather than improvisational.
- Arithmetic worth reusing on a small paired gate: the statistic is over the 10 TASKS, not trials.
  With nine 0.0 diffs and one +1.0, sd is pinned at 0.3162 and SE at 0.1000 for ANY trial count, so
  R2's tie could never be bought out with more trials — only a second task moving could clear it.
  I computed that BEFORE choosing `reject` over `provisional`, and before deciding R3's target. On a
  10-task board, work out how many tasks must move; do not shop for trials.
- Cheap habit that paid for itself repeatedly: falsify each proposed predicate against the ON-DISK
  gold before spending a rollout (which tasks does it fire on? what is gold's emptiness? how many
  formula cells?). It pre-killed three plausible edits, including one that would have broken all 5
  passing tasks.
- What to try next iteration (if rounds remained): 47766's residual is now a CodeAct-REPLAY defect,
  not an anchor defect — hardcoded literal year constants in code that gets re-run on other graded
  copies. That is a general rule, targets the one task still able to move, and is the highest-value
  edit left. Also note a pre-gate prediction of mine was falsified by the traces (I wrote off 47766
  case 2 as unreachable; a trial passed it) — worth stating predictions explicitly in PROCESS.md
  precisely so the traces can refute them.

<!-- cap-evolve:meta-insights-append-below -->
