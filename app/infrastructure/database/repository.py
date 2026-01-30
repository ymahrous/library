from abc import ABC, abstractmethod

class Repository(ABC):

    @abstractmethod
    def add_book(self, book):
        raise NotImplementedError

    @abstractmethod
    def get_book(self, book_id):
        raise NotImplementedError

    @abstractmethod
    def remove_book(self, book_id):
        raise NotImplementedError

    @abstractmethod
    def search_books(self, **filters):
        raise NotImplementedError

    @abstractmethod
    def save_borrow_record(self, record):
        raise NotImplementedError

    @abstractmethod
    def get_borrowed_books(self):
        raise NotImplementedError