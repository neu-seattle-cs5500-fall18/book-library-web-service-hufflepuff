from sqlalchemy import Column, String, Integer, Date, ForeignKey
from .Model import Model

from pyld import jsonld


class Listitem(Model):
    """
        The listitem model for storing books in a list
    """
    __tablename__ = 'listitem'

    listitem_id = Column(Integer, primary_key=True, autoincrement=True)
    list_id = Column(Integer, ForeignKey('list.list_id'))
    book_id = Column(Integer, ForeignKey('library.book_id'))

    def __init__(self, listitem_id, list_id, book_id):
        self.listitem_id = listitem_id
        self.book_id = book_id
        self.list_id = list_id

    def serialize(self):
        compacted_json = jsonld.compact({
            "http://schema.org/listitem_id": self.listitem_id,
            "http://schema.org/book_id": self.book_id,
            "http://schema.org/list_id": self.list_id
        }, self.get_context())
        del compacted_json['@context']
        return compacted_json

    def get_context(self):
        return {
            "@context": {
                "listitem_id": "http://schema.org/listitem_id",
                "book_id": "http://schema.org/book_id",
                "list_id": "http://schema.org/list_id"
            }
        }
