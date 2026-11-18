<!--
  Per-task user message. The {placeholders} below are filled in by the adapter and are
  load-bearing. REQUIRED: {instruction} {spreadsheet_path} {spreadsheet_content}
  {instruction_type} {answer_position} {output_path}. OPTIONAL: {max_turns}.
  A literal brace must be written {{ or }}.
-->
Solve the following spreadsheet manipulation task. It is described by six fields:

- **instruction** — what the user wants. It is usually phrased as a request for a formula;
  what is graded is the resulting *values*, so read it as a description of the result.
- **spreadsheet_path** — the input workbook. Load this file and edit it; do not rebuild it.
- **spreadsheet_content** — a partial preview: the first few rows of each sheet, plus the
  size of the target. It is lossy. It does not show you exact cell types, trailing spaces,
  merged cells, which cells hold formulas, or any row past the preview — so do not plan
  your solution from the preview alone.
- **instruction_type** — `Cell-Level Manipulation`: answer_position is the exact graded
  cells. `Sheet-Level Manipulation`: answer_position is the maximum region you may modify.
- **answer_position** — the graded range(s). Every cell in it is compared against the gold
  workbook, including cells the instruction does not ask you to change.
- **output_path** — write the finished workbook to exactly this path.

### instruction
{instruction}

### spreadsheet_path
{spreadsheet_path}

### spreadsheet_content
{spreadsheet_content}

### instruction_type
{instruction_type}

### answer_position
{answer_position}

### output_path
{output_path}

## How to work

You have up to {max_turns} rounds. In each round reply with **exactly one Python code
block**; its output (or its traceback, if it raises) is returned to you in the next round.
Work through these four steps in order — do not skip ahead and do not combine step 1 with
step 2.

**Step 1 — Inspect (required; write nothing yet).** Print what you actually need from the
input: the sheet names, `ws.max_row` / `ws.max_column`, and the **values together with
their Python types** (`repr(v), type(v).__name__`) for the columns the instruction refers
to and for the whole answer range. Note which cells in the answer range are already
populated and whether any of them hold a formula string. Any example answers that the sheet
or the instruction gives you belong in this printout too — and for each one, say whether it
sits **inside** `answer_position` (part of the answer: leave it alone unless it cannot match)
or **outside** it (a hand-drawn illustration: a check on your rule, never cells to copy).

**Step 2 — Compute, then write.** Write your rule as one function of its inputs, and apply it
to **every** cell the instruction asks you to produce a value for — including cells that
already hold something. Collect the results in a dict `mine` keyed by cell coordinate *before*
you decide what to write, and print its size plus the entries that matter (if it is large,
print the first and last few, never all of it). `mine` is the set checklist items 2 and 4
below are judged against, so do not shrink it by skipping cells that look already-done — a
cell that already holds something is a comparison to make, not a cell to skip. Then write:
assign the literal values (never a string beginning with `=`), leaving alone every cell your
rule produces no value for, and save to `output_path` (create its parent directory first).

**Step 3 — Verify (required; do not declare yourself finished before this round has run).**
Re-open the file you just wrote the way the grader does and look at what it actually
contains:

```python
from openpyxl import load_workbook

SHEET, RNG = "<the graded sheet>", "<the graded range>"   # wb.worksheets[0] if unprefixed
graded = load_workbook(OUTPUT_PATH, data_only=True)[SHEET]  # exactly how the grader reads it
raw    = load_workbook(OUTPUT_PATH)[SHEET]                  # reveals formulas left behind
_in    = load_workbook(INPUT_PATH,  data_only=True)
src    = _in[SHEET] if SHEET in _in.sheetnames else None    # the original values (may be a
                                                            # sheet you had to create)

cells = [c.coordinate for row in graded[RNG] for c in row]
shown = cells if len(cells) <= 24 else cells[:12] + cells[-12:]   # big range: just the ends
for co in shown:
    g = graded[co].value
    print(co, "graded:", repr(g), type(g).__name__,
          "| raw:", repr(raw[co].value),
          "| input:", repr(src[co].value) if src is not None else "(new sheet)")

# A formula is invisible to the grader: data_only reads it as None, so check the raw copy.
left = [co for co in cells
        if isinstance(raw[co].value, str) and raw[co].value.startswith("=")]
assert not left, f"formulas the grader will read as empty: {{left}}"
print("graded non-empty:", sum(graded[co].value is not None for co in cells),
      "of", len(cells))

# For every cell your rule covered that ALREADY held something, show the decision you made.
# Cap the output: print the first and last few, then the totals.
clashes = [] if src is None else [(co, src[co].value, mine[co]) for co in mine
                                  if co in cells and src[co].value is not None]
for co, old, new in (clashes if len(clashes) <= 12 else clashes[:6] + clashes[-6:]):
    print(co, "was", repr(old), type(old).__name__, "-> my rule", repr(new),
          type(new).__name__, "-> wrote", repr(graded[co].value))
print("pre-filled cells my rule covers:", len(clashes))
```

Then read that output against this checklist. Every item must be answered from a value you
actually printed — a line that restates your rule and ends in "checked" does not satisfy
any item:

1. No cell in the graded range is a formula string, and none is an Excel error text
   (`#N/A`, `#NUM!`, `#VALUE!`, `#REF!`, `#DIV/0!`).
2. For every coordinate in `mine` the graded file now holds a value the grader can match:
   its Python type is the type the gold would hold — a real `datetime` for a date, a number
   for a number, the sheet's own text for text. In particular no cell in `mine` still holds
   carried-over text that cannot normalise to the number or date your rule produced for it
   (see "the one exception" under "Change only what was asked"). Judge this over all of
   `mine`, not only over the cells you happened to write.
3. Every cell in the range your rule produced **no** value for still holds the value it had
   in the input, and cells whose correct answer is "nothing" are `None`. A mostly-empty
   graded range is a normal, correct answer — do not fill cells to raise the non-empty count.
4. Re-derive each worked value available to you **by calling your rule**, and print the
   `where | worked value | my rule's value | agree?` line for each. The worked values are the
   `clashes` list above (the pre-filled cells your rule covers — already capped) plus every
   concrete case stated in the instruction. Compare the way the grader does — round both
   numbers to 2 decimals, coerce numeric strings — then act on it:
   - **Both sides hold a value and they still differ** → a real disagreement. Before changing
     anything, rule out the four benign causes: the user hand-rounded, float-representation
     noise, a stale formula cache from older data, and a neighbouring cell produced by a
     *different* rule (read its own header or row label). If none of those explains it, your
     rule is wrong — fix the rule and recompute from the source data.
   - **The worked value is blank or missing where your rule produced a value** → not a
     disagreement. Keep your value; a hand-typed illustration is allowed to be incomplete.
   - **No worked value exists** → say so explicitly instead of asserting the item.

A round that does not modify `output_path` does not replace your submitted solution — the
graded solution is the last code block that wrote `output_path`. So verifying costs you
nothing but a round.

**Step 4 — Fix and re-verify.** If any checklist item fails, correct the code, write
`output_path` again, and run step 3 again. Only when all four items hold do you reply
without a code block.
