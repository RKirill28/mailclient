import uvicorn

from contextlib import asynccontextmanager

from fastapi import FastAPI

from api import router as apiRouter 
from core.config import settings
from core.models.db_helper import dbHelper


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup action
    
	yield
    
    # Shutdown action
	await dbHelper.dispose()
    


app = FastAPI(lifespan=lifespan)
app.include_router(apiRouter,
				   prefix=settings.api.api_prefix)


if __name__ == '__main__':
	uvicorn.run('main:app',
			 	host=settings.run.host,
			 	port=settings.run.port, 
			 	reload=True)