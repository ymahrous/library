from datetime import datetime, timedelta
from .models.borrow import BorrowRecord

class BorrowPolicy:
    BORROW_DAYS = 14
    DAILY_LATE_FEE = 2

    @classmethod
    def create_record(cls, user_id, book_id):
        now = datetime.now()
        return BorrowRecord(
            user_id=user_id,
            book_id=book_id,
            borrow_date=now,
            due_date=now + timedelta(days=cls.BORROW_DAYS)
        )

    @classmethod
    def calculate_fee(cls, due_date):
        now = datetime.now()
        if now <= due_date:
            return 0
        return (now - due_date).days * cls.DAILY_LATE_FEE