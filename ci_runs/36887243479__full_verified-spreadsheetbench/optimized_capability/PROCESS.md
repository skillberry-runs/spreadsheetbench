# PROCESS — what I did this iteration (explainability; REQUIRED)

**Headline:** both remaining failures are the *same* defect — the agent let **cells inside
`answer_position`** decide what its rule should compute, in a case where those cells could not
settle the question. 59595 baked the pre-filled placeholder `'n/a'` into its rule as a branch;
50768 cited a pre-filled example cell on the matrix **diagonal** as "proof" of a grid
orientation that the sheet's own axis labels contradicted. Eight additive edits across both files
make the sheet's structural evidence the authority and make "is this example even capable of
discriminating?" a printed step rather than an assumption.

**The decisive evidence this iteration, found in read-only context.** The prior run at
`reused_seed_run/run_suite/rollouts/val/` holds rollouts of the **identical** `prompt.md` +
`task_template.md` pair (its `cand_0003` == my parent `cand_0001`) on **both** of my failing
tasks, scoring **reward 1.0** on each. So for both clusters I have a measured, correct
trajectory: I can read the gold values and the winning rule rather than guess them. Flakiness
table across that run's five candidates (val split, same tasks):

| task | c1 | c2 | c3 | c4 | c5 | fails |
| --- | --- | --- | --- | --- | --- | --- |
| 50768 | 1 | 0 | **1** | 0 | 0 | 3/5 |
| 59595 | 0 | 1 | **1** | 0 | 1 | 2/5 |

Both are **coin-flips on exactly the ambiguity identified below** — not hard zeros. That is the
single best argument that pinning the ambiguity down is the right lever: the agent already
reaches the correct answer about half the time and has no rule telling it which way to go.

## Ranked issue list (clusters, biggest first)
| rank | cluster | tasks | shared root cause | tag | leverage |
| --- | --- | --- | --- | --- | --- |
| 1 | **A pre-filled answer cell was used to DEFINE the rule, not to check it** | 59595, 50768 (both failures) | the prompt says pre-filled answer cells are "ground truth … If your rule disagrees with the user's own worked rows, your rule is wrong", and the agent over-applied it: it reshaped its *rule* to reproduce those cells. In 59595 that meant emitting a placeholder string; in 50768 it meant trusting a non-discriminating example over the sheet's labels. | CONFLICT + KNOWLEDGE | 2 tasks × 1 trial × 1.0 = **2.0** |
| 1a | ↳ **placeholder text carried into a numeric column** | 59595 | `if current_date < first_date + timedelta(days=6): return "n/a"` — a branch that exists *only* to reproduce `C4:C6='n/a'`. Scorer: "3 cell(s) hold str where int was expected". The existing "one exception" paragraph has a loophole the agent walked through: the exception "does not apply when your rule's own output for that cell is text" — so by making the rule *output* `'n/a'`, the agent made the exception not fire. | CONFLICT (loophole) | 1.0 |
| 1b | ↳ **grid axes taken from the instruction's word order, against the sheet's labels** | 50768 | the sheet labels its axes (`D12='Impact'` heading the row-level strip `E12:E14`=3,2,1; `F16='Liklihood'` heading the column-level strip `F15:H15`=1,2,3). The agent printed all of that and then wrote: *"Despite labels in the sheet appearing swapped vs prompt wording, the worked value F14='1, 3, 5' proves F:H correspond to Impact"*. F14 is the **diagonal** cell (Impact 1, Likelihood 1) — invariant under transposition, so it proves nothing. | KNOWLEDGE + reasoning rule | 1.0 |

**Environment faults: none.** Both traces ran all three rounds, executed every code block
without error, completed the mandated verify round, and printed a clean checklist. Nothing
infrastructural; these are capability failures.

**No other clusters exist this iteration.** The other 38 tasks score exactly 1.0 (binary
reward, 1 trial each); there is no partial-credit or communication/omission failure to cluster.
I did not invent a third cluster to pad the candidate — the prior run lost three consecutive
iterations to exactly that reflex (see META_INSIGHTS).

