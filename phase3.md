# Phase 3 — Feasibility, Prioritization and Economics

Updated: 2026-11-05. Status: decision framework; no validated winner or populated commercial ranking.

## Withdraw the initial ranking

The original weights summed to 105%, its overall scores did not reproduce, risk-score direction was unclear, and the top-five narrative differed from the ranking. The complete historical arithmetic audit is in [CHANGELOG.md](CHANGELOG.md).

Normalizing the old numbers does not repair unsupported inputs. Do not reuse the corrected historical scores to choose a business.

## Pre-pilot selection: do not require future outcomes

Compare reachable buyer access, repeated problem evidence, permitted sample availability, independent evaluability, implementation effort and error consequences. Record pass/fail/unknown and a next experiment; do not assign speculative commercial totals. Prioritize the cheapest decisive uncertainty reduction. Unknown economics permits an offline measurement experiment, not an unchecked paid production launch.

The technical baseline selects N01 for evaluability without credentials. Commercial selection remains open. The [operator brief](pilot/operator_brief.md) and [buyer evidence protocol](pilot/buyer_evidence.md) collect the missing inputs. Do not use retention, realized margins or measured learning gains as prerequisites to starting discovery.

## Feasibility gates before scoring

Record pass, fail or unknown with a source and date. Unknown is not a pass; fatal gaps cannot be offset by an attractive market score.

| Gate | Evidence needed |
| --- | --- |
| Buyer access | Reachable budget owner and a credible purchasing path |
| Data access | Permission and representative inputs sufficient for a pilot |
| Evaluability | Independent reviewer or reliable ground truth; explicit failure classes |
| Scope | Bounded outcome with manageable error consequences and action permissions |
| Economics | Plausible positive contribution profit after review and rework |
| Delivery | Minimal integrations, security and operational support within actual resources |

A paid pilot requires adequate gates for its limited scope. Production autonomy requires stronger evidence and separate authorization.

## Post-pilot scoring after gates

This model is for post-pilot comparison, when outcomes can be observed. It must not block initial experiments by requiring future renewal or learning evidence. Weights sum to 100%. Higher scores always mean more attractive. Scores compare opportunities, not probabilities of success.

| Criterion | Weight | Score 1 | Score 3 | Score 5 |
| --- | --- | --- | --- | --- |
| Buyer pain and payment evidence | 20% | No concrete buyer evidence | Repeated buyer reports and defined budget owner | Paid use with repeated value and renewal evidence |
| Contribution economics | 15% | Negative or unmeasured | Plausible margin with measured major costs | Positive observed margin across varied cases |
| Validated learning benefit | 15% | No correction signal or measured gain | Reliable labels and a feasible improvement test | Repeated held-out gains net of learning cost |
| Acquisition feasibility | 15% | Buyers inaccessible | Reachable channel with observed responses | Repeatable paying acquisition at measured acceptable cost |
| Time to paid value | 10% | Long unknown dependency chain | Scoped pilot with manageable dependencies | Demonstrated short path from access to paid value |
| Data and evaluation quality | 10% | Unavailable or unreliable | Permitted representative samples and reviewers | Stable access, high-quality labels and prospective feedback |
| Repeatability/productization | 5% | Bespoke delivery each time | Shared core with some onboarding variation | Repeated delivery with low incremental customization |
| Defensibility | 5% | Easily substituted with no advantage shown | Some integration or specialized evaluation advantage | Demonstrated retention tied to hard-to-replicate delivery assets |
| Manageable operational risk | 5% | Errors hard to detect or reverse | Reviewable workflow with explicit controls | Low-consequence scope and tested recovery |

Formula: score out of 100 = sum(weight_percent × rating / 5). Use whole-number totals when presenting rankings. Unknown ratings remain null, not zero or an invented midpoint. Do not compare partially scored totals as if complete.

Record evidence confidence separately: verified observation, supported estimate, hypothesis or unknown. Distinguish customer-reported numbers from measured costs. After real inputs exist, test rankings under greater emphasis on near-term cash flow, low supervision and restricted budgets.

## Current candidate decision table

