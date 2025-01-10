from fastapi import APIRouter

from .v1 import router as api_v1_router

from core.config import settings


##########################
### MAIN ROUTER API V1 ###
##########################

router = APIRouter(prefix=settings.api.api_prefix)
router.include_router(api_v1_router)