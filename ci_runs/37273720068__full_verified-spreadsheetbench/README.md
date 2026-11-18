# full_verified / spreadsheetbench — run 37273720068

A cap-evolve benchmark run, backfilled on 2026-11-18 from its CI artifact (the run predates per-run folders, so `recipe/` is missing). Its row is on the [benchmark-runs dashboard](https://skillberry-runs.github.io/dashboard/).

[Actions run](https://github.com/skillberry-ai/cap-evolve/actions/runs/37273720068) · [commit `61dbc7992`](https://github.com/skillberry-ai/cap-evolve/tree/61dbc7992e8aa32e5d1c66f502b91f548c0b0165)

## Run

| | |
|---|---|
| Benchmark / tier | `spreadsheetbench` / `full_verified` |
| Source | manual (run/gemma-self-opt) |
| Date (UTC) | 2026-10-05T06:42:57Z |
| Conclusion | failure |
| Agent model | `ibm-rits/google/gemma-4-31B-it` |
| Optimizer model | `ibm-rits/google/gemma-4-31B-it` |
| Algorithm | `agent-optimize` |
| Iterations / trials | 5 / 1 |
| Gate (k·SE) | 0.2 |

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
  -f iterations=5 -f trials=1 -f agent_model=ibm-rits/google/gemma-4-31B-it \
  -f optimizer_model=ibm-rits/google/gemma-4-31B-it -f algorithm=agent-optimize
```

Model calls are sampled, so a re-run gives a new measurement, not the same numbers.
