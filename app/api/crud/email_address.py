from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from core.models.email_address import EmailAddress

async def getAllEmailAddresses(
		session: AsyncSession
	) -> list[EmailAddress]:
	stmt = select(EmailAddress).order_by(EmailAddress.id) # "order_by" for sort by id
	res = await session.scalars(stmt)
	return res.all()