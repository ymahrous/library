from app.infrastructure.database.in_memory_db import InMemoryRepository
from app.services.library_service import LibraryService
from app.domain.models.book import Book
import pytest

def test_update_book():
    repo = InMemoryRepository()
    service = LibraryService(repo)

    book = Book(1, "Old", "A", "C", 10)
    repo.add_book(book)

    service.update_book(1, title="New")
    assert book.title == "New"

def test_remove_nonexistent_book():
    repo = InMemoryRepository()
    service = LibraryService(repo)

    with pytest.raises(Exception):
        service.remove_book(99)