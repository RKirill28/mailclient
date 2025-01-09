from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from core.config import settings
from core.schemas.email_address import EmailAddressRead
from core.models import dbHelper

from api.crud.email_address import getAllEmailAddresses


router = APIRouter(
	prefix=settings.api.v1.email_addresses_prefix,
	tags=['Email']
)

@router.get('', response_model=list[EmailAddressRead])
async def getAddresses(
	session: AsyncSession = Depends(dbHelper.session_getter)
):
	addresses = await getAllEmailAddresses(session=session)
	return addresses