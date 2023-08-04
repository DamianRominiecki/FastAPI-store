from pydantic import BaseModel
from typing import Optional
from enum import Enum


class Category(str, Enum):
    equipments = "equipments"
    clothes = "clothes"
    electronics = "electronics"
    food = "food"
    drinks = "drinks"
    alcohols = "alcohols"
    others = "others"


class Item(BaseModel):
    name: str
    price: float
    category: Category
    brand: Optional[str] = None


class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    category: Optional[str] = None
    brand: Optional[str] = None
