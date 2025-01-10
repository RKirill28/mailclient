from sqlalchemy import (
	ForeignKey,
	DateTime,
)
import sqlalchemy as sa

from sqlalchemy.orm import (
	Mapped
)

from sqlalchemy.orm import (
	mapped_column,
	relationship,
)

from .base import Base

from datetime import datetime

class Message(Base):
	__tablename__ = 'messages'

	id: Mapped[int] = mapped_column(primary_key=True)

	from_to: Mapped[str] = mapped_column()
	subject: Mapped[str] = mapped_column()
	body: Mapped[str] = mapped_column()
	received_at: Mapped[datetime] = mapped_column(default=datetime.utcnow, server_default=sa.func.now())
	email_address_id = mapped_column(ForeignKey('addresses.id'))

	email_address: Mapped['EmailAddress'] = relationship(back_populates='messages')




