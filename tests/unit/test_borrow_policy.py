from app.domain.policies import BorrowPolicy
from datetime import datetime, timedelta

def test_borrow_record_creation():
    record = BorrowPolicy.create_record(1, 10)

    assert record.user_id == 1
    assert record.book_id == 10
    assert record.due_date > record.borrow_date

def test_late_fee_calculation():
    overdue_date = datetime.now() - timedelta(days=5)
    fee = BorrowPolicy.calculate_fee(overdue_date)

    assert fee == 5 * BorrowPolicy.DAILY_LATE_FEE