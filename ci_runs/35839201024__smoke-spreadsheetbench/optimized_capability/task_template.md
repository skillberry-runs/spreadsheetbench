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

You have up to {max_turns} rounds. Each round, reply with EXACTLY ONE ```python fenced code
block and nothing outside it (a reply with no code block runs nothing and wastes the round;
keep reasoning to short `#` comments inside the block). Work in this order and do not skip a step:

1. INSPECT (do this first, every task). Load the workbook with openpyxl and PRINT what is
   actually there: the sheet names, the header row(s), which column letter holds each field
   you need, and the current values in and just around answer_position — including where the
   real data starts and ends. Do not assume column names or cell positions from the preview;
   the preview may relabel headers (e.g. `Unnamed: N`) or show only the first rows.
2. SOLVE. Using the coordinates you just confirmed, COMPUTE each answer cell from the data you
   read (never hardcode a value copied from the preview — your final code is re-run on other
   copies with different data). Write only the target cell(s) with openpyxl and save to
   output_path, creating any missing parent directories first.
3. VERIFY (required before you finish). Re-open output_path and PRINT the value of every cell
   in answer_position. Stop only once you have checked and ALL of these hold:
   - every target cell holds the intended value;
   - the type is right (a number stored as a number, float where the result is fractional,
     text left as text — not converted to a date/number);
   - no cell OUTSIDE answer_position was changed, and every other sheet is still present.
   If any check fails, fix the code and write again. Reply WITHOUT a code block only after this
   verification has passed.
If your code raises an error, the traceback is returned to you; read it and fix the code — do
not resend the same code unchanged.
