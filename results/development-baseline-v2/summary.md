# N01 development baseline v2 — 2026-11-09

Condition A, same deterministic engine and 12 authored synthetic cases; stronger evaluator and new coverage diagnostics. No Hermes or model ran. No independent reviewer evaluated outputs. This is a measurement repair, not an observed learning gain.

| Observation | Result |
| --- | --- |
| Exact authored cases / escalation agreement | 12/12 each |
| Findings | 6 true positives; 0 false positives; 0 false negatives |
| Source/evidence consistency | Passed against supplied normalized inputs |
| Operation-removal coverage | 2 cases; illustrative minimum 5 |
| Parameter-change coverage | 6 cases; illustrative minimum 5 |
| Scope/negative-control coverage | 4 cases; illustrative minimum 5 |
| Aggregate development score | null — insufficient_data |
| Promotion / expertise | false / not_established |
| Human acceptance, review time, total delivery cost | Not measured |

See [benchmark.json](benchmark.json), [metrics.json](metrics.json), [manifest.json](manifest.json), [outputs](outputs.jsonl) and [unfilled review packet](review.md). Reproduction commands are in [benchmarks/README.md](../../benchmarks/README.md). All failures and assumptions remain visible; perfect fixture agreement is not real-domain accuracy.

The run was produced from a downloaded working snapshot based on a08deb83c706d1273f39783413f69f6dcabff670 plus this revision's files. The manifest's Git commit is null because the working snapshot had no .git directory; this is disclosed rather than invented. File hashes identify the evaluated code/data. The containing Git commit supplies publication provenance. Historical v1 used a different scorer and is not a comparable learning time point.
