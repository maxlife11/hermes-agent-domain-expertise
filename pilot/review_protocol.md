# Review and acceptance protocol

The command creates review.md and reviews.jsonl beside outputs and manifest. The packet cites normalized source fields; the reviewer must also inspect the corresponding input case.

1. For a fair A/B/C comparison, have an evaluator assign neutral output IDs and hide condition/model identity from reviewers. Randomize order. This blinding is a manual protocol, not implemented automation.
2. Check source provenance and whether each claimed mismatch follows from the supplied versions and example.
3. Verify scope: no-supported-drift means neither supported rule found a change, not that the documentation is correct.
4. Mark each case accept, edit, reject or escalate. Record reviewer identity/qualification, minutes, critical_error true/false, and notes. Null means unreviewed, never zero effort.
5. Escalate disputed intended behavior to a maintainer. Record disagreement and adjudication rather than averaging away critical errors.
6. A second model can assist triage but cannot alone establish independent ground truth.
7. Accept only when evidence is accurate and the proposal does not invent values or replacement operations. No automatic merge/publish.
8. Sum review, rework, setup and support effort for delivery economics. The machine scorer checks finding fields only.

Reviewer records are not yet populated. The synthetic expected labels were authored during development; they are not independent expert judgments.
