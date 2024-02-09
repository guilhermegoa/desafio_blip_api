from fastapi import APIRouter
from api.services.analyzer import Analyzer
from api.models.analyzer import AnalyzeSentiment


router = APIRouter()


@router.get("/sentiment/{sentence}", response_model=AnalyzeSentiment)
def analyzeSentiment(sentence: str):
    analyzer = Analyzer()
    return analyzer.analyzeSentiment(sentence)
