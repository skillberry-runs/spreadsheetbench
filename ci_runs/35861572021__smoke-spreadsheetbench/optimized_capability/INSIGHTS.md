# INSIGHTS — summarized, verified findings (accumulate across the whole run)

The JOURNAL is your per-iteration diary; THIS file is the distilled, VERIFIED takeaway a future iteration should read instead of re-reading the whole journal or old sessions/traces. Update it whenever you have a genuinely NEW, confirmed finding (an accepted/rejected RESULT counts as confirmation; a guess does not) — not every iteration needs a new entry. Structure each addition as:

    ## <task or mechanism name>
    - What worked (confirmed by a RESULT, cite the candidate id):
    - What didn't (confirmed by a RESULT, cite the candidate id):
    - Promising but not yet tried:

## MEASUREMENT RESOLUTION on this run (read this before believing any small win)
- What worked (confirmed by a RESULT): nothing yet moved val beyond noise. Round 1's decisive
  number is not a candidate delta at all: two BYTE-IDENTICAL null-control replicates of the seed
  (ctl_null_i0, ctl_null_i0r1 — same bytes, same seeds, same n_trials=3, full 10-task val) scored
  **0.6000 and 0.4667**, so `null_delta_between_control_replicates = 0.1333`. The stored baseline
  (0.50) vs a fresh control also drifted 0.10 (`parent_vs_gate_ref_drift`). This run's evidence bar
  is therefore ~0.13 reward on full val at 3 trials.
- Consequence for future iterations: a candidate must move val by MORE than roughly one whole task
  (0.1 = one of ten tasks flipping all three trials) before the gate can see it. Chasing two or three
  single-trial fixes in one round is not enough — the round must credibly flip a WHOLE task, or
  several. Do not present a delta of 0.05–0.10 as a win; the gate will not, and neither should the
  report.

## Cluster: formula text read as a number (`data_only=True`)
- What worked: the FIX itself is verified at the code level, independent of the gate — replaying
  374-9's own final solution code with `data_only=True` added and nothing else changed makes all 32
  graded cells match gold including the float type at B10 (0/3 -> 3/3). This is the only edit in the
  run so far with an end-to-end verification.
- What didn't (confirmed by RESULT): shipping that fact as PROSE did not reliably produce the fix.
  cand_1a (prompt.md, full knowledge sections, 948 words) came out at reward 0.5111, gate_delta
  −0.0889, and REGRESSED 52216 and 53161 — the one candidate in the round with a stable verdict, and
  it was a reject. Knowledge stated in the system prompt is not knowledge applied.
