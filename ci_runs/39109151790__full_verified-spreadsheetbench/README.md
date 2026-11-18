# full_verified / spreadsheetbench — run 39109151790

A cap-evolve benchmark run, backfilled on 2026-11-18 from its CI artifact (the run predates per-run folders, so `recipe/` is missing). Its row is on the [benchmark-runs dashboard](https://skillberry-runs.github.io/dashboard/).

[Actions run](https://github.com/skillberry-ai/cap-evolve/actions/runs/39109151790) · [commit `5409b401a`](https://github.com/skillberry-ai/cap-evolve/tree/5409b401a67b6b3ac711786c2e9127e6b660d18a) · [Open UI](https://skillberry-runs.github.io/dashboard/viewer/index.html?dataBase=https%3A%2F%2Fskillberry-runs.github.io%2Fdashboard%2Fspreadsheetbench%2Fci_ui%2F39109151790__full_verified-spreadsheetbench#/runs/run_suite)

## Run

| | |
|---|---|
| Benchmark / tier | `spreadsheetbench` / `full_verified` |
| Source | manual (exp/871-E1F-v2b-eval) |
| Date (UTC) | 2026-10-18T10:05:54Z |
| Conclusion | cancelled |
| Agent model | `ibm-rits/google/gemma-4-31B-it` |
| Optimizer model | `ibm-rits/google/gemma-4-31B-it` |
| Algorithm | `hill-climb-all` |
| Iterations / trials | 0 / 1 |
| Gate (k·SE) | 0.2 |
| Reward metric | hard_no_recalc |

## Results

- No suite result: the run did not finish successfully (see `report.md` and the Actions run).

Details per task are in `report.md`.

## Files

- [`runmeta.json`](runmeta.json) — how the run was launched: models, tier, iterations, trials, commit
- [`metrics.jsonl`](metrics.jsonl) — one row per task: baseline vs optimized reward
- `recipe/` was not available for this run (published from its CI artifact); the tier's definition is `ci/benchmarks/spreadsheetbench/full_verified/` at the commit above.

## Re-running it

The tier's tasks, split and overrides are committed in cap-evolve under `ci/benchmarks/spreadsheetbench/full_verified/`. To run the same configuration again, dispatch the Benchmarks workflow on a branch at the commit above:

```bash
gh workflow run benchmarks.yml -R skillberry-ai/cap-evolve --ref <branch> -f tier=full_verified -f bench=spreadsheetbench \
  -f iterations=0 -f trials=1 -f agent_model=ibm-rits/google/gemma-4-31B-it \
  -f optimizer_model=ibm-rits/google/gemma-4-31B-it -f algorithm=hill-climb-all
```

Model calls are sampled, so a re-run gives a new measurement, not the same numbers.
