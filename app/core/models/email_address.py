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

from models.base import Base


class EmailAddress(Base):
	__tablename__ = 'addresses'

	id: Mapped[int] = mapped_column(primary_key=True)
	email_address: Mapped[str] = mapped_column(index=True)
	# mailbox_id = mapped_column(ForeignKey('mailboxes.id'))

	# mailbox: Mapped['Mailbox'] = relationship(back_populates='email_address')