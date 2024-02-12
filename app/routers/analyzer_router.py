from fastapi import APIRouter, Depends
from app.configurations.validations.str_validation import str_validation
from app.configurations.validations.word_validation import word_validation
from app.services.analyzer_service import Analyzer
from app.models.analyzer_model import AnalyzeSentiment


router = APIRouter(dependencies=[Depends(str_validation), Depends(word_validation)])


@router.get("/sentiment", response_model=AnalyzeSentiment)
def analyzeSentiment(sentence: str):
    
    analyzer = Analyzer()
    return analyzer.analyzeSentiment(sentence)
