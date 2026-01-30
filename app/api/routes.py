from fastapi import FastAPI
from app.api.schemas import (
    BookCreateSchema,
    BookResponseSchema,
    SearchQuerySchema,
    BorrowRequestSchema,
    BorrowResponseSchema,
)
from app.domain.models.book import Book

def create_app(services):
    app = FastAPI(title="Library Management System")

    library = services["library"]
    search = services["search"]
    borrow = services["borrow"]

    @app.post("/books", response_model=BookResponseSchema)
    def add_book(payload: BookCreateSchema):
        book = Book(**payload.dict())
        library.add_book(book)
        return book

    @app.get("/books/search")
    def search_books(query: SearchQuerySchema):
        return search.search(**query.dict(exclude_none=True))

    @app.post("/borrow", response_model=BorrowResponseSchema)
    def borrow_book(payload: BorrowRequestSchema):
        return borrow.borrow(payload.user_id, payload.book_id)

    return app