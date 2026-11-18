# Process

## Failure Clusters
1. **Formula Use (KNOWLEDGE/CONTRACT)** - High Leverage. (Resolved in cand_0001)
2. **Excel Error Text (KNOWLEDGE/CONTRACT)** - Medium Leverage. (Resolved in cand_0001)
3. **Over-Modification (BEHAVIORAL)** - Medium Leverage. (Resolved in cand_0001)
4. **Empty/Missing Output (BEHAVIORAL)** - Low Leverage. (Resolved in cand_0001)

## New Failure Clusters (Diagnosed in cand_0003)
1. **Type Mismatch (KNOWLEDGE/CONTRACT)** - Low Leverage. Task 31628. Agent writes `datetime` object when an `int` (Excel serial date number) was expected.
   - Lever: Clarify "Typed Values" rule. If the instruction asks for a "number" or "static number" for a date, write the integer serial value, not a datetime object.
   - Verification: Trace 31628 says "1 cell(s) hold datetime where int was expected". The instruction asked for "resulting date in cell B1 as a static number".
2. **Logic Error / Value Mismatch (KNOWLEDGE)** - Medium Leverage. Tasks 51-12, 43436, 59595, 227-40. Agent computes the wrong value or misses some cells in the range.
   - Lever: Improve the "Verify" step in `task_template.md` to be a mandatory, explicit check of the final values against the logic.
   - Verification: Trace 51-12 feedback: "number LOWER than expected". Trace 43436: "different value of the right type".
3. **Range Bleed / Over-Modification (BEHAVIORAL)** - Medium Leverage. Tasks 39046, 395-36, 50768. Agent writes values outside the target range or modifies cells that should remain unchanged.
   - Lever: Tighten "Precision & Minimal Change" rule. Explicitly forbid writing outside `answer_position` unless explicitly instructed.
   - Verification: Trace 39046: "3 cell(s) were CHANGED although the expected value is the cell's own original input". Trace 395-36: "written past where the answer ends".
4. **Silent Failure / Missing Write (BEHAVIORAL)** - Low Leverage. Task 37456. Agent computes results but doesn't write them to the target range.
   - Lever: Add a pre-save checklist in `task_template.md` that requires the agent to confirm the target cells were actually modified.
   - Verification: Trace 37456: "target range is EMPTY in your output — nothing was written there".


## Edits and Verification
- **prompt.md**: Updated "Precision & Minimal Change" to explicitly forbid writing outside `answer_position`. Targets Range Bleed cluster (39046, 395-36, 50768). Verified against 39046: "3 cell(s) were CHANGED although the expected value is the cell's own original input". This additive rule prevents such changes.
- **prompt.md**: Updated "Typed Values" to handle "date as number" requests. Targets Type Mismatch cluster (31628). Verified against 31628: "1 cell(s) hold datetime where int was expected". The new rule tells the agent to use the integer serial value when "number" is requested.
- **task_template.md**: Changed "Verification" from a recommendation to "Mandatory Verification" requiring printing of written values. Targets Logic Error / Value Mismatch cluster (51-12, 43436, 59595, 227-40). Verified against 51-12: agent wrote a value but it was "LOWER than expected"; mandatory printing makes this discrepancy visible before saving.
- **task_template.md**: Added "Confirmation" constraint to ensure target cells are actually modified. Targets Silent Failure cluster (37456). Verified against 37456: "target range is EMPTY in your output"; the confirmation step forces the agent to check if it actually wrote the values.

## Subagents Used
None.
