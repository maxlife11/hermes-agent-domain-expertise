# Revision Record

## 2026-11-05 — Replace unsupported conclusions with a validation plan

Authorized scope: update the repository's documents with the review findings and proposed changes. Operational actions, spending, customer outreach, scheduling and deployment remain unperformed.

### Changes

- Rewrote README and all four phases to distinguish inspected facts, hypotheses and pending work.
- Replaced the incomplete 61+ niche claim with 12 bounded workflow hypotheses and stable IDs.
- Withdrew the unsupported contract-review winner, expertise timelines, market/margin forecasts and unlimited pricing.
- Replaced the broken ranking with feasibility gates and a proposed 100%-weight scoring model. New candidates remain unscored.
- Added simple-versus-Hermes baselines, held-out evaluation, independent feedback and controlled skill promotion.
- Added costed review, acquisition and learning effort to the economics model.
- Replaced the unconditional build with two-week validation and a conditional 90-day plan.
- Added source provenance and uncertainty in EVIDENCE.md.
- Added a deterministic report generator/check; full_report.md is generated from phases 1–4.
- Preserved the original report in Git history rather than presenting unsupported assertions as current findings.

### Historical score audit — not a current ranking

Source: [original Phase 3](https://github.com/maxlife11/hermes-agent-domain-expertise/blob/2a5ce196a88a1469ff3765bb2cf30257fd2102f6/phase3.md).

Original weights in column order: 30%, 25%, 15%, 15%, 10%, 5%, 5%, totaling 105%.
Raw total = sum(original rating × stated percentage / 100).
Normalized total = raw total / 1.05, on a 1–5 scale.
The table retains original rank order; it is not a new recommendation. Two decimal places are used only to make arithmetic discrepancies inspectable.

| Original rank | Niche | Reported | Raw weighted total | Normalized |
| --- | --- | ---: | ---: | ---: |
| 1 | AI Contract Review & Obligation Extraction SaaS | 4.7 | 4.50 | 4.29 |
| 2 | AI-Powered Real Estate Valuation SaaS | 4.6 | 4.55 | 4.33 |
| 3 | AI Compliance & Regulatory Change Management | 4.5 | 4.10 | 3.90 |
| 4 | AI Financial Model Builder for Startups & VCs | 4.4 | 4.20 | 4.00 |
| 5 | AI Clinical Trial Matching Platform | 4.3 | 4.05 | 3.86 |
| 6 | AI-Powered Insurance Underwriting Automation | 4.2 | 3.95 | 3.76 |
| 7 | AI ESG & Sustainability Reporting Automation | 4.2 | 3.85 | 3.67 |
| 8 | AI Technical Documentation Generator for Engineering Teams | 4.1 | 3.95 | 3.76 |
| 9 | AI-Powered Digital Marketing Campaign Optimization | 4.0 | 3.70 | 3.52 |
| 10 | AI Meeting Transcription & Decision-Making SaaS | 3.9 | 3.80 | 3.62 |
| 11 | AI Customer Analytics & Churn Prediction Agent | 3.8 | 3.80 | 3.62 |
| 12 | AI B2B Lead Generation & Sales Outreach Automation | 3.7 | 3.75 | 3.57 |
| 13 | AI Supply Chain & Logistics Optimization | 3.7 | 3.70 | 3.52 |
| 14 | AI Healthcare AI-Triage & Diagnosis Support | 3.6 | 3.80 | 3.62 |
| 15 | AI Legal Research & Case Analysis Agent | 3.5 | 3.55 | 3.38 |
| 16 | AI Smart Home Energy Management | 3.5 | 3.70 | 3.52 |
| 17 | AI Talent Acquisition & Recruitment Automation | 3.4 | 3.45 | 3.29 |
| 18 | AI Content Moderation & Community Management | 3.3 | 3.60 | 3.43 |
| 19 | AI Agricultural Disease Detection & Crop Monitoring | 3.2 | 3.65 | 3.48 |
| 20 | AI Legal Document Automation & Generation | 3.1 | 3.30 | 3.14 |

Even normalized values inherit unsupported ratings and unclear risk semantics. The initial top-five narrative omitted rank 4 and included rank 6. The corrected strategy makes no winner claim.

### Scope of verification

The initial commit contained six Markdown documents and no executable agent, evaluation harness or recorded customer results. The combined report was a whitespace-equivalent concatenation of phases 1–4. This does not prove no related work exists outside this repository.

The current revision adds documentation-maintenance tooling only. Passing its checks does not establish commercial validity, domain expertise or runtime readiness.

## 2026-11-05 — Executable pilot foundation

Added an offline normalized API drift baseline, runner/scorer, 12 synthetic development cases, five regression tests, reviewer packets, manifests and CI configuration. Added operator/pilot briefs, buyer discovery, review and release protocols, decision log and repository-local candidate skill. Split pre-pilot discovery from post-pilot scoring to remove circular evidence requirements. Updated all phase documents and regenerated the combined report. Recorded a development run with explicit limits; no customer validation, independent holdout, Hermes adapter, installed skill or operational deployment is claimed.

## 2026-11-09 — Domain benchmark foundation after a08deb8

- Replaced the generic index requirement with separate knowledge registry, capability map, benchmark manifest and immutable result ledger. Added per-domain contracts for all 12 workflows and a staged rollout focused on one real deliverable.
- Added OCPI/ICE primary-source analogy and HELM/τ-bench research references; distinguished measurement design from claims of fungible expertise, independent certification or profit.
- Added executable N01 development profile/report with fixed task families, coverage gates, descriptive uncertainty, provenance fingerprints and matched comparison checks. Aggregate stays null on the current 2/6/4 family counts; promotion is always false for synthetic development.
- Hardened the scorer against fabricated source/evidence, inconsistent status, unsafe/non-template proposals and duplicate escalations. This corrects a limitation of our own earlier baseline. General semantic judgment remains unimplemented.
- Added regression tests for validation corruption, insufficient/missing coverage, invalid weights and incompatible comparisons. Preserved historical v1 artifacts and added a new v2 run without claiming improvement across scoring versions.
- Removed duplicated Phase 3/4 index insertions and the rule that missing index readiness erases all commercial evidence. Linked the canonical methodology across phases and regenerated the combined report.
- Retired the non-idempotent insertion helper into a read-only validator; added duplicate-heading checks and benchmark execution to CI. No agent deployment, outreach, paid service, private data ingestion or schedule was activated.
