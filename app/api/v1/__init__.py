from fastapi import APIRouter

from core.config import settings

from .email_address import router as email_addresses_router


##############################
### EMAIL ADDRESSES ROUTER ###
##############################

router = APIRouter(
	prefix=settings.api.v1.prefix
)
router.include_router(
	email_addresses_router
)