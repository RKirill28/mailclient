from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.ext.asyncio import AsyncSession

from core.config import settings
from core.schemas.email_address import EmailAddressRead, EmailAddressCreate, EmailAddressBase
from core.models import dbHelper

from api.crud.email_address import getAllEmailAddresses, createEmailAddress, deleteEmailAddress

from typing import Annotated, Union


router = APIRouter(
	prefix=settings.api.v1.email_addresses_prefix,
	tags=['Email addresses']
)

@router.get('', response_model=list[EmailAddressRead])
async def getAddresses(
	session: Annotated[AsyncSession, Depends(dbHelper.session_getter)]
):
	res = await getAllEmailAddresses(session=session)
	if not res.success: raise HTTPException(500)
	return res.data

@router.post('', response_model=EmailAddressRead)
async def createAddress(
	session: Annotated[AsyncSession, Depends(dbHelper.session_getter)],
	emailAddressCreate: EmailAddressCreate
):
	res = await createEmailAddress(session, emailAddressCreate)
	if not res.success: raise HTTPException(500)
	return res.data

@router.delete(
		'/{emailAddressId}', 
		responses={
			404: {'description': 'Email address not found'}
		}
)
async def deleteAddress(
	session: Annotated[AsyncSession, Depends(dbHelper.session_getter)],
	emailAddressId: int
) -> Union[dict[str, bool], None]:
	res = await deleteEmailAddress(session, emailAddressId)
	if not res.success:
		raise HTTPException(res.code, res.error)
	return {'ok': True}