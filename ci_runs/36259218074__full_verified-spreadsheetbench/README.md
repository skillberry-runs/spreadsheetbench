# full_verified / spreadsheetbench — run 36259218074

A cap-evolve benchmark run, backfilled on 2026-11-18 from its CI artifact (the run predates per-run folders, so `recipe/` is missing). Its row is on the [benchmark-runs dashboard](https://skillberry-runs.github.io/dashboard/).

[Actions run](https://github.com/skillberry-ai/cap-evolve/actions/runs/36259218074) · [commit `31478d5d0`](https://github.com/skillberry-ai/cap-evolve/tree/31478d5d03974422672724241f565fdce7f0bf89)

## Run

| | |
|---|---|
| Benchmark / tier | `spreadsheetbench` / `full_verified` |
| Source | manual (temp-no-skill-measurement) |
| Date (UTC) | 2026-09-26T17:31:14Z |
| Conclusion | failure |
| Agent model | `rits/google/gemma-4-31B-it` |
| Optimizer model | `aws/claude-opus-5` |
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
  -f iterations=1 -f trials=1 -f agent_model=rits/google/gemma-4-31B-it \
  -f optimizer_model=aws/claude-opus-5 -f algorithm=hill-climb-all
```

Model calls are sampled, so a re-run gives a new measurement, not the same numbers.
