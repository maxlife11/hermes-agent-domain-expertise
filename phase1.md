# Phase 1 — Workflow Hypotheses and Evidence Requirements

Updated: 2026-11-05. Status: discovery candidates; commercial demand unverified.

## Scope and correction

The initial report asserted 61+ niches but described ten and left the remaining categories as a placeholder. This revision deliberately replaces that breadth target with 12 specific workflow hypotheses. It does not claim exhaustive market coverage or newly validated TAM estimates.

Define an opportunity as **buyer + recurring problem + bounded workflow + measurable deliverable + payment hypothesis**. A parent industry's size is not the service's accessible market. Large budgets do not establish access to buyers, data or procurement approval.

The original 2025–2027 outlook is not a verified forecast. Future research must distinguish historical observations, current offers, and forecasts, retaining source dates and uncertainty.

## Candidate inventory

All commercial propositions below have **unverified** confidence. Mechanistic reasons to test a workflow are design judgments, not proof of demand. IDs remain stable across phases.

| ID | Buyer and problem | Narrow deliverable and value hypothesis | Required access and evaluation | Principal obstacle |
| --- | --- | --- | --- | --- |
| N01 | Developer-tools company; docs drift after API releases | Source-linked drift report, tested examples and draft documentation PR | Authorized repository/specification, docs, test environment; maintainer acceptance and example execution | Existing tooling may solve enough of the problem; reviewer burden may erase savings |
| N02 | SaaS support lead; resolved issues fail to reach the knowledge base | Draft article updates linked to resolved tickets and approved product facts | Authorized, minimized tickets and KB; blinded editor review and measured editing time | Privacy, conflicting answers, weak incremental willingness to pay |
| N03 | Operations/procurement lead; renewal and notice dates are scattered | Reviewed register of dates, conditions, notice methods and source passages | Authorized contracts and qualified reviewer; exact field correctness and critical-miss analysis | Amendments, ambiguous dates and missed obligations |
| N04 | B2B sales engineering lead; repetitive questionnaires | Draft responses supported only by approved evidence, with unresolved gaps flagged | Current approved answer library; evidence validity and reviewer acceptance | Confidentiality and unsupported commitments |
| N05 | E-commerce operations lead; inconsistent product catalogs | Detect attribute, variant and policy mismatches; propose a correction queue | Authorized catalog exports and platform rules; item-level correctness | Integration variability and low value per correction |
| N06 | Agency analytics lead; tracking failures undermine reporting | Read-only event/schema checks and a prioritized issue report | Test events, authorized analytics access and expected event specification | Establishing ground truth and attributing business value |
| N07 | Customer-success operations lead; account records are incomplete | Source-backed reconciliation suggestions and duplicate review queue | CRM exports and approved matching rules; false-merge and correction rates | Incorrect merges, stale data and permissions |
| N08 | Finance operations lead; invoices conflict with approved orders | Exception packets with matched fields, discrepancies and evidence | Authorized invoice/order data; exact reconciliation and reviewer time | Sensitive data and costly matching errors; no autonomous payments |
| N09 | Real-estate brokerage operations lead; listing data is inconsistent | Listing QA against supplied source documents and brokerage rules | Licensed data and reviewer; field accuracy and compliance with supplied rules | Data rights and local variation; excludes autonomous valuation |
| N10 | Compliance operations lead; relevant source changes are missed | Dated source-change digest with citations and reviewer routing | Defined official sources and reviewer-owned relevance rules | Coverage gaps and interpretation burden; excludes compliance determinations |
| N11 | B2B product-marketing lead; competitive changes are hard to track | Evidence-linked pricing/feature changes and draft sales-enablement updates | Permitted public sources and dated snapshots; factual change verification | Public information may be easy to replicate and hard to monetize |
| N12 | SaaS support operations lead; escalations lack reproducible context | Structured reproduction/evidence packets for engineering triage | Authorized tickets, logs and isolated repro environment; engineer acceptance | Secrets in logs, unreliable reproduction and environment drift |

## Initial discovery set

Investigate N01, N02 and N03 first because their deliverables can be inspected and kept under review. This is a proposed test order, not a claim that they are the three most profitable niches.

| Candidate | First proof to obtain | Initial boundary | What would disqualify it |
| --- | --- | --- | --- |
| N01 | A maintainer provides actual drift examples and evaluates a sample | Draft PR only; no merge or release authority | Existing checks deliver comparable results at lower total cost |
| N02 | A support lead provides authorized sample tickets and measures editing effort | Draft articles; no publishing or customer replies | Review effort equals or exceeds manual authoring |
| N03 | A buyer and qualified reviewer provide representative contracts | Extract and cite; reviewer approves register and reminders | Critical omissions remain hard to detect affordably |

Buyer access can change this order. No access advantage has been established in this repository.

## Treatment of the original broad opportunities

Retain the original ideas as historical leads, not recommendations. General contract review, autonomous property valuation, insurance underwriting, clinical trial matching and diagnosis support require evidence and controls beyond the initial pilot scope. Procurement response work is narrowed to N04, regulatory monitoring to N10, real-estate operations to N09, and contract operations to N03.

Financial modeling, cybersecurity threat hunting, ESG reporting, meeting intelligence, advertising optimization, churn prediction, logistics, smart-home energy, recruitment, moderation, agricultural detection and legal document generation are deferred rather than declared unprofitable. Their source access, buyer economics and error exposure have not been adequately investigated. Historical descriptions are preserved in the initial commit linked from README.md.

## Evidence required before selection

For each finalist record:

- Named buyer role, purchasing trigger, existing workaround, frequency and actual time/cost burden.
- Reachable acquisition channel and observed purchasing process, not an assumed enterprise sales motion.
- Permitted representative data, independent reviewers and labels, including difficult cases.
- Specific competing offers and dated prices; advertised pricing is not evidence of realized sales.
- A testable scoped offer and a concrete buying signal. Distinguish interview interest, trial use, payment, renewal and retention.
- Delivery costs including onboarding, review, exceptions, support and acquisition.
- Two independent evidence sources where available, including direct buyer evidence; multiple summaries of one study count as one source.
- Contradictory evidence, freshness requirements and the next cheapest uncertainty-reducing test.

Use [EVIDENCE.md](EVIDENCE.md) for provenance. Do not populate unknown fields with invented numbers. Collect no customer-sensitive data without explicit permission and an appropriate handling agreement.

## Execution update

N01 is now the first offline technical experiment, with 12 authored synthetic cases and a deterministic normalized-input baseline. This does not change its unverified commercial confidence or the comparative status of N02/N03. See [pilot scope](pilot/brief.md) and [buyer discovery](pilot/buyer_evidence.md). Buyer access remains unconfirmed.
