from pydantic import BaseModel



class UserCreate(BaseModel):
    first_name: str
    last_name: str
    Age: int
    Email: str
    Pasword: str


class UserResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    Age: int
    Email: str
    Pasword: str

    class Config:
        from_attributes = True