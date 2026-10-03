from pydantic import BaseModel



class AdminCreate(BaseModel):
    first_name: str
    last_name: str
    Email: str
    Pasword: str


class AdminResponse(BaseModel):
    first_name: str
    last_name: str
    Email: str
    Pasword: str

    class Config:
        from_attributes = True