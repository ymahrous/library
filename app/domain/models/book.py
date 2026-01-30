class Book:
    def __init__(self, book_id, title, author, category, price, copies=1):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.category = category
        self.price = price
        self.copies = copies

        self.borrowed_count = 0
        self.sold_count = 0

    def is_available(self):
        return self.copies > 0