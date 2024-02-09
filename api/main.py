from fastapi import FastAPI

from api.routers.appRouter import app_routers


api = FastAPI()


api.include_router(app_routers, prefix="/api/v1")
