from sqlalchemy.orm import Session
from app.models.vender_model import Vender as VenderModel
from app.DTO.vender_dto import VenderCreate


def create_Vender(db: Session, Vender: VenderCreate):
    new_Vender = VenderModel(
    first_name=  Vender.first_name,
    last_name= Vender.last_name,
    Age=Vender.Age,
    Company_name=Vender.Company_name,
    GST_NO= Vender.GST_NO,
    Company_addrese= Vender.Company_name,
    Email=Vender.Email,
    Pasword=  Vender.Pasword
    )

    db.add(new_Vender)
    db.commit()
    db.refresh(new_Vender)

    return new_Vender

