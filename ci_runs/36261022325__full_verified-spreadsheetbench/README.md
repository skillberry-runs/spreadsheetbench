# full_verified / spreadsheetbench — run 36261022325

A cap-evolve benchmark run, backfilled on 2026-11-18 from its CI artifact (the run predates per-run folders, so `recipe/` is missing). Its row is on the [benchmark-runs dashboard](https://skillberry-runs.github.io/dashboard/).

[Actions run](https://github.com/skillberry-ai/cap-evolve/actions/runs/36261022325) · [commit `31478d5d0`](https://github.com/skillberry-ai/cap-evolve/tree/31478d5d03974422672724241f565fdce7f0bf89) · [Open UI](https://skillberry-runs.github.io/dashboard/viewer/index.html?dataBase=https%3A%2F%2Fskillberry-runs.github.io%2Fdashboard%2Fspreadsheetbench%2Fci_ui%2F36261022325__full_verified-spreadsheetbench#/runs/run_suite)

## Run

| | |
|---|---|
| Benchmark / tier | `spreadsheetbench` / `full_verified` |
| Source | manual (temp-no-skill-measurement) |
| Date (UTC) | 2026-09-26T21:16:19Z |
| Conclusion | success |
| Agent model | `rits/google/gemma-4-31B-it` |
| Optimizer model | `aws/claude-opus-5` |
| Algorithm | `hill-climb-all` |
| Iterations / trials | 1 / 1 |
| Gate (k·SE) | 1.0 |

## Results

- **Reward:** 0.668 → 0.668 (280 tasks), each measured in this run against its own baseline.
- **Cost:** eval $0.0000, optimizer $12.0504.

Details per task are in `report.md`.

## Files

- [`report.md`](report.md) — the run's metrics report (also its PR comment)
- [`runmeta.json`](runmeta.json) — how the run was launched: models, tier, iterations, trials, commit
- [`metrics.jsonl`](metrics.jsonl) — one row per task: baseline vs optimized reward
- [`steps.jsonl`](steps.jsonl) — one row per iteration: cost and time
- [`capability.diff`](capability.diff) — the optimized capability vs the seed
- [`optimized_capability/`](optimized_capability/) — the optimized capability
- `recipe/` was not available for this run (published from its CI artifact); the tier's definition is `ci/benchmarks/spreadsheetbench/full_verified/` at the commit above.

## Re-running it

The tier's tasks, split and overrides are committed in cap-evolve under `ci/benchmarks/spreadsheetbench/full_verified/`. To run the same configuration again, dispatch the Benchmarks workflow on a branch at the commit above:

```bash
gh workflow run benchmarks.yml -R skillberry-ai/cap-evolve --ref <branch> -f tier=full_verified -f bench=spreadsheetbench \
  -f iterations=1 -f trials=1 -f agent_model=rits/google/gemma-4-31B-it \
  -f optimizer_model=aws/claude-opus-5 -f algorithm=hill-climb-all
```

Model calls are sampled, so a re-run gives a new measurement, not the same numbers.
