class BorrowRecord:
    def __init__(self, user_id, book_id, borrow_date, due_date):
        self.user_id = user_id
        self.book_id = book_id
        self.borrow_date = borrow_date
        self.due_date = due_date