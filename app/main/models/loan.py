from sqlalchemy import Column, String, Integer, Date, ForeignKey
from .Model import Model

from pyld import jsonld


class Loan(Model):
    """
        The loan model for storing loan details
    """
    __tablename__ = 'loan'

    loan_id = Column(Integer, primary_key=True, autoincrement=True)
    book_id = Column(Integer, ForeignKey('library.book_id'))
    user_id = Column(Integer, ForeignKey('users.user_id'))
    status = Column(String(20))
    borrowed_date = Column(Date, nullable=False)
    return_by = Column(Date)
    returned_on = Column(Date)

    def __init__(self, book_id, user_id, status,
                 borrowed_date, return_by, returned_on):
        self.book_id = book_id
        self.user_id = user_id
        self.status = status
        self.borrowed_date = borrowed_date
        self.return_by = return_by
        self.returned_on = returned_on

    def serialize(self):
        compacted_json = jsonld.compact({
            "http://schema.org/loan_id": self.loan_id,
            "http://schema.org/book_id": self.book_id,
            "http://schema.org/user_id": self.user_id,
            "http://schema.org/status": self.status,
            "http://schema.org/borrowed_date": str(self.borrowed_date),
            "http://schema.org/return_by": str(self.return_by),
            "http://schema.org/returned_on": str(self.returned_on)
        }, self.get_context())
        del compacted_json['@context']
        return compacted_json

    def get_context(self):
        return {
            "@context": {
                "loan_id": "http://schema.org/loan_id",
                "book_id": "http://schema.org/book_id",
                "user_id": "http://schema.org/user_id",
                "status": "http://schema.org/status",
                "borrowed_date": "http://schema.org/borrowed_date",
                "return_by": "http://schema.org/return_by",
                "returned_on": "http://schema.org/returned_on"
            }
        }
