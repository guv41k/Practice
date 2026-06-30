from pydantic import BaseModel
from typing import Optional

# ===== CATEGORY =====

class CategoryBase(BaseModel):
    title: str

class CategoryCreate(CategoryBase):
    pass

class CategoryResponse(CategoryBase):
    id: int

    class Config:
        from_attributes = True

# ===== BOOK =====

class BookBase(BaseModel):
    title: str
    description: Optional[str] = None
    price: Optional[float] = None
    url: Optional[str] = None
    category_id: int

class BookCreate(BookBase):
    pass

class BookResponse(BookBase):
    id: int

    class Config:
        from_attributes = True
