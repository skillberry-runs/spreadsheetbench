### Guidance for Spreadsheet Manipulation

#### 1. Handling Data Types
- **Dates**: Use `datetime` objects. Avoid `strftime` or converting dates to strings.
- **Numbers**: Use `int` or `float`. Avoid `str()` conversion for numeric results.
- **Empty Cells**: Use `None` or leave them as is if they should be empty.

#### 2. Writing Values
- **No Formulas**: Do not use `openpyxl.cell.cell.Formula` or strings starting with `=`. The grader cannot execute them.
- **Precision**: If the task involves currency or percentages, ensure the numeric value is correct; formatting is handled by Excel, but the underlying value must be a number.

#### 3. Avoiding Over-Modification
- **Strict Range**: Only modify cells in the `answer_position`.
- **Preservation**: When using `pandas.to_excel`, be careful not to overwrite the entire sheet if you only need to change a few cells. Using `openpyxl` to load a workbook and modifying specific cells is generally safer for preserving existing data.

#### 4. Verification Step (Required)
Before submitting your answer, run a code block that:
1. Loads the `output_path` file.
2. Prints the values in the target range.
3. Confirms that:
   - No formulas were written.
   - Types are correct (e.g., `type(val)` is `datetime.datetime` or `float`).
   - Only the intended cells were changed.
