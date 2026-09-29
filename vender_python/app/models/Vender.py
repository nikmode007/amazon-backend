from sqlalchemy import Column, Integer, String
from app.database.connection import Base


class Vender(Base):
    __tablename__ = "vender"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    Age = Column(Integer)
    Company_name = Column(String(100), nullable=False)
    GST_NO = Column(String(100), unique=True, nullable=False)
    Company_addrese = Column(String(100), nullable=False)
    Email = Column(String(100), unique=True, nullable=False)
    Pasword = Column(String(100), unique=True, nullable=False)

