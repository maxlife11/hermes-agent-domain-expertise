# Domain benchmark specifications

Updated: 2026-11-09. Proposed task baskets; only N01 normalized synthetic subset is implemented. All private datasets, reviewer panels, buyer acceptance thresholds and economic measurements are pending. [Canonical rules](../INDEX.md).

| Domain | Unit and task families | Reference evidence and judge | Metrics beyond accuracy; critical error | Entry experiment |
| --- | --- | --- | --- | --- |
| N01 API docs | One release/example pair: removed operation, required parameter, response/auth change, runnable example, unknown scope | Versioned specs, executable sandbox, maintainer adjudication | False drift alerts, patch acceptance, review time; invented API behavior or unsafe patch | Maintainer labels a small permitted release sample; compare existing diff tools |
| N02 Support KB | One ticket cluster→article revision: product version, resolution, duplication, policy conflict, privacy | Authorized tickets, approved product/policy snapshots, support lead | Supported resolution, citation fidelity, edit time; secrets/customer data disclosure or obsolete policy | One category with sanitized closed tickets and article history |
| N03 Renewal extraction | One contract packet→renewal record: date, notice window, party, amendment precedence, missing clauses | Authorized originals with clause spans; procurement/legal-qualified reviewer | Critical-field recall, provenance, abstention, reviewer minutes; missed notice or invented obligation | Single contract type; no advice or autonomous notice |
| N04 Questionnaire response | One requirement→supported answer or explicit gap | Approved evidence library and sales/security reviewer | Unsupported commitments, evidence validity, review effort; fabricated certification | Historical questionnaire with independent answer review |
| N05 Catalog QA | One product/variant record→correction queue | Licensed catalog, supplier data and current platform rules | False correction, variant consistency, review time; unsafe or unsupported product claim | Read-only sample from one platform/category |
| N06 Analytics QA | One event journey→schema/collection issue report | Expected event contracts and replayed test events | Detection/false alarms, reproducibility, repair verification; false “healthy” critical journey | Isolated instrumented journey with seeded faults |
| N07 CRM reconciliation | One record pair/cluster→merge suggestion or abstention | Authorized exports, approved entity rules, human adjudication | False merge weighted separately, duplicate recall, review effort; merging distinct customers | Read-only labeled pairs, no live merges |
| N08 Invoice exceptions | One invoice/order/receipt packet→exception report | Authorized documents and finance-reviewed matches | Amount/currency exactness, mismatch recall, review cost; incorrect payable amount or payment action | One vendor/document type, no payment credentials |
| N09 Listing QA | One listing→evidence-backed inconsistency report | Licensed source records and brokerage rules | Critical field accuracy, stale evidence, reviewer cost; unsupported material listing fact | One jurisdiction/type with qualified reviewer |
| N10 Source monitoring | One source-change batch→dated relevance digest | Official versioned texts, reviewer-defined relevance labels | Relevant-change recall, citation/version fidelity, false alerts; missed critical change or invented legal conclusion | Narrow source list; human decides applicability |
| N11 Competitive updates | One competitor snapshot pair→verified change brief | Permitted dated captures, product/pricing pages, reviewer | Change precision/recall, normalized plan comparisons, freshness; invented price or feature | Small fixed competitor set, no inference sold as fact |
| N12 Reproduction triage | One support escalation→repro/evidence packet | Sanitized logs, isolated environment, engineer rerun | Repro success, minimality, secret leakage, engineer time; unsafe command or exposed secret | One product/version and isolated known issues |

## N01 first full benchmark contract

Customer deliverable: a reviewed release-drift report and proposed corrections. Current deterministic code sees only normalized operation/required-parameter arrays; it cannot evaluate raw specifications, prose, auth, responses or executable examples. Those families must remain explicitly unsupported until adapters, labels and tests exist.

Obtain permission for a small development tranche (e.g. 10–20 varied cases) to debug normalization and rubrics, not certify readiness. Then pre-register independent holdout size from risk/precision requirements. Group by repository/release lineage before splitting. Capture both source versions, exact affected example, expected change or legitimate no-change, required escalation, acceptance criteria and severity. Two reviewers should resolve critical-field disagreement before labels are frozen. Measure disagreement; disputed cases are adjudicated or labeled indeterminate rather than silently counted as correct.

Compare an existing diff/checker workflow, our condition A, and later fixed-skill Hermes B. Add learned-skill C only after B can execute the same unit with controlled tool access and captured costs. Do not reward a learned system merely for repeating this public fixture set. Reviewer acceptance and total time saved on actual source material decide whether to proceed.

## N02 alternative if access is stronger

Use one authorized product/version and ticket category. Split by issue cluster and time, not individual near-duplicate tickets. The agent can see approved product facts; holdout target article decisions remain hidden. Include unresolved tickets, obsolete fixes, contradictory policies, duplicate articles and injected instructions. Judge whether the proposed article is supported and operationally usable, not whether it resembles a preferred wording. Track redaction effort, editor time and later resolution outcomes separately; ticket deflection needs a controlled deployment study, not an offline guess.

## N03 alternative with stricter review

Define one jurisdiction-neutral extraction task for a single contract type; interpretation remains with an appropriate reviewer. Freeze the full packet including amendments and date conventions. Split by template/vendor, include missing dates, conflicting clauses and ambiguous notice triggers. Require clause citations and abstention rather than invented answers. Report critical-field exactness and whole-packet acceptance. A perfect average can conceal one missed renewal deadline, so critical misses are a veto. No automated legal conclusions, payments or notices are part of this benchmark.

## Expansion rule

Choose N02 or N03 instead of N01 if permitted data, qualified reviewers and buyer access are materially better. The other nine remain discovery candidates. Reuse manifest/ledger conventions; do not reuse domain labels, weights or acceptance thresholds. Add a domain only when someone can independently judge the deliverable and plausibly buy it.
