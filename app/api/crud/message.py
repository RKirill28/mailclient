from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from sqlalchemy import select, insert

from core.models import Message
from core.schemas.message import MessageRead, MessageCreate

from . import Result

async def getAllMessages(
		session: AsyncSession
	) -> Result:
	stmt = select(Message).order_by(Message.id) # "order_by" for sort by id
	res = await session.scalars(stmt)
	return Result(
			success=True,
			code=200,
			data=res.all(),
		)

async def addMessage(
		session: AsyncSession,
		messageCreate: MessageCreate
) -> Result:
	message = Message(**messageCreate.model_dump())
	session.add(message)
	try:
		await session.commit()
		return Result(
				success=True,
				code=200,
				data=message,
			)
	except IntegrityError as e:
		await session.rollback()
		error = f'Email address by {messageCreate.email_address_id=} not found' if 'foreign key constraint' in str(e.orig).lower() else e
		return Result(
			success=False,
			code=400,
			error=error,
		)
	except Exception as e:
		return Result(
			success=False,
			code=500,
			error=e,
		)