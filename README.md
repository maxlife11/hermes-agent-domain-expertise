# Hermes Agent Domain Expertise — Evidence and Validation Plan

Updated: 2026-11-05 (America/New_York). Status: **offline baseline implemented; commercial hypotheses unvalidated; no deployed Hermes agent.**

## Objective

Find one narrow, repeatable digital workflow that customers will pay for, deliver it reliably, and test whether Hermes memory and reusable skills improve quality or reduce total delivery cost. Profitability and autonomous expertise are outcomes to demonstrate, not assumptions.

## Current evidence

| Area | Completed | Still required |
| --- | --- | --- |
| Repository review | All six original Markdown files reviewed; arithmetic and completeness defects identified | External validation of commercial claims |
| Opportunity design | 12 bounded workflow hypotheses; three candidates for initial discovery | Buyer access, task samples, purchasing evidence |
| Learning and evaluation | Offline condition A runner/scorer, 12 synthetic cases and regression checks | Private holdout, independent review, Hermes B/C adapters and learning gains |
| Economics | Cost model and decision gates defined | Measured review/support effort, real pricing and retention |
| Implementation | Narrow API drift baseline, review packets, pilot artifacts and CI configuration | Real-input ingestion, Hermes integration, customer pilot and deployment |

A synthetic development run is recorded; no independent benchmark, customer interview, paid pilot or business revenue is established. See [development results](results/development-baseline-v1/summary.md).

## Read the report

1. [Phase 1 — Workflow hypotheses and evidence requirements](phase1.md)
2. [Phase 2 — Controlled learning and bounded autonomy](phase2.md)
3. [Phase 3 — Feasibility, prioritization and economics](phase3.md)
4. [Phase 4 — Conditional validation and implementation plan](phase4.md)
5. [Combined report](full_report.md), generated from the four phases
6. [Evidence register](EVIDENCE.md)
7. [Revision record and historical score audit](CHANGELOG.md)

Edit the phase files, not the combined report. Run:

```sh
python3 scripts/build_report.py
python3 scripts/build_report.py --check
```

The check verifies report synchronization and repository-local Markdown links. It does not validate market assertions or agent performance.

## Corrections to the initial draft

The original claimed 61+ niches but detailed ten before a placeholder. Its ranking weights summed to 105%; displayed scores were not reproducible. Its top-five narrative differed from its ranking. Numerical market, adoption, margin and expertise-timeline claims lacked claim-level sources.

This revision withdraws the original winner designation, unsupported expert timelines, margin claims, and unlimited-document pricing. Historical text remains available in [the initial commit](https://github.com/maxlife11/hermes-agent-domain-expertise/tree/2a5ce196a88a1469ff3765bb2cf30257fd2102f6); the score audit is preserved in CHANGELOG.md. This is a replacement strategy, not a completed fresh market survey.

## Next decision

Compare buyer access and sample-task availability for API documentation maintenance, support knowledge-base maintenance, and contract renewal/notice extraction. Select one paid-pilot experiment only after feasibility checks. These are test candidates, not market rankings.

The earlier chat's $3,000/month budget, solo-operator setup, target geography and 90-day commitment were planning assumptions, not confirmed user constraints. Confirm operating constraints before expenditure.

## Boundaries

Updating this repository authorizes documentation changes only. The schedules, outreach, integrations and deployments described here are proposals; none has been activated. Keep customer-confidential data, credentials and clinical records out of this repository.

This repository contains research and planning material, not validated legal, medical, financial or underwriting services.

## Run the first technical experiment

The [pilot brief](pilot/brief.md) selects N01 for an offline demonstration only. Follow [evaluation instructions](evals/README.md). Review the [operator brief](pilot/operator_brief.md), [buyer evidence protocol](pilot/buyer_evidence.md), [decision log](pilot/decision_log.md), [review protocol](pilot/review_protocol.md), and [release checklist](pilot/release_checklist.md). The [candidate procedure](skills/check-api-doc-drift/SKILL.md) is repository-local, not an installed Hermes or personal skill.

CI configuration runs document synchronization, regression tests and fixture scoring on pushes and PRs. It does not deploy an agent or enforce commercial acceptance.
