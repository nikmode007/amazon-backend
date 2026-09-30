from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column

from app.database.connection_db import Base


class Vender(Base):
    __tablename__ = "vender"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    first_name: Mapped[str] = mapped_column(String(100), nullable=False)
    last_name: Mapped[str] = mapped_column(String(100), nullable=False)
    Age: Mapped[int | None] = mapped_column(Integer)
    Company_name: Mapped[str] = mapped_column(String(100), nullable=False)
    GST_NO: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    Company_addrese: Mapped[str] = mapped_column(String(100), nullable=False)
    Email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    Pasword: Mapped[str] = mapped_column(String(100), nullable=False)
