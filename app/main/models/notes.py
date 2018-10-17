from sqlalchemy import Column, String, Integer, Date, ForeignKey
from .Model import Model

from pyld import jsonld


class Notes(Model):
    """
        The library model for storing notes for a book
    """
    __tablename__ = 'notes'

    note_id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey('library.book_id'))
    user_id = Column(Integer, ForeignKey('users.user_id'))
    notes = Column(String(500), nullable=False)

    def __init__(self, note_id, book_id, user_id, notes):
        self.note_id = note_id
        self.book_id = book_id
        self.user_id = user_id
        self.notes = notes

    def serialize(self):
        compacted_json = jsonld.compact({
            "http://schema.org/note_id": self.note_id,
            "http://schema.org/name": self.book_id,
            "http://schema.org/user_id": self.user_id,
            "http://schema.org/notes": self.notes
        }, self.get_context())
        del compacted_json['@context']
        return compacted_json

    def get_context(self):
        return {
            "@context": {
                "note_id": "http://schema.org/note_id",
                "book_id": "http://schema.org/book_id",
                "user_id": "http://schema.org/user_id",
                "notes": "http://schema.org/notes"
            }
        }
