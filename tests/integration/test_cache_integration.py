from app.infrastructure.database.in_memory_db import InMemoryRepository
from app.infrastructure.cache.lru_cache import LRUCache
from app.services.search_service import SearchService
from app.domain.models.book import Book

def test_search_cache_hits():
    repo = InMemoryRepository()
    cache = LRUCache(capacity=3)
    search = SearchService(repo, cache)

    repo.add_book(Book(1, "A", "X", "C", 10))

    result1 = search.search(author="X")
    result2 = search.search(author="X")

    assert result1 == result2
    assert len(cache.store) == 1