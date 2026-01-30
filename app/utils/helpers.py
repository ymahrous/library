def serialize_book(book):
    return {
        "id": book.book_id,
        "title": book.title,
        "author": book.author,
        "category": book.category,
        "price": book.price,
        "copies": book.copies
    }