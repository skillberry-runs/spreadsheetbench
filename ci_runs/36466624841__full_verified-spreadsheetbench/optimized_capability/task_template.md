<!--
PLACEHOLDER CONTRACT — all six of these must survive any edit, or every task scores 0:
{instruction} {spreadsheet_path} {spreadsheet_content} {instruction_type}
{answer_position} {output_path}.  {max_turns} is optional.  A literal brace is {{ or }}.
-->
Solve the spreadsheet manipulation task below. The fields mean:

- **instruction** — what the user wants done. It is written by a spreadsheet user, so it often
  asks for "a formula"; what is graded is the resulting **values**, so compute them in Python.
- **spreadsheet_path** — the input workbook. Read it; never modify it in place.
- **spreadsheet_content** — a `pandas.read_excel(..., header=0)` preview of each sheet. The
  column labels you see are the contents of **Excel row 1**, and preview row `i` is **Excel
  row i + 2**. Treat it as a hint about shape only, and confirm every real cell address by
  opening the file.
- **instruction_type** — `Cell-Level Manipulation`: `answer_position` is the exact cell(s) to
  fill. `Sheet-Level Manipulation`: `answer_position` is the **maximum** range you may modify,
  not a quota to fill.
- **answer_position** — the graded cell(s). When it carries a sheet name (`'Sheet1'!A2:A19`),
  write to **that sheet, selected by name**. Cells in this range that the instruction does not
  ask you to change must keep their original values.
- **output_path** — write the modified workbook to this exact path. Everything outside
  `answer_position` should be preserved as it was in the input.

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

## How to use your {max_turns} rounds

Reply with exactly **ONE** ```python fenced code block per round — only the FIRST block in
your reply is executed, so a reply with several blocks silently throws the rest away. Put
your reasoning in comments inside that one block. Its stdout (or its traceback) comes back to
you as the next message.

Work in this order, one round each:

1. **Inspect.** Open `spreadsheet_path` and `print` what you actually need: the sheet names,
   and the real coordinates and values of the header row, the first data rows, and the cells
   in and around `answer_position`. Nothing is graded this round, so look before you leap —
   guessing a header row or a label is the most common way these tasks are lost. Print the
   cells of `answer_position` as they are in the input, and print any rows below the data that
   look like a worked example of the wanted output — those two tell you the layout and whether
   a formula is already sitting in the range.
2. **Solve.** Compute the answer values in Python and write them, as literals of the right
   type, to `answer_position`; save the workbook to `output_path`.
3. **Audit.** Re-open the **saved output file**, print every cell of `answer_position` with
   its value and Python type, and check each one. A formula string, a `#N/A`-style error token,
   or a wrong Python type is always a defect. A blank cell is a defect only where the
   instruction supplies a value — past the end of the real data, and where you were asked to
   clear a cell, blank is correct, so do not pad the range out to look full. Also check that
   the cells you were not asked to change still hold their original values. Types being right
   is not the same as values being right, so also re-derive **one** value by hand from the input
   and print both numbers side by side — a wrong count or a wrong lookup passes every type check
   there is. This round must only READ — it must not write the output file.
4. **Correct if needed.** If the audit found a problem, send **one complete replacement
   solution** that reads `spreadsheet_path` and writes `output_path` from scratch, then audit
   again. Do not patch the existing output file with a partial snippet.

`[Code executed successfully with no output]` means only that nothing raised — it is not
evidence that your answer is correct or even present. The audit in step 3 is the only
evidence, so do not treat the task as finished before it comes back clean.

When the audit is clean, reply with a one-sentence summary and **no code block** — that ends
the task. Never resubmit a block you have already run unchanged: it cannot produce a new
result, and repeating it wastes rounds you could spend fixing a real defect.
