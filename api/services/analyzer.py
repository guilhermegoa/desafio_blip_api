from nltk.sentiment.vader import SentimentIntensityAnalyzer


class Analyzer:
    def __init__(self):
        pass

    def analyzeSentiment(self, sentence: str):
        if not sentence or sentence == "" or type(sentence) is not str:
            raise Exception({"error": "No sentence provided"})
        
        sid = SentimentIntensityAnalyzer()
        ss = sid.polarity_scores(sentence)

        return ss