- Promising but not yet tried: make the typed read OBSERVABLE rather than advised. The strongest
  form available on the two editable surfaces is a worked code block the agent can copy in round 1
  (cand_1b does this and was the round's best at 0.60) — but going further, the template could
  require the agent to print `type(...).__name__` for the exact source cells and quote those types
  back before it is allowed to compute.

## Form matters more than content on this reader (gemma-4-31B-it)
- What didn't: the largest prose addition (cand_1a, prompt.md only) scored WORST of the three and
  regressed two previously-passing tasks. More rules on the system-prompt surface traded correct
  behaviour for rule-following.
- What worked best, though not resolvably: the STRUCTURAL edit on `task_template.md` (cand_1b) —
  turning the 3-round list into an ordered procedure whose round 3 is check-by-comparison, and
  DELETING the old "reply without a code block when you are satisfied" + "print the values you
  wrote" lines. reward 0.6000 vs the run's 0.50 baseline, gate_delta ≈ 0.0 against a fresh control,
  no regressions on any task. Inside the 0.1333 noise floor, so inconclusive, not an accept.
- Promising but not yet tried: the composition (cand_1c, both surfaces, 0.5556) landed BETWEEN its
  two parents, which is the signature of the prose surface actively costing something. If a future
  round wants both, put the knowledge INSIDE the procedure step that needs it rather than in
  prompt.md.

## Rules that look obviously right and are NOT (do not re-derive these)
Verified against the fixtures and the adapter, not guessed. Half this suite is row-deletion /
row-shift work, so each of these regresses a currently-passing task:
- "Always edit in place with openpyxl, never rebuild with `df.to_excel`" — 160-6's PASSING mechanism
  is `dropna(how='all')` + `to_excel`; the row shift IS the answer. Also hits 47484 and 418-29.
  8 of 12 passing traces.
- "Leave every cell outside answer_position identical; never blank a cell inside it" — factually
  false here: 160-6's gold changes 30 cells OUTSIDE answer_position, 418-29's gold blanks 4 INSIDE
  it, 347-49's gold blanks 237. The adapter grades ONLY cells inside answer_position, so the
  outside-range half is not even a contract the scorer holds.
- "Diff input vs output and fix outside-range differences" — would order 160-6 to undo its correct
  row shift, turning 3/3 into ~0.

## Still-uncracked clusters, with what is known about each
- **347-49 (0/3, the largest single gap):** its blank-run scan uses `else: break`, stopping at the
  first non-blank row, so it deletes 10 rows where gold deletes 72 (a repeating header block).
  Verified to reproduce the scorer's 1037/222/182/92 counts exactly. A pure pandas round-trip with
  NO deletion is byte-identical to the input, so `to_excel` is not the culprit — the scan logic is.
- **32468 (0/3):** t0/t1 use a 12-month window where gold implies 13; the instruction names a ~39M
  anchor no trial ever checked. t2 separately pairs `range(4,35)` (pandas, header consumed) with
  `row = 5 + idx` (openpyxl) and lands every value one month late plus a trailing `None` at I35.
- **55457 (0/3):** its `instruction` field is literally blank, so the value semantics are
  UNKNOWABLE from the prompt. Only its filler damage is addressable, and trial t1 already shows the
  A/B: dropping `else: results.append(0)` removed all 5 filler violations at no cost.
- **53161 (0.333):** t0 is a one-column extent error (`range(6,31)` = F..AD, missing AE); t2
  hardcodes table rows 16/17/21 when the real block is header 11, data 12–17.
- **40467 (0.667):** t2 only — `read_excel(p)` paired with `to_excel(header=False)`, one-row shift.

## Growth result for cand_1b (growth round 1, +6 val trials -> pooled n=9) — the resolution lever, and why it could not resolve
- `grow.py --candidate cand_1b --add-trials 6 --growth-round 1 --k-se 1.0` returned
  **recommendation: promote** — pooled val 0.5889 (stderr 0.1438) vs the reference at 0.500,
  paired Δ=+0.0889 > 1.0·SE=0.0699. I did NOT book that as an accept, because grow.py gates
  against `--current` = the run's `best_id` (the STORED seed), and the stored seed's reward is a
  number measured in an earlier round: this run already measured `parent_vs_gate_ref_drift = 0.10`
  between that stored number and a byte-identical control run concurrently. The briefing's own rule
  is to gate against a CONCURRENT control for exactly this reason.
- Re-checked with `gate_check.py` against each concurrent control replicate (no new rollouts, the
  trials were already on disk). The verdict FLIPS:
  | reference | ref reward | Δ | threshold | verdict |
  | --- | --- | --- | --- | --- |
  | ctl_null_i0 | 0.6000 | **−0.0111** | 0.0452 | reject |
  | ctl_null_i0r1 | 0.4667 | **+0.1222** | 0.0730 | accept |
  | both pooled (6 trials) | 0.5333 | +0.0622 | 0.0448 | accept |
  | seed (stored, drifted) | 0.5000 | +0.0889 | 0.0699 | accept |
- **The instability is in the REFERENCE, not in the candidate — so growth is structurally unable to
  fix it.** The whole ±0.067 spread of the deltas above is the 0.1333 gap between two BYTE-IDENTICAL
  control replicates of the seed. Adding trials to cand_1b shrinks cand_1b's stderr (0.1633 -> 0.1438)
  and therefore the threshold, but it cannot shrink the reference's spread, so no number of extra
  candidate trials makes this verdict stable in EITHER direction. A second growth round was available
  (max_growth_rounds=2) and I declined it on that reasoning rather than on budget.
- Also worth recording honestly: growing 3 -> 9 trials moved cand_1b DOWN, 0.6000 -> 0.5889, toward
  the pooled-control region (0.5333). The 0.600 first reading was the high end of its own band. Even
  the most favourable honest comparison (pooled control, +0.0622) is well under the run's stated
  evidence bar of 0.1333, so no reading of these numbers supports an accept. Booked inconclusive.
  Regressions: NONE under any of the four references.


## MEASUREMENT RESOLUTION on this run (read this before believing any small win)
- What worked (confirmed by a RESULT): nothing yet moved val beyond noise. Round 1's decisive
  number is not a candidate delta at all: two BYTE-IDENTICAL null-control replicates of the seed
  (ctl_null_i0, ctl_null_i0r1 — same bytes, same seeds, same n_trials=3, full 10-task val) scored
  **0.6000 and 0.4667**, so `null_delta_between_control_replicates = 0.1333`. The stored baseline
  (0.50) vs a fresh control also drifted 0.10 (`parent_vs_gate_ref_drift`). This run's evidence bar
  is therefore ~0.13 reward on full val at 3 trials.
- Consequence for future iterations: a candidate must move val by MORE than roughly one whole task
  (0.1 = one of ten tasks flipping all three trials) before the gate can see it. Chasing two or three
  single-trial fixes in one round is not enough — the round must credibly flip a WHOLE task, or
  several. Do not present a delta of 0.05–0.10 as a win; the gate will not, and neither should the
  report.

## Cluster: formula text read as a number (`data_only=True`)
- What worked: the FIX itself is verified at the code level, independent of the gate — replaying
  374-9's own final solution code with `data_only=True` added and nothing else changed makes all 32
  graded cells match gold including the float type at B10 (0/3 -> 3/3). This is the only edit in the
  run so far with an end-to-end verification.
- What didn't (confirmed by RESULT): shipping that fact as PROSE did not reliably produce the fix.
  cand_1a (prompt.md, full knowledge sections, 948 words) came out at reward 0.5111, gate_delta
  −0.0889, and REGRESSED 52216 and 53161 — the one candidate in the round with a stable verdict, and
  it was a reject. Knowledge stated in the system prompt is not knowledge applied.
- Promising but not yet tried: make the typed read OBSERVABLE rather than advised. The strongest
  form available on the two editable surfaces is a worked code block the agent can copy in round 1
  (cand_1b does this and was the round's best at 0.60) — but going further, the template could
  require the agent to print `type(...).__name__` for the exact source cells and quote those types
  back before it is allowed to compute.

## Form matters more than content on this reader (gemma-4-31B-it)
- What didn't: the largest prose addition (cand_1a, prompt.md only) scored WORST of the three and
  regressed two previously-passing tasks. More rules on the system-prompt surface traded correct
  behaviour for rule-following.
- What worked best, though not resolvably: the STRUCTURAL edit on `task_template.md` (cand_1b) —
  turning the 3-round list into an ordered procedure whose round 3 is check-by-comparison, and
  DELETING the old "reply without a code block when you are satisfied" + "print the values you
  wrote" lines. reward 0.6000 vs the run's 0.50 baseline, gate_delta ≈ 0.0 against a fresh control,
  no regressions on any task. Inside the 0.1333 noise floor, so inconclusive, not an accept.
- Promising but not yet tried: the composition (cand_1c, both surfaces, 0.5556) landed BETWEEN its
  two parents, which is the signature of the prose surface actively costing something. If a future
  round wants both, put the knowledge INSIDE the procedure step that needs it rather than in
  prompt.md.

## Rules that look obviously right and are NOT (do not re-derive these)
Verified against the fixtures and the adapter, not guessed. Half this suite is row-deletion /
row-shift work, so each of these regresses a currently-passing task:
- "Always edit in place with openpyxl, never rebuild with `df.to_excel`" — 160-6's PASSING mechanism
  is `dropna(how='all')` + `to_excel`; the row shift IS the answer. Also hits 47484 and 418-29.
  8 of 12 passing traces.
- "Leave every cell outside answer_position identical; never blank a cell inside it" — factually
  false here: 160-6's gold changes 30 cells OUTSIDE answer_position, 418-29's gold blanks 4 INSIDE
  it, 347-49's gold blanks 237. The adapter grades ONLY cells inside answer_position, so the
  outside-range half is not even a contract the scorer holds.
- "Diff input vs output and fix outside-range differences" — would order 160-6 to undo its correct
  row shift, turning 3/3 into ~0.

## Still-uncracked clusters, with what is known about each
- **347-49 (0/3, the largest single gap):** its blank-run scan uses `else: break`, stopping at the
  first non-blank row, so it deletes 10 rows where gold deletes 72 (a repeating header block).
  Verified to reproduce the scorer's 1037/222/182/92 counts exactly. A pure pandas round-trip with
  NO deletion is byte-identical to the input, so `to_excel` is not the culprit — the scan logic is.
- **32468 (0/3):** t0/t1 use a 12-month window where gold implies 13; the instruction names a ~39M
  anchor no trial ever checked. t2 separately pairs `range(4,35)` (pandas, header consumed) with
  `row = 5 + idx` (openpyxl) and lands every value one month late plus a trailing `None` at I35.
- **55457 (0/3):** its `instruction` field is literally blank, so the value semantics are
  UNKNOWABLE from the prompt. Only its filler damage is addressable, and trial t1 already shows the
  A/B: dropping `else: results.append(0)` removed all 5 filler violations at no cost.
- **53161 (0.333):** t0 is a one-column extent error (`range(6,31)` = F..AD, missing AE); t2
  hardcodes table rows 16/17/21 when the real block is header 11, data 12–17.
- **40467 (0.667):** t2 only — `read_excel(p)` paired with `to_excel(header=False)`, one-row shift.

<!-- cap-evolve:insights-append-below -->
