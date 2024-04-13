from pydantic import BaseModel

class Quote(BaseModel):
	content: str

	class Config:
		orm_mode = True
