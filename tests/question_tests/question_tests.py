import unittest

from src.question_c.main import get_most_likely_ancestor_consensus


class QuestionTests(unittest.TestCase):

    def test_sample_case(self):
        a, b, c = get_most_likely_ancestor_consensus(
            "GATATATGCATATACTT",
            "ATAT"
        )
        self.assertEqual(a, 2)
        self.assertEqual(b, 4)
        self.assertEqual(c, 10)

    def test_no_matches(self):
        result = get_most_likely_ancestor_consensus(
            "AAAAAAAAAAAA",
            "CGTA"
        )
        self.assertEqual(result, ())

    def test_overlapping_matches(self):
        result = get_most_likely_ancestor_consensus(
            "AAAAAA",
            "AAAA"
        )
        self.assertEqual(result, (1, 2, 3))

