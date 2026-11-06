# Development baseline v1

Run date: 2026-11-05 (America/New_York). Condition: A, offline deterministic rules.

| Check | Observed result |
| --- | --- |
| Regression tests | 5 passed |
| Synthetic development cases | 12 |
| Exact finding and escalation matches | 12/12 |
| True-positive findings | 6 |
| False-positive findings | 0 |
| False-negative findings | 0 |
| External API cost | $0; no network/model calls |
| Human review, normalization and labor cost | Unknown; not measured |
| Hermes / learned skill execution | None |

These authored public fixtures are development checks, not an independent benchmark or private holdout. Precision/recall of 1.0 applies only to six expected findings in these cases. It is not an estimate of real-world accuracy. Cases include no-change examples, unknown operations and intentionally unsupported existing defects.

Artifacts: [manifest](manifest.json), [outputs](outputs.jsonl), [field metrics](metrics.json), [review packet](review.md), [unfilled reviewer records](reviews.jsonl).

Source: [input cases](../../evals/fixtures/cases.jsonl), [development labels](../../evals/fixtures/labels.jsonl), [protocol](../../evals/README.md).

The run was generated in a workspace before the repository commit was created, so git_commit is null. Engine, runner and input SHA-256 hashes identify the executed content. The commit containing this directory provides the saved snapshot. Timings are machine-specific; reruns need not have identical elapsed seconds.

No source example execution, full OpenAPI parsing, real customer data, independent human review, willingness-to-pay test, B/C comparison or autonomous release was performed.
