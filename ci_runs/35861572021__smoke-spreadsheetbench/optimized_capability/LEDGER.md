# LEDGER — factual run record (framework-maintained; READ-ONLY)

The measured record of every iteration: which candidate, its parent, whether the gate ACCEPTED it, the val reward + Δ, and the tasks it broke / fixed. Facts only — your own narrative, lessons, and refuted hypotheses go in JOURNAL.md. Use this to never re-introduce a change that broke a task, and to see which approaches the gate accepted vs rejected.

`broke` / `fixed` list only tasks whose move EXCEEDED 2·SE of its own per-task measurement error, so they are claims the measurement can support. A task that moved by less is in `unresolved`: it is NOT evidence the edit did anything to that task, in either direction, and must not be reasoned about as a regression or a win. Do not redesign an edit because a task appears there — re-measure it, or ignore it.

## Iterations
| iter | candidate | parent | outcome | val | Δ vs parent | broke (were passing) | fixed | unresolved (moved < 2·SE) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | cand_1a | seed | reject | 0.511 | +0.011 | {52216} | {} | {40467, 53161} |
| 2 | cand_1c | seed | reject | 0.556 |  | {} | {} | {40467, 52216} |
| 3 | cand_1b | seed | reject | 0.589 |  | {} | {} | {40467, 52216, 53161} |

## Current best: seed
