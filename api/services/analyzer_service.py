from nltk.sentiment.vader import SentimentIntensityAnalyzer

from api.models.analyzer_model import AnalyzeSentiment


class Analyzer:
    """
    Classe responsável por realizar a análise de uma frase.
    """

    def __init__(self):
        pass

    def analyzeSentiment(self, sentence: str) -> AnalyzeSentiment:
        """
        Analisa o sentimento da frase fornecida.

        Args:
            sentence (str): A frase para análise de sentimento.

        Returns:
            Dict[str, float]: Um dicionário contendo as pontuações de sentimento.
                As chaves do dicionário são 'neg', 'neu', 'pos' e 'compound'.
        """
        if not sentence or sentence == "" or type(sentence) is not str:
            raise Exception({"error": "No sentence provided"})
        
        sid = SentimentIntensityAnalyzer()
        ss = sid.polarity_scores(sentence)

        return ss