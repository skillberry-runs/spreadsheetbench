# Process: Initial Capability Creation

## Ranked issue list (clusters by # failing tasks × trials, biggest first)
| rank | cluster | tasks | shared root cause | tag | planned change class |
| --- | --- | --- | --- | --- | --- |
| 1 | Formula-Induced Failures | 37378, 46897, 46897, ... | Agent writes Excel formulas; grader reads values without recalculation. | KNOWLEDGE | Add explicit rule to compute in Python and write literals. |
| 2 | Over-Modification | 39046, 50768, ... | Agent modifies cells outside target range or changes original inputs. | BEHAVIORAL | Add precision and minimality rule. |
| 3 | Type Mismatches | 37456, etc. | Agent writes numbers as strings or uses wrong numeric types. | KNOWLEDGE | Add type integrity rule. |

## Changes made this iteration (one row per edit — aim for MULTIPLE classes, incl. a NEW tool when a cluster needs one)
| cluster | edit class | file / tool | what & why it generalizes | protects passing? |
| --- | --- | --- | --- | --- |
| Formula-Induced Failures | Add Rule | prompt.md | Compute in Python, Write Literals. Prevents zero-scores on formula tasks. | Yes |
| Over-Modification | Add Rule | prompt.md | Precision and Minimality. Prevents regressing original data. | Yes |
| Type Mismatches | Add Rule | prompt.md | Type Integrity. Ensures numeric types are used for numbers. | Yes |
| All | Structure | prompt.md | Added Operational Workflow to guide agent step-by-step. | Yes |

## Verify-the-fix (one line per change: the trace it targets → what the guard/computation/new-tool now does on those exact inputs)
- 37378 / 46897 -> Agent will now compute the COUNTA/COUNTIF logic in Python and write the resulting integer instead of the formula string.
- 39046 -> Agent will only modify cells in the target answer_position, preserving other cells.

## Process & features used
- Serial fallback: performed diagnosis and creation in a single session.

## Good things to PRESERVE (do not let a future iteration undo these)
- The "Compute in Python, Write Literals" rule is the single most important constraint for this benchmark.

## Deliberately skipped (cluster + why — already-passing / needs gold / infra noise)
- None.

---

# DIAGNOSIS.json
```json
{
  "candidate": "cand_0002",
  "headline": "Initial capability creation focusing on eliminating formula-induced zeros",
  "clusters": [
    {
      "id": "C1",
      "name": "Formula-Induced Failures",
      "detail": "Agent writes Excel formulas which the grader cannot recalculate, resulting in empty reads.",
      "tasks": ["37378", "46897"],
      "scope": "SYSTEMIC",
      "latent": false,
      "tag": "KNOWLEDGE"
    },
    {
      "id": "C2",
      "name": "Over-Modification",
      "detail": "Agent modifies cells outside the target range or changes original inputs.",
      "tasks": ["39046", "50768"],
      "scope": "WIDESPREAD",
      "latent": false,
      "tag": "BEHAVIORAL"
    },
    {
      "id": "C3",
      "name": "Type Mismatches",
      "detail": "Agent writes numbers as strings or uses wrong numeric types.",
      "tasks": ["37456"],
      "scope": "BOUNDED",
      "latent": false,
      "tag": "KNOWLEDGE"
    }
  ],
  "edits": [
    {
      "id": "E1",
      "title": "Compute in Python, Write Literals",
      "files": ["prompt.md"],
      "lever": "KNOWLEDGE",
      "clusters": ["C1"],
      "blast_radius": "WIDE",
      "verified": "Directly addresses the formula failure feedback."
    },
    {
      "id": "E2",
      "title": "Precision and Minimality",
      "files": ["prompt.md"],
      "lever": "BEHAVIORAL",
      "clusters": ["C2"],
      "blast_radius": "WIDE",
      "verified": "Prevents unintended changes to the spreadsheet."
    },
    {
      "id": "E3",
      "title": "Type Integrity",
      "files": ["prompt.md"],
      "lever": "KNOWLEDGE",
      "clusters": ["C3"],
      "blast_radius": "WIDE",
      "verified": "Ensures correct numeric types are written."
    }
  ],
  "skipped": [],
  "techniques": ["failure-clustering", "knowledge-injection"]
}
```
