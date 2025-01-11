from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.ext.asyncio import AsyncSession

from core.config import settings
from core.schemas.message import MessageCreate, MessageRead
from core.models import dbHelper

from api.crud.message import getAllMessages, addMessage, getMessagesByEmailAddress

from typing import Annotated, Union


router = APIRouter(
	prefix=settings.api.v1.messages_prefix,
	tags=['Messages']
)

@router.get('', response_model=list[MessageRead])
async def getMessages(
	session: Annotated[AsyncSession, Depends(dbHelper.session_getter)]
):
	res = await getAllMessages(session=session)
	if not res.success:
		raise HTTPException(500)
	return res.data

@router.post('', response_model=MessageRead)
async def createMessage(
	session: Annotated[AsyncSession, Depends(dbHelper.session_getter)],
	messageCreate: MessageCreate
):
	res = await addMessage(session, messageCreate)
	if not res.success:
		raise HTTPException(res.code, res.error)
	return res.data

@router.get('/{emailAddressId}', response_model=list[MessageRead])
async def getMessagesByEmailAdddresId(
	session: Annotated[AsyncSession, Depends(dbHelper.session_getter)],
	emailAddressId: int
):
	res = await getMessagesByEmailAddress(session, emailAddressId)
	if not res.success:
		raise HTTPException(500)
	return res.data