## Changes made this iteration (one row per edit)
| # | cluster | edit class (from `guidance/system-prompt/SKILL.md`) | file | what it does |
| --- | --- | --- | --- | --- |
| A | 1b | **4. add a rule the source requires** + **5. add an example** | `prompt.md` — new §"A 2-D grid: the sheet's own labels fix which axis is which" | defines *level strip* (the label run bordering the grid, explicitly **including below/right**, because an upward-increasing matrix puts its column labels underneath), gives the 3-line lookup idiom, and states: the strips are the authority, the instruction's word order is not. Carries the **no-strip fallback** (then the wording *is* the authority) and the diagonal-invariance caution. |
| B | 1a | **consolidate a contradiction** (tighten in place, delete nothing) | `prompt.md` §"Change only what was asked", the "one exception" clause | the escape hatch now reads "text **that the rule took from the source data**", and adds "Text your rule emits only because the answer cell it is filling already held that text is **not** that case". Closes the exact loophole 59595 used. |
| C | 1 | **4. add a rule** + **2. add the reason** | `prompt.md` §"Change only what was asked", new bullet | "**A pre-filled answer cell CHECKS your rule; it never DEFINES it.**" Enumerates the reads that remain legitimate (append point, column layout of existing rows, pre-filled *formula*, in-place transform) and forbids one thing: a literal/threshold/cut-off/branch existing only to reproduce a pre-filled **value**. Then the numeric-column case with its reason (a non-numeric string can never normalise to the gold's number, so carrying it through is wrong *with certainty*). |
| D | 1 | **4. add a rule** (reasoning criterion) | `prompt.md` §"Check your logic against the examples you were given" | "**An agreeing example confirms your rule only where a wrong rule would have disagreed.**" When a choice between two readings was forced, run both, print where they differ, and classify the example: agrees-everywhere ⇒ settles nothing (fall back on the sheet's structure); differs ⇒ decisive; differs nowhere ⇒ choice is moot. |
| E | 1b | **6. restructure → ordered precondition** | `task_template.md` step 1 | for a multi-row **and** multi-column `answer_position`, printing all four bordering strips + the cell beyond each, and emitting `rows = <var> (read from <cells>), columns = <var> (read from <cells>)`, is now required **before** step 2 computes anything. Turns "look at the labels" from advice into produced evidence. |
| F | 1 | **6. restructure → ordered precondition** | `task_template.md` step 2 | when a reading had to be chosen, both candidates must be built and the disagreeing coordinates printed with the evidence that picked the winner; and "a worked value at a coordinate where both readings give the same answer … may not be cited as the reason for your choice." |
| G | 1a | **8. tighten the output contract** (checklist item 2) | `task_template.md` step 3 | a provenance requirement: for every non-numeric string the rule produced in a range whose other cells hold numbers, print the **source cell outside `answer_position`** it came from; if none can be named, delete the branch, compute the number, rewrite and re-verify. |
| H | 1b | **8. tighten the contract** (checklist item 4) | `task_template.md` step 3 | adds the "both sides agree" arm: agreement confirms the rule only if the rejected reading would have differed there, else print `non-discriminating`. |

**Seven distinct edit classes** from the capability skill — added sourced rule, worked example,
reason-for-rule, consolidation of a contradiction, restructure-into-ordered-precondition (×2),
output-contract tightening (×2). No lever repeated mechanically, and **nothing deleted**: edit B
is the only change to existing text and it adds a qualifying clause rather than removing a
constraint (constraint-line count rises in both files).

## Verify-the-fix + blast radius (one line per edit)

- **A, E, H (grid axes) — VERIFIED against a measured 1.0 trajectory.** The failing trace's own
  comment is the evidence: `# Matrix labels: Impact levels down E12:E14, Likelihood levels
  across F15:H15.` immediately followed by `col_to_impact = {... ws.cell(15, c).value ...}` and
  `row_to_likelihood = {r: ws.cell(r, 5).value ...}` — it named the strips correctly and then
  bound them backwards. The **passing** run of the identical prompt
  (`reused_seed_run/.../50768__cand_0003__t0.json`) wrote exactly what edit A prescribes:
  `impact_label = ws.cell(row, 5).value` / `likelihood_label = ws.cell(15, col).value`, producing
  `F14='1, 3, 5'`, `G14='2'`, `H12='4, 6'` → **reward 1.0**. The failing run put the `'2'` at
  `F13` instead of `G14`; those are precisely the "1 cell holds a value where the expected output
  has none; 1 cell is empty where a value is expected" in the feedback. So the contract I state
  matches what the SCORER compared, not merely what the old prompt said.
  **Blast radius: BOUNDED.** A subagent enumerated all **10 passing tasks whose
  `answer_position` is multi-row AND multi-column**: 142-12, 227-40, 37456, 395-36, 402-43,
  43436, 45635, 560-12, 7902, 80-42. Six are flat tables with no axis question (142-12, 227-40,
  395-36, 402-43, 80-42, 560-12). The four orientation-dependent ones **already do what edit A
  says**: 37456 reads `ws.cell(row, 6)` (the `F11='Date'` strip) and `ws.cell(11, col)` (product
  headers); 43436 reads column-G department labels and the `I1:K1` month headers; 7902 reads the
  `D2:J2` bucket headers plus B/C row labels; 45635 reads the mirrored `A5:A7` strip. Zero would
  flip. The one task with **no** strip at all (560-12, `I2:J7` into an empty region) is why edit A
  carries the explicit no-strip fallback and edit E lets step 1 say "no label strip borders the
  block" — without that clause this edit would have been unbounded for 560-12, which is exactly
  the check that produced the clause.
- **B, C, G (pre-filled value → rule) — VERIFIED against a measured 1.0 trajectory.** Failing
  trace line: `if current_date < first_date + timedelta(days=6): return "n/a"`, with the
  docstring "Match the worked examples". Its verify round then printed `C4 | worked value 'n/a' |
  my rule's value 'n/a' | agree? True` and declared success — the loophole made the checklist
  pass on a wrong answer. The **passing** run (`59595__cand_0003__t0.json`) has no such branch at
  all: one uniform `sum(p for _, d, p in data if start <= d <= cd)`, writing `C4=4, C5=6, C6=12`
  over the `'n/a'`s → **reward 1.0**. Those three ints are the gold, read off a scored artifact,
  and they confirm the scorer feedback "3 cell(s) hold str where int was expected". Under edit G
  the agent must name a source cell outside `answer_position` for `'n/a'`; there is none (it came
  from `C4:C6`, inside), so it must delete the branch and recompute — which is the 1.0 behaviour.
  Note the rule needs no new validation: the five pre-filled numeric rows C7:C11 already
  confirmed it (18/26/32/26/14 all agree).
  **Blast radius: BOUNDED.** A subagent audited the **8 passing tasks with the most pre-filled
  answer cells** (142-12:15, 382-10:17, 416-15:18, 463-17:17, 48588:17, 55049:21, 7902:16,
  2768:8). Result: **none** reads a pre-filled answer *value* as a rule input, and **none** emits
  a non-numeric placeholder — a grep for `'n/a'/'N/A'/'TBD'` across all 8 is empty. Three
  (142-12, 382-10, 416-15) are `Sheet-Level` **in-place transforms** where the cell's own prior
  value legitimately *is* the input (`return f_value`, `remove_time_keep_date(old)`) — edit C
  explicitly permits that, and permits 416-15's read of `ws["A2"].number_format` (formatting) and
  7902's read of pre-filled **formula text** to learn the calculation. 80-42 infers its
  source→target column map from rows already in the range: permitted by name ("to match the
  column layout of rows already present"), and its uniformly-textual `'N/A'` column comes from
  source sheets outside `answer_position`, so edit B's tightened clause still covers it and edit
  C's numeric-column case cannot fire (that instruction asks for no numeric quantity). Each of
  those four allowances is in the text *because* that audit found a passing task that needed it.
- **D, F (discriminating evidence) — VERIFIED.** The failing trace's rationalisation is quoted
  verbatim in the cluster table: it treated `F14` agreeing as proof. `F14` is Impact 1 ×
  Likelihood 1 — the diagonal — so the transposed rule produces the identical string there;
  `H12` (3×3) is likewise invariant. The two readings differ on **exactly one** cell of the nine
  (`G14` vs `F13`), and no worked value sits there. Under edit F the agent must print that
  disagreeing coordinate and find that no example covers it, which forces it to edit A's strips.
  **Blast radius: BOUNDED** — D and F are gated on "the instruction forced a CHOICE between two
  defensible readings". Unambiguous tasks skip them entirely; the cost where they do fire is
  extra printing in a round that does not write `output_path` (the template already states the
  graded solution is the last block that *wrote* the file, so an extra inspection cannot cost a
  correct answer). Edit H only adds an arm to a checklist branch that previously had no "agree"
  case at all, so it cannot change a verdict that was already being made.
- **Placeholder contract (would zero all 40 tasks if broken).** Re-parsed `task_template.md`
  with `string.Formatter`: all six required placeholders present (`instruction`,
  `spreadsheet_path`, `spreadsheet_content`, `instruction_type`, `answer_position`,
  `output_path`), `max_turns` present, and the literal `{{left}}` intact. The only non-required
  field name is `placeholders`, inside the top HTML comment — **byte-identical to the accepted
  champion `candidates/cand_0001/task_template.md`**, which scored val 0.950, so the adapter
  demonstrably does not render this file through bare `str.format`. I left that comment alone
  rather than "fixing" a header the measured champion already validates.
- **Generalization check.** No edit names a task id, sheet, cell, date or answer. The constants
  are domain-level: the placeholder enum (`n/a`, `-`, `?`, `TBD`, `—`) and the 2-D-range
  condition. Edit A is about any cross-tab; B/C/G about any numeric column with a stand-in;
  D/F/H about any forced reading choice.

## What I deliberately did NOT do
- **No third cluster.** 38/40 tasks pass; there is no other failing signature in this
  iteration's trajectories. Manufacturing a speculative edit is how the prior run lost
  cand_0004 and cand_0005.
- **Did not re-try the two refuted edits** (JOURNAL cand_0001, "Refuted hypotheses"): the
  openpyxl single-cell-range `TypeError` guard (prior cand_0005: val 1.000 → 0.975) and the
  defensive sheet-prefix quote-stripping (prior cand_0004: 1.000 → 0.950). Both factually
  correct, both measured as regressions.
- **Did not touch** the literal-value contract, the normalisation table, the four-step
  procedure, or §"Open at time T" — these carry the +0.600 the champion earned.
- **Did not edit** any adapter, harness, scorer, benchmark or environment file; no shell command
  mutated anything outside this working dir. The only files changed are `prompt.md`,
  `task_template.md` and the handover files I own.

## Process & features used
- **Subagents: yes, two read-only `Explore` agents in parallel**, both for the SAFE test rather
  than for diagnosis (with only two failures, I read those traces myself). One audited the 8
  passing tasks with the most pre-filled answer cells for rule-vs-check leakage; one enumerated
  every passing task with a 2-D `answer_position` and judged whether an axis-label rule would
  flip it. Both came back "zero would flip" **and** each returned a wording caution that is now
  in the shipped text (the no-strip fallback for 560-12; the in-place-transform and
  column-layout allowances for 142-12/382-10/416-15/80-42). The audits changed the edits — they
  were not a rubber stamp.
- **Prior iterations read:** `LEDGER.md` (1 row, ACCEPT, broke nothing), `JOURNAL.md` in full
  including cand_0001's refuted-hypotheses list, `RUNMAP.md`, `prior_iterations/cand_0001/`,
  `INSIGHTS.md`, `META_INSIGHTS.md`. `rejected.jsonl` for **this** run is empty (no refuted
  candidate yet), so no proposal here can be a re-proposal; the refuted ideas I avoided come
  from the prior run's record, cited above.
- **Verification method worth reusing:** `reused_seed_run/run_suite/rollouts/val/` contains
  per-candidate rollouts for the same tasks, so a currently-failing task often has a *scored*
  passing trajectory of the same artifact. Diffing the failing against the passing run gives the
  gold values and the winning rule directly — far stronger than inferring a contract from
  feedback strings. See INSIGHTS.md.
