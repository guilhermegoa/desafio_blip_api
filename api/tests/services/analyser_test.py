import unittest
from api.services.analyzer import Analyzer

class TestAnalyzer(unittest.TestCase):

    def setUp(self):
        self.analyzer = Analyzer()
        self.error_object = "{'error': 'No sentence provided'}"

    def test_analyzeSentiment_with_valid_sentence(self):
        sentence = "I love Python!"
        result = self.analyzer.analyzeSentiment(sentence)
        self.assertIsInstance(result, dict)
        self.assertTrue("neg" in result)
        self.assertTrue("neu" in result)
        self.assertTrue("pos" in result)
        self.assertTrue("compound" in result)

    def test_analyzeSentiment_with_empty_sentence(self):
        with self.assertRaises(Exception) as context:
            self.analyzer.analyzeSentiment("")
        self.assertEqual(str(context.exception), self.error_object)

    def test_analyzeSentiment_with_invalid_input(self):
        with self.assertRaises(Exception) as context:
            self.analyzer.analyzeSentiment(None)
        self.assertEqual(str(context.exception), self.error_object)

    def test_analyzeSentiment_with_invalid_input_type(self):
        with self.assertRaises(Exception) as context:
            self.analyzer.analyzeSentiment(123)
        self.assertEqual(str(context.exception), self.error_object)

if __name__ == "__main__":
    unittest.main()
