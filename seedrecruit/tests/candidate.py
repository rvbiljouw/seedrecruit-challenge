import unittest
from seedrecruit.data.candidate import Candidate


class CandidateTests(unittest.TestCase):
    def setUp(self):
        self.candidate_file = "profile1.xml"

    def test_parser(self):
        """ This function tests whether the parsing of profile1 succeeds.
        """
        candidate = Candidate(self.candidate_file)
        self.assertEqual(candidate.first_name, "Dan",
                         msg="candidate.first_name not correctly parsed")
        self.assertEqual(candidate.last_name, "Jacobs",
                         msg="candidate.last_name not correctly parsed")
        self.assertEqual(candidate.id, "14",
                         msg="candidate.id not correctly parsed")
        self.assertIsNotNone(candidate.locations,
                             msg="candidate.locations not correctly parsed")