## Smoke suite — spreadsheetbench  (train-fit, no holdout)

Agent `rits/google/gemma-4-31B-it` · optimizer Claude Code `aws/claude-opus-5` · 3 iteration(s) · **all 10 tasks optimized together** · `train==val==test` (FIT metric, not a generalization/held-out claim).

| bench | task | reward (base→opt) | Δ | note |
|---|---|---|---|:--:|
| spreadsheetbench | `49945` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `47766` | 0.000 → 0.667 | +0.667 |  |
| spreadsheetbench | `52532` | 0.667 → 0.667 | +0.000 |  |
| spreadsheetbench | `56915` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `438-18` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `168-17` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `53449` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `43213` | 0.667 → 1.000 | +0.333 |  |
| spreadsheetbench | `160-6` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `188-39` | 0.000 → 0.000 | +0.000 |  |

**Suite (train-fit):** mean reward 0.533 → 0.733 (Δ +0.200 (+37% rel)) · best = `cand_3_anchorblock` · optimizer $55.87 over 3 iter(s)

### Iterations

| phase | iter | candidate | accepted | reward | optimizer $ | optimizer time | eval $ | eval time |
|---|:--:|---|:--:|---|---|---|---|---|
| baseline | — | `seed` | — | 0.533 | $0.0000 | 0s | $0.0000 | 9m32s |
| iterate | 1 | `cand_1_anchor` | ❌ | 0.567 | $15.2600 | 21m40s | $0.0000 | 10m33s |
| iterate | 2 | `cand_2_procedure` | ❌ | 0.667 | $18.5900 | 20m00s | $0.0000 | 8m33s |
| iterate | 3 | `cand_3_anchorblock` | ✅ | 0.689 | $22.0200 | 60m00s | $0.0000 | 8m37s |
| finalize | — | `cand_3_anchorblock` | — | 0.733 | $0.0000 | 0s | $0.0000 | 8m43s |
| finalize_baseline | — | `seed` | — | 0.567 | $0.0000 | 0s | $0.0000 | 8m58s |

**Totals:** optimizer $55.8700 over 101m40s · eval $0.0000 over 54m56s
