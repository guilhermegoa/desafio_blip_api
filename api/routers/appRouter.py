from fastapi import APIRouter

from api.routers import test

app_routers = APIRouter()
app_routers.include_router(test.router, prefix="/test")