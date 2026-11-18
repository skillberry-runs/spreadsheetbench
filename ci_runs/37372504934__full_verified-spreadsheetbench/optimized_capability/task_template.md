You need to solve the following spreadsheet manipulation question. It contains six pieces of information:
- instruction: the question about spreadsheet manipulation.
- spreadsheet_path: the path of the spreadsheet file you need to manipulate.
- spreadsheet_content: the first few rows of the content of the spreadsheet file.
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

You have up to {max_turns} rounds of interaction. In each round, reply with exactly ONE python code block.

## Interaction Contract
1. **Information-gathering**: Write Python code to inspect the spreadsheet (e.g., reading specific sheets, checking data types, or printing a subset of the data).
2. **Final Solution**: Write Python code that performs the required calculations and writes the modified spreadsheet to `output_path`.
3. **Mandatory Verification**: Before saving the workbook, you MUST write Python code that reads back the values you just wrote to the `answer_position` and prints them to the console. Compare these values against your calculated results to ensure accuracy and that no other cells were modified.

## Critical Constraints
- **No Formulas**: Do NOT write Excel formulas into the file. Calculate the result in Python and write the literal value.
- **Preservation**: Modify only the cells required by the instruction and within the `answer_position`. Leave all other cells untouched. Writing outside the `answer_position` is strictly forbidden unless explicitly instructed.
- **Correct Types**: Ensure you write numbers as numbers and dates as dates, not as strings. If the instruction asks for a date as a "number", write the integer serial value.
- **Confirmation**: Before completing the task, verify that the `answer_position` cells were actually modified and contain the expected values.

Once the file exists at `output_path`, the task is considered complete.
