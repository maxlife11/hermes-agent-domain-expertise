# Public review and AI-agent contributions

Updated: 2026-11-09. Human and AI-assisted contributions are welcome as pull requests to this repository. This is a contribution protocol, not an operating agent network. No automated external submissions, reviewer invitations or scheduled jobs are activated.

## What contributors can do

- Propose public-source cases with pinned versions, redistribution basis, hashes and exact evidence locations.
- Independently attempt public development tasks and submit output artifacts, cost/time and failure logs.
- Challenge provisional labels with a specific counterexample and source evidence.
- Improve validators, reproducibility, negative controls and documentation with regression checks.
- Propose knowledge or skill corrections linked to an observed failure; do not change production permissions.

Public-source discovery agents, task-solving agents, skeptical review agents and validator agents can work separately. Their roles and evidence matter more than the number of agents. A contributor cannot certify its own labels or approve its own changes. Model agreement is not independent evidence when agents share models, training data, prompts or sources.

## Submission contract

Use the [review template](reviews/submission-template.json) in a pull request. Include dataset/case IDs, source and task versions/hashes, scope, proposed conclusion, cited evidence, original and corrected outputs where applicable, model/provider/version (or human reviewer), tool versions, prompts or a reproducible description, time/cost (unknown if unavailable), answer exposure, conflicts and limitations. Do not submit secrets, private prompts containing personal data, customer content or unlicensed source copies.

Disclose AI assistance even when a person submits the PR. A self-reported model name is not verified identity. If answers were visible, mark label exposure true; do not represent that run as blind or held out. A public task may still be useful for regression or error discovery, but not for proving unseen generalization. Run submitted code only after review in an isolated environment with no secrets, bounded resources and restricted network.

## Review states and authority

States: proposed → reproducibility checked → evidence reviewed → accepted, disputed or rejected. Every state change needs an attributable reviewer and rationale. “Open for review” is not “reviewed.” An AI review is a disclosed evidence contribution, not an independent human review. Record reviewer type separately; do not count several agent reviews as several independent experts.

Maintainers check source rights, provenance, scope, reproducibility and leakage. A qualified human reviewer adjudicates consequential or ambiguous semantic labels. The current project has no appointed independent reviewer, so those labels remain provisional. A maintainer may accept a transparent structural correction while preserving its limited review status. Do not silently promote a development label to expert ground truth.

Accepted corrections create a new dataset version and preserve the old record. Add a changelog reason and re-score affected historical outputs only where compatible. A change in labels/evaluator breaks score comparability; use the methodology in [INDEX.md](INDEX.md). Contributions to public development data never receive access to private holdout answers or customer data.

## Practical starting task

Review [github-rest-dev-v1](datasets/github-rest-dev-v1/README.md): confirm the pinned source extraction, investigate the one modified operation, challenge the 16 provisional labels and identify missing dependency context. Propose additional historical transitions as a new version rather than adding contrived changes to the current snapshot. The first useful success is a reproducible correction or independently supported label—not a leaderboard score.

Contributions of new code, task instructions and labels under this protocol must be explicitly submitted under MIT terms; include the applicable notice when needed. Third-party excerpts retain their original licenses. This policy does not grant rights over material the contributor does not own or change licenses elsewhere in the repository.
