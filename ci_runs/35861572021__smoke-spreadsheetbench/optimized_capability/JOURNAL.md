# JOURNAL — optimizer handover (append-only, whole run)

YOU (the optimizer) own this file. It is the running, accumulating handover across ALL iterations — accepted AND rejected — and it is NEVER reset. Each iteration you APPEND one new entry at the bottom (under the marker line); you do NOT edit or delete earlier entries. Read the whole journal before proposing, so you build on EVERY prior attempt (not just the last accepted one) and never re-test a refuted idea.

You CANNOT know your own gate result while you write — the harness scores you AFTER you stop and stamps a **RESULT** line (outcome + Δ + the tasks you measurably broke/fixed, plus the ones whose move was too small to resolve) right below your entry. So do NOT write 'what worked' as a guess. To learn what actually worked, READ the framework RESULT lines of prior entries (and LEDGER.md): an entry whose RESULT says `rejected` with `broke={...}` tells you which specific edits to drop or redesign — its diff.patch is in ./prior_iterations/<id>/.

Append your entry for THIS iteration below the marker, using this shape (INTENT only — the framework appends the RESULT):

    ## Iteration <your candidate id> — <one-line headline of what you tried>
    - Changes I made (1 line per edit; name the file/tool + cluster it targets):
    - Per change, the EXPECTED effect + why it's safe (which failing task it should fix;
      why no passing task changes behavior):
    - Building on prior RESULTS: which prior entries' broke/fixed I used, and what I
      did NOT re-try because a prior RESULT showed it regressed (cite ids):
    - Refuted hypotheses (a prior RESULT proved this is NOT the fix — never re-test):
    - High-value clusters still NOT cracked (and the guard/tool designs already tried):
    - Plateau signal (are the last few RESULTs flat/negative? if so, which LEVER to switch
      to — e.g. a NEW composite tool instead of another guard, or prompt instead of code):
    - Focus next iteration:

## Iteration cand_1a / cand_1b / cand_1c (round 1) — fix the silent formula-string read + the print-is-not-a-check verification, on two different surfaces

- Changes I made (per sibling; all three target the SAME diagnosed clusters, deliberately on DIFFERENT surfaces/forms):
  - cand_1a — `prompt.md` ONLY. Four added sections, all KNOWLEDGE / worked-example form: (1) `load_workbook()` without
    `data_only=True` returns formula TEXT, so an `isinstance(v,(int,float))` guard silently drops it and totals come out
    too LOW — with a worked two-handle read/write example [cluster: "number LOWER than expected", 374-9 x3, 53161 t2];
    (2) never pad a range with invented `0`/`''`/`None`, WITH an explicit carve-out that instruction-directed blanking
    and row-shift blanks ARE the answer [55457 t0/t2, 32468 t2]; (3) the DataFrame-index vs Excel-row offset table
    (+2 / +1 / none) and the read/write header-pairing rule [40467 t2, 32468 t2]; (4) derive extents from the data, and
    Python's exclusive upper bound [53161 t0, 347-49].
  - cand_1b — `task_template.md` ONLY. Same clusters, STRUCTURAL form instead of knowledge: the 3-step round list is
    rewritten as an ORDERED procedure in which each step is a precondition of the next; round 1 is a look-before-compute
    round that must print source cells WITH their types; round 3 becomes "check by COMPARISON" (recompute one target
    cell by a second route, cell count vs the TARGET SIZE the adapter already prints, row count before/after, any total
    the instruction itself names). DELETED the old line "Reply without a code block when you are satisfied the saved
    file is correct" and the old round-3 wording "re-open output_path and print the values you wrote" — the traces show
    that print-only step is exactly what let every failure through.
  - cand_1c — BOTH surfaces, composed without duplication: 1a's knowledge in `prompt.md`, plus a shorter ordered
    procedure in `task_template.md` that INVOKES the checks rather than restating the facts.
- Expected effect + why safe: the formula-read fix is the one edit verified end-to-end — replaying 374-9's own final
  code with `data_only=True` added and nothing else changed makes all 32 cells match gold, including the float type on
  B10 (0/3 -> 3/3). Blast radius checked against all 12 passing traces: 52216 t1/t2 already pass `data_only=True`;
  47484 / 160-6 / 418-29 read via pandas (already cached values), so the rule is a no-op for them; adding the flag to
  52216 t0's read was verified to produce byte-identical output. Every kept edit is ADDITIVE, or a clarification of a
  contract the passing tasks already satisfy.
