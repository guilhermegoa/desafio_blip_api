from fastapi import APIRouter

from api.routers import test, analyzer

app_routers = APIRouter()
app_routers.include_router(test.router, prefix="/test")
app_routers.include_router(analyzer.router, prefix="/analyzer")