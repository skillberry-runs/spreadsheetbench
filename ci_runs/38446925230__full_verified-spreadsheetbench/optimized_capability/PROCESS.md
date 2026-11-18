# Process: Iteration 3

## Ranked Failure Clusters
1. **"How can I" -> Formula-as-String** (KNOWLEDGE GAP)
   - Tasks: 46897
   - Leverage: High (Recover 1.0 reward, prevents "how-to" confusion)
   - Lever: Knowledge / Contract clarification
2. **Unrequested Modifications / Clearing Cells** (BEHAVIORAL)
   - Tasks: 50768, 48527, 59196
   - Leverage: Medium (Recover reward by preserving original data)
   - Lever: Decision-rule narrowing (Precision)
3. **Logic Errors / Unexpected Empty Output** (BEHAVIORAL)
   - Tasks: 37456, 43436, 53647
   - Leverage: Medium (Recover reward by fixing logic/verification)
   - Lever: Ordered procedure / Verification check

## Edits and Verification
- **Edit 1 (Precision)**: Sharpened "Precision" rule in `prompt.md` and `task_template.md` to explicitly forbid clearing cells unless requested.
  - Verify: Trace 48527 cleared cells when not requested -> new rule "do not clear cells... unless instructions explicitly tell you to".
  - Blast Radius: BOUNDED. Passing tasks like 9569 that clear cells likely do so because it's part of the "modification" requested.
- **Edit 2 (Value-Based Writing)**: Added clarification that "How can I..." instructions request the RESULT, not the formula text.
  - Verify: Trace 46897 wrote formula text `"=COUNTIF..."` -> new rule "If an instruction asks 'How can I create a formula...', it is NOT asking you to write the formula text".
  - Blast Radius: BOUNDED. Passing tasks already write results.
- **Edit 3 (Verification)**: Added sanity and coverage checks to "Verify Before Finishing" in `prompt.md`.
  - Verify: Trace 53647 wrote nothing to the target range -> new rule "Ensure the target range is not unexpectedly empty".
  - Blast Radius: BOUNDED. All passing tasks should have non-empty results if they modified the sheet.

## Subagents/Features Used
- Used Bash scripts to analyze trajectories for patterns (Formula-as-String, Clearing Cells).

## Environment Faults
- None diagnosed.
