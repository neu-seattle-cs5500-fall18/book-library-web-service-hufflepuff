from sqlalchemy import Column, String, Integer, Date, ForeignKey
from .Model import Model

from pyld import jsonld


class List(Model):
    """
        The list model for storing list details
    """
    __tablename__ = 'list'

    list_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    list_name = Column(String(20))

    def __init__(self, user_id, list_name):
        self.user_id = user_id
        self.list_name = list_name

    def serialize(self):
        compacted_json = jsonld.compact({
            "http://schema.org/list_id": self.list_id,
            "http://schema.org/user_id": self.user_id,
            "http://schema.org/list_name": self.list_name
        }, self.get_context())
        del compacted_json['@context']
        return compacted_json

    def get_context(self):
        return {
            "@context": {
                "list_id": "http://schema.org/list_id",
                "user_id": "http://schema.org/user_id",
                "list_name": "http://schema.org/list_name"
            }
        }
