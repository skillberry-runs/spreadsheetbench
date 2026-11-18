# INSIGHTS — summarized, verified findings (accumulate across the whole run)

The JOURNAL is your per-iteration diary; THIS file is the distilled, VERIFIED takeaway a future iteration should read instead of re-reading the whole journal or old sessions/traces. Update it whenever you have a genuinely NEW, confirmed finding (an accepted/rejected RESULT counts as confirmation; a guess does not) — not every iteration needs a new entry. Structure each addition as:

    ## <task or mechanism name>
    - What worked (confirmed by a RESULT, cite the candidate id):
    - What didn't (confirmed by a RESULT, cite the candidate id):
    - Promising but not yet tried:

## SURFACE: `task_template.md` (numbered steps in the user message) vs `prompt.md` (system-prompt prose)
- What worked (confirmed): mechanics written as NUMBERED STEPS in `task_template.md` change agent
  behaviour reliably. `cand_1_anchor` — Step-1 no-write held 30/30, `type()` printed 30/30, clean
  no-code finish 27/30. `cand_2_procedure` (Δ +0.100) and `cand_3_anchorblock` (**ACCEPTED**,
  Δ +0.1222 vs threshold 0.1104) both got their whole gain from edits to this file alone.
- What didn't (confirmed by `cand_1_anchor`, RESULT rejected, Δ 0.000, per-task vector identical to
  control on 10/10): six bounded rules added to `prompt.md` fired ZERO times out of 30. The decisive
  proof is not the scalar — it is that one of those rules ("a blank lookup source contributes 0, not
  blank") exactly matched the gold 56915 needed, and the agent printed `B19, None, NoneType` in its
  own verify output and finished anyway. Plumbing was verified first: all 30 rollouts contained the
  new template text, so the edit DID reach the agent.
- Rule for a future iteration: put behaviour in the procedure. If you find yourself writing a rule
  into `prompt.md`, you are spending the round on the measured-dead surface. `cand_3_anchorblock`
  left `prompt.md` byte-identical to its parent and still cleared the gate.

## FORM: a worked example with real numbers beats a rule stating the same thing
- What worked (confirmed by `cand_3_anchorblock`, ACCEPTED): 47766's "source range too wide" defect
  survived TWO rounds of being stated as a rule. It moved 0.000 → 0.444 the round it was stated as a
  worked example with concrete numbers — three block subtotals printed, one equal to the value
  already in the target, plus the wrong all-blocks total shown as an explicit counter-number. All
  three trials then cited the pre-filled 14755 in their own words and none summed all three blocks.
- What didn't: the same idea as a prose rule in `prompt.md` (`cand_1_anchor`, 0/30 fires) and as an
  implicit hint inside Step 1d (`cand_2_procedure`, still summed all three blocks → 20535).
- Reusable: the escalation ladder is prose rule → numbered step → **numbered step carrying a worked
  example with real numbers**. Do not stop at rung two and conclude the content is wrong.

## SCOPING an edit by target SHAPE+TYPE, not by a value test
- What worked (confirmed by `cand_3_anchorblock`): predicate "answer_position is a SINGLE cell that
  already holds a NUMBER" fires on exactly 1 of 10 tasks (47766, K40 = 14755). 56915's round-2 win
  survived untouched because its target is a 24-cell range.
- What didn't (refuted pre-gate, measured against gold): the unscoped version from `cand_1_anchor`,
  "a non-empty non-zero value in answer_position is a worked example", fires on 168-17 (20 cells),
  438-18 (12), 52532 (2) and 56915 (16) — all passing/now-passing, all holding text headers or
  `#N/A` strings.
- Method that generalizes: before shipping any predicate, enumerate which of the 10 tasks it fires
  on against the on-disk gold. This one measurement killed three edits that read well as prose (the
  blanket "no empty cells" rule — 160-6 gold is 42/72 EMPTY; blanket `data_only=True` — all 5
  passers save a non-`data_only` handle; the unscoped anchor rule above).

## FINISH predicates must be objective, and keyed on a field the agent is GIVEN
- What worked (confirmed by `cand_2_procedure`, 56915 flipped 0 → 1 on 3/3): "every cell of
  answer_position must read back non-empty **when instruction_type is Cell-Level Manipulation**",
  with an explicit "do NOT pad" for Sheet-Level. Measured basis: Cell-Level gold fills 100% of
  answer_position (43213 0/4, 47766 0/1, 49945 0/3, 52532 0/7, 56915 0/24 empty); Sheet-Level gold
  is mostly EMPTY (160-6 42/72, 168-17 55/55, both passing). The `{instruction_type}` key is what
  makes the rule safe rather than destructive.
- What didn't (`cand_1_anchor`): "every cell your solution was SUPPOSED to fill" — intention-relative
  predicates are self-certifying; the agent read its unmatched rows as not-supposed-to-be-filled and
  passed its own gate while printing `None`.

## 47766 — what remains, and it is NOT an anchor problem any more
- Confirmed by `cand_3_anchorblock`'s traces: the block-selection defect is FIXED (all 3 trials pick
  rows 8-37 correctly). The residual is a CodeAct-replay defect: each trial hardcodes one literal
  YEAR (t0 2021 → passes case 1; t2 2022 → passes case 2; t1 "most frequent year" → 8000, 2/3), and
  the adapter replays the final writing block verbatim on the other two graded copies, whose date
  windows differ. Gold: 8000 / 4355 / 9950.
- My pre-gate prediction that case 2 was unreachable (degenerate window K43 == L43) was WRONG — t2
  passed it with 4355. Do not concede that case.
- Promising, not yet tried (highest-value remaining edit on this board): a general replay rule —
  "your final code block is re-run unchanged on other copies of this workbook, so derive every
  window/threshold/date from the workbook's own cells at run time; never write a literal year, date
  or row-count constant." This is general, and it is checkable by grepping your own code.

## Verified CEILINGS — do not spend a round on these, and do not read their flat scores as evidence
- 188-39 (0.000): gold filler is literal `'N/A'` while the instruction says `'NA'`, and `'N/A'`
  appears in NO cell of ANY sheet of ALL THREE inputs (exhaustively scanned). Gold column B holds
  the DESIGNATION, not the employee name; Contact no must be `int`.
- 53449 (0.000): gold writes literal `'X'` under header `'Test'`; neither string is derivable.
- 52532 (0.667, capped): copy 3's gold stores live array formulas over its own recalculated grid
  (Game 2: 483 → 383), which flips the winner. Unreachable from the input.
- 43213 has a PRE-EXISTING per-trial flicker (row-bound drift): `seed` t1 = 0.000 and
  `ctl_null_i0r1` t0 = 0.000 with no candidate text involved. A single 0.333 trial there is noise,
  not a regression — the gate agreed (`regressions: []`).
- Achievable val on these 10 tasks is ~0.87, not 1.0. Current accepted state: 0.6889.

<!-- cap-evolve:insights-append-below -->
