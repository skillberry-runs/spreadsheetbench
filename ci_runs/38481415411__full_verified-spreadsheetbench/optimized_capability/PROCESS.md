# PROCESS — Iteration 3

## Failure Clusters
1. **Type Mismatch (String vs Number)**: (High Leverage)
   - Tasks: 402-43, 9569, 46897, 560-12, 53647.
   - Diagnosis: Agent writes numbers as strings or vice versa.
   - Lever: CONTRACT (Updated `prompt.md` "Typed Values" and `task_template.md` verification).
2. **Range Coverage / Boundary Errors**: (Medium Leverage)
   - Tasks: 227-40, 402-43, 80-42, 50768, 560-12, 59196.
   - Diagnosis: Agent leaves cells empty in the target range or writes outside of it.
   - Lever: STRUCTURE (Updated `prompt.md` "Verification" coverage rules).
3. **Minimal Impact / Over-editing**: (Medium Leverage)
   - Tasks: 227-40, 48527, 50768, 560-12, 59196.
   - Diagnosis: Agent modifies cells that already have the correct value.
   - Lever: CONTRACT (Added "No Over-writing" check to `prompt.md` "Verification").
4. **Logic / Calculation Errors**: (Low Leverage)
   - Tasks: 51-12, 37456, 6698, 53647, 267-18, 43436, 48620.
   - Diagnosis: Incorrect values computed.
   - Lever: N/A this iteration (too diverse).
5. **Infrastructure / Output Failure**: (Low Leverage)
   - Task: 37378.
   - Diagnosis: Agent wrote the file, but the grader reports no output file. Likely an environment or path mismatch.
   - Lever: N/A (Handed back as environment fault).

## Kept Edits
- `prompt.md`: Updated "Verification" -> "Coverage" to be more explicit about boundaries.
- `prompt.md`: Updated "Verification" -> added "No Over-writing" check.
- `prompt.md`: Updated "Typed Values" to explicitly forbid writing numbers as strings.
- `task_template.md`: Updated "Verify" step to include explicit data type matching.

## Verification
- `prompt.md` (Coverage): trace 227-40 wrote past range end -> new rule "ensure you have not written a single value outside those boundaries" directly addresses this.
- `prompt.md` (No Over-writing): trace 227-40 changed cells that matched original input -> new rule "Confirm you have not modified any cell that was not explicitly requested" directly addresses this.
- `prompt.md` (Typed Values): trace 9569 wrote floats as strings -> new rule "do NOT write them as strings" directly addresses this.
- `task_template.md` (Types): trace 402-43 wrote int instead of str -> updated verification to "data types... match the expected output exactly".

## Blast Radius
- Bounded: All edits are additive clarifications to verification or type constraints.
- Passing tasks (e.g., 142-12, 382-10) already follow these rules (they don't over-edit, they use correct types, and they stay in range).

## Subagents/Features
- None used; performed diagnosis and edits inline.
