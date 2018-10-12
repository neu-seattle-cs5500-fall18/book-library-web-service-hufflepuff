from sqlalchemy import Column, String, Integer, Date, ForeignKey


class Loan(Model):
    """
        The loan model for storing loan details
    """
    __tablename__ = 'loan'

    loan_id = Column(Integer, primary_key=True, autoincrement=True)
    book_id = Column(Integer, ForeignKey('library.book_id'))
    user_id = Column(Integer, ForeignKey('user.user_id'))
    list_name = Column(String(100), nullable=False, unique=True)
    status = Column(String(20))
    borrowed_date = Column(Date, nullable=False)
    return_date = Column(Date)

    def __init__(self, loan_id, book_id, user_id, list_name, status,
                 borrowed_date, return_date):
        self.loan_id = loan_id
        self.book_id = book_id
        self.user_id = user_id
        self.list_name = list_name
        self.status = status
        self.borrowed_date = borrowed_date
        self.return_date = return_date
