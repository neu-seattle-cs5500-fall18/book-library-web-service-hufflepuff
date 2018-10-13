from sqlalchemy import Column, String, Integer, Date, ForeignKey
from .Model import Model

from pyld import jsonld


class Library(Model):
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

    def __init__(self, book_id, name, author, subject, published_date, status):
        self.book_id = book_id
        self.name = name
        self.author = author
        self.subject = subject
        self.published_date = published_date
        self.status = status

    def __repr__(self):
        return '<bookid {}>'.format(self.book_id)

    #
    # METHODS
    #

    def serialize(self):
        compacted_json = jsonld.compact({
            "http://schema.org/book_id": self.book_id,
            "http://schema.org/name": self.name,
            "http://schema.org/author": self.author,
            "http://schema.org/subject": self.subject,
            "http://schema.org/status": self.status
            "http://schema.org/published_date":published_date
        }, self.get_context())
        del compacted_json['@context']
        return compacted_json

    def get_context(self):
        return {
            "@context": {
                "book_id": "http://schema.org/book_id",
                "name": "http://schema.org/name",
                "author": "http://schema.org/author",
                "subject": "http://schema.org/subject",
                "status": "http://schema.org/status",
                "published_date":"http://schema.org/published_date"
            }
        }