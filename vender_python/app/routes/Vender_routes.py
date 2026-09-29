from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.Vender import VenderCreate, VenderResponse
from app.controllers.Vender_controller import (
    create_Vender,
    get_Vender,
    get_Vender,
    delete_Vender
)

router = APIRouter(
    prefix="/Venders",
    tags=["Venders"]
)


@router.post("/", response_model=VenderResponse)
def add_Vender(
    Vender: VenderCreate,
    db: Session = Depends(get_db)
):

    return create_Vender(db, Vender)


@router.get("/", response_model=list[VenderResponse])
def get_all_Venders(
    db: Session = Depends(get_db)
):

    return get_Venders(db)


@router.get("/{Vender_id}", response_model=VenderResponse)
def get_Vender_by_id(
    Vender_id: int,
    db: Session = Depends(get_db)
):

    Vender = get_Vender(db, Vender_id)

    if not Vender:
        raise HTTPException(
            status_code=404,
            detail="Vender not found"
        )

    return Vender


@router.delete("/{Vender_id}")
def remove_Vender(
    Vender_id: int,
    db: Session = Depends(get_db)
):

    Vender = delete_Vender(db, Vender_id)

    if not Vender:
        raise HTTPException(
            status_code=404,
            detail="Vender not found"
        )

    return {
        "message": "Vender deleted successfully"
    }