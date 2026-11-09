import hashlib
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).parents[1]/'datasets/github-rest-dev-v1'

class PublicDatasetTests(unittest.TestCase):
    def test_artifacts_match_manifest(self):
        manifest = json.loads((ROOT/'source_manifest.json').read_text())
        for name, expected in manifest['artifacts_sha256'].items():
            self.assertEqual(hashlib.sha256((ROOT/name).read_bytes()).hexdigest(), expected)

    def test_case_coverage_and_provisional_status(self):
        tasks = [json.loads(s) for s in (ROOT/'tasks.jsonl').read_text().splitlines()]
        labels = [json.loads(s) for s in (ROOT/'provisional_labels.jsonl').read_text().splitlines()]
        self.assertEqual(len(tasks),16)
        self.assertEqual(len({t['id'] for t in tasks}),16)
        self.assertEqual({t['id'] for t in tasks},{t['id'] for t in labels})
        for t in tasks:
            self.assertNotIn('classification',t)
            for op in [t['before'],t['after']]:
                if op is not None:
                    self.assertIsInstance(op['operationId'],str)
        for label in labels:
            self.assertEqual(label['review_status'],'provisional_auto_structural')
            self.assertEqual(label['independent_reviews'],0)
