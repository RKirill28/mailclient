from pydantic import BaseModel


class EmailAddressBase(BaseModel):
	email_address: str

class EmailAddressCreate(EmailAddressBase):
	mailbox_id: int

class EmailAddressRead(EmailAddressBase):
	id: int