- What I deliberately did NOT ship, having diagnosed it as UNSAFE (the round's main finding): three rules that read as
  obvious fixes each regress a currently-passing task, because half this suite is row-deletion/shift work rather than
  fill-a-column work. (i) "always edit in place with openpyxl, never rebuild via df.to_excel" would force 160-6 off the
  `dropna` + `to_excel` rewrite that IS its passing mechanism, and 47484 / 418-29 t0/t1 too — 8 of 12 passing traces.
  (ii) "leave every cell outside answer_position identical / never blank a cell inside it" is FALSE here: 160-6's own
  gold changes 30 cells OUTSIDE answer_position, 418-29's gold blanks 4 cells INSIDE it, and 347-49's gold blanks 237.
  (iii) "diff input vs output and fix any outside-range difference" would order 160-6 to undo its correct row shift.
  Confirmed from the adapter: grading reads ONLY cells inside answer_position, so an outside-range diff is not a
  contract the scorer holds the agent to. I scoped edit (2) with an explicit carve-out instead of shipping (ii).
- Building on prior RESULTS: none exist — this is round 1 (LEDGER holds the baseline only; rejected.jsonl absent).
- Refuted hypotheses: none yet by a RESULT. The three rules above are recorded as diagnosed-unsafe-before-spending,
  which is not the same as refuted by measurement.
- High-value clusters still not cracked: 32468 (12- vs 13-month window — a semantic guess; the instruction names a ~39M
  anchor that no trial ever checked, which the round-3 comparison step only reaches indirectly) and 55457 (its
  `instruction` field is literally blank, so the value semantics are unknowable; only its filler and type damage is
  addressable). 347-49 needs its blank-run scan to span a repeating HEADER block, addressed here only via the row-count
  check.
- Focus next round: read whichever sibling gates best and check in its traces whether round 1 / round 3 were actually
  EXERCISED. Never exercised => the FORM is wrong (switch surface); exercised and still wrong => the content is.

> **RESULT (framework, measured):** REJECTED (champion unchanged) · val=0.511 Δ=+0.011 · fixed={—} · broke={52216} · unresolved={40467, 53161} (moved less than 2·SE of its own measurement — NOT evidence the edit touched those tasks; do not redesign on them). — its WHOLE batch was reverted; re-introduce only the edits that did NOT break a task above, dropping/redesigning the ones that did.
<!-- cand_1a: rejected val=0.511 Δ=+0.011 -->

## Iteration cand_1c — (duplicate handover; optimizer re-appended a prior entry unchanged)

> **RESULT (framework, measured):** UNRESOLVED (not judged; champion unchanged) · val=0.556 Δ=— · fixed={—} · broke={—} · unresolved={40467, 52216} (moved less than 2·SE of its own measurement — NOT evidence the edit touched those tasks; do not redesign on them). — the measurement could not separate this edit from re-measurement noise, so it is NOT evidence against the edit. Its batch was still reverted. To resolve it, re-measure it under a FRESH tag (re-running the same tag REPLACES its rollouts) or with more trials in ONE evaluation; do not redesign it on this round's numbers, and do not re-derive it as a new idea.
<!-- cand_1c: unresolved val=0.556 Δ=— -->

## Iteration cand_1b (round 1; covers siblings cand_1a and cand_1c, whose handover blocks were filed under this same round) — fix the silent formula-string read + the print-is-not-a-check verification, on two different surfaces

- Changes I made (per sibling; all three target the SAME diagnosed clusters, deliberately on DIFFERENT surfaces/forms):
  - cand_1a — `prompt.md` ONLY. Four added sections, all KNOWLEDGE / worked-example form: (1) `load_workbook()` without
    `data_only=True` returns formula TEXT, so an `isinstance(v,(int,float))` guard silently drops it and totals come out
    too LOW — with a worked two-handle read/write example [cluster: "number LOWER than expected", 374-9 x3, 53161 t2];
    (2) never pad a range with invented `0`/`''`/`None`, WITH an explicit carve-out that instruction-directed blanking
    and row-shift blanks ARE the answer [55457 t0/t2, 32468 t2]; (3) the DataFrame-index vs Excel-row offset table
    (+2 / +1 / none) and the read/write header-pairing rule [40467 t2, 32468 t2]; (4) derive extents from the data, and
    Python's exclusive upper bound [53161 t0, 347-49].
  - cand_1b — `task_template.md` ONLY. Same clusters, STRUCTURAL form instead of knowledge: the 3-step round list is
    rewritten as an ORDERED procedure in which each step is a precondition of the next; round 1 is a look-before-compute
    round that must print source cells WITH their types; round 3 becomes "check by COMPARISON" (recompute one target
    cell by a second route, cell count vs the TARGET SIZE the adapter already prints, row count before/after, any total
    the instruction itself names). DELETED the old line "Reply without a code block when you are satisfied the saved
    file is correct" and the old round-3 wording "re-open output_path and print the values you wrote" — the traces show
    that print-only step is exactly what let every failure through.
  - cand_1c — BOTH surfaces, composed without duplication: 1a's knowledge in `prompt.md`, plus a shorter ordered
    procedure in `task_template.md` that INVOKES the checks rather than restating the facts.
- Expected effect + why safe: the formula-read fix is the one edit verified end-to-end — replaying 374-9's own final
  code with `data_only=True` added and nothing else changed makes all 32 cells match gold, including the float type on
  B10 (0/3 -> 3/3). Blast radius checked against all 12 passing traces: 52216 t1/t2 already pass `data_only=True`;
  47484 / 160-6 / 418-29 read via pandas (already cached values), so the rule is a no-op for them; adding the flag to
  52216 t0's read was verified to produce byte-identical output. Every kept edit is ADDITIVE, or a clarification of a
  contract the passing tasks already satisfy.
- What I deliberately did NOT ship, having diagnosed it as UNSAFE (the round's main finding): three rules that read as
  obvious fixes each regress a currently-passing task, because half this suite is row-deletion/shift work rather than
  fill-a-column work. (i) "always edit in place with openpyxl, never rebuild via df.to_excel" would force 160-6 off the
  `dropna` + `to_excel` rewrite that IS its passing mechanism, and 47484 / 418-29 t0/t1 too — 8 of 12 passing traces.
  (ii) "leave every cell outside answer_position identical / never blank a cell inside it" is FALSE here: 160-6's own
  gold changes 30 cells OUTSIDE answer_position, 418-29's gold blanks 4 cells INSIDE it, and 347-49's gold blanks 237.
  (iii) "diff input vs output and fix any outside-range difference" would order 160-6 to undo its correct row shift.
  Confirmed from the adapter: grading reads ONLY cells inside answer_position, so an outside-range diff is not a
  contract the scorer holds the agent to. I scoped edit (2) with an explicit carve-out instead of shipping (ii).
- Building on prior RESULTS: none exist — this is round 1 (LEDGER holds the baseline only; rejected.jsonl absent).
- Refuted hypotheses: none yet by a RESULT. The three rules above are recorded as diagnosed-unsafe-before-spending,
  which is not the same as refuted by measurement.
- High-value clusters still not cracked: 32468 (12- vs 13-month window — a semantic guess; the instruction names a ~39M
  anchor that no trial ever checked, which the round-3 comparison step only reaches indirectly) and 55457 (its
  `instruction` field is literally blank, so the value semantics are unknowable; only its filler and type damage is
  addressable). 347-49 needs its blank-run scan to span a repeating HEADER block, addressed here only via the row-count
  check.
- Focus next round: read whichever sibling gates best and check in its traces whether round 1 / round 3 were actually
  EXERCISED. Never exercised => the FORM is wrong (switch surface); exercised and still wrong => the content is.

> **RESULT (framework, measured):** UNRESOLVED (not judged; champion unchanged) · val=0.589 Δ=— · fixed={—} · broke={—} · unresolved={40467, 52216, 53161} (moved less than 2·SE of its own measurement — NOT evidence the edit touched those tasks; do not redesign on them). — the measurement could not separate this edit from re-measurement noise, so it is NOT evidence against the edit. Its batch was still reverted. To resolve it, re-measure it under a FRESH tag (re-running the same tag REPLACES its rollouts) or with more trials in ONE evaluation; do not redesign it on this round's numbers, and do not re-derive it as a new idea.
<!-- cand_1b: unresolved val=0.589 Δ=— -->

<!-- cap-evolve:journal-append-below — add your Iteration entry under this line; do not edit anything above it -->
