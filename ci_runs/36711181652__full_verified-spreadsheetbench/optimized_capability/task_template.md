<!--
  PLACEHOLDER CONTRACT — filled in per task by the adapter. All six of these MUST appear
  somewhere in this file or every task scores 0:
    {instruction} {spreadsheet_path} {spreadsheet_content} {instruction_type}
    {answer_position} {output_path}
  {max_turns} is optional. A literal brace must be written {{ or }}.
-->
Solve the following spreadsheet manipulation task. You are given six pieces of information:

- **instruction** — what to do. It is written by a spreadsheet user, so it usually asks for
  "a formula". Treat it as a description of the RESULT you must produce, not of the bytes to
  write into the cell: you must store the computed value (see output contract below).
- **spreadsheet_path** — the workbook to modify.
- **spreadsheet_content** — only the FIRST FEW ROWS, as a preview. It is a hint, not a
  specification: the real header row, data extent, and sheet layout may differ from what it
  suggests. Verify anything you rely on by reading the actual file.
- **instruction_type** — `Cell-Level Manipulation` (answer_position is the exact cell(s) to
  fill) or `Sheet-Level Manipulation` (answer_position is the MAXIMUM range you may modify).
- **answer_position** — the only cell(s) that are graded.
- **output_path** — write the modified workbook to this exact path.

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

## Output contract

Your answer is read back by a program, with no recalculation:

```python
openpyxl.load_workbook({output_path!r}, data_only=True)   # then reads answer_position
```

- Every graded cell must hold a **literal value** — a number, string, or datetime you
  computed in Python. A formula string assigned through openpyxl has no cached value and
  reads back as empty, scoring 0 even when the formula is correct. So compute the result in
  Python and assign it.
- Load the workbook with `data_only=True` unless you specifically need existing formula
  text; a default load drops the cached values of formula cells you never touched and can
  blank a graded cell.
- Match the answer cell for cell, blanks included. `answer_position` is a bounding box, not
  a quota: never invent a placeholder such as `0` for a cell whose answer is blank. But where
  the answer is blank and the input holds a value, clearing that cell to `None` IS part of
  the answer — deletion, removal and de-duplication tasks are graded exactly that way.
- Only values are compared; fills, fonts, and number formats are ignored.

## How to work

You have up to {max_turns} rounds. Each round, reply with exactly ONE python code block.

1. **Inspect first.** Print the sheet names, the header row, where the data really ends, the
   current contents of `answer_position`, and any column your logic reads.
2. **Calibrate.** If a worked example or "expected result" block sits outside
   `answer_position`, compute your own value for it and confirm it matches before filling
   the rest — that is free ground truth for your interpretation. A pre-filled cell inside
   `answer_position` is only a hint; where the instruction states the expected result, the
   instruction wins.
3. **Solve.** Compute the values in Python, write them to `answer_position` (creating the
   named sheet if it does not exist yet), and save to `output_path`.
4. **Verify before finishing.** In a round of its own that writes nothing, re-open
   `output_path` with `data_only=True` and print the value of every graded cell. Check it
   against the answer you computed — same values, same types, blank in exactly the cells
   your answer leaves blank. A `None` you did NOT intend means you stored a formula; fix it
   and re-save. A `None` you did intend is correct — do not fill it.

Creating the output file is not the end of the task; a verified-correct answer inside it is.
Reply with no code block once that readback looks right, and you are done.

If your code raises, the traceback comes back to you — fix the cause and retry.
