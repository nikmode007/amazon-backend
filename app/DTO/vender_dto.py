from pydantic import BaseModel



class VenderCreate(BaseModel):
    first_name: str
    last_name: str
    Age: int
    Company_name: str
    GST_NO: str
    Company_addrese: str
    Email: str
    Pasword: str


class VenderResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    Age: int
    Company_name: str
    GST_NO: str
    Company_addrese: str
    Email: str
    Pasword: str

    class Config:
        from_attributes = True