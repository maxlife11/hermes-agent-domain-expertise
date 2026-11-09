# Hermes domain expertise: evidence before autonomy

Updated: 2026-11-09. Twelve business workflow hypotheses; one deterministic offline baseline; no verified Hermes deployment, learning improvement, independent expert benchmark or commercial winner.

The next step is a reviewer-labeled **real task packet and measured baseline** for one reachable buyer workflow. N01 API documentation is the current technical demonstration. N02 support knowledge maintenance or N03 renewal extraction may be better if buyer/data/reviewer access is stronger.

| Start here | What it provides |
| --- | --- |
| [INDEX.md](INDEX.md) | Canonical knowledge registry, benchmark design, progress metrics, sub-agent boundaries and longitudinal rules |
| [Domain contracts](benchmarks/DOMAIN_SPECS.md) | Units, task families, reference evidence and failure classes for N01–N12 |
| [Benchmark roadmap](benchmarks/ROADMAP.md) | Staged path from synthetic plumbing to supervised paid delivery |
| [Runnable benchmark](benchmarks/README.md) | Reproducible commands, implemented scope and missing capabilities |
| [Recorded v2 run](results/development-baseline-v2/summary.md) | 12/12 authored cases pass; aggregate withheld for insufficient coverage; no promotion |
| [Phase 1](phase1.md), [Phase 2](phase2.md), [Phase 3](phase3.md), [Phase 4](phase4.md) | Candidate workflows, learning controls, economics and conditional implementation |
| [Combined report](full_report.md) | Generated phase content; edit phase files, then run the generator |
| [Evidence](EVIDENCE.md), [changes](CHANGELOG.md) | Sources, uncertainty, corrected assumptions and historical audit |
| [Pilot brief](pilot/brief.md), [operator constraints](pilot/operator_brief.md), [buyer evidence](pilot/buyer_evidence.md) | Missing commercial inputs and experiment boundaries |

## Reproduce locally

Python 3.11+, standard library; no credentials, model spend or network required.

```sh
python scripts/build_report.py --check
python -m unittest discover -s evals -p 'test_*.py' -v
python -m evals.run --cases evals/fixtures/cases.jsonl --out results/local-demo
python -m evals.score --cases evals/fixtures/cases.jsonl --labels evals/fixtures/labels.jsonl --outputs results/local-demo/outputs.jsonl --require-exact
python -m benchmarks.report --profile benchmarks/domains/N01.json --cases evals/fixtures/cases.jsonl --labels evals/fixtures/labels.jsonl --outputs results/local-demo/outputs.jsonl --out results/local-demo/benchmark.json
```

Use a new directory for every run. To regenerate documentation: `python scripts/build_report.py`. CI checks the generated report, links, duplicate phase headings, regression tests and development benchmark execution. The old `add_index_step.py` now only validates; its former string insertion could duplicate content.

The benchmark follows OCPI's useful measurement analogy: bounded units, admissible evidence and versioned methods. Expertise additionally requires multidimensional task evaluation, critical-error gates and independent outcomes. Knowledge accumulation alone is not learning evidence. Public synthetic labels are development aids, never a private test set.

## Public-source increment — 2026-11-09

Selected GitHub REST from [four candidates](datasets/PROJECT_SELECTION.md). Added [16 source-linked development tasks](datasets/github-rest-dev-v1/README.md): 11 added operations, one modified operation and four unchanged inline controls. Labels are provisional and public; no agent score or independent review is claimed. [Human and AI-agent contribution protocol](CONTRIBUTING.md) supports reproducible reviews and challenges through pull requests.
