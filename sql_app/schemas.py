from pydantic import BaseModel

class ItemBase(BaseModel):
    title: str
    description: str | None = None

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class BlogBase(BaseModel):
    email: str

class BlogCreate(BlogBase):
    pass

class Blog(BlogBase):
    id: int
    is_active: bool
    items: list[Item] = []

    class Config:
        orm_mode = True