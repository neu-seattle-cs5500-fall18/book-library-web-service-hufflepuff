from sqlalchemy import Column, String, Integer, Date, ForeignKey


class library(Model):
    """
        The library model for storing books details
    """
    __tablename__ = 'library'

    book_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    author = Column(String(30), nullable=False)
    subject = Column(String(20))
    status = Column(String(20))
    published_date = Column(Date)

    def __init__(self, book_id, name, author, subject, published_date):
        self.book_id = book_id
        self.name = name
        self.author = author
        self.subject = subject
        self.published_date = published_date
