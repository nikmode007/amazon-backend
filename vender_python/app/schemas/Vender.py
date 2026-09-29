from pydantic import BaseModel


class VenderCreate(BaseModel):

    name: str
    email: str
    age: int


class VenderResponse(BaseModel):

    id: int
    name: str
    email: str
    age: int

    class Config:
        from_attributes = True