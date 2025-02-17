import uvicorn

from contextlib import asynccontextmanager

from fastapi import FastAPI

from api import router as apiRouter 
from core.config import settings
from core.models import dbHelper


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup action
	print('Startup app')
	yield
    # Shutdown action
	print('Shutdown app')
	await dbHelper.dispose()

app = FastAPI(lifespan=lifespan)
app.include_router(apiRouter)


if __name__ == '__main__':
	uvicorn.run('main:app',
			 	host=settings.run.host,
			 	port=settings.run.port, 
			 	reload=True)