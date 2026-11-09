# Runnable benchmark diagnostics

The [methodology](../INDEX.md) and [domain contracts](DOMAIN_SPECS.md) define the target. Current implementation is deliberately limited to the existing 12 public synthetic N01 cases and a deterministic runner. A pass proves agreement with authored labels and consistency with supplied normalized inputs, not source truth, independent expertise, profit or Hermes learning.

```sh
python -m unittest discover -s evals -p 'test_*.py' -v
python -m evals.run --cases evals/fixtures/cases.jsonl --out results/local-benchmark
python -m evals.score --cases evals/fixtures/cases.jsonl --labels evals/fixtures/labels.jsonl --outputs results/local-benchmark/outputs.jsonl --require-exact --report results/local-benchmark/metrics.json
python -m benchmarks.report --profile benchmarks/domains/N01.json --cases evals/fixtures/cases.jsonl --labels evals/fixtures/labels.jsonl --outputs results/local-benchmark/outputs.jsonl --out results/local-benchmark/benchmark.json
python scripts/build_report.py --check
```

Use a new output directory each run. Files refuse overwrite. The report recomputes validation from raw outputs; it does not trust a supplied aggregate score. Its profile contains an exhaustive, non-overlapping assignment of case IDs to three task families. Current counts are 2/6/4 against illustrative minimum 5 each: overall score is null, status `insufficient_data`, promotion false, even when all 12 cases pass. Do not add easy cases merely to reach the minimum.

The scorer now rejects fabricated source/evidence, mismatched status, unsupported findings, duplicate findings/escalations and proposals outside fixed safe templates. This is intentionally restrictive; free-form agent proposals need a separately validated evaluator. It does not inspect the truth of source documents or certify semantic safety. It shares input validation with the baseline, so independent real-source validation remains necessary.

For paired diagnostics add `--previous path/to/previous/benchmark.json`. It requires identical profile/case/label/scorer/validator/reporter fingerprints; outputs may differ. A series break requires a bridge experiment, not bypassing the check. The helper is for trusted local artifacts, not tamper-proof third-party certification. Statistical significance, repeated-trial reliability, privacy isolation, reviewer scoring, model provenance capture and autonomous promotion are not implemented.

See [recorded run](../results/development-baseline-v2/summary.md). Earlier v1 artifacts are preserved as historical field-only scoring and are not comparable to v2. A source hash supports reproducibility, not data independence or correctness.
