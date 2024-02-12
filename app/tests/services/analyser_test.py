import unittest
from app.configurations.exceptions.sentiment_analyze_exception import SentimentAnalyzerException
from app.services.analyzer_service import Analyzer


class TestAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = Analyzer()
    
    def test_analyze_sentiment_valid_sentence(self):
        sentence = "Life is good"
        result = self.analyzer.analyzeSentiment(sentence)
        self.assertIsInstance(result, dict)
        self.assertIn('neg', result)
        self.assertIn('neu', result)
        self.assertIn('pos', result)
        self.assertIn('compound', result)

    def test_analyze_sentiment_invalid_input(self):
        sentence = None
        with self.assertRaises(SentimentAnalyzerException):
            self.analyzer.analyzeSentiment(sentence)

if __name__ == '__main__':
    unittest.main()