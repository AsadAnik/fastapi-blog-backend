# Define Pydantic models for data validation and serialization
from pydantic import BaseModel

class ItemBase(BaseModel):
    name: str
    description: str

class ItemCreate(ItemBase):
    pass

class ItemUpdate(ItemBase):
    id: int

class ItemDelete(BaseModel):
    id: int

class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True