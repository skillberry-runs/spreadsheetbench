<!--
  THE AGENT'S JOB DESCRIPTION — editable capability text, same as prompt.md.

  Everything below is sent to the agent as its first user message, so it is part of the
  skill you are optimizing: reword it, restructure it, add or remove guidance, change the
  interaction contract. This comment block is STRIPPED before the agent sees it.

  LOAD-BEARING PLACEHOLDERS — these are filled in per task and must SURVIVE any edit:
    {instruction} {spreadsheet_path} {spreadsheet_content} {instruction_type}
    {answer_position} {output_path}
  Optional: {max_turns}. No other {braces} are allowed.

  If a required placeholder goes missing, or an unknown one appears, the candidate is
  REJECTED before any task runs — the agent would otherwise be told to write its answer to
  a path it was never given. A literal brace must be doubled: {{ or }}.
-->
You need to solve the following spreadsheet manipulation question. It contains six pieces of information:
- instruction: the question about spreadsheet manipulation.
- spreadsheet_path: the path of the spreadsheet file you need to manipulate.
- spreadsheet_content: the target range's total size, the location of the other graded copies
  of this workbook, each sheet's real data extent, and the first few rows of the content.
- instruction_type: Cell-Level Manipulation (answer_position is exact cell(s)) or Sheet-Level Manipulation (answer_position is the maximum range you may modify).
- answer_position: the cell(s)/range you must modify or fill in.
- output_path: write the modified spreadsheet file to this exact path.

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

You have up to {max_turns} rounds of interaction. Reply with exactly ONE python code block per
round; its execution result comes back to you. Work through these steps IN ORDER — each one is a
precondition of the next, so do not skip ahead to writing the file.

**Step 1 — INSPECT (always your first round; never skip it).** Do not write output_path in this
round. Open the input file TWICE and keep both handles for the rest of the task:

```python
from openpyxl import load_workbook
# Paths are NOT pre-defined variables in the sandbox — assign them yourself, as literal
# strings copied from the sections above, in EVERY code block you send.
spreadsheet_path = "<the spreadsheet_path given above>"
wb_val = load_workbook(spreadsheet_path, data_only=True)   # READ values through this one
wb_out = load_workbook(spreadsheet_path)                   # WRITE and save through this one
```

This is not optional bookkeeping. Without `data_only=True` a cell containing a formula reads
back as the formula's TEXT (`'=(B8*12)/12'`), not its number, so every sum over that column
silently becomes 0 or raises a TypeError. Read every source value from `wb_val`; make every
assignment on `wb_out`. Never save `wb_val` — saving a `data_only` workbook erases the formulas
of every other cell in the file.

Then print, from `wb_val`, and read the results before writing any solution code:
   a. every cell of answer_position with its value and type — this tells you whether the target
      is blank, partly pre-filled, or already holds a worked example;
   b. the header cell of every row/column that answer_position covers, in the TARGET sheet;
   c. for each source column you intend to read: print `repr()` of a few cells. If any comes back
      as a string starting with `=`, you are reading the wrong handle — go back to `wb_val`;
   d. the candidate SOURCE cells your calculation would read, and — if your calculation
      aggregates a block of rows — the subtotal of EACH candidate block separately, printed as
      its own line. Do not print only the combined total: you cannot tell which block is the
      right one from a single number.

**Step 1b — MATCH THE NUMBER THAT IS ALREADY THERE (only when answer_position is a SINGLE cell
that already holds a number).** That number is not stale junk to overwrite blindly — it is the
same calculation, and it tells you WHICH rows to read. Your job is usually to recompute it with
one extra restriction, so find the block that reproduces it first.

Worked example. Suppose answer_position is a single cell already holding `14755`, and the
instruction quotes three SUMIF formulas over three separate row-blocks and asks you to add a date
restriction. Step 1d prints, for the criterion but with NO date filter:

```
block rows 8-37 : 14755      <-- equals the number already in the target
block rows 41-58: 117800
block rows 62-74: 12335
```

The target came from rows 8-37 ALONE, not from all three blocks summed (144890). So apply the new
date restriction to rows 8-37 only, and the answer becomes a number SMALLER than 14755. Had you
summed all three blocks and then filtered by date, you would have got 20535 — larger than the
value that was already sitting there, which is the tell that the source range is too wide.

The general rule: when your restricted result comes out LARGER than the unrestricted value that
was already in the cell, your source range is too wide — narrow it, do not re-check the
arithmetic. Adding a restriction can only keep a sum the same or make it smaller. If no single
block reproduces the existing value, print the subtotals and pick the one closest to it rather
than summing everything.

   Base your solution on what these prints actually say, not on what you expected them to say.

**Step 2 — SOLVE.** Assign into `wb_out` and save it to output_path. Preserve everything the
instruction does not ask you to change.

**Step 3 — VERIFY (required; you are NOT finished when the file merely exists).** A saved file
proves nothing: a wrong value, a value stored as text, and a cell left empty all save perfectly.
Re-open output_path with `data_only=True` and print EVERY cell of answer_position as
`coordinate, repr(value), type(value).__name__` — the whole range, not a sample, not only the
cells you believe you touched.

**Step 4 — FINISH.** Reply with NO code block, and in that reply state the values you wrote.
Check the Step 3 print-out against this list FIRST, and treat each failure as a defect in your
logic rather than as an acceptable outcome:

   1. **Coverage.** When instruction_type is Cell-Level Manipulation, every single cell of
      answer_position must read back non-empty — the graded reference fills all of them, so a
      `None` anywhere in the range is a guaranteed miss. This includes cells your lookup found no
      match for: a spreadsheet function over a blank or unmatched numeric source returns 0, so
      write 0 there rather than leaving the cell empty. The one exception is an instruction that
      states a per-row condition (wording like "both X and Y on the same day", "where", "if",
      "flag", "mark"): then fill only the rows that satisfy it and leave the others alone.
      When instruction_type is Sheet-Level Manipulation, do NOT pad the range — a correct answer
      there often leaves most of it empty.
   2. **Type.** Every number reads back as `int`/`float` and every date as a date, never as a
      `str`. If the value arrived as text from the source and the column holds numbers, convert it.
   3. **Scope.** No cell outside the part of answer_position the instruction asks you to change
      was altered from its original input value.
   4. **Consistency.** The values agree with the instruction and with any value the target
      already held in Step 1. In particular, if answer_position was a single cell holding a
      number and your task was to recompute it with an ADDED restriction, your new number must be
      smaller than or equal to the old one. A larger number means you widened the source range
      instead of restricting it — go back to Step 1b and find the block that reproduces the
      original value.

   If any check fails, go back to Step 2 and change the LOGIC. Do not re-send a code block that
   differs from an earlier one only in comments or variable names — that round cannot change the
   graded file, and you have a limited number of rounds. If a printed number is not the one you
   expected, the bug is in which cells you read, not in the arithmetic.

If your code raises an error, the traceback will be returned to you; fix the code and try again.
