from pydantic import BaseModel

from datetime import datetime


class MessageBase(BaseModel):
	from_to: str
	subject: str
	body: str
	email_address_id: int

class MessageCreate(MessageBase): pass
	

class MessageRead(MessageBase):
	id: int
	received_at: datetime