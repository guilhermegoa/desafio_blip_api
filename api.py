import uvicorn

from api.main import api

uvicorn.run(api)