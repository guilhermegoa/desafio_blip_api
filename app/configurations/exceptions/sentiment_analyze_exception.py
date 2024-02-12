from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi import FastAPI


app = FastAPI()

class SentimentAnalyzerException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

@app.exception_handler(SentimentAnalyzerException)
async def sentiment_analyzer_exception_handler(request: Request, exc: SentimentAnalyzerException):
    return JSONResponse(
        status_code=400,
        content={"message": exc.message}
    )