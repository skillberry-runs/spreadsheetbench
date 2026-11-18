# smoke / spreadsheetbench — run 36156846985

A cap-evolve benchmark run, backfilled on 2026-11-18 from its CI artifact (the run predates per-run folders, so `recipe/` is missing). Its row is on the [benchmark-runs dashboard](https://skillberry-runs.github.io/dashboard/).

[Actions run](https://github.com/skillberry-ai/cap-evolve/actions/runs/36156846985) · [commit `da4781c8c`](https://github.com/skillberry-ai/cap-evolve/tree/da4781c8c51a48f2c2bd7fb0cfc779d3940bf05b) · [Open UI](https://skillberry-runs.github.io/dashboard/viewer/index.html?dataBase=https%3A%2F%2Fskillberry-runs.github.io%2Fdashboard%2Fspreadsheetbench%2Fci_ui%2F36156846985__smoke-spreadsheetbench#/runs/run_suite)

## Run

| | |
|---|---|
| Benchmark / tier | `spreadsheetbench` / `smoke` |
| Source | manual (main) |
| Date (UTC) | 2026-09-25T18:32:56Z |
| Conclusion | success |
| Agent model | `rits/google/gemma-4-31B-it` |
| Optimizer model | `aws/claude-opus-5` |
| Algorithm | `agent-optimize` |
| Iterations / trials | 3 / 3 |
| Gate (k·SE) | 1.0 |

## Results

- **Reward:** 0.533 → 0.733 (10 tasks), each measured in this run against its own baseline.
- **Cost:** eval $0.0000, optimizer $55.8700.

Details per task are in `report.md`.

## Files

- [`report.md`](report.md) — the run's metrics report (also its PR comment)
- [`runmeta.json`](runmeta.json) — how the run was launched: models, tier, iterations, trials, commit
- [`metrics.jsonl`](metrics.jsonl) — one row per task: baseline vs optimized reward
- [`steps.jsonl`](steps.jsonl) — one row per iteration: cost and time
- [`capability.diff`](capability.diff) — the optimized capability vs the seed
- [`optimized_capability/`](optimized_capability/) — the optimized capability
- `recipe/` was not available for this run (published from its CI artifact); the tier's definition is `ci/benchmarks/spreadsheetbench/smoke/` at the commit above.

## Re-running it

The tier's tasks, split and overrides are committed in cap-evolve under `ci/benchmarks/spreadsheetbench/smoke/`. To run the same configuration again, dispatch the Benchmarks workflow on a branch at the commit above:

```bash
gh workflow run benchmarks.yml -R skillberry-ai/cap-evolve --ref <branch> -f tier=smoke -f bench=spreadsheetbench \
  -f iterations=3 -f trials=3 -f agent_model=rits/google/gemma-4-31B-it \
  -f optimizer_model=aws/claude-opus-5 -f algorithm=agent-optimize
```

Model calls are sampled, so a re-run gives a new measurement, not the same numbers.
