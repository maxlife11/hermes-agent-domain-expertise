"""Fail-closed N01 validation and field scoring. Not a semantic expert judge."""
import argparse
import hashlib
import json
from pathlib import Path
from evals.baseline import analyze


def indexed(path):
    result = {}
    for line in Path(path).read_text(encoding='utf-8').splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        if not isinstance(row, dict) or not isinstance(row.get('id'), str) or not row['id']:
            raise ValueError('nonempty string case id required')
        if row['id'] in result:
            raise ValueError('duplicate case id')
        result[row['id']] = row
    if not result:
        raise ValueError('empty dataset')
    return result


def fields(obj, names):
    if not isinstance(obj, dict) or set(obj) != set(names.split()):
        raise ValueError('unexpected or missing fields')


def finding_key(f):
    for name in ('doc_ref', 'operation', 'kind'):
        if not isinstance(f.get(name), str) or not f[name]:
            raise ValueError('invalid finding identifier')
    if f.get('kind') not in {'removed_operation', 'missing_new_required_parameter'}:
        raise ValueError('unsupported finding kind')
    if f['kind'] == 'removed_operation' and f.get('parameter') is not None:
        raise ValueError('removed operation parameter must be null')
    if f['kind'] != 'removed_operation' and (not isinstance(f.get('parameter'), str) or not f['parameter']):
        raise ValueError('parameter name required')
    return (f['doc_ref'], f['operation'], f['kind'], f['parameter'])


def escalation_keys(rows):
    if not isinstance(rows, list):
        raise ValueError('escalations must be a list')
    keys = []
    for row in rows:
        fields(row, 'doc_ref operation reason')
        if any(not isinstance(v, str) or not v for v in row.values()):
            raise ValueError('invalid escalation')
        if row['reason'] != 'operation_not_in_baseline':
            raise ValueError('unsupported escalation reason')
        keys.append((row['doc_ref'], row['operation'], row['reason']))
    if len(set(keys)) != len(keys):
        raise ValueError('duplicate escalations')
    return set(keys)


def validate_output(output, case):
    fields(output, 'id source findings escalations status')
    if output['id'] != case['id'] or output['source'] != case['source']:
        raise ValueError('source or id mismatch')
    if not isinstance(output['findings'], list):
        raise ValueError('findings must be a list')
    docs = {d['ref']: d for d in case['docs']}
    seen = set()
    for f in output['findings']:
        fields(f, 'doc_ref operation kind parameter evidence proposal')
        k = finding_key(f)
        if k in seen:
            raise ValueError('duplicate findings')
        seen.add(k)
        doc = docs.get(f['doc_ref'])
        op = f['operation']
        if doc is None or doc['operation'] != op or op not in case['before']:
            raise ValueError('finding not supported by source example')
        before, after = case['before'][op], case['after'].get(op)
        if f['evidence'] != {'before': before, 'after': after}:
            raise ValueError('evidence does not match source versions')
        if f['kind'] == 'removed_operation':
            if after is not None:
                raise ValueError('operation was not removed')
            proposal = 'Review or retire this example; replacement is unknown.'
        else:
            p = f['parameter']
            if after is None or p not in after['required'] or p in before['required'] or p in doc['params']:
                raise ValueError('required-parameter finding unsupported')
            proposal = f'Document required parameter {p}; obtain a valid value from the maintainer.'
        if f['proposal'] != proposal:
            raise ValueError('unapproved proposal: v1 accepts reviewed safe templates only')
    for ref, op, reason in escalation_keys(output['escalations']):
        if ref not in docs or docs[ref]['operation'] != op or op in case['before']:
            raise ValueError('unsupported escalation')
    expected_status = 'review_required' if output['findings'] or output['escalations'] else 'no_supported_drift'
    if output['status'] != expected_status:
        raise ValueError('invalid status')
    return seen


def score(outputs, labels, cases):
    if not cases or set(outputs) != set(labels) or set(labels) != set(cases):
        raise ValueError('outputs, labels and cases must have identical nonempty IDs')
    tp = fp = fn = exact = escalation_exact = 0
    case_outcomes = {}
    for cid, case in cases.items():
        fields(case, 'id source before after docs')
        analyze(case)  # Input shape validation only; never used as expected answers.
        if case['id'] != cid:
            raise ValueError('case key mismatch')
        actual = validate_output(outputs[cid], case)
        label = labels[cid]
        fields(label, 'id findings escalations')
        if label['id'] != cid or not isinstance(label['findings'], list):
            raise ValueError('invalid labels')
        expected_keys = []
        for f in label['findings']:
            fields(f, 'doc_ref operation kind parameter')
            expected_keys.append(finding_key(f))
        if len(expected_keys) != len(set(expected_keys)):
            raise ValueError('duplicate label findings')
        expected = set(expected_keys)
        tp += len(actual & expected)
        fp += len(actual - expected)
        fn += len(expected - actual)
        a, b = escalation_keys(outputs[cid]['escalations']), escalation_keys(label['escalations'])
        escalation_exact += a == b
        passed = actual == expected and a == b
        exact += passed
        case_outcomes[cid] = passed
    return {'cases': len(cases), 'exact_cases': exact, 'true_positive': tp,
            'false_positive': fp, 'false_negative': fn,
            'precision': tp/(tp+fp) if tp+fp else None,
            'recall': tp/(tp+fn) if tp+fn else None,
            'escalation_exact_cases': escalation_exact, 'case_outcomes': case_outcomes,
            'source_consistency': 'passed', 'proposal_policy': 'safe-template-v1',
            'human_acceptance': 'not_measured',
            'limitations': 'Consistency with supplied normalized inputs only; labels and source truth are not independently certified.'}


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for name in ('outputs', 'labels', 'cases'):
        p.add_argument('--' + name, required=True)
    p.add_argument('--require-exact', action='store_true')
    p.add_argument('--report', help='Write a new evidence report; existing paths refused')
    args = p.parse_args()
    result = score(indexed(args.outputs), indexed(args.labels), indexed(args.cases))
    result['evaluation_fingerprints'] = {name: digest(getattr(args, name)) for name in ('outputs', 'labels', 'cases')}
    result['evaluation_fingerprints']['scorer'] = digest(__file__)
    result['evaluation_fingerprints']['input_validator'] = digest(Path(__file__).with_name('baseline.py'))
    result['review_fingerprint'] = None
    if args.report:
        with open(args.report, 'x', encoding='utf-8') as f:
            json.dump(result, f, indent=2)
            f.write('\n')
    print(json.dumps(result, indent=2))
    if args.require_exact and result['exact_cases'] != result['cases']:
        raise SystemExit(1)

if __name__ == '__main__':
    main()
