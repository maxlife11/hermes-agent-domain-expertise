# GitHub REST real-source development dataset v1

Built 2026-11-09 from GitHub's MIT-licensed REST API description. **16 public development tasks, provisional structural labels, zero independent reviews.** This is source-change analysis, not evidence of actual documentation bugs or API runtime behavior.

## Source and selection

[source_manifest.json](source_manifest.json) pins before/after commits, download URLs and SHA-256 hashes. The before commit is the after commit's parent. [tasks.jsonl](tasks.jsonl) contains exact inline operation objects extracted from those snapshots; [provisional_labels.jsonl](provisional_labels.jsonl) contains separately stored structural expectations. [UPSTREAM_LICENSE.txt](UPSTREAM_LICENSE.txt) preserves the upstream MIT notice. Derived task instructions and labels are released under the same MIT terms; this does not relicense unrelated repository content.

Selection is exhaustive for inline operation changes in this one transition: 11 additions and one modification, plus four explicitly selected unchanged controls. The modified operation is GET /repos/{owner}/{repo}/actions/runs: the after object adds a 304 response reference. Additions are concentrated in Copilot code-review endpoints. This narrow cluster is not a representative sample of API maintenance.

Unchanged means the inline operation object is unchanged. Referenced components, path-level parameters, external documentation and runtime behavior are outside this task's scope. References are retained verbatim but not resolved. A component change can affect an apparently unchanged operation. No required-parameter additions or removed operations were manufactured to fill coverage gaps.

## Task and review scope

Classify added/removed/modified/unchanged; list changed top-level keys; cite the JSON pointer. Provisional labels are mechanically derived from raw JSON comparison. They are not an independent test of that comparison algorithm and cannot validate semantic expertise. A reviewer should verify extraction against the pinned full source, assess label correctness and flag limits. Broader impact analysis needs resolved dependencies and qualified review before labels can be extended.

This dataset does not fit evals/baseline.py's normalized-input contract and is deliberately excluded from the existing N01 score. No agent has been evaluated on it. No live requests, credentials, customer data or upstream issues were used. Public answers make it unsuitable for private holdout evaluation.

## Reproduce

Download the two exact URLs in source_manifest.json to separate local files. Then run from repository root:

```sh
python scripts/build_github_dataset.py /path/before.json /path/after.json /tmp/new-github-dataset
```

The builder rejects source-hash mismatch and existing output directories. Compare the two generated JSONL files byte-for-byte with this directory. Full upstream snapshots are not duplicated in the repository. CI validates included artifact hashes and source/task structure; fetching upstream is an explicit reproduction step, not part of offline CI.

Review through the [public contribution protocol](../../CONTRIBUTING.md). No review or maintainer endorsement is implied by publication.
