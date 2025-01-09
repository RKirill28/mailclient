from sqlalchemy import (
	ForeignKey
)

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

	from_to: Mapped[str] 
	subject: Mapped[str]
	body: Mapped[str]
	received_at: Mapped[datetime] = mapped_column(default=datetime.utcnow())
	mailbox_id = mapped_column(ForeignKey('mailboxes.id'))

	mailbox: Mapped['Mailbox'] = relationship(back_populates='messages')



