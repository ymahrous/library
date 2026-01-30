from app.domain.exceptions import BookNotFoundError

class LibraryService:
    def __init__(self, repository):
        self.repo = repository

    def add_book(self, book):
        self.repo.add_book(book)

    def remove_book(self, book_id):
        if not self.repo.get_book(book_id):
            raise BookNotFoundError()
        self.repo.remove_book(book_id)

    def update_book(self, book_id, **fields):
        book = self.repo.get_book(book_id)
        if not book:
            raise BookNotFoundError()

        for key, value in fields.items():
            if hasattr(book, key):
                setattr(book, key, value)