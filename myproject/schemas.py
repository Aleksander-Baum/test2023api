from pydantic import BaseModel

class ItemBase(BaseModel):
    title: str
    description: str
class Item(ItemBase): ## ITEM OUT
    id: int
    owner_id: int

class ItemCreate(ItemBase): # ITEM IN
    pass

class UserBase(BaseModel):
    email: str

class User(UserBase): ## USER OUT
    id: int
    is_active: bool
    items: list[Item] = []

    class Config:
        from_attributes = True

class UserCreate(UserBase): ## USER IN
    password: str