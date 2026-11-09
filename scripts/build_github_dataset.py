"""Build a public structural-change development set from two pinned GitHub specs.
Usage: python scripts/build_github_dataset.py BEFORE.json AFTER.json NEW_OUTPUT_DIR
Downloads are deliberately separate; input hashes must match the pinned source files.
"""
import hashlib
import json
import sys
from pathlib import Path

BEFORE = 'f1b7900c19a5672ed37ea63a0e992817c27436f7'
AFTER = 'df36add4edaeda9577169ce42ad4b2b756191852'
SOURCE_PATH = 'descriptions/api.github.com/api.github.com.json'
METHODS = {'get', 'post', 'put', 'delete', 'patch', 'head', 'options'}
CONTROLS = [('/repos/{owner}/{repo}', 'get'), ('/repos/{owner}/{repo}/issues', 'get'),
            ('/repos/{owner}/{repo}/pulls', 'get'), ('/repos/{owner}/{repo}/actions/workflows', 'get')]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def operations(spec):
    return {(p, m): op for p, item in spec['paths'].items() for m, op in item.items() if m in METHODS}


def main():
    before_path, after_path, out_path = map(Path, sys.argv[1:])
    raw = [before_path.read_bytes(), after_path.read_bytes()]
    pinned = json.loads((Path(__file__).parents[1]/'datasets/github-rest-dev-v1/source_manifest.json').read_text())
    if [sha(b) for b in raw] != [pinned['sources'][k]['sha256'] for k in ('before', 'after')]:
        raise ValueError('source bytes differ from pinned snapshots')
    specs = [json.loads(b) for b in raw]
    old, new = map(operations, specs)
    changed = [k for k in sorted(old.keys() | new.keys()) if old.get(k) != new.get(k)]
    if any(k not in old or old[k] != new.get(k) for k in CONTROLS):
        raise ValueError('control no longer unchanged in inline operation scope')
    tasks, labels = [], []
    for i, (p, m) in enumerate(changed + CONTROLS, 1):
        cid = f'gh-rest-{i:03}'
        a, b = old.get((p,m)), new.get((p,m))
        pointer = '/paths/' + p.replace('~','~0').replace('/','~1') + '/' + m
        tasks.append({'id': cid, 'method': m.upper(), 'path': p, 'source_pointer': pointer,
                      'before': a, 'after': b,
                      'instruction': 'Classify added/removed/modified/unchanged within these inline operation objects; list changed top-level keys and cite the source pointer. Do not infer live API behavior or dereference components. No external action.'})
        status = 'added' if a is None else 'removed' if b is None else 'unchanged' if a == b else 'modified'
        keys = sorted(k for k in (a or {}).keys() | (b or {}).keys() if (a or {}).get(k) != (b or {}).get(k))
        labels.append({'id':cid, 'classification':status, 'changed_top_level_keys':keys,
                       'source_pointer':pointer, 'review_status':'provisional_auto_structural',
                       'independent_reviews':0})
    out_path.mkdir(parents=True, exist_ok=False)
    for name, rows in [('tasks.jsonl',tasks), ('provisional_labels.jsonl',labels)]:
        (out_path/name).write_text(''.join(json.dumps(r,sort_keys=True)+'\n' for r in rows))
    print(f'Built {len(tasks)} tasks; no expert or human-reviewed labels claimed')

if __name__ == '__main__':
    main()
