from sqlalchemy.orm import (
	DeclarativeBase,
	Mapped
)
from sqlalchemy.orm import mapped_column


class Base(DeclarativeBase):
	id: Mapped[int] = mapped_column(primary_key=True)




# class Mailbox(Base):
# 	__tablename__ = 'mailboxes'

# 	id: Mapped[int] = mapped_column(primary_key=True)

# 	email_address: Mapped['EmailAddress'] = relationship(back_populates='mailbox', cascade="all, delete-orphan")
# 	messages: Mapped[list['Message']] = relationship(back_populates="mailbox", cascade="all, delete-orphan")


# class Message(Base):
# 	__tablename__ = 'messages'

# 	id: Mapped[int] = mapped_column(primary_key=True)

# 	from_to: Mapped[str] 
# 	subject: Mapped[str]
# 	body: Mapped[str]
# 	received_at: Mapped[datetime] = mapped_column(default=datetime.utcnow())
# 	mailbox_id = mapped_column(ForeignKey('mailboxes.id'))

# 	mailbox: Mapped['Mailbox'] = relationship(back_populates='messages')

