from app.infrastructure.database.in_memory_db import InMemoryRepository
from app.infrastructure.cache.lru_cache import LRUCache
from app.services.library_service import LibraryService
from app.services.search_service import SearchService
from app.services.borrowing_service import BorrowingService
from app.domain.models.book import Book

def test_full_library_flow():
    repo = InMemoryRepository()
    cache = LRUCache()

    library = LibraryService(repo)
    search = SearchService(repo, cache)
    borrow = BorrowingService(repo)

    library.add_book(Book(1, "1984", "Orwell", "Dystopia", 15, 1))

    results = search.search(author="Orwell")
    assert len(results) == 1

    borrow.borrow(user_id=1, book_id=1)
    assert repo.get_book(1).copies == 0