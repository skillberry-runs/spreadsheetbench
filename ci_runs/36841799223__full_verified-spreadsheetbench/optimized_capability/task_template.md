<!--
  THE AGENT'S JOB DESCRIPTION — editable capability text, same as prompt.md.
  This comment block is STRIPPED before the agent sees it.

  LOAD-BEARING PLACEHOLDERS — filled in per task, must SURVIVE any edit:
    {instruction} {spreadsheet_path} {spreadsheet_content} {instruction_type}
    {answer_position} {output_path}
  Optional: {max_turns}. No other {braces}. A literal brace must be doubled: {{ or }}.
-->
Solve the following spreadsheet manipulation question.

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

## What these fields mean

- **instruction** — the change to make, written by the owner of the file. Read it to the end. Any
  method it names (a specific Excel function, an array formula, a macro) is a preference about how
  they imagined doing it, never part of the deliverable: you are graded on the resulting cell
  values, so solve it whichever way is reliable in Python.
- **spreadsheet_path** — the input workbook. Read it; never modify it in place.
- **spreadsheet_content** — the target range's size, each sheet's real data extent, and a pandas
  preview of the first rows. In that preview the leftmost column is a 0-based pandas index and
  sheet row 1 was consumed as the header, so **preview row `i` is Excel row `i + 2`**, and pandas
  column position `j` is Excel column `j + 1`. Columns shown as `Unnamed: N` are real columns whose
  header cell is blank — not columns to skip; and if *every* column comes back `Unnamed: N`, then
  sheet row 1 is not the header row at all — the real headers sit further down, so find them by
  printing cells before you anchor anything to a row number. The preview is only the first few rows;
  derive the ranges you actually use from cells you print yourself.
- **instruction_type** — `Cell-Level Manipulation`: `answer_position` is the exact cell(s).
  `Sheet-Level Manipulation`: `answer_position` is the MAXIMUM range you may modify. Either way
  every cell in `answer_position` is checked, and nothing outside it is.
- **answer_position** — the only cells you may change, and the only ones that are graded. It is a
  bounding *box*: it bounds how much room the answer may occupy, not where inside it each part goes.
  A start cell the instruction names inside the box beats the box's own top-left corner, and any row
  or column of the box the answer never reaches keeps its original contents.
- **output_path** — write the finished workbook here, at exactly this path.

<example>
`answer_position` is `D4:F20` and the instruction says "list each region with its total starting at
D6, headers in row 5". The anchor is row 5, not row 4: `D4:F4` keeps whatever it already held, the
headers go in row 5, the regions start at row 6, and the rows after the last region stay empty.
Which of E and F holds the total is settled by the header text you print out of row 5, never by
assuming the number belongs in the box's last column.
</example>

## Set up: two loads, two purposes

```python
import os, datetime, openpyxl

IN, OUT = "{spreadsheet_path}", "{output_path}"
SHEET = "SheetNameFromAnswerPosition"   # or wb.sheetnames[0] when answer_position names none
RANGE = "B2:B43"                        # answer_position with any 'Sheet'! prefix removed

wb  = openpyxl.load_workbook(IN)                            # EDIT and SAVE this one
ws  = wb[SHEET]
wsv = openpyxl.load_workbook(IN, data_only=True)[SHEET]     # READ cached values from this one
```

`ws[a1].value` gives a formula back as TEXT (`'=SUM(C5)/(C19+C20)'`), not a number — anything you
derive from that string is wrong from the start. The computed number lives in `wsv`. Never save
`wsv`'s workbook.

## Round 1 — READ before you compute

Print, with `repr()` and type, every cell you will read from, key off, or anchor to, plus the
distinct values of any column you will filter on:

```python
for a1 in ["A2", "C5", "H2"]:
    print(a1, "formula:", repr(ws[a1].value), "| value:", repr(wsv[a1].value))

vals = [wsv[f"G{{r}}"].value for r in range(2, 40)]
print("distinct:", sorted({{(repr(v), type(v).__name__) for v in vals}})[:20])
```

Print the cells of `answer_position` as they arrive in the input, too, along with the rest of the
column they sit in. **A cell that already holds a value is usually a worked example of the intended
answer**: check your rule against it, keep that same rule running over the cells that are still
empty, and leave the example cell as it is. Three things make it *not* an example to preserve —

