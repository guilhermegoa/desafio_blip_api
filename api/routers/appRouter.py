from fastapi import APIRouter

from api.routers import test_router, analyzer_router

app_routers = APIRouter()
app_routers.include_router(test_router.router)
app_routers.include_router(analyzer_router.router, prefix="/analyze")