from app.domain.policies import BorrowPolicy
from app.domain.exceptions import BookNotFoundError, BookUnavailableError

class BorrowingService:
    def __init__(self, repository):
        self.repo = repository

    def borrow(self, user_id, book_id):
        book = self.repo.get_book(book_id)
        if not book:
            raise BookNotFoundError()

        if not book.is_available():
            self.repo.add_to_waitlist(book_id, user_id)
            raise BookUnavailableError("Added to waitlist")

        book.copies -= 1
        book.borrowed_count += 1

        record = BorrowPolicy.create_record(user_id, book_id)
        self.repo.save_borrow_record(record)
        return record