- it holds a **formula**, which cannot survive the save, so write the value it stood for;
- it holds a **marker that is the odd one out in its column**, where the neighbouring rows hold real
  computed entries: that is a placeholder standing in for the value you were asked to compute, so
  compute it and write over it (a marker the *whole* column uses is the opposite case — it is the
  table's way of writing "no value", and you match it);
- it holds a **rounded transcription** of a value the sheet stores at full precision, because owners
  type what their number format displays. The full value is what is expected.

Agreement you had to round to obtain is not agreement. Reproduce an example's rule, never its digit
count.

Years, ids and codes are stored as numbers in one column and as text in another, so
`2014 == '2014'` is False, and text criteria differ in case and trailing spaces. Normalise both
sides when matching, and note that `''` is a present, empty value, not a failed lookup.

Where the prose is loose, the sheet is precise. The **header text over the target column** and any
**example the user left in a neighbouring column or row** — a worked formula, a hand-filled answer,
a row of markers — are a tighter specification than the sentence you were given, and they win when
the two disagree. A header reading "Open by end of May" settles a prose clause about "not closed
before the first day of the month"; it means the state at one instant, not activity across a period.

## Round 2 — SOLVE

Compute the values in Python, assign only the cells the instruction asks for, and save:

```python
os.makedirs(os.path.dirname(OUT), exist_ok=True)
ws["B19"] = 16        # a literal int / float / datetime / str — never a string starting with "="
wb.save(OUT)
```

## Round 3 — CHECK the saved file (required; this is what "done" means)

Re-open the file you saved and verify it, addressing cells by their literal A1 names rather than by
the indices you wrote with:

```python
from openpyxl.utils import range_boundaries, get_column_letter

chk = openpyxl.load_workbook(OUT)[SHEET]    # data_only=False, so any formula shows as text
src = openpyxl.load_workbook(IN)[SHEET]

c0, r0, c1, r1 = range_boundaries(RANGE)              # works for "B2:B12" and for "B4"
r1 = min(r1, max(chk.max_row, r0))                    # a range may extend far past the real data
cells = [f"{{get_column_letter(c)}}{{r}}" for r in range(r0, r1 + 1) for c in range(c0, c1 + 1)]

formulas = [a1 for a1 in cells if isinstance(chk[a1].value, str) and chk[a1].value.startswith("=")]
changed  = [a1 for a1 in cells if chk[a1].value != src[a1].value]
filled   = [a1 for a1 in cells if chk[a1].value not in (None, "")]

print(f"{{len(cells)}} checked (rows {{r0}}-{{r1}}) | {{len(filled)}} non-empty | {{len(changed)}} changed")
assert not formulas, f"these cells still hold formulas: {{formulas[:10]}}"
for a1 in changed[:40]:
    print(a1, repr(chk[a1].value), type(chk[a1].value).__name__)
print("changed:", changed[:80])
```

Each block runs under a time limit, so keep this bounded: the clip to `chk.max_row` above stops you
walking thousands of empty rows, and the slices stop the printout flooding. For a very large range,
print the counts plus a sample of the first and last populated rows rather than every cell.

Read the output and confirm all four:

1. **No cell in the range holds a formula** (the assert above), and none holds an Excel error
   string such as `#N/A`, `#NAME?`, `#VALUE!` or `#NUM!`.
2. **Every type is the type the answer should be** — numbers as `int`/`float`, dates as `datetime`,
   text as `str`, and cells whose answer is nothing left as `None`.
3. **`changed` is exactly the set of cells the instruction asked you to compute**, plus any cell
   that previously held a formula. If it is larger, you have overwritten cells whose expected value
   was their own original content; if it is smaller, you have skipped cells you were asked to fill.
4. **At least one written value agrees with a figure you did not compute yourself** — a pre-filled
   cell of the target range, a cached result elsewhere in the sheet (via `wsv`), or a total the
   sheet already contains. Compare with `==` against the unrounded source value: agreement you had
   to round to obtain is not agreement, and is the one way this check certifies a wrong answer. It
   is corroboration rather than proof, so when a figure the owner left behind contradicts a rule the
   rest of the sheet supports, say so and go with the rule.

## The interaction contract

You have up to {max_turns} rounds. Each reply is exactly ONE ```python fenced code block — nothing
outside the fence, and no second block. Work through the rounds above in order; take extra rounds
when you need to read more or to correct a write.

An output file existing is **not** being done, and neither is a check that prints the right SHAPE —
the expected count of non-empty cells, all of the right type — over wrong values. You are done when
the Round-3 output is all-clear. Reply then with no code block, and that ends the task. Once the
readback matches what you intended, stop: do not save the file again.

If the check shows a problem, the next block must be diagnostic — print the source cells with
`repr()` and their types, and the intermediate lookups — and then a corrected write. Never re-send
the same block, and never "fix" it by narrowing the write so that it stops touching the cells that
came out wrong: a correction fixes the rule, not which cells the rule is responsible for. A cell you
leave alone is still graded, as a claim that its original contents were the expected answer. If your
code raises an error, the traceback comes back to you; fix the cause rather than re-running it.
