from pydantic import BaseModel


class PydanticModel(BaseModel):
	class Config:
		from_attributes = True
