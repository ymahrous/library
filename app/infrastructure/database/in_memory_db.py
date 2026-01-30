import heapq
from collections import defaultdict

class InMemoryRepository:
    def __init__(self):
        self.books = {}
        self.borrowed = {}
        self.waitlists = defaultdict(list)
        self.user_history = defaultdict(list)

    # BOOKS
    def add_book(self, book):
        self.books[book.book_id] = book

    def get_book(self, book_id):
        return self.books.get(book_id)

    def remove_book(self, book_id):
        self.books.pop(book_id, None)

    def search_books(self, **filters):
        results = []
        for book in self.books.values():
            match = True
            for key, value in filters.items():
                if value is not None and getattr(book, key) != value:
                    match = False
                    break
            if match:
                results.append(book)
        return results

    # BORROWING
    def save_borrow_record(self, record):
        self.borrowed[record.book_id] = record
        self.user_history[record.user_id].append(record.book_id)

    def get_borrowed_books(self):
        return list(self.borrowed.values())

    # WAITLIST
    def add_to_waitlist(self, book_id, user_id, priority=0):
        heapq.heappush(self.waitlists[book_id], (priority, user_id))

    def pop_waitlist(self, book_id):
        if self.waitlists[book_id]:
            return heapq.heappop(self.waitlists[book_id])
        return None