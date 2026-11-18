Solve the spreadsheet manipulation task below.

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

---

## What these fields mean

- **instruction** — the change to make. It is a forum-style question, so it often says "what
  formula would I use?" or "can VBA do this?". Ignore the phrasing about *which tool*: you are
  producing the finished spreadsheet, in Python. Do extract every concrete requirement it
  states (which columns hold what, rounding, decimals, what to leave blank, priority order).
- **spreadsheet_content** — a preview of the FIRST FEW ROWS ONLY, rendered by pandas. Its
  column headers (`Unnamed: 3`) and `NaN`s are pandas artifacts, not sheet contents. Treat it
  as a hint about the file, never as its layout.
- **instruction_type** — `Cell-Level Manipulation`: `answer_position` is the exact set of cells
  to fill. `Sheet-Level Manipulation`: `answer_position` is the *maximum* region you are
  permitted to touch — it is a budget, not a fill target. Inside it, change only what the
  instruction asks for and leave every other cell exactly as it was.
- **answer_position** — the only cells the grader reads. A `'Sheet'!A1:B9` prefix names the
  sheet; with no prefix it is the first/active sheet. `D1,D5,D9` is a list, not a range.
- **output_path** — write your finished workbook to exactly this path.

## Interaction contract

Each round, reply with **exactly ONE python code block** and nothing else — every round except
the last one, where you are done and reply with one sentence and no code (Step 4 below). The
block is executed and its stdout (or its traceback) comes back to you. You have {max_turns}
rounds; spending three or four to get it right is correct and expected — finishing fast is worth
nothing, only the cell values are scored.

**Only the FIRST code block in your reply is executed; any further block is silently
discarded.** So never put an inspection block and a solution block in the same reply — the
second one will not run, and you will believe you checked something you never checked. One
block, one round, then read the result before deciding the next block.

The result also has to actually tell you something. A block whose last statement is
`wb.save(...)` returns `[Code executed successfully with no output]`, which is a *success*
message carrying no information. If you wanted to know a value, you have to `print()` it.

## Procedure — follow these steps in order

**Step 1 — Inspect the real file. Do not skip this, and do not write `output_path` yet.**
Your first block only prints. You cannot place values correctly until you have seen the actual
grid, because the preview hides title rows, side-by-side tables and extra sheets.

```python
import pandas as pd
from openpyxl import load_workbook

wb = load_workbook('{spreadsheet_path}')
print('SHEETS:', wb.sheetnames)
for name in wb.sheetnames:
    ws = wb[name]
    print(f'--- {{name}}  dims={{ws.dimensions}}  {{ws.max_row}}x{{ws.max_column}} ---')
    for row in ws.iter_rows(min_row=1, max_row=min(ws.max_row, 40)):
        cells = [(c.coordinate, c.value) for c in row if c.value is not None]
        if cells:
            print(cells)
```

Read the output and fix in your mind: which sheet, which rows/columns hold the inputs, what
Python type each relevant cell currently has, and what is already in the target cells.

Two things this printout must settle before you move on, because assuming either of them is a
frequent cause of a wrong answer:
- **Every cell your solution will read.** If you are about to write a formula or a lookup,
  print the cells it references and confirm they hold what you expect. A criteria column that
  is one column off, or empty, produces plausible-looking numbers that are all wrong.
- **Any literal text you match on.** If the instruction quotes a label to search for, confirm
  that string really occurs in the column you intend to search. A label quoted in the
  instruction is often a *header* elsewhere in the sheet, so an `==` test against it silently
  matches nothing and leaves the range untouched.

If what you see contradicts your plan, change the plan — do not write the file anyway.

**Step 2 — Compute and write.**
Use openpyxl in place (load the workbook, assign only the target cells, `wb.save(output_path)`).
Write real typed values; write `None` for blank. Prefer computing values in Python; a plain
non-array formula that cannot error is also acceptable.

**Step 3 — Verify the written file, in a new block. This step is mandatory.**
Re-open the file you just wrote and print what is actually in the graded range. This is the
only way you learn whether your row/column indices landed where you intended — writing the
file tells you nothing.

```python
from openpyxl import load_workbook
chk = load_workbook('{output_path}')
print('SHEETS:', chk.sheetnames)                 # every original sheet still present?
ws = chk['Sheet1']                               # the sheet named in answer_position
for row in ws['D8:D11']:                         # exactly the answer_position range
    for c in row:
        print(c.coordinate, repr(c.value), type(c.value).__name__)
```

Then check the printed output against this list, and go back to Step 2 if any item fails:
1. Every cell the instruction should have filled holds a value, and cells that should be blank
   print as `None`.
2. Each value has the right **type** — numbers/dates are not strings, and text that was text in
   the input is still text.
3. No value is `nan`, `NaT`, `'nan'`, `'None'`, `'Unnamed: 3'`, or an Excel error string
   (`#N/A`, `#DIV/0!`, `#VALUE!`).
4. **`chk.sheetnames` still lists every sheet the input had, and the sheet named in
   `answer_position` is one of them.** If a sheet is missing or has become `Sheet1`, you
   round-tripped through pandas — redo Step 2 with openpyxl in place. The grader cannot find a
   renamed sheet and will score zero without comparing any value.
5. Cells outside `answer_position` are unchanged — spot-check a few, including on other sheets.
6. The numbers are right — recompute one or two of them independently and compare.

**Step 4 — Finish.** Once Step 3 prints a clean result, reply with a one-sentence confirmation
and no code block. Do not re-send a block you have already run.
