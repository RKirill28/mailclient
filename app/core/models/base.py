from sqlalchemy.orm import (
	DeclarativeBase,
	Mapped
)
from sqlalchemy.orm import mapped_column


class Base(DeclarativeBase):
	id: Mapped[int] = mapped_column(primary_key=True)
