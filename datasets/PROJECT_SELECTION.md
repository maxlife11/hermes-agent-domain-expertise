# Public API project selection

Checked 2026-11-09. These are technical dataset candidates, not validated customers or profitability rankings.

| Candidate | Primary repository | Why useful | Main constraint |
| --- | --- | --- | --- |
| GitHub REST — selected | https://github.com/github/rest-api-description | Provider-owned OpenAPI, MIT license, commit-pinned history; fits developer-tools workflow | Large schemas and shared references; this first transition is dominated by one product family |
| Stripe | https://github.com/stripe/openapi | Provider-owned OpenAPI with MIT license; rich billing/integration domain | Version semantics and financial workflows need tighter scope; no live payments in evaluation |
| Cloudflare | https://github.com/cloudflare/api-schemas | Provider-owned OpenAPI with BSD-3-Clause license; infrastructure workflows | Broad product surface; schema assertions need runtime-independent interpretation |
| APIs.guru directory | https://github.com/APIs-guru/openapi-directory | Broad cross-provider discovery and later transfer experiments | Aggregator rather than one API project; confirm each selected source's origin and license before reuse |

Selection rationale: start with GitHub because it matches the existing N01 focus and permits source extraction without credentials or live API actions. Compare only a bounded part of its specification initially. Stripe and Cloudflare are plausible subsequent transfer datasets; using them now would expand normalization effort before we establish reviewer throughput.

Repository README/license pages were inspected for candidate screening. Only the selected GitHub source snapshots were downloaded and transformed. No claim is made that upstream maintainers have reviewed or endorsed this dataset.
