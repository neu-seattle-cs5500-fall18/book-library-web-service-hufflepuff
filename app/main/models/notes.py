from sqlalchemy import Column, String, Integer, Date, ForeignKey
from .Model import Model


class Notes(Model):
    """
        The library model for storing notes for a book
    """
    __tablename__ = 'note'

    note_id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey('library.book_id'))
    user_id = Column(Integer, ForeignKey('user.user_id'))
    notes = Column(String(500), nullable=False)

    def __init__(self, note_id, book_id, user_id, notes):
        self.note_id = note_id
        self.book_id = book_id
        self.user_id = user_id
        self.notes = notes
