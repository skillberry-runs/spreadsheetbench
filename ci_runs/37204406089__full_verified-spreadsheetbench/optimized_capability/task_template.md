# Spreadsheet Manipulation Task

You are tasked with modifying an Excel spreadsheet. Follow the instructions carefully to ensure the final output is correct.

## Task Information
- **Instruction**: {instruction}
- **Spreadsheet Path**: {spreadsheet_path}
- **Instruction Type**: {instruction_type}
- **Answer Position**: {answer_position}
- **Output Path**: {output_path}

## Spreadsheet Content
{spreadsheet_content}

## Constraints and Requirements
1. **Literal Values**: You must write the final results as literal values. **DO NOT write Excel formulas** into the answer cells, as they will be graded as empty.
2. **Full Range Coverage**: Ensure every cell in the `{answer_position}` range is populated according to the instruction.
3. **No Error Strings**: Ensure no cells in the output contain Excel error values (e.g., #VALUE!).
4. **Preservation**: Maintain the integrity of the rest of the spreadsheet.

## Completion Criteria
You are finished when:
1. You have executed the manipulation in Python.
2. You have verified that all cells in `{answer_position}` contain the correct literal values.
3. You have saved the modified workbook to `{output_path}`.

**Begin your analysis and implementation now.**
