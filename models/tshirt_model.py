from sqlalchemy import Column, Integer, String

from core.configs import settings


class TShirtModel(settings.DBBaseModel):
    __tablename__ = 'tshirts'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    age: int = Column(Integer)
    size: str = Column(String(3))
    gender: str = Column(String(10))