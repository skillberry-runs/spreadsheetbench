# recipes/

Each system's arm code, launchers and settings for the issue #895 experiment, **as they ran**.
These are archived copies (staged by `scripts/stage_history.py`), a record of the experiment, not
a runnable checkout. Read this before trying to rerun anything.

## How the runs were set up

The searches and test windows ran on CCC (LSF) from two directories, neither of which is this repo:

| Name in the scripts | What it was | In this repo |
|---|---|---|
| `$EXP` = `…/cap-evolve-spread-worktrees/exp895` | the experiment workspace: `arms/`, `competitors/`, `tools/` (`node_env.sh`, `gateway.py`, `sandbox/`, `warmup.py`), `runs/` | partly copied here (table below); `tools/node_env.sh`, `competitors/` and the raw `runs/` are **not** here (they're in the off-repo archive) |
| `$REPO` = `…/cap-evolve-spread-worktrees/sbv400-main` (CapEvolve v2: `sbv400-k02`) | a cap-evolve worktree, pinned to the commit below | not here; it's the cap-evolve code |

`tools/node_env.sh` put `$REPO/templates/adapters/spreadsheetbench` on `PYTHONPATH`. That's how
`common/rollout.py` (`CommonRollout`) and `scripts/test_window.py` get `import adapter`: they call the
SpreadsheetBench adapter's `run_target`/`score` from that cap-evolve checkout.

Where the files here came from:

| Here | From |
|---|---|
| `recipes/<system>/` | `$EXP/arms/<system>/` (launchers from `$EXP/tools/`) |
| `recipes/common/` (`rollout.py`, the budget layer) | `$EXP/arms/common/` |
| `recipes/split_ids.json` | `$REPO/ci/benchmarks/spreadsheetbench/full_verified/split_ids.json` |
| `scripts/` | `$EXP/tools/` |

## The cap-evolve commit each run used

Recorded as `code_sha=` in every `results/<system>/s<seed>/search/run_meta.txt`:

| cap-evolve commit | Systems |
|---|---|
| `73103f429fb833883a5c915cd87fe5c5c68fc423` | ACE, CapEvolve (v1), EvoSkill, GEPA, GEPA-full, Meta-Harness, MIPROv2, SkillOpt, Trace2Skill, WikiSkill |
| `0d791eeb78cf11449b30c464e43344997e15bb74` | CapEvolve v2 |

**Neither commit is on GitHub** (checked 2026-11-17: not in `skillberry-ai/cap-evolve` or any fork
branch). They exist only in the CCC worktrees above. To keep the runs reproducible, push them from
there, for example as tags:

```bash
git -C …/cap-evolve-spread-worktrees/sbv400-main tag exp895-main 73103f4 && git -C …/sbv400-main push origin exp895-main
git -C …/cap-evolve-spread-worktrees/sbv400-k02  tag exp895-k02  0d791ee && git -C …/sbv400-k02  push origin exp895-k02
```

(`skillopt_sha=79124b3…` in SkillOpt's `run_meta.txt` is the upstream SkillOpt repo, not cap-evolve.)

## cap-evolve's layout has changed since

cap-evolve [#959](https://github.com/skillberry-ai/cap-evolve/pull/959) (2026-11-08) moved `templates/`
and `examples/` into `benchmarks/`. The recorded commits predate it, so **checking out those commits
needs no changes**. Against a newer cap-evolve, these paths (used in the scripts here) must change:

| Path in these scripts | Path in cap-evolve since #959 |
|---|---|
| `templates/adapters/spreadsheetbench/` (the adapter, on `PYTHONPATH`) | `benchmarks/spreadsheetbench/template/` |
| `templates/adapters/model_config.py` | `benchmarks/_shared/model_config.py` |
| `templates/project/optimizer/INSTRUCTIONS.md` | `benchmarks/_scaffold/project/optimizer/INSTRUCTIONS.md` |

The adapter's behaviour may also have changed after the recorded commit, so a rerun against a
newer cap-evolve is a new experiment, not a reproduction.

## Names that changed with the migration

This repo was cap-evolve's `spreadsheet-history` branch until 2026-11-10. Where a script or doc says
"the spreadsheet-history branch", read
[`skillberry-runs/spreadsheetbench`](https://github.com/skillberry-runs/spreadsheetbench) (this repo).
`scripts/stage_history.py` stages "the branch tree"; today that means this repo.
