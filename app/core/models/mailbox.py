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

class Mailbox(Base):
	__tablename__ = 'mailboxes'

	id: Mapped[int] = mapped_column(primary_key=True)

	email_address: Mapped['EmailAddress'] = relationship(back_populates='mailbox', cascade="all, delete-orphan")
	messages: Mapped[list['Message']] = relationship(back_populates="mailbox", cascade="all, delete-orphan")