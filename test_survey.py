import unittest
from survey import AnonymousSurvey


class TestAnonymousServey(unittest.TestCase):
    """ Test for the class AnonymousSurvey """

    def setUp(self):
        """Create survey and set of responses for use in all test methods"""
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ["English", 'Spanish', 'Mandarin']

    def test_single_response(self):
        """ Test that a single response is stored properly """
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_three_responses(self):
        """ Test that thress responses stored correctly"""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


unittest.main()
