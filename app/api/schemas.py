from pydantic import BaseModel
from typing import Optional

class BookCreateSchema(BaseModel):
    id: int
    title: str
    author: str
    category: str
    price: float
    quantity: int

class BookResponseSchema(BookCreateSchema):
    pass

class SearchQuerySchema(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    category: Optional[str] = None

class BorrowRequestSchema(BaseModel):
    user_id: int
    book_id: int

class BorrowResponseSchema(BaseModel):
    user_id: int
    book_id: int
    success: bool
    message: str