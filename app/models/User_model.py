from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column

from app.database.connection_db import Base


class User(Base):
    __tablename__ = "User"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    first_name: Mapped[str] = mapped_column(String(100), nullable=False)
    last_name: Mapped[str] = mapped_column(String(100), nullable=False)
    Age: Mapped[int | None] = mapped_column(Integer)
    Email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    Pasword: Mapped[str] = mapped_column(String(100), nullable=False)
