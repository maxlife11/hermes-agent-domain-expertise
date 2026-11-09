# Offline evaluation protocol

Implemented condition A: deterministic checks on normalized API operation maps. Python 3.11+, standard library only. No model calls, credentials or network access required.

From repository root:

```sh
python3 -m unittest discover -s evals -p 'test_*.py' -v
python3 -m evals.run --cases evals/fixtures/cases.jsonl --out results/local-demo
python3 -m evals.score --outputs results/local-demo/outputs.jsonl --labels evals/fixtures/labels.jsonl --cases evals/fixtures/cases.jsonl --require-exact
```

Choose a new output directory for each run: existing runs are never overwritten. Only synthetic sanitized results should be committed. Local customer data belongs outside this repository in approved storage.

## Input contract

Each JSONL task has exactly id, source, before, after, docs.
before and after map operation strings (for example GET /items) to objects containing only a required list of parameter names.
docs contains objects with unique ref, operation, and params (provided parameter names).
Operations and parameter names are exact, case-sensitive strings.

This is not OpenAPI. Normalize real inputs only with a documented, reviewed conversion; normalization can introduce errors and its labor must be counted. Unsupported schema fields fail validation. Missing baseline operations escalate. Only required parameters newly added in the transition are checked; existing documentation defects are out of scope.

Public cases.jsonl and labels.jsonl are development fixtures. They cover removal, required changes, already-correct examples, no change, unknown operations, multiple missing parameters, scope boundaries and untrusted reference text. They were authored for this implementation; passing them is regression evidence, not independent or held-out performance.

## Outputs and metrics

Each run emits outputs.jsonl, manifest.json, review.md and initially unfilled reviews.jsonl. Manifest records input/runner/engine hashes, Python, available Git revision, elapsed machine time and explicit unknown labor/review costs. External API cost is zero for this offline baseline; total delivery cost is unknown.

score.py requires exact case-ID coverage and rejects duplicate findings/escalations, source/evidence mismatch, inconsistent status and proposals outside fixed safe templates. It reports TP/FP/FN, precision/recall (null when undefined), exact cases and escalation agreement. It validates consistency with supplied normalized inputs, not source truth, general prose quality, criticality, business usefulness or reviewer independence. Optional --report writes hashes for cases, labels, outputs, scorer and input validator. See the [benchmark runner](../benchmarks/README.md) for coverage and longitudinal diagnostics.

Malformed input fails the batch before output creation. No partial result is silently labeled successful. Output directories are immutable by convention; hashes make provenance inspectable but are not tamper-proof signatures.

## Next evaluations

A: this baseline. B: future Hermes with frozen reviewed skills. C: future candidate changes.
No B/C execution adapter exists yet. Pin the Hermes version and model before adding one. Use a separate agent-visible input mount and evaluator-only labels mount for private holdouts, with customer/template/version splits. A public label file on the same filesystem is not a security boundary.

Do not call the current synthetic set a holdout. Obtain permitted real cases and independent labels before generalization or commercial claims. Change one component at a time and count normalization, review and learning costs.

See [review protocol](../pilot/review_protocol.md) and [release controls](../pilot/release_checklist.md).
