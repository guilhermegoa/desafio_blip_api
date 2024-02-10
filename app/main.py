from fastapi import FastAPI

from app.routers.appRouter import app_routers


app = FastAPI()


app.include_router(app_routers, prefix="/api/v1")
