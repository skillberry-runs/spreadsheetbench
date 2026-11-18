## Smoke suite — spreadsheetbench  (train-fit, no holdout)

Agent `Azure/gpt-5-mini-2025-08-07` · optimizer Claude Code `claude-opus-4-8` · 3 iteration(s) · **all 10 tasks optimized together** · `train==val==test` (FIT metric, not a generalization/held-out claim).

| bench | task | reward (base→opt) | Δ | note |
|---|---|---|---|:--:|
| spreadsheetbench | `55457` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `47484` | 0.667 → 1.000 | +0.333 |  |
| spreadsheetbench | `418-29` | 0.222 → 0.444 | +0.222 |  |
| spreadsheetbench | `374-9` | 0.333 → 0.333 | +0.000 |  |
| spreadsheetbench | `40467` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `52216` | 0.778 → 1.000 | +0.222 |  |
| spreadsheetbench | `347-49` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `32468` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `53161` | 1.000 → 0.667 | -0.333 | ↓ |
| spreadsheetbench | `160-6` | 1.000 → 1.000 | +0.000 |  |

**Suite (train-fit):** mean reward 0.500 → 0.544 (Δ +0.044 (+9% rel)) · best = seed (no candidate beat baseline) · optimizer $7.95 over 3 iter(s)

### Iterations

| phase | iter | candidate | accepted | reward | optimizer $ | optimizer time | eval $ | eval time |
|---|:--:|---|:--:|---|---|---|---|---|
| baseline | — | `seed` | — | 0.500 | $0.0000 | 0s | $0.2764 | 10m08s |
| iterate | 1 | `cand_1` | ❌ | 0.533 | $0.0000 | — | — | — |
| iterate | 2 | `cand_2` | ❌ | 0.400 | $0.0000 | — | — | — |
| iterate | 3 | `cand_3` | ❌ | 0.456 | $0.0000 | — | — | — |
| finalize | — | `seed` | — | 0.544 | $0.0000 | 0s | $0.3108 | 12m11s |

**Totals:** optimizer $0.0000 over 0s · eval $0.5872 over 22m20s
