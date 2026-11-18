# smoke / spreadsheetbench — run 37205067594

A cap-evolve benchmark run, backfilled on 2026-11-18 from its CI artifact (the run predates per-run folders, so `recipe/` is missing). Its row is on the [benchmark-runs dashboard](https://skillberry-runs.github.io/dashboard/).

[Actions run](https://github.com/skillberry-ai/cap-evolve/actions/runs/37205067594) · [commit `557fea840`](https://github.com/skillberry-ai/cap-evolve/tree/557fea8407cc7c9045b7967a23ff15e00e5a42b2) · [Open UI](https://skillberry-runs.github.io/dashboard/viewer/index.html?dataBase=https%3A%2F%2Fskillberry-runs.github.io%2Fdashboard%2Fspreadsheetbench%2Fci_ui%2F37205067594__smoke-spreadsheetbench#/runs/run_suite)

## Run

| | |
|---|---|
| Benchmark / tier | `spreadsheetbench` / `smoke` |
| Source | manual (ci/provider-order-fallback) |
| Date (UTC) | 2026-10-04T13:51:01Z |
| Conclusion | cancelled |
| Agent model | `ibm-rits/google/gemma-4-31B-it` |
| Optimizer model | `ibm-ete-int/claude-opus-4-8` |
| Algorithm | `hill-climb-all` |
| Iterations / trials | 1 / 1 |
| Gate (k·SE) | 1.0 |
| Reward metric | soft_no_recalc |

## Results

- No suite result: the run did not finish successfully (see `report.md` and the Actions run).

Details per task are in `report.md`.

## Files

- [`runmeta.json`](runmeta.json) — how the run was launched: models, tier, iterations, trials, commit
- [`metrics.jsonl`](metrics.jsonl) — one row per task: baseline vs optimized reward
- `recipe/` was not available for this run (published from its CI artifact); the tier's definition is `ci/benchmarks/spreadsheetbench/smoke/` at the commit above.

## Re-running it

The tier's tasks, split and overrides are committed in cap-evolve under `ci/benchmarks/spreadsheetbench/smoke/`. To run the same configuration again, dispatch the Benchmarks workflow on a branch at the commit above:

```bash
gh workflow run benchmarks.yml -R skillberry-ai/cap-evolve --ref <branch> -f tier=smoke -f bench=spreadsheetbench \
  -f iterations=1 -f trials=1 -f agent_model=gemma-4-31B-it \
  -f optimizer_model=claude-opus-4-8 -f algorithm=hill-climb-all
```

Model calls are sampled, so a re-run gives a new measurement, not the same numbers.
