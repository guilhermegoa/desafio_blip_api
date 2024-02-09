from pydantic import BaseModel


class AnalyzeSentiment(BaseModel):
    neg: float
    neu: float
    pos: float
    compound: float