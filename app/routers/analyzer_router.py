from fastapi import APIRouter, HTTPException
from app.services.analyzer_service import Analyzer
from app.models.analyzer_model import AnalyzeSentiment


router = APIRouter()


@router.get("/sentiment/{sentence}", response_model=AnalyzeSentiment)
def analyzeSentiment(sentence: str):
    if sentence.strip() == "":
        raise HTTPException(status_code=400, detail="Invalid sentence")
    
    analyzer = Analyzer()
    return analyzer.analyzeSentiment(sentence)
