## Smoke suite — spreadsheetbench  (train-fit, no holdout)

Agent `Azure/gpt-5-mini-2025-08-07` · optimizer Claude Code `claude-opus-4-8` · 3 iteration(s) · **all 10 tasks optimized together** · `train==val==test` (FIT metric, not a generalization/held-out claim).

| bench | task | reward (base→opt) | Δ | note |
|---|---|---|---|:--:|
| spreadsheetbench | `55457` | 0.000 → ⚠️ infra-error | — | ⚠️ |
| spreadsheetbench | `47484` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `418-29` | 0.267 → 0.933 | +0.667 |  |
| spreadsheetbench | `374-9` | 0.200 → 0.267 | +0.067 |  |
| spreadsheetbench | `40467` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `52216` | 0.933 → 0.800 | -0.133 | ↓ |
| spreadsheetbench | `347-49` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `32468` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `53161` | 0.800 → 1.000 | +0.200 |  |
| spreadsheetbench | `160-6` | 1.000 → 0.800 | -0.200 | ↓ |

**Suite (train-fit):** mean reward 0.520 → 0.580 (Δ +0.060 (+12% rel)) · best = `cand_extent2` · optimizer $9.31 over 3 iter(s) · 1 task(s) infra-errored

### Iterations

| phase | iter | candidate | accepted | reward | optimizer $ | optimizer time | eval $ | eval time |
|---|:--:|---|:--:|---|---|---|---|---|
| baseline | — | `seed` | — | 0.520 | $0.0000 | 0s | $0.9112 | 41m21s |
| iterate | 1 | `cand_extent` | ❌ | 0.540 | $0.0000 | — | $1.0198 | 31m57s |
| iterate | 2 | `cand_extent2` | ✅ | 0.563 | $0.0000 | — | $0.9631 | 31m58s |
| iterate | 3 | `cand_e2_typecode` | ❌ | 0.600 | $0.0000 | — | $0.9066 | 30m45s |
| finalize | — | `cand_extent2` | — | 0.580 | $0.0000 | 0s | $0.9359 | 39m39s |
| finalize_baseline | — | `seed` | — | 0.510 | $0.0000 | 0s | $0.9712 | 35m32s |
| unattributed | — | `(whole run)` | — | — | $9.3148 | 334m46s | $9.6760 | 331m21s |

**Totals:** optimizer $9.3148 over 334m46s · eval $15.3838 over 542m32s

> The `unattributed` row is metered spend no phase above owns (optimizer $9.3148 — agent mode runs ONE optimizer process, metered whole-loop, so no round owns a share of it; eval $9.6760 — control replicates, re-gates and abandoned rounds are real evaluations that no committed step references). It is shown rather than dropped so these totals match what the run actually paid: `spent` reads $15.38 runner + $9.31 optimizer.
