import uvicorn
from app.api.routes import create_app
from app.infrastructure.database.in_memory_db import InMemoryRepository
from app.infrastructure.cache.lru_cache import LRUCache
from app.services.library_service import LibraryService
from app.services.search_service import SearchService
from app.services.borrowing_service import BorrowingService
from app.services.analytics_service import AnalyticsService
from app.domain.models.book import Book


def bootstrap():
    repo = InMemoryRepository()
    cache = LRUCache()

    library_service = LibraryService(repo)
    search_service = SearchService(repo, cache)
    borrowing_service = BorrowingService(repo)
    analytics_service = AnalyticsService(repo)

    return {
        "library": library_service,
        "search": search_service,
        "borrow": borrowing_service,
        "analytics": analytics_service,
        "repo": repo,
    }


if __name__ == "__main__":
    services = bootstrap()
    app = create_app(services)
    # Add some sample books
    library = services["library"]
    library.add_book(Book(1, "1984", "George Orwell", "Dystopia", 15, 2))
    library.add_book(Book(2, "Animal Farm", "George Orwell", "Political", 10, 1))

    uvicorn.run(app, host="127.0.0.1", port=5000)
