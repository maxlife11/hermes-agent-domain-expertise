import copy
import json
import unittest
from pathlib import Path
from benchmarks.report import summarize, compare

class BenchmarkTests(unittest.TestCase):
    def setUp(self):
        self.profile = json.loads((Path(__file__).parents[1]/'benchmarks/domains/N01.json').read_text())
        self.outcomes = {c: True for s in self.profile['strata'] for c in s['case_ids']}

    def test_all_pass_is_not_expertise_or_sufficient_coverage(self):
        r = summarize(self.profile, self.outcomes)
        self.assertEqual(r['status'], 'insufficient_data')
        self.assertIsNone(r['development_score'])
        self.assertFalse(r['promotion_eligible'])

    def test_missing_or_duplicate_cases_rejected(self):
        missing = dict(self.outcomes)
        missing.pop('removed')
        with self.assertRaises(ValueError):
            summarize(self.profile, missing)
        self.profile['strata'][1]['case_ids'].append('removed')
        with self.assertRaises(ValueError):
            summarize(self.profile, self.outcomes)

    def test_empty_stratum_suppresses_score(self):
        self.profile['strata'][0]['case_ids'] = []
        del self.outcomes['removed'], self.outcomes['unused-removed']
        self.assertIsNone(summarize(self.profile, self.outcomes)['development_score'])

    def test_invalid_weights_rejected(self):
        for value in (0, float('nan'), 1):
            p = copy.deepcopy(self.profile)
            p['strata'][0]['weight'] = value
            with self.assertRaises(ValueError):
                summarize(p, self.outcomes)

    def test_comparison_requires_unchanged_measurement(self):
        a = {'fingerprints': {k:'x' for k in ('profile','cases','labels','scorer','input_validator','reporter')}, 'case_outcomes': {'a':False,'b':True}}
        b = copy.deepcopy(a)
        b['case_outcomes']['a'] = True
        self.assertEqual(compare(a,b)['paired_wins'], 1)
        b['fingerprints']['labels'] = 'changed'
        with self.assertRaises(ValueError):
            compare(a,b)
