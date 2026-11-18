# Task: Modify Spreadsheet

You have been assigned to modify a spreadsheet based on the following instructions.

## Input Information
- **Spreadsheet Path**: `{spreadsheet_path}`
- **Spreadsheet Content**: 
`{spreadsheet_content}`
- **Instructions**: 
`{instruction}`
- **Instruction Type**: `{instruction_type}`
- **Answer Position**: `{answer_position}`
- **Output Path**: `{output_path}`

## Requirements
1. **Follow the instructions exactly**.
2. **Write only literal values**. Do not write formulas (e.g., `=SUM(...)`) or "how-to" formula text to the spreadsheet. If asked "how to calculate" something, implement the logic in Python and write the result.
3. **Maintain spreadsheet integrity**. Do not modify cells outside the target range or clear existing values unless the instructions explicitly tell you to do so.
4. **Verify your work**. Read the cells you modified to ensure they contain the expected literal values before finishing.

Your goal is to produce an output file at `{output_path}` that satisfies the grader's requirements.
