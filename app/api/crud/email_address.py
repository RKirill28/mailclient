from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert

from core.models import EmailAddress
from core.schemas.email_address import EmailAddressCreate


async def getAllEmailAddresses(
		session: AsyncSession
	) -> list[EmailAddress]:
	stmt = select(EmailAddress).order_by(EmailAddress.id) # "order_by" for sort by id
	res = await session.scalars(stmt)
	return res.all()

async def createEmailAddress(
		session: AsyncSession,
		emailAddressCreate: EmailAddressCreate
) -> None:
	emailAddress = EmailAddress(email_address=emailAddressCreate.email_address)
	session.add(emailAddress)
	await session.commit()
	return emailAddress