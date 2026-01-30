from collections import defaultdict

class AnalyticsService:
    def __init__(self, repository):
        self.repo = repository

    def most_popular(self):
        author_count = defaultdict(int)
        category_count = defaultdict(int)

        for book in self.repo.books.values():
            author_count[book.author] += book.borrowed_count
            category_count[book.category] += book.borrowed_count

        most_borrowed = max(self.repo.books.values(), key=lambda b: b.borrowed_count, default=None)
        most_sold = max(self.repo.books.values(), key=lambda b: b.sold_count, default=None)

        return {
            "top_author": max(author_count, key=author_count.get, default=None),
            "top_category": max(category_count, key=category_count.get, default=None),
            "most_borrowed": most_borrowed.title if most_borrowed else None,
            "most_sold": most_sold.title if most_sold else None
        }