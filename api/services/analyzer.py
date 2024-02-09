from nltk.sentiment.vader import SentimentIntensityAnalyzer


class Analyzer:
    # def __init__(self, data):
    #     self.data = data

    def analyzeSentiment(self, sentence: str):
        if not sentence or sentence == "" or type(sentence) is not str:
            raise {"error": "No sentence provided"}
        
        sid = SentimentIntensityAnalyzer()
        print(sentence)
        ss = sid.polarity_scores(sentence)

        return ss