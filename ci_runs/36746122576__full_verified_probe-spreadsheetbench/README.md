# full_verified_probe / spreadsheetbench — run 36746122576

A cap-evolve benchmark run, backfilled on 2026-11-18 from its CI artifact (the run predates per-run folders, so `recipe/` is missing). Its row is on the [benchmark-runs dashboard](https://skillberry-runs.github.io/dashboard/).

[Actions run](https://github.com/skillberry-ai/cap-evolve/actions/runs/36746122576) · [commit `5104939de`](https://github.com/skillberry-ai/cap-evolve/tree/5104939de9cfc31da7bea7c8c73e1f71809681b7) · [Open UI](https://skillberry-runs.github.io/dashboard/viewer/index.html?dataBase=https%3A%2F%2Fskillberry-runs.github.io%2Fdashboard%2Fspreadsheetbench%2Fci_ui%2F36746122576__full_verified_probe-spreadsheetbench#/runs/run_suite)

## Run

| | |
|---|---|
| Benchmark / tier | `spreadsheetbench` / `full_verified_probe` |
| Source | manual (exp/606-reader-profile) |
| Date (UTC) | 2026-09-30T18:35:01Z |
| Conclusion | success |
| Agent model | `ibm-rits/google/gemma-4-31B-it` |
| Optimizer model | `ibm-ete-int/aws/claude-opus-5-5` |
| Algorithm | `hill-climb-all` |
| Iterations / trials | 1 / 1 |
| Gate (k·SE) | 0.2 |
| Reward metric | hard_no_recalc |

## Results

- **Reward:** 0.430 → 0.680 (100 tasks), each measured in this run against its own baseline.
- **Cost:** eval $0.0000, optimizer $2.5033.

Details per task are in `report.md`.

## Files

- [`report.md`](report.md) — the run's metrics report (also its PR comment)
- [`runmeta.json`](runmeta.json) — how the run was launched: models, tier, iterations, trials, commit
- [`metrics.jsonl`](metrics.jsonl) — one row per task: baseline vs optimized reward
- [`steps.jsonl`](steps.jsonl) — one row per iteration: cost and time
- [`capability.diff`](capability.diff) — the optimized capability vs the seed
- [`optimized_capability/`](optimized_capability/) — the optimized capability
- `recipe/` was not available for this run (published from its CI artifact); the tier's definition is `ci/benchmarks/spreadsheetbench/full_verified_probe/` at the commit above.

## Re-running it

The tier's tasks, split and overrides are committed in cap-evolve under `ci/benchmarks/spreadsheetbench/full_verified_probe/`. To run the same configuration again, dispatch the Benchmarks workflow on a branch at the commit above:

```bash
gh workflow run benchmarks.yml -R skillberry-ai/cap-evolve --ref <branch> -f tier=full_verified_probe -f bench=spreadsheetbench \
  -f iterations=1 -f trials=1 -f agent_model=ibm-rits/google/gemma-4-31B-it \
  -f optimizer_model=ibm-ete-int/aws/claude-opus-5-5 -f algorithm=hill-climb-all
```

Model calls are sampled, so a re-run gives a new measurement, not the same numbers.
