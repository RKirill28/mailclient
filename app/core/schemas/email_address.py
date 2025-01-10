from pydantic import BaseModel


class EmailAddressBase(BaseModel):
	email_address: str

class EmailAddressCreate(EmailAddressBase): pass

class EmailAddressRead(EmailAddressBase):
	id: int