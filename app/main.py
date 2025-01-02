import uvicorn

from fastapi import FastAPI

from api import router as apiRouter 
from core.config import settings


app = FastAPI()
app.include_router(apiRouter,
				   prefix=settings.api.api_prefix)


if __name__ == '__main__':
	uvicorn.run('main:app', reload=True)