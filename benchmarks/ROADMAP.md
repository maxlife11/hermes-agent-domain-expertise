# Benchmark rollout and decisions

Updated: 2026-11-09. Proposed sequence, not activated schedules or promised expertise timelines.

| Stage | Work and accountable role | Exit evidence / decision |
| --- | --- | --- |
| Now: measurement foundation | Operator: run N01 diagnostics and inspect failures; maintainer: preserve versions | Tests and fingerprints reproduce; missing coverage remains visible. Implemented in this revision |
| Next 1–2 weeks: select real task | Operator + reachable buyer + qualified reviewer: choose N01, N02 or N03; obtain permission; define task acceptance and cost ceiling | One bounded deliverable, access basis, reviewer and buyer experiment. If absent, pause infrastructure expansion |
| Next 2–4 weeks, conditional | Curator + independent reviewer: small development tranche, task taxonomy, disagreement audit, source normalization cost | Runnable task adapter and reliable labels; pre-register holdout size, split and promotion thresholds |
| Following 2–4 weeks, conditional | Evaluator: freeze anchor/holdout; compare deterministic A with fixed-skill Hermes B at fixed budgets | Blinded task results, full costs/review, repeated reliability. Use A if it is sufficient and cheaper |
| Following learning cycles | Specialist proposes corrections; evaluator measures C vs B; reviewer promotes or rejects | Paired gains on unseen tasks, no critical regression, affordable learning cost. Retain B if learning adds no value |
| Paid supervised pilot | Buyer and operator: deliver reviewed output, measure time/value and continuation | Positive observed contribution and acceptable errors; no autonomy expansion by default |

## First real run checklist

Record scope/unsupported inputs; dataset owner/permission; source versions; task families/weights; independent label reviewer and adjudication policy; private split storage/access; model/Hermes/tool versions; skill/memory snapshots; spend/time limits; failure taxonomy; customer acceptance thresholds; planned statistical analysis; rollback version; buyer offer and cost ledger. Any missing field is recorded as unknown, with its consequence for interpretation.

The next useful deliverable is a **reviewer-labeled real task packet plus a measured baseline**, not a larger synthetic score or twelve populated indices. No real reviewer, customer dataset, Hermes connection or budget is currently supplied. These dependencies cannot be manufactured by agent self-learning.
