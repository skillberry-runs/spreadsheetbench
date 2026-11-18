# smoke / spreadsheetbench — run 35838239772

A cap-evolve benchmark run, backfilled on 2026-11-18 from its CI artifact (the run predates per-run folders, so `recipe/` is missing). Its row is on the [benchmark-runs dashboard](https://skillberry-runs.github.io/dashboard/).

[Actions run](https://github.com/skillberry-ai/cap-evolve/actions/runs/35838239772) · [commit `39c1d9ea7`](https://github.com/skillberry-ai/cap-evolve/tree/39c1d9ea75a165ed346b343a6a4364113071044c)

## Run

| | |
|---|---|
| Benchmark / tier | `spreadsheetbench` / `smoke` |
| Source | manual (test-rits-x-508) |
| Date (UTC) | 2026-09-23T08:38:42Z |
| Conclusion | failure |
| Agent model | `rits/Qwen/Qwen3-8B` |
| Optimizer model | `claude-opus-4-8` |
| Algorithm | `hill-climb-all` |
| Iterations / trials | 3 / 3 |
| Gate (k·SE) | 1.0 |

## Results

- No suite result: the run did not finish successfully (see `report.md` and the Actions run).

Details per task are in `report.md`.

## Files

- [`runmeta.json`](runmeta.json) — how the run was launched: models, tier, iterations, trials, commit
- `recipe/` was not available for this run (published from its CI artifact); the tier's definition is `ci/benchmarks/spreadsheetbench/smoke/` at the commit above.

## Re-running it

The tier's tasks, split and overrides are committed in cap-evolve under `ci/benchmarks/spreadsheetbench/smoke/`. To run the same configuration again, dispatch the Benchmarks workflow on a branch at the commit above:

```bash
gh workflow run benchmarks.yml -R skillberry-ai/cap-evolve --ref <branch> -f tier=smoke -f bench=spreadsheetbench \
  -f iterations=3 -f trials=3 -f agent_model=rits/Qwen/Qwen3-8B \
  -f optimizer_model=claude-opus-4-8 -f algorithm=hill-climb-all
```

Model calls are sampled, so a re-run gives a new measurement, not the same numbers.
