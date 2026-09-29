from sqlalchemy.orm import Session

from app.models.Vender import Vender
from app.schemas.Vender import VenderCreate


def create_Vender(db: Session, Vender: VenderCreate):
    new_Vender = Vender(
        name=Vender.name,
        email=Vender.email,
        age=Vender.age
    )

    db.add(new_Vender)
    db.commit()
    db.refresh(new_Vender)

    return new_Vender


def get_Vender(db: Session):
    return db.query(Vender).all()


def get_Vender(db: Session, Vender_id: int):
    return db.query(Vender).filter(
        Vender.id == Vender_id
    ).first()


def delete_Vender(db: Session, Vender_id: int):
    Vender = db.query(Vender).filter(
        Vender.id == Vender_id
    ).first()

    if Vender:
        db.delete(Vender)
        db.commit()

    return Vender