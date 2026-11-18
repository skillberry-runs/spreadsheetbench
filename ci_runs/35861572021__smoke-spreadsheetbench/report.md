## Smoke suite — spreadsheetbench  (train-fit, no holdout)

Agent `rits/google/gemma-4-31B-it` · optimizer Claude Code `aws/claude-opus-5` · 3 iteration(s) · **all 10 tasks optimized together** · `train==val==test` (FIT metric, not a generalization/held-out claim).

| bench | task | reward (base→opt) | Δ | note |
|---|---|---|---|:--:|
| spreadsheetbench | `55457` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `47484` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `418-29` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `374-9` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `40467` | 0.667 → 0.667 | +0.000 |  |
| spreadsheetbench | `52216` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `347-49` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `32468` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `53161` | 0.333 → 0.333 | +0.000 |  |
| spreadsheetbench | `160-6` | 1.000 → 1.000 | +0.000 |  |

**Suite (train-fit):** mean reward 0.500 → 0.500 (Δ +0.000 (+0% rel)) · best = seed (no candidate beat baseline) · optimizer $15.98 over 3 iter(s)

> No candidate was accepted, so base→opt is the seed against itself and Δ is 0.000 by construction. Re-scoring those same bytes for the finalize read 0.489 against the baseline's 0.500 — a spread of 0.011. That is this tier's re-measurement **noise**, not a change in the capability, and it is the floor any real effect here would have to clear.

### Iterations

| phase | iter | candidate | accepted | reward | optimizer $ | optimizer time | eval $ | eval time |
|---|:--:|---|:--:|---|---|---|---|---|
| baseline | — | `seed` | — | 0.500 | $0.0000 | 0s | $0.0000 | 17m17s |
| iterate | 1 | `cand_1a` | ❌ | 0.511 | $4.4000 | 40m00s | $0.0000 | 16m43s |
| iterate | 2 | `cand_1c` | ❌ | 0.556 | $0.4000 | 5m00s | $0.0000 | 12m51s |
| iterate | 3 | `cand_1b` | ❌ | 0.589 | $1.2000 | 50m00s | $0.0000 | 22m42s |
| finalize | — | `seed` | — | 0.489 | $0.0000 | 0s | $0.0000 | 15m16s |
| unattributed | — | `(whole run)` | — | — | $9.9828 | 78m07s | $0.0000 | — |

**Totals:** optimizer $15.9828 over 173m07s · eval $0.0000 over 84m49s

> The `unattributed` row is metered spend no phase above owns (optimizer $9.9828 — agent mode runs ONE optimizer process, metered whole-loop, so no round owns a share of it). It is shown rather than dropped so these totals match what the run actually paid: `spent` reads $0.00 runner + $15.98 optimizer.
