from sqlalchemy.orm import Session
from app.models.Admin_model import Admin as AdminModel
from app.DTO.Admin_dto import AdminCreate


def create_Admin(db: Session, Admin: AdminCreate):
    new_Admin = AdminModel(
    first_name=  Admin.first_name,
    last_name= Admin.last_name,
    Email= Admin.Email,
    Pasword=  Admin.Pasword
    )

    db.add(new_Admin)
    db.commit()
    db.refresh(new_Admin)

    return new_Admin