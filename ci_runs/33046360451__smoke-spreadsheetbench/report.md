## Smoke suite — spreadsheetbench  (train-fit, no holdout)

Agent `Azure/gpt-5-mini-2025-08-07` · optimizer Claude Code `claude-opus-4-8` · 3 iteration(s) · **all 10 tasks optimized together** · `train==val==test` (FIT metric, not a generalization/held-out claim).

| bench | task | reward (base→opt) | Δ | note |
|---|---|---|---|:--:|
| spreadsheetbench | `55457` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `47484` | 0.900 → 0.900 | +0.000 |  |
| spreadsheetbench | `418-29` | 0.400 → 0.400 | +0.000 |  |
| spreadsheetbench | `374-9` | 0.267 → 0.267 | +0.000 |  |
| spreadsheetbench | `40467` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `52216` | 0.833 → 0.833 | +0.000 |  |
| spreadsheetbench | `347-49` | 0.100 → 0.100 | +0.000 |  |
| spreadsheetbench | `32468` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `53161` | 0.600 → 0.600 | +0.000 |  |
| spreadsheetbench | `160-6` | 1.000 → 1.000 | +0.000 |  |

**Suite (train-fit):** mean reward 0.510 → 0.510 (Δ +0.000 (+0% rel)) · best = seed (no candidate beat baseline) · optimizer $9.11 over 2 iter(s)

> No candidate was accepted, so base→opt is the seed against itself and Δ is 0.000 by construction. Re-scoring those same bytes for the finalize read 0.527 against the baseline's 0.510 — a spread of 0.017. That is this tier's re-measurement **noise**, not a change in the capability, and it is the floor any real effect here would have to clear.

### Iterations

| phase | iter | candidate | accepted | reward | optimizer $ | optimizer time | eval $ | eval time |
|---|:--:|---|:--:|---|---|---|---|---|
| baseline | — | `seed` | — | 0.510 | $0.0000 | 0s | $0.9265 | 28m34s |
| iterate | 1 | `cand_1` | ❌ | 0.497 | $0.0000 | — | $1.6969 | 43m10s |
| iterate | 2 | `cand_2_hi` | ❌ | 0.553 | $0.0000 | — | $1.6178 | 60m49s |
| finalize | — | `seed` | — | 0.527 | $0.0000 | 0s | $1.0108 | 26m59s |

**Totals:** optimizer $9.1108 over 0s (whole-loop — one optimizer process drove every round, so there is no per-round figure to attribute) · eval $5.2519 over 159m31s
