from app.infrastructure.database.in_memory_db import InMemoryRepository
from app.services.analytics_service import AnalyticsService
from app.domain.models.book import Book

def test_most_popular_books():
    repo = InMemoryRepository()

    b1 = Book(1, "A", "Auth1", "Cat1", 10)
    b2 = Book(2, "B", "Auth2", "Cat2", 10)

    b1.borrowed_count = 5
    b2.borrowed_count = 2
    b2.sold_count = 10

    repo.add_book(b1)
    repo.add_book(b2)

    analytics = AnalyticsService(repo)
    result = analytics.most_popular()

    assert result["most_borrowed"] == "A"
    assert result["most_sold"] == "B"