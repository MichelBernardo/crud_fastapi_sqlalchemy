from typing import Optional
from pydantic import BaseModel


class TShirt(BaseModel):
    id: Optional[int] = None
    qte: int
    age: int
    gender: str
