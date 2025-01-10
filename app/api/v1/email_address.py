from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from core.config import settings
from core.schemas.email_address import EmailAddressRead, EmailAddressCreate
from core.models import dbHelper

from api.crud.email_address import getAllEmailAddresses, createEmailAddress

from typing import Annotated


router = APIRouter(
	prefix=settings.api.v1.email_addresses_prefix,
	tags=['Email']
)

@router.get('', response_model=list[EmailAddressRead])
async def getAddresses(
	session: Annotated[AsyncSession, Depends(dbHelper.session_getter)]
):
	addresses = await getAllEmailAddresses(session=session)
	return addresses

@router.post('', response_model=EmailAddressRead)
async def createAddress(
	session: Annotated[AsyncSession, Depends(dbHelper.session_getter)],
	emailAddressCreate: EmailAddressCreate
):
	return await createEmailAddress(session, emailAddressCreate)