| Candidate | Discovery priority | Gates | Commercial score | Next decisive test |
| --- | --- | --- | --- | --- |
| N01 API documentation maintenance | Offline baseline implemented | Buyer/data/economics unknown | Not scored | Maintainer reviews real-input sample and scoped paid offer |
| N02 Support KB maintenance | Initial set | Unknown | Not scored | Support lead measures time saved on authorized ticket-to-article tasks |
| N03 Renewal/notice extraction | Initial set | Unknown | Not scored | Buyer and qualified reviewer test critical-field extraction and cost |
| N04–N12 | Reserve set | Unknown | Not scored | Revisit if access or evidence is stronger than the initial set |

N01 may be a useful first technical demonstration because code/spec references permit explicit checks. That is not a conclusion about willingness to pay. Existing buyer access can make N02 or N03 the better first commercial test. No first-choice niche has been approved.

## Initial offer hypotheses

| ID | Scoped offer | Proposed delivery model | Distribution experiment | Primary failure reason |
| --- | --- | --- | --- | --- |
| N01 | One release's drift audit and reviewed draft fixes | Paid diagnostic, then capped managed maintenance | Discuss recent docs failures with reachable developer-tools maintainers | Existing tools plus staff are cheaper |
| N02 | One approved ticket category's KB update batch | Capped managed service with human editorial approval | Work with reachable support leads or support-service partners | Editing and privacy overhead erase value |
| N03 | One contract type's reviewed renewal register | Paid setup plus capped reviewed maintenance | Work with operations/procurement leads and an appropriate reviewer | Missing critical terms makes review uneconomic |

These channels have not been exercised. Writing an outreach plan is not permission to send messages.

Avoid freemium and unlimited usage until acquisition economics and delivery costs support them. Define volume in pages, complexity, integrations, turnaround and review scope; document count alone may conceal large cost variation. Do not propose fixed prices as market facts before testing a scoped offer.

## Unit economics worksheet

Populate downside, base and upside cases from observed ranges. No revenue or margin forecast is currently defensible.

| Variable | Include |
| --- | --- |
| Recurring revenue | Actual contracted charge and billable volume |
| Setup revenue | Report separately; do not hide recurring losses with setup fees |
| Variable technical costs | Model inference, retrieval, APIs, compute, storage and retries |
| Delivery labor | Review, rework, exceptions, support and ongoing onboarding burden |
| Learning costs | Candidate generation, annotation, evaluations and failed experiments |
| Other variable costs | Payment fees, refunds and incident allowance where applicable |
| Fixed operating costs | Base infrastructure, software, administration and fixed staffing |
| Acquisition costs | Prospecting/sales labor, tools, channel payments and onboarding acquisition effort |

Recurring contribution per customer = recurring revenue − variable technical costs − delivery labor − allocated learning/other variable costs.

Contribution margin = contribution / recurring revenue. Labor is hours × an explicit replacement-cost rate even when performed by the founder. Report cash spending separately.

Break-even customer count = ceiling(fixed monthly operating cost / positive monthly contribution per customer), subject to delivery capacity. If contribution is zero or negative, scaling does not establish break-even.

CAC payback months = acquisition cost per new paying customer / positive monthly contribution, with setup charges and onboarding treatment disclosed. Do not calculate confident lifetime value before retention evidence exists.

Stress-test longer documents, difficult cases, model price changes, review spikes, low utilization and lost customers. Track customer concentration and founder capacity.

## Proposed pilot decision gates

Set exact buyer-specific thresholds before seeing results. Suggested starting hypotheses:

- Concrete buying evidence: a paid pilot or equivalent purchasing commitment, not enthusiasm alone.
- Material net time reduction including review; a 30% improvement can be a pilot hypothesis, not a universal benchmark.
- Positive contribution profit at a price the buyer will actually accept.
- All critical fields/actions reviewed within the agreed initial scope.
- Zero observed critical errors in the evaluation is necessary for some scopes but is not proof of a zero underlying error rate.
- A willingness to continue or renew after observed delivery.

If demand fails, revise the offer or candidate before adding infrastructure. If A matches B at lower cost, use A. If C fails to improve on B, retain fixed skills. If review remains unaffordable, narrow the workflow or stop.

## Economics status

The offline manifest reports zero external API spend but leaves review time and labor costs null. No human review or normalization effort has been measured. Zero model spend does not mean zero delivery cost. The [review protocol](pilot/review_protocol.md) specifies records needed before contribution profit can be calculated.
