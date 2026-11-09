"""Recompute evidence and report a fixed development basket; never certify expertise."""
import argparse
import json
import math
from pathlib import Path
from evals.score import digest, indexed, score


def wilson(successes, n):
    if not n:
        return None
    z = 1.96
    p = successes / n
    denominator = 1 + z*z/n
    center = (p + z*z/(2*n))/denominator
    half = z*math.sqrt(p*(1-p)/n + z*z/(4*n*n))/denominator
    return [max(0, center-half), min(1, center+half)]


def summarize(profile, outcomes):
    if profile.get('schema_version') != 1 or profile.get('evidence_class') != 'synthetic_development':
        raise ValueError('only synthetic development profiles implemented')
    strata = profile['strata']
    if not strata or len({s['id'] for s in strata}) != len(strata):
        raise ValueError('nonempty unique strata required')
    weights = [s['weight'] for s in strata]
    if any(type(w) not in (float, int) or not math.isfinite(w) or w <= 0 for w in weights) or not math.isclose(sum(weights), 1):
        raise ValueError('positive finite weights must sum to one')
    ids = [cid for s in strata for cid in s['case_ids']]
    if len(ids) != len(set(ids)) or set(ids) != set(outcomes):
        raise ValueError('each observed case must occur in exactly one stratum')
    if any(type(x) is not bool for x in outcomes.values()):
        raise ValueError('boolean outcomes required')
    rows = []
    for s in strata:
        minimum = s['minimum_cases']
        if type(minimum) is not int or minimum < 1:
            raise ValueError('positive integer minimum required')
        n = len(s['case_ids'])
        passed = sum(outcomes[cid] for cid in s['case_ids'])
        rows.append({'id': s['id'], 'weight': s['weight'], 'n': n, 'passed': passed,
                     'rate': passed/n if n else None, 'minimum_cases': minimum,
                     'sufficient': n >= minimum, 'wilson_95_descriptive': wilson(passed, n)})
    sufficient = all(s['sufficient'] for s in rows)
    return {'domain': profile['domain'], 'basket_version': profile['basket_version'],
            'evidence_class': profile['evidence_class'], 'strata': rows,
            'status': 'development_only' if sufficient else 'insufficient_data',
            'development_score': 100*sum(s['weight']*s['rate'] for s in rows) if sufficient else None,
            'promotion_eligible': False, 'expertise_level': 'not_established',
            'critical_failure_rate': None, 'review_minutes': None, 'commercial_value': None,
            'uncertainty_note': 'Intervals describe authored cases under an IID assumption that is not established. They do not estimate real-world expertise. Repeats are not additional independent cases.'}


def compare(old, new):
    keys = ('profile', 'cases', 'labels', 'scorer', 'input_validator', 'reporter')
    if any(old['fingerprints'][k] != new['fingerprints'][k] for k in keys):
        raise ValueError('incomparable evaluations: bridge or rebase required')
    a, b = old['case_outcomes'], new['case_outcomes']
    if set(a) != set(b) or not a:
        raise ValueError('matched nonempty cases required')
    wins = sum(not a[k] and b[k] for k in a)
    losses = sum(a[k] and not b[k] for k in a)
    return {'paired_wins': wins, 'paired_losses': losses, 'ties': len(a)-wins-losses,
            'unweighted_delta_percentage_points': 100*(wins-losses)/len(a),
            'learning_attribution': 'not_established',
            'note': 'Matched development cases only. Compare model, tools, budget, memory and skill versions before attributing a change to learning.'}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for key in ('profile', 'cases', 'labels', 'outputs', 'out'):
        p.add_argument('--'+key, required=True)
    p.add_argument('--previous', help='Optional compatible report for paired diagnostics')
    args = p.parse_args()
    profile = json.loads(Path(args.profile).read_text())
    metrics = score(indexed(args.outputs), indexed(args.labels), indexed(args.cases))
    result = summarize(profile, metrics['case_outcomes'])
    result['case_outcomes'] = metrics['case_outcomes']
    result['validation'] = metrics
    result['fingerprints'] = {k: digest(getattr(args, k)) for k in ('profile', 'cases', 'labels', 'outputs')}
    result['fingerprints'].update(scorer=digest(Path(__file__).parents[1]/'evals/score.py'),
                                  input_validator=digest(Path(__file__).parents[1]/'evals/baseline.py'),
                                  reporter=digest(__file__))
    if args.previous:
        result['comparison'] = compare(json.loads(Path(args.previous).read_text()), result)
    with open(args.out, 'x', encoding='utf-8') as f:
        json.dump(result, f, indent=2)
        f.write('\n')
    print(json.dumps({'status': result['status'], 'development_score': result['development_score'],
                      'promotion_eligible': False}))

if __name__ == '__main__':
    main()
