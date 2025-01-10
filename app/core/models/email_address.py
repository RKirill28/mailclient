from sqlalchemy.orm import (
	Mapped
)

from sqlalchemy.orm import (
	mapped_column,
	relationship,
)

from .base import Base


class EmailAddress(Base):
	__tablename__ = 'addresses'

	id: Mapped[int] = mapped_column(primary_key=True)
	email_address: Mapped[str] = mapped_column(index=True)

	messages: Mapped[list['Message']] = relationship(back_populates="email_address", cascade="all, delete-orphan")
