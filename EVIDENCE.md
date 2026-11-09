# Evidence Register and Research Gaps

Updated: 2026-11-05. This register distinguishes inspected facts from proposals. It is not a fresh market-validation study.

## Inspected sources

| ID | Source | Checked | Supports | Does not establish |
| --- | --- | --- | --- | --- |
| E01 | [Initial repository snapshot](https://github.com/maxlife11/hermes-agent-domain-expertise/tree/2a5ce196a88a1469ff3765bb2cf30257fd2102f6) | 2026-11-05 | Original contents, placeholders, scoring defects and lack of implementation artifacts in its six files | That external deployments or customers do not exist elsewhere |
| E02 | [Official Hermes skills reference](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills/) | 2026-11-05 | Agent-managed procedural skills and write-approval staging | Independent expertise gains or business ROI |
| E03 | [Official Hermes memory reference](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory) | 2026-11-05 | Bounded factual memory, session context and separate profile guidance | A complete production multi-tenant memory system |
| E04 | [Official Hermes overview](https://hermes-agent.nousresearch.com/docs) | 2026-11-05 | Documented scheduling, tools, provider flexibility and delegation | Configured integrations or reliable execution in this project |
| E05 | [Official working-with-skills guide](https://hermes-agent.nousresearch.com/docs/guides/work-with-skills) | 2026-11-05 | Focused procedures and maintaining stale skills | Automatic correctness of agent-generated procedures |
| E06 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | 2026-11-05 | Upstream project identity and documentation entry point | A pinned/tested upstream release; runtime audit remains pending |

The upstream pages are mutable. Capture the chosen release/commit and applicable documentation versions before implementation. Recheck security-sensitive behavior and API compatibility at deployment.

## Claim disposition

| Claim group from the initial report | Status in this revision | Required replacement evidence |
| --- | --- | --- |
| 61+ niches researched | Corrected: ten originally detailed; current plan has 12 workflow hypotheses | Completed, sourced records if broader discovery is later justified |
| Contract review is the best niche | Withdrawn | Feasibility gates, buyer evidence, cost measurements and defensible comparisons |
| 0–3 / 3–9 / 9–18 month expertise progression | Withdrawn | Task-defined evaluations and observed learning curves |
| Top 10% expertise | Withdrawn | Representative comparative benchmark and uncertainty |
| Market sizes, growth, adoption and funding percentages | Unverified; excluded from active recommendations | Claim-specific dated original sources and correct market scope |
| 85–92% gross margins and proposed annual contract values | Unverified; excluded from forecasts | Actual offers, realized payments and fully costed delivery |
| More customer documents automatically create a data moat | Hypothesis rejected as automatic | Permission, correction labels, measurable improvement and retained customer value |
| $99/month unlimited processing is viable | Withdrawn | Usage distribution, review costs, capacity and price acceptance |
| Regulatory requirements create a ready-made moat | Unverified strategic assumption | Evidence the operator can meet requirements and buyers value the service |
| Hermes skill updates imply model-weight training | Not established | Explicit separate training pipeline and evaluation |
| N01/N02/N03 are attractive first experiments | Analyst proposal | Buyer access and pilot results |
| Budget, staffing, geography and deadlines from earlier chat | Unconfirmed scenario assumptions | Operator confirmation before operational commitments |

Withdrawal means the evidence is insufficient for the decision; it does not prove every historical number false.

## New evidence record format

Use a stable ID, candidate ID, precise claim, source URL or authorized private reference, author/publisher, publication/effective date, retrieval date, relevant passage or measurement, evidence type, limitations, contradiction notes, owner and next review trigger.

Types: observed result; buyer-reported fact; vendor claim; supported estimate; analyst hypothesis; unknown. Do not treat duplicated reports as independent corroboration. Record rejected hypotheses and failed experiments as well as successes.

Keep raw customer-confidential data outside this public research repository. Reference approved, minimized summaries only. Source information never expands the agent's permissions.

## Pending research

- Buyer conversations and purchasing evidence for N01/N02/N03.
- Representative tasks, permissions and independent reviewers.
- Dated competitor offers and customer alternatives.
- Measured inference, integration, review and support costs.
- Selected upstream version and feature verification.
- Condition A synthetic baseline completed (E07); independent held-out evaluations and prospective monitoring pending.
- Domain-specific legal/security review where the selected scope requires it.

No item above is represented as completed.

## E07 — Offline implementation evidence

[Recorded development run](results/development-baseline-v1/summary.md), generated on 2026-11-05 (America/New_York). Condition A checks two rules over normalized synthetic inputs. Five regression tests passed; 12/12 development cases matched expected finding/escalation fields, with six true-positive findings, zero false positives and zero false negatives. Labels were authored during development, not independently reviewed. No inference about generalization, pricing or Hermes learning follows. B/C runs, private holdout and real customer data are still pending. Source hashes and measured machine time appear in the run manifest; human time/cost are unknown.

## Benchmark research and implementation — 2026-11-09

| ID | Primary source / observation | Supports | Limitation |
| --- | --- | --- | --- |
| E07 | [Ornn OCPI methodology](https://data.ornn.com/methodology), checked 2026-11-09; page dates publication 2026-07-24 | Explicit units, admissible transaction observations and method governance | Analogy only; not evidence of agent expertise or project economics |
| E08 | [ICE OCPI B200 product specification](https://www.ice.com/products/83050009), checked 2026-11-09 | A specific cash-settled index-linked contract | Does not establish universal first-index or sole-founder claims |
| E09 | [Stanford HELM introduction](https://crfm.stanford.edu/2022/11/17/helm.html), 2022-11-17, checked 2026-11-09 | Evaluating multiple metrics and making coverage gaps visible | No direct validation of our domain baskets |
| E10 | [τ-bench paper](https://arxiv.org/abs/2406.12045), 2024-06-17, checked 2026-11-09 | Task-end-state evaluation and repeated-trial reliability | Historical experimental results do not predict this project's performance |
| E11 | [Prior main snapshot](https://github.com/maxlife11/hermes-agent-domain-expertise/tree/a08deb83c706d1273f39783413f69f6dcabff670) and local reproduction | Duplicate phase sections; generated-report mismatch; original scorer did not validate supporting evidence/proposals | Repo-specific defects, not claims about upstream Hermes |
| E12 | [v2 run](results/development-baseline-v2/summary.md) and current regression suite | Source-consistency validation, frozen family profile, null aggregate on missing coverage | Synthetic authored data; no independent labels, agent execution, actual reviewer time or commercial outcomes |

The four-record architecture, domain contracts, weights, learning gates and rollout are project proposals informed by these sources, not externally validated standards. Equal family weights and a five-case development minimum are illustrative plumbing settings. No industry percentile, expertise certification or probability of business success is claimed. Original v1 results remain historical; changed scorers require a series break.

## Public-source dataset — 2026-11-09

[GitHub REST development v1](datasets/github-rest-dev-v1/README.md) records 16 tasks extracted from pinned upstream snapshots. Source bytes and extracted artifacts have SHA-256 hashes; upstream MIT notice retained. Labels are mechanically derived structural expectations, not independent ground truth. The one modified operation adds a 304 response reference; no documentation defect or runtime behavior was verified. The dataset is public and correlated within one transition, so it cannot support unseen-generalization claims. [Candidate screening](datasets/PROJECT_SELECTION.md) covers GitHub, Stripe, Cloudflare and APIs.guru; only GitHub was transformed. [Public review](CONTRIBUTING.md) is available but no independent reviews or outside agent runs have occurred.
