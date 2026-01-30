import pytest
from app.infrastructure.database.in_memory_db import InMemoryRepository
from app.services.borrowing_service import BorrowingService
from app.domain.models.book import Book
from app.domain.exceptions import BookUnavailableError

def test_waitlist_multiple_users():
    repo = InMemoryRepository()
    service = BorrowingService(repo)

    repo.add_book(Book(1, "Test", "A", "C", 10, copies=0))

    with pytest.raises(BookUnavailableError):
        service.borrow(1, 1)

    with pytest.raises(BookUnavailableError):
        service.borrow(2, 1)

    assert len(repo.waitlists[1]) == 2