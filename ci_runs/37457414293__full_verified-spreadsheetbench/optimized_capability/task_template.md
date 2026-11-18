You are tasked with manipulating an Excel spreadsheet. 

### Input Information:
- **Instruction**: {instruction}
- **Spreadsheet Path**: {spreadsheet_path}
- **Spreadsheet Content**: {spreadsheet_content}
- **Instruction Type**: {instruction_type}
- **Answer Position**: {answer_position}
- **Output Path**: {output_path}

### Requirements:
1. **Compute and Write**: You must implement the logic described in the instruction using Python.
2. **Literal Values**: Write the final results as literal values (numbers or text) into the cells. **Do not write Excel formulas**, as the grader cannot execute them.
3. **Targeted Modification**: Only modify the cells at the `Answer Position`. Do not change any other part of the spreadsheet.
4. **Output**: Save the modified spreadsheet to the `Output Path`.

### Interaction Contract:
- You have up to {max_turns} turns to complete this task.
- In each turn, you can write Python code to analyze the spreadsheet, perform calculations, and save the final output.
- You are finished when the final modified spreadsheet is saved to the `Output Path` and you have verified that the values are correct, types are accurate, and no unnecessary cells were modified.

Please begin by analyzing the spreadsheet and implementing the requested changes.
