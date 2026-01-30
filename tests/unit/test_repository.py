from app.infrastructure.database.in_memory_db import InMemoryRepository
from app.domain.models.book import Book

def test_add_and_get_book():
    repo = InMemoryRepository()
    book = Book(1, "Test", "Author", "Cat", 10)

    repo.add_book(book)
    assert repo.get_book(1) == book

def test_search_books():
    repo = InMemoryRepository()
    repo.add_book(Book(1, "A", "X", "C1", 10))
    repo.add_book(Book(2, "B", "Y", "C2", 15))

    results = repo.search_books(author="X")
    assert len(results) == 1
    assert results[0].title == "A"