## Smoke suite — spreadsheetbench  (train-fit, no holdout)

Agent `rits/Qwen/Qwen3-8B` · optimizer Claude Code `claude-opus-4-8` · 3 iteration(s) · **all 10 tasks optimized together** · `train==val==test` (FIT metric, not a generalization/held-out claim).

| bench | task | reward (base→opt) | Δ | note |
|---|---|---|---|:--:|
| spreadsheetbench | `49945` | 0.000 → ⚠️ infra-error | — | ⚠️ |
| spreadsheetbench | `47766` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `52532` | 0.000 → 0.444 | +0.444 |  |
| spreadsheetbench | `56915` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `438-18` | 0.667 → 1.000 | +0.333 |  |
| spreadsheetbench | `168-17` | 0.000 → 0.667 | +0.667 |  |
| spreadsheetbench | `53449` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `43213` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `160-6` | 0.667 → 1.000 | +0.333 |  |
| spreadsheetbench | `188-39` | 0.000 → 0.000 | +0.000 |  |

**Suite (train-fit):** mean reward 0.148 → 0.311 (Δ +0.163 (+110% rel)) · best = `cand_0001` · optimizer $14.67 over 3 iter(s) · 1 task(s) infra-errored

### Iterations

| phase | iter | candidate | accepted | reward | optimizer $ | optimizer time | eval $ | eval time |
|---|:--:|---|:--:|---|---|---|---|---|
| baseline | — | `seed` | — | 0.148 | $0.0000 | 0s | $0.0000 | 30m20s |
| iterate | 1 | `cand_0001` | ✅ | 0.244 | $2.4059 | 8m57s | $0.0000 | 44m09s |
| iterate | 2 | `cand_0002` | ❌ | 0.233 | $5.1896 | 9m45s | $0.0000 | 40m16s |
| iterate | 3 | `cand_0003` | ❌ | 0.311 | $7.0705 | 14m18s | $0.0000 | 30m26s |
| finalize | — | `cand_0001` | — | 0.311 | $0.0000 | 0s | $0.0000 | 31m44s |
| finalize_baseline | — | `seed` | — | 0.267 | $0.0000 | 0s | $0.0000 | 24m43s |

**Totals:** optimizer $14.6661 over 33m00s · eval $0.0000 over 201m39s
