# full_verified / spreadsheetbench — run 36300445911

A cap-evolve benchmark run, backfilled on 2026-11-18 from its CI artifact (the run predates per-run folders, so `recipe/` is missing). Its row is on the [benchmark-runs dashboard](https://skillberry-runs.github.io/dashboard/).

[Actions run](https://github.com/skillberry-ai/cap-evolve/actions/runs/36300445911) · [commit `cfcba9ebc`](https://github.com/skillberry-ai/cap-evolve/tree/cfcba9ebca4c3e46108d7f39b2f90c613d9bc458)

## Run

| | |
|---|---|
| Benchmark / tier | `spreadsheetbench` / `full_verified` |
| Source | manual (temp-no-skill-run3) |
| Date (UTC) | 2026-09-27T07:20:58Z |
| Conclusion | failure |
| Agent model | `ibm-rits/google/gemma-4-31B-it` |
| Optimizer model | `ibm-ete-int/aws/claude-opus-5` |
| Algorithm | `hill-climb-all` |
| Iterations / trials | 1 / 1 |
| Gate (k·SE) | 1.0 |

## Results

- No suite result: the run did not finish successfully (see `report.md` and the Actions run).

Details per task are in `report.md`.

## Files

- [`runmeta.json`](runmeta.json) — how the run was launched: models, tier, iterations, trials, commit
- `recipe/` was not available for this run (published from its CI artifact); the tier's definition is `ci/benchmarks/spreadsheetbench/full_verified/` at the commit above.

## Re-running it

The tier's tasks, split and overrides are committed in cap-evolve under `ci/benchmarks/spreadsheetbench/full_verified/`. To run the same configuration again, dispatch the Benchmarks workflow on a branch at the commit above:

```bash
gh workflow run benchmarks.yml -R skillberry-ai/cap-evolve --ref <branch> -f tier=full_verified -f bench=spreadsheetbench \
  -f iterations=1 -f trials=1 -f agent_model=ibm-rits/google/gemma-4-31B-it \
  -f optimizer_model=ibm-ete-int/aws/claude-opus-5 -f algorithm=hill-climb-all
```

Model calls are sampled, so a re-run gives a new measurement, not the same numbers.
