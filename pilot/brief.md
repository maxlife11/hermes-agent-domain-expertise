# Pilot brief — API documentation drift

Status: selected for an offline technical experiment only; commercial selection pending.

- Candidate: N01.
- Hypothesized buyer: developer-tools team lead or documentation owner.
- Problem hypothesis: API changes leave examples inconsistent, creating avoidable maintenance and support work.
- Initial deliverable: one source-linked review packet for one supplied version transition.
- Input contract: normalized operation maps and structured documentation examples; see [evaluation protocol](../evals/README.md).
- Implemented scope: removed operations and newly required parameter names missing from examples.
- Exclusions: OpenAPI ingestion, prose extraction, type changes, response schemas, authentication changes, runtime example execution, automatic patches or publication.
- Turnaround: local command execution measured; customer service deadline not established.
- Volume: 12 synthetic development cases; production limits unset.
- Price: not set; buyer evidence and full delivery cost absent.
- Acceptance: findings match declared scope and cite inputs; ambiguity escalates; reviewer approves any proposed correction.
- Critical errors: unsupported replacement endpoint/value, treating unsupported checks as complete coverage, unauthorized publication, or misleading assurance.
- Commercial gate: concrete purchasing evidence plus authorized representative data and affordable review.
- Next evidence: a buyer's actual version change, intended behavior and reviewer timing, with permission.
- Stop/pivot: existing tooling is sufficient, no buyer access, or review erases the value.

A full OpenAPI parser or LLM adapter should be added only if a permitted real example demonstrates the need. The current implementation tests plumbing and scope, not product-market fit.

## Benchmark alignment — 2026-11-09

Use the [canonical methodology](../INDEX.md), [domain contracts](../benchmarks/DOMAIN_SPECS.md) and [rollout](../benchmarks/ROADMAP.md). Current [v2 evidence](../results/development-baseline-v2/summary.md) is synthetic development only; human acceptance and commercial value remain unknown. Historical entries above are retained, not evidence of current promotion. Private labels must remain outside specialist access; benchmark changes require a version break.
