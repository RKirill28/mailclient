from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert

from core.models import EmailAddress
from core.schemas.email_address import EmailAddressCreate

from . import Result


async def getAllEmailAddresses(
		session: AsyncSession
	) -> Result:
	stmt = select(EmailAddress).order_by(EmailAddress.id) # "order_by" for sort by id

	res = await session.scalars(stmt)
	return Result(
		success=True,
		code=200,
		data=res.all()
	)

async def createEmailAddress(
		session: AsyncSession,
		emailAddressCreate: EmailAddressCreate
) -> Result:
	emailAddress = EmailAddress(email_address=emailAddressCreate.email_address)

	session.add(emailAddress)
	await session.commit()

	return Result(
		success=True,
		code=200,
		data=emailAddress
	)

async def deleteEmailAddress(
		session: AsyncSession,
		emailAddressId: int
) -> Result:
	emailAddress = await session.get(EmailAddress, emailAddressId)
	if not emailAddress:
		return Result(
			success=False,
			code=404,
			error='Email address not found'
		)
	
	await session.delete(emailAddress)
	await session.commit()

	return Result(
		success=True,
		code=200,
		data=emailAddress
	)