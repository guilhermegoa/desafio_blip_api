from pydantic import BaseModel


class AnalyzeSentiment(BaseModel):
    """
    Sentiment analysis result
    """
    neg: float
    neu: float
    pos: float
    compound: float