# RUNMAP — every prior iteration's working dir (read these before proposing)

For each prior iteration, its artifacts are copied into `./prior_iterations/<candidate>/`:
- `PROCESS.md` — what that iteration did (ranked issues, changes, verify-the-fix, process)
- `diff.patch` — the EXACT capability edit it made vs its parent

The live run dir (read-only) is at `/vol/home/skillberry/.cache/capevolve-gh-runner/_work/cap-evolve/cap-evolve/ci/benchmarks/.work/suite_smoke_spreadsheetbench_proj/.capevolve/run_suite` if you need `rollouts/<split>/` traces or the git log.

| iter | candidate | parent | outcome | val | ./prior_iterations/<id>/ |
| --- | --- | --- | --- | --- | --- |
| 1 | cand_1_anchor | seed | reject | 0.567 | PROCESS.md + diff.patch |
| 2 | cand_2_procedure | seed | reject | 0.667 | PROCESS.md + diff.patch |
| 3 | cand_3_anchorblock | seed | ACCEPT | 0.689 | PROCESS.md + diff.patch |

Before proposing, read the PROCESS.md + diff.patch of the prior iterations that targeted the SAME cluster you are about to work on — so you BUILD ON them rather than repeat a rejected or already-tried edit. Cross-reference LEDGER.md for which of them the gate accepted vs rejected, and JOURNAL.md for the lessons.
