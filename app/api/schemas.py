from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field

class BaseSchema(BaseModel):
    class Config:
        orm_mode = True
        anystr_strip_whitespace = True


# -------------------- BOOK SCHEMAS --------------------
class BookCreateSchema(BaseSchema):
    book_id: int = Field(..., gt=0)
    title: str = Field(..., min_length=1)
    author: str = Field(..., min_length=1)
    category: str = Field(..., min_length=1)
    price: float = Field(..., gt=0)
    copies: int = Field(default=1, ge=0)

class BookUpdateSchema(BaseSchema):
    title: Optional[str] = Field(None, min_length=1)
    author: Optional[str] = Field(None, min_length=1)
    category: Optional[str] = Field(None, min_length=1)
    price: Optional[float] = Field(None, gt=0)
    copies: Optional[int] = Field(None, ge=0)

class BookResponseSchema(BaseSchema):
    book_id: int
    title: str
    author: str
    category: str
    price: float
    copies: int
    borrowed_count: int
    sold_count: int

class BookListResponseSchema(BaseSchema):
    books: List[BookResponseSchema]

# -------------------- USER SCHEMAS --------------------
class UserCreateSchema(BaseSchema):
    user_id: int = Field(..., gt=0)
    name: str = Field(..., min_length=1)

class UserResponseSchema(BaseSchema):
    user_id: int
    name: str

# -------------------- BORROWING SCHEMAS --------------------
class BorrowRequestSchema(BaseSchema):
    user_id: int = Field(..., gt=0)
    book_id: int = Field(..., gt=0)

class BorrowResponseSchema(BaseSchema):
    user_id: int
    book_id: int
    borrow_date: datetime
    due_date: datetime

# -------------------- WAITLIST SCHEMAS --------------------
class WaitlistEntrySchema(BaseSchema):
    user_id: int
    priority: int

class WaitlistResponseSchema(BaseSchema):
    book_id: int
    waitlist: List[WaitlistEntrySchema]

# -------------------- OVERDUE / FEES SCHEMAS --------------------
class OverdueBookSchema(BaseSchema):
    user_id: int
    book_id: int
    due_date: datetime
    late_days: int
    extra_fee: float

class OverdueListResponseSchema(BaseSchema):
    overdue_books: List[OverdueBookSchema]

# -------------------- SEARCH SCHEMAS --------------------
class SearchQuerySchema(BaseSchema):
    title: Optional[str]
    author: Optional[str]
    category: Optional[str]

# -------------------- ANALYTICS SCHEMAS --------------------
class PopularBooksSchema(BaseSchema):
    top_author: Optional[str]
    top_category: Optional[str]
    most_borrowed: Optional[str]
    most_sold: Optional[str]

# -------------------- PURCHASE SCHEMAS --------------------
class PurchaseRequestSchema(BaseSchema):
    user_id: int = Field(..., gt=0)
    book_id: int = Field(..., gt=0)

class PurchaseResponseSchema(BaseSchema):
    user_id: int
    book_id: int
    price_paid: float
    purchased_at: datetime

# -------------------- RECOMMENDATION SCHEMAS --------------------
class RecommendationRequestSchema(BaseSchema):
    user_id: int = Field(..., gt=0)
    limit: int = Field(default=3, ge=1, le=10)

class RecommendationResponseSchema(BaseSchema):
    user_id: int
    recommendations: List[str]

# -------------------- ERROR SCHEMA --------------------
class ErrorResponseSchema(BaseSchema):
    error: str
    details: Optional[str] = None