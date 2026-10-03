from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.connection_db import get_db
from app.DTO.Admin_dto import AdminCreate, AdminResponse
from app.controllers.Admin_controllers import (
    create_Admin
)

routersAdmin = APIRouter(
    prefix="/Admins",
    tags=["Admins"]
)


@routersAdmin.post("/add_admin", response_model=AdminResponse)
def add_admin(
    User: AdminCreate,
    db: Session = Depends(get_db)
):

    return create_Admin(db, User)
