from fastapi import APIRouter
from app.services.analyzer_service import Analyzer
from app.models.analyzer_model import AnalyzeSentiment


router = APIRouter()


@router.get("/sentiment/{sentence}", response_model=AnalyzeSentiment)
def analyzeSentiment(sentence: str):
    analyzer = Analyzer()
    return analyzer.analyzeSentiment(sentence)
