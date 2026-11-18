## Smoke suite — spreadsheetbench  (train-fit, no holdout)

Agent `ibm-rits/google/gemma-4-31B-it` · optimizer Claude Code `ibm-rits/google/gemma-4-31B-it` · 1 iteration(s) · **all 10 tasks optimized together** · `train==val==test` (FIT metric, not a generalization/held-out claim).

| bench | task | reward (base→opt) | Δ | note |
|---|---|---|---|:--:|
| spreadsheetbench | `262-17` | 0.667 → 0.667 | +0.000 |  |
| spreadsheetbench | `32438` | 0.000 → 0.333 | +0.333 |  |
| spreadsheetbench | `54638` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `47766` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `52216` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `48365` | 0.000 → 0.444 | +0.444 |  |
| spreadsheetbench | `250-20` | 0.667 → 0.667 | +0.000 |  |
| spreadsheetbench | `32902` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `493-18` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `48745` | 1.000 → 1.000 | +0.000 |  |

**Suite (train-fit):** mean reward 0.333 → 0.411 (Δ +0.078 (+23% rel)) · best = `cand_0001` · optimizer $4.95 over 1 iter(s)

### Metrics by candidate and split

| candidate | split | n | `soft_restriction` | `hard_restriction` | `soft_no_recalc` | `hard_no_recalc` |
|---|---|--:|--:|--:|--:|--:|
| seed | val | 10 | 0.3333 | 0.2000 | 0.3333 | 0.2000 |
| seed | test | 10 | 0.3333 | 0.2000 | 0.3333 | 0.2000 |
| best | val | 10 | 0.4333 | 0.2667 | 0.4333 | 0.2667 |
| best | test | 10 | 0.4111 | 0.2333 | 0.4111 | 0.2333 |

### Iterations

| phase | iter | candidate | accepted | reward | traded | optimizer $ | optimizer time | eval $ | eval time |
|---|:--:|---|:--:|---|---|---|---|---|---|
| baseline | — | `seed` | — | 0.333 | — | $0.0000 | 0s | $0.0000 | 13m21s |
| iterate | 1 | `cand_0001` | ✅ | 0.433 | — | $4.9523 | 5m05s | $0.0000 | 23m44s |
| finalize | — | `cand_0001` | — | 0.411 | — | $0.0000 | 0s | $0.0000 | 30m06s |
| finalize_baseline | — | `seed` | — | 0.333 | — | $0.0000 | 0s | $0.0000 | 8m47s |

**Totals:** optimizer $4.9523 over 5m05s · eval $0.0000 over 75m59s
