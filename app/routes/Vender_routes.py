from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.connection_db import get_db
from app.DTO.vender_dto import VenderCreate, VenderResponse
from app.controllers.Vender_controller import (
    create_Vender
)

router = APIRouter(
    prefix="/Venders",
    tags=["Venders"]
)


@router.post("/add_vendor", response_model=VenderResponse)
def add_Vender(
    Vender: VenderCreate,
    db: Session = Depends(get_db)
):

    return create_Vender(db, Vender)
