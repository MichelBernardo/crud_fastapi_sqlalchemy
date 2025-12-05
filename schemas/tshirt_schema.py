from typing import Optional
from pydantic import BaseModel as SCBaseModel


class TShirtSchema(SCBaseModel):
    id: Optional[int] = None
    age: int
    size: str
    gender: str

    class Config:
        from_attributes = True