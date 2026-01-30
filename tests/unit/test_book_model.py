from app.domain.models.book import Book

def test_book_creation():
    book = Book(1, "1984", "Orwell", "Dystopia", 15, 2)

    assert book.book_id == 1
    assert book.title == "1984"
    assert book.is_available() is True

def test_book_availability():
    book = Book(1, "Test", "A", "B", 10, 0)
    assert book.is_available() is False