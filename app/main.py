from app.infrastructure.database.in_memory_db import InMemoryRepository
from app.infrastructure.cache.lru_cache import LRUCache
from app.services.library_service import LibraryService
from app.services.search_service import SearchService
from app.services.borrowing_service import BorrowingService
from app.domain.models.book import Book

repo = InMemoryRepository()
cache = LRUCache()

library = LibraryService(repo)
search = SearchService(repo, cache)
borrow = BorrowingService(repo)

library.add_book(Book(1, "1984", "George Orwell", "Dystopia", 15, 2))
library.add_book(Book(2, "Animal Farm", "George Orwell", "Political", 10, 1))

print(search.search(author="George Orwell"))
borrow.borrow(user_id=101, book_id=1)