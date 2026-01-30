import pytest
from app.infrastructure.database.in_memory_db import InMemoryRepository
from app.services.borrowing_service import BorrowingService
from app.domain.models.book import Book
from app.domain.exceptions import BookUnavailableError

def test_successful_borrow():
    repo = InMemoryRepository()
    service = BorrowingService(repo)

    book = Book(1, "Test", "A", "C", 10, copies=1)
    repo.add_book(book)

    record = service.borrow(user_id=1, book_id=1)
    assert book.copies == 0
    assert record.user_id == 1

def test_waitlist_when_unavailable():
    repo = InMemoryRepository()
    service = BorrowingService(repo)

    book = Book(1, "Test", "A", "C", 10, copies=0)
    repo.add_book(book)

    with pytest.raises(BookUnavailableError):
        service.borrow(user_id=1, book_id=1)

    assert len(repo.waitlists[1]) == 1