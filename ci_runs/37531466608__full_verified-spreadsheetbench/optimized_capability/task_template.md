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

You have up to {max_turns} rounds of interaction. In each round, reply with exactly ONE python code block:
1. Information-gathering code (e.g. inspecting the file) — the execution result is returned to you.
2. Final solution code that writes the modified file to output_path — once that file exists, you are done.
If your code raises an error, the traceback will be returned to you; fix the code and try again.
