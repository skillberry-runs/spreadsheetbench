# Process for Iteration 5

## Ranked Failure Clusters

1. **MISSED/EXTRA VALUES (CONTRACT/STRUCTURE)**
   - Tasks: 395-36, 560-12, 50768, 7902, 37456, 48527
   - Leverage: High (6 tasks)
   - Diagnosis: Agent is either missing cells in the target range or writing outside it. Often caused by incorrect indexing when using pandas/openpyxl.
   - Lever: STRUCTURE (Explicit target range check and verification).

2. **WRONG VALUE/TYPE (KNOWLEDGE/CONTRACT)**
   - Tasks: 43436, 53647, 51-12, 267-18
   - Leverage: Medium (4 tasks)
   - Diagnosis: Logic errors in calculation or mismatched types (e.g., int instead of float).
   - Lever: CONTRACT (Explicit type and precision rules).

## Kept Edits and Verification

(To be filled)

## Environment Faults
None diagnosed.

## Kept Edits and Verification

- **Guidance: MINIMAL MODIFICATION**: Added "Do not write data into cells outside the specified `answer_position`". 
  - Lever: CONTRACT. 
  - Verify: Tasks 395-36, 560-12, 50768 wrote past the answer range.
  - Blast Radius: BOUNDED. Passing tasks already follow this.
- **Guidance: Boundary Check**: Added step 2 to checklist: "Did I write any values OUTSIDE the `answer_position`?". 
  - Lever: STRUCTURE. 
  - Verify: Directly addresses "written past where the answer ends" in 395-36, 560-12, 50768.
  - Blast Radius: BOUNDED.
- **Guidance: Indexing Guidance**: Added explicit mapping for Excel $\rightarrow$ Pandas/Openpyxl. 
  - Lever: KNOWLEDGE. 
  - Verify: Tasks 7902, 43436 showed indexing confusion (e.g. `i+2`, `min(6, num_rows)`).
  - Blast Radius: BOUNDED.
- **Guidance: Type Precision**: Added rule about `int` vs `float`. 
  - Lever: CONTRACT. 
  - Verify: Task 53647 failed due to `int` where `float` was expected.
  - Blast Radius: BOUNDED.
- **System Prompt**: Created a basic, strong prompt with Inspect $\rightarrow$ Plan $\rightarrow$ Execute $\rightarrow$ Verify cycle. 
  - Lever: STRUCTURE. 
  - Verify: Overall robustness; ensures agent doesn't just jump to code.
  - Blast Radius: UNBOUNDED (but necessary since it was empty).
