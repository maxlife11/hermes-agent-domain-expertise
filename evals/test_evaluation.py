import copy
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from evals.baseline import analyze
from evals.score import indexed, score

ROOT = Path(__file__).resolve().parents[1]

class EvaluationTests(unittest.TestCase):
    def setUp(self):
        self.cases = indexed(ROOT / 'evals/fixtures/cases.jsonl')
        self.labels = indexed(ROOT / 'evals/fixtures/labels.jsonl')

    def test_authored_development_expectations(self):
        outputs = {cid: analyze(c) for cid, c in self.cases.items()}
        result = score(outputs, self.labels)
        self.assertEqual(result['exact_cases'], 12)
        self.assertEqual(result['false_positive'], 0)
        self.assertEqual(result['false_negative'], 0)

    def test_scorer_detects_false_positives_and_misses(self):
        outputs = {cid: analyze(c) for cid, c in self.cases.items()}
        extra = copy.deepcopy(outputs['new-required']['findings'][0])
        outputs['new-required']['findings'] = []
        outputs['unchanged']['findings'] = [extra]
        result = score(outputs, self.labels)
        self.assertEqual(result['false_positive'], 1)
        self.assertEqual(result['false_negative'], 1)
        self.assertEqual(result['exact_cases'], 10)

    def test_missing_case_rejected(self):
        with self.assertRaises(ValueError):
            score({}, self.labels)

    def test_unsupported_schema_rejected(self):
        c = copy.deepcopy(self.cases['unchanged'])
        c['after']['GET /items']['response_schema'] = {}
        with self.assertRaises(ValueError):
            analyze(c)

    def test_cli_artifacts_no_overwrite_and_no_label_leakage(self):
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / 'run'
            cmd = [sys.executable, '-m', 'evals.run', '--cases', str(ROOT / 'evals/fixtures/cases.jsonl'), '--out', str(out)]
            result = subprocess.run(cmd, cwd=ROOT, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue((out / 'review.md').exists())
            self.assertIsNone(json.loads((out / 'manifest.json').read_text())['review_minutes'])
            self.assertNotEqual(subprocess.run(cmd, cwd=ROOT, capture_output=True).returncode, 0)
            bad = Path(td) / 'leaked.jsonl'
            case = copy.deepcopy(self.cases['unchanged'])
            case['expected'] = []
            bad.write_text(json.dumps(case) + '\n')
            fail = subprocess.run([sys.executable, '-m', 'evals.run', '--cases', str(bad), '--out', str(Path(td) / 'bad')], cwd=ROOT, capture_output=True)
            self.assertNotEqual(fail.returncode, 0)
            self.assertFalse((Path(td) / 'bad').exists())

if __name__ == '__main__':
    unittest.main()
