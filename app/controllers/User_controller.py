from sqlalchemy.orm import Session
from app.models.User_model import User as UserModel
from app.DTO.User_dto import UserCreate


def create_User(db: Session, User: UserCreate):
    new_User = UserModel(
    first_name=  User.first_name,
    last_name= User.last_name,
    Age= User.Age,
    Email= User.Email,
    Pasword=  User.Pasword
    )

    db.add(new_User)
    db.commit()
    db.refresh(new_User)

    return new_User
