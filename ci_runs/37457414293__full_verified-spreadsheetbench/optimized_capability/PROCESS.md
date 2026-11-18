# Optimization Process - Iteration 3

## Ranked Failure Clusters

1. **Infinite Execution Loops** [LEVERAGE: High | TYPE: STRUCTURE]
   - Tasks: 51-12, 267-18, 227-40, 2768, 9726
   - Diagnosis: Agent repeats identical or nearly identical code across multiple turns after failure, failing to analyze the root cause.
   - Fix: Add "Failure Reflection" to Recovery Guidance, requiring explicit discrepancy identification before retry.

2. **Logic & Coverage Failures** [LEVERAGE: High | TYPE: KNOWLEDGE/CONTRACT]
   - Tasks: 560-12, 39046, 50768, 37456, 43436
   - Diagnosis: Computation errors (mismatched values) or missing output (empty cells).
   - Fix: Strengthen the "Compute" step with a mandatory "Sample Trace" to verify logic against 1-2 rows before full application.

## Proposed Edits

- **Edit 1 (prompt.md)**: Added "Failure Reflection" to Recovery Guidance.
  - **Lever**: STRUCTURE (Better reflection/failure analysis).
  - **Verify**: trace 51-12, 267-18: repeated same code ~25 times. New rule forces analysis of *why* it failed.
  - **Blast Radius**: BOUNDED. This is additive guidance for the failure case; passing tasks do not fail and thus don't trigger this.

- **Edit 2 (prompt.md)**: Updated "Compute" step in Operational Procedure to include "Sample Trace".
  - **Lever**: KNOWLEDGE/STRUCTURE (Sample tracing).
  - **Verify**: trace 39046, 43436: incorrect computation of results. Explicit sample tracing forces verification of the logic on a small set.
  - **Blast Radius**: BOUNDED. An additive step for the computation phase that improves correctness without changing the final intended action on passing tasks.

## Verifications

- **Edit 1 (Failure Reflection)**: trace 51-12: repeated same code block 24 times → reflection rule forces identification of discrepancy.
- **Edit 2 (Sample Trace)**: trace 39046: values higher than expected → manual trace of 1-2 rows would identify the logic error before the full write.

## Subagents used
- Used an Agent subagent to analyze trajectories and cluster failures.
