from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.connection_db import get_db
from app.DTO.User_dto import UserCreate, UserResponse
from app.controllers.User_controller import (
    create_User
)

router = APIRouter(
    prefix="/Users",
    tags=["Users"]
)


@router.post("/add_User", response_model=UserResponse)
def add_User(
    User: userCreate,
    db: Session = Depends(get_db)
):

    return create_User(db, User)
