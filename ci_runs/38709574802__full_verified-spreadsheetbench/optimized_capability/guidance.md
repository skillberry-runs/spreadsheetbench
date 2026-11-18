### Guidance

#### Core Output Contract: Literals Only
- **NO FORMULAS**: Never write Excel formulas (e.g., `=SUM(...)`, `=VLOOKUP(...)`) to cells. The grader reads the saved values and does not recalculate.
- **COMPUTE IN PYTHON**: Perform all calculations, lookups, and concatenations using Python. Write the resulting **literal value** (number, string, date) directly to the cell.
- **NO ERROR STRINGS**: Do not write Excel error text (e.g., `#N/A`, `#VALUE!`, `#REF!`) to cells. If a lookup fails or data is missing, handle this in Python and write a clean value (e.g., `0`, an empty string, or the original value) as required by the task.
- **TYPE FIDELITY**: Write the correct Python type to the cell:
  - For numbers/currency: use `int` or `float`.
  - For text: use `str`.
  - Do not wrap numbers in quotes (e.g., write `100`, not `"100"`) unless the task specifically asks for a string.

#### Precision and Modification
- **TARGET RANGE ONLY**: Modify ONLY the cells explicitly requested. Do not touch cells outside the target range.
- **PRESERVE INPUTS**: If the expected result for a cell is its own original input, do not overwrite it with a new value of the same content; leave it untouched.
- **VERIFY BEFORE SAVING**: Before saving the workbook, verify that:
  1. No formulas were written.
  2. No `#N/A` or other error strings are present in the output range.
  3. No cells outside the target range were accidentally modified.
