from fastapi import APIRouter

from .v1 import router as api_v1_router


##########################
### MAIN ROUTER API V1 ###
##########################

router = APIRouter()
router.include_router(api_